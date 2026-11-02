# FILE_MAP

Read order: manifest.json → FILE_MAP.json → index/tests_index.json (filter) → tests/<GAME>/<test_id>.json (only the selected tests) → latest/*.json (full data, for analysis)

skip any file whose sha256 (manifest / FILE_MAP) or test fingerprint (index) equals what you already have

| Path | Size | Contains | Read when |
|---|---|---|---|
| `manifest.json` | 11,880 B | run metadata, per-dataset status/sha256/stale, layer pointers, change_summary | always first; compare sha256 / aggregate_fingerprint with what you cached |
| `FILE_MAP.json` | 11,497 B | this map (machine-readable) | second, to find files |
| `index/tests_index.json` | 642,248 B | one entry per test: game, name, tier, status, dates, Hebrew summary, mechanism, coverage, glossary concepts, tags he/en, flags, detail_file, fingerprint | third: filter here, then open only the detail files you need |
| `CHANGES.md` | 10,724 B | what changed per run (tests added/updated, sections regenerated, needs attention) | when deciding what to re-read |
| `FILE_MAP.md` | 6,191 B | this map (human-readable) | optional |
| `PROCESSING_LOG.md` | 5,512 B | what was checked against which source version; what is still missing; accesses not retried | when a field is missing / unclear |
| `README.md` | 1,695 B | repo readme | once |
| `docs/CLAUDE_CODE_README.md` | 6,380 B | data dictionary, metric definitions, glossary, HQ access, Claude Code readme | reference |
| `docs/GLOSSARY.md` | 11,038 B | data dictionary, metric definitions, glossary, HQ access, Claude Code readme | reference |
| `docs/HQ_ACCESS.md` | 4,106 B | data dictionary, metric definitions, glossary, HQ access, Claude Code readme | reference |
| `docs/METRIC_DEFINITIONS.md` | 30,583 B | data dictionary, metric definitions, glossary, HQ access, Claude Code readme | reference |
| `docs/data_dictionary.md` | 14,755 B | data dictionary, metric definitions, glossary, HQ access, Claude Code readme | reference |
| `history/2026-11-01` (dir, 10 files) | 3,417,577 B | copies of datasets + manifest published that day | audit / diffs over time |
| `history/2026-11-02` (dir, 10 files) | 3,524,373 B | copies of datasets + manifest published that day | audit / diffs over time |
| `latest/explanations_learnings_decisions.json` | 687,350 B | legacy 8-question Hebrew explanations, decisions, cross-studio learnings | decisions / cross-studio learnings; per-test copies are in tests/ |
| `latest/game_metrics.json` | 40,309 B | daily game KPIs (BigQuery) with completeness flags | game-level context |
| `latest/glossary.json` | 93,776 B | org glossary: canonical term, aliases, per-game usage, source spellings, definition + refs, status, open question, not_same_as | to interpret terms / build tags; check not_same_as before comparing across games |
| `latest/metric_definitions.json` | 34,779 B | metric definitions: source text, approval status, questions | before using any metric number |
| `latest/open_issues.json` | 13,926 B | open decisions awaiting Eden / data team: topic, games, affected datasets/fields/def_ids/test_ids, Hebrew+English display note, since | to show limitations in the app; never hide data because of it |
| `latest/test_registry.json` | 1,601,102 B | full registry (all tests, all fields) | full-data analysis; the index + per-test files are derived from it |
| `latest/test_results.json` | 181,770 B | all results rows (append-only, revisions) | full-data analysis of results |
| `latest/whatsapp_items.json` | 217,233 B | WhatsApp extracts with match info | source checks; per-test copies are in tests/ |
| `schemas/explanations_learnings_decisions.schema.json` | 10,239 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/game_metrics.schema.json` | 4,549 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/glossary.schema.json` | 3,727 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/manifest.schema.json` | 2,800 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/metric_definitions.schema.json` | 2,396 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/open_issues.schema.json` | 2,860 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/test_detail.schema.json` | 11,567 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/test_registry.schema.json` | 4,525 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/test_results.schema.json` | 4,175 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/tests_index.schema.json` | 3,473 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `schemas/whatsapp_items.schema.json` | 1,189 B | JSON Schemas (draft 2020-12) | when validating / generating types |
| `state/processing_state.json` | 360,857 B | per-test fingerprints per section, source versions, not-retried accesses | by the producer for incremental runs; consumers rarely need it |
| `tests/DICE` (dir, 292 files) | 2,593,805 B | one test: registry record, results rows, 6-section Hebrew explanation (with tags, refs, fingerprints), structured understanding, legacy 8-question explanation, decisions, WhatsApp items, fetched Monday updates | only for tests selected from the index; skip if fingerprint unchanged |
| `tests/DIS` (dir, 262 files) | 2,009,268 B | one test: registry record, results rows, 6-section Hebrew explanation (with tags, refs, fingerprints), structured understanding, legacy 8-question explanation, decisions, WhatsApp items, fetched Monday updates | only for tests selected from the index; skip if fingerprint unchanged |
| `tests/DOM` (dir, 127 files) | 1,204,661 B | one test: registry record, results rows, 6-section Hebrew explanation (with tags, refs, fingerprints), structured understanding, legacy 8-question explanation, decisions, WhatsApp items, fetched Monday updates | only for tests selected from the index; skip if fingerprint unchanged |
| `validate.py` | 15,837 B | validator: python3 validate.py . (exit 0 ok, 2 stale/partial, 1 errors) | after every pull |
