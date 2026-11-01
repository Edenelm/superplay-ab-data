#!/usr/bin/env python3
"""Validate a provider drop: JSON Schema + contract rules + manifest health/staleness.
Usage: python3 validate.py [PROVIDER_DIR] [--now ISO8601] [--json]
Exit codes: 0 = OK, 1 = contract/schema errors, 2 = OK but stale or a dataset status != ok.
--json report includes dataset_errors{dataset: [...]} and datasets_passed (used by tools/assemble_repo.py to publish per dataset).
'_manifest' / '_files' errors are global and block publishing entirely.
Uses the `jsonschema` package if installed; otherwise a built-in subset validator (type, required, properties,
additionalProperties, items, enum, const, pattern, minimum, minItems, minLength). No network, no secrets."""
import json, os, re, sys, hashlib, datetime
ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]
ROOT = ARGS[0] if ARGS else os.path.dirname(os.path.abspath(__file__))
NOW = None
if '--now' in sys.argv: NOW = datetime.datetime.fromisoformat(sys.argv[sys.argv.index('--now') + 1])
TZ = datetime.timezone(datetime.timedelta(hours=2))
NOW = NOW or datetime.datetime.now(TZ)
errors, warnings = [], []
DS_ERR = {}
def err(ds, msg):
    errors.append(msg); DS_ERR.setdefault(ds, []).append(msg)
TYPES = {'string': str, 'number': (int, float), 'integer': int, 'boolean': bool, 'object': dict, 'array': list, 'null': type(None)}
def tcheck(v, t):
    if t in ('number', 'integer') and isinstance(v, bool): return False
    return isinstance(v, TYPES[t])
def sub(v, s, path, out):
    if 'const' in s and v != s['const']: out.append(f'{path}: expected const {s["const"]!r}'); return
    if 'enum' in s and v not in s['enum']: out.append(f'{path}: {v!r} not in enum'); return
    if 'type' in s:
        ts = s['type'] if isinstance(s['type'], list) else [s['type']]
        if not any(tcheck(v, t) for t in ts): out.append(f'{path}: type {type(v).__name__} not in {ts}'); return
    if isinstance(v, str):
        if 'pattern' in s and not re.search(s['pattern'], v): out.append(f'{path}: {v[:60]!r} !~ {s["pattern"]}')
        if 'minLength' in s and len(v) < s['minLength']: out.append(f'{path}: too short')
    if isinstance(v, (int, float)) and not isinstance(v, bool) and 'minimum' in s and v < s['minimum']: out.append(f'{path}: < minimum')
    if isinstance(v, dict):
        for r in s.get('required', []):
            if r not in v: out.append(f'{path}: missing required {r!r}')
        props = s.get('properties', {})
        for k, x in v.items():
            if k in props: sub(x, props[k], f'{path}.{k}', out)
            elif isinstance(s.get('additionalProperties'), dict): sub(x, s['additionalProperties'], f'{path}.{k}', out)
            elif s.get('additionalProperties') is False: out.append(f'{path}: unexpected {k!r}')
    if isinstance(v, list):
        if 'minItems' in s and len(v) < s['minItems']: out.append(f'{path}: fewer than {s["minItems"]} items')
        if 'items' in s:
            for i, x in enumerate(v): sub(x, s['items'], f'{path}[{i}]', out)
def schema_validate(doc, schema, name):
    out = []
    try:
        import jsonschema
        for e in jsonschema.Draft202012Validator(schema).iter_errors(doc): out.append(f'{name}: {"/".join(map(str, e.path))}: {e.message[:160]}')
    except ImportError:
        sub(doc, schema, name, out)
    return out
def load(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f: return json.load(f)
# ---- manifest ----
man = load('manifest.json')
for e in schema_validate(man, load('schemas/manifest.schema.json'), 'manifest'): err('_manifest', e)
docs = {}
for ds, m in man['datasets'].items():
    fp = os.path.join(ROOT, m.get('file') or '')
    if m['status'] == 'failed' and (not m.get('file') or not os.path.exists(fp)):
        warnings.append(f'{ds}: status=failed and no last-good file published yet error={m.get("error")}'); m['_computed'] = {'age_hours': None, 'stale': True}; continue
    if not os.path.exists(fp): err(ds, f'{ds}: file missing {m["file"]}'); continue
    b = open(fp, 'rb').read()
    if hashlib.sha256(b).hexdigest() != m['sha256']: err(ds, f'{ds}: sha256 mismatch (partial/corrupt write?)')
    docs[ds] = json.loads(b)
    for e in schema_validate(docs[ds], load(m['schema']), ds): err(ds, e)
    if m['status'] != 'ok': warnings.append(f'{ds}: status={m["status"]} error={m.get("error")}')
    ls = m.get('last_success_at')
    age = (NOW - datetime.datetime.fromisoformat(ls)).total_seconds() / 3600 if ls else None
    wd = NOW.astimezone(TZ).weekday()  # Mon=0 .. Fri=4, Sat=5, Sun=6
    limit = man['stale_after_hours'] + (48 if wd in (4, 5) or (wd == 6 and NOW.astimezone(TZ).hour < 11) else 0)
    stale = age is None or age > limit
    if stale: warnings.append(f'{ds}: STALE (age {age and round(age,1)} h > {limit} h)')
    m['_computed'] = {'age_hours': age and round(age, 2), 'stale': stale}
# ---- contract rules ----
def nulls_have_reasons(rec, fields, where, ds):
    nr = rec.get('null_reasons') or {}
    for f in fields:
        if rec.get(f, 'absent') is None and f not in nr: err(ds, f'{where}: {f} is null without null_reasons[{f}]')
reg = docs.get('test_registry', {}).get('records', [])
ids = [r['test_id'] for r in reg]
if len(ids) != len(set(ids)): err('test_registry', 'test_registry: duplicate test_id')
items = [r['board_item_id'] for r in reg]
if len(items) != len(set(items)): err('test_registry', 'test_registry: duplicate board_item_id (dedupe failed)')
idset = set(ids)
for r in reg:
    nulls_have_reasons(r, ['business_question','hypothesis','change','audience','control_vs_test','split','primary_kpi','guardrails','outcome_label'], r['test_id'], 'test_registry')
    if r['lifecycle'] == 'live' and (not r['is_live'] or r['has_results']): err('test_registry', f'{r["test_id"]}: lifecycle/live flags inconsistent')
    if r['lifecycle'] == 'backlog' and r['is_live']: err('test_registry', f'{r["test_id"]}: backlog marked live')
    if r.get('outcome_label') == 'success' and not r.get('has_results'): err('test_registry', f'{r["test_id"]}: success without results')
res = docs.get('test_results', {}).get('records', [])
rids = [x['result_id'] + f'#r{x["revision"]}' for x in res]
if len(rids) != len(set(rids)): err('test_results', 'test_results: duplicate result_id+revision')
for x in res:
    if x['test_id'] not in idset: err('test_results', f'{x["result_id"]}: unknown test_id')
    nulls_have_reasons(x, ['relative_diff_pct', 'abs_diff_pp'], x['result_id'], 'test_results')
    for g in x['groups']:
        if g.get('population_size') is None and 'population_size' not in x['null_reasons']: err('test_results', f'{x["result_id"]}: population_size null without reason')
    if x['abs_diff_pp'] is not None and x['relative_diff_pct'] is not None and abs(x['abs_diff_pp']) == abs(x['relative_diff_pct']) and x['abs_diff_pp'] != 0:
        warnings.append(f'{x["result_id"]}: pp equals % — check %/pp were not mixed')
    if x['verification'] == 'VERIFIED' and not (x['source'].get('ref')): err('test_results', f'{x["result_id"]}: VERIFIED without source ref')
ed = docs.get('explanations_learnings_decisions', {})
for e in ed.get('explanations', []):
    if e['test_id'] not in idset: err('explanations_learnings_decisions', f'explanation {e["test_id"]}: unknown test_id')
    for q, f in e['questions'].items():
        if f['text_he'] is None and not f.get('null_reason'): err('explanations_learnings_decisions', f'{e["test_id"]}.{q}: null without reason')
        if f['text_he'] is not None and not f['source_refs']: err('explanations_learnings_decisions', f'{e["test_id"]}.{q}: text without source_refs')
        if f['text_he'] is not None and f['tag'] is None: err('explanations_learnings_decisions', f'{e["test_id"]}.{q}: text without tag')
for d in ed.get('decisions', []):
    if d['test_id'] is not None and d['test_id'] not in idset: err('explanations_learnings_decisions', f'{d["decision_id"]}: unknown test_id')
for l in ed.get('cross_studio_learnings', []):
    if len(l['per_game_evidence']) < 2: err('explanations_learnings_decisions', f'{l["learning_id"]}: fewer than 2 games')
for g in docs.get('game_metrics', {}).get('records', []):
    nulls_have_reasons(g, ['revenue_gross_usd','revenue_net_usd','ad_revenue_usd','payers','active_users_dau','period_unique_users'], g['metric_id'], 'game_metrics')
    for k in ('revenue_gross_usd','revenue_net_usd','payers','active_users_dau'):
        if g.get(k) == 0: warnings.append(f'{g["metric_id"]}: {k} == 0 — confirm real zero (missing must be null)')
MDEFS = {d['def_id']: d for d in docs.get('metric_definitions', {}).get('records', [])}
for d in MDEFS.values():
    if d['status'] == 'needs_approval' and not d['questions']: err('metric_definitions', f"{d['def_id']}: needs_approval without a question")
    for st in d['source_texts']:
        if st['source_text'] is None and not st.get('null_reason'): err('metric_definitions', f"{d['def_id']}: {st['ref']} source_text null without null_reason")
for g in docs.get('game_metrics', {}).get('records', []):
    fc = g.get('field_completeness') or {}
    if g.get('is_final') != all(v['status'] == 'final' for v in fc.values()): err('game_metrics', f"{g['metric_id']}: is_final inconsistent with field_completeness")
    if (g.get('completeness') == 'final') != bool(g.get('is_final')): err('game_metrics', f"{g['metric_id']}: completeness inconsistent with is_final")
    if MDEFS:
        for k, ref in (g.get('definition_refs') or {}).items():
            if ref not in MDEFS: err('game_metrics', f"{g['metric_id']}: definition_refs.{k} -> unknown {ref}")
            elif g['definition_status'].get(k) != MDEFS[ref]['status']: err('game_metrics', f"{g['metric_id']}: definition_status.{k} out of date")
# ---- secret scan ----
SECRET = re.compile(r'(?i)(api[_-]?key|secret|token|password|bearer)\s*["\']?\s*[:=]\s*["\'][^"\']{12,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{30,}|xox[bp]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_-]{30,}')
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith(('.json', '.md', '.py', '.js', '.sh', '.txt')) and f != 'validate.py':
            t = open(os.path.join(dp, f), encoding='utf-8', errors='ignore').read()
            if SECRET.search(t): err('_files', f'secret-like string in {os.path.relpath(os.path.join(dp, f), ROOT)}')
report = {'root': ROOT, 'checked_at': NOW.isoformat(timespec='seconds'), 'errors': errors, 'warnings': warnings,
          'datasets': {k: v.get('_computed') for k, v in man['datasets'].items()}, 'counts': man.get('counts'),
          'dataset_errors': DS_ERR, 'datasets_passed': [k for k in man['datasets'] if k not in DS_ERR],
          'result': 'FAIL' if errors else ('STALE_OR_PARTIAL' if warnings and any('STALE' in w or 'status=' in w for w in warnings) else 'OK')}
if '--json' in sys.argv: print(json.dumps(report, ensure_ascii=False, indent=1))
else:
    print(f"result: {report['result']}  errors: {len(errors)}  warnings: {len(warnings)}")
    for e in errors[:50]: print('  ERROR', e)
    for w in warnings[:50]: print('  WARN ', w)
    print('counts:', json.dumps(report['counts']))
sys.exit(1 if errors else (2 if report['result'] == 'STALE_OR_PARTIAL' else 0))
