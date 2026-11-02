# For Claude Code: consuming the CRO data feed

> **You can start building the app now.** The open questions (metric definitions, HQ access, unclear Disney tests, status conflicts, the 21-day rule) do not block the build. They are published as data in `latest/open_issues.json`. Show them as limitations, and the app picks up the answers automatically when they change. Contract **v1.5.0** (v1.5: per-group `population_size` and p-value/CI/significance cells in `test_results`, new `test_structured` dataset — check `definition_status` and `question` before using a value; v1.4: `test_results.diff_method`; relative_diff_pct is the tab's own diff cell; use the highest revision per result_id).

The **producer** (Grok Bot) collects the data and publishes it. The **consumer** (your app) only reads. Do not write into the drop folder.

## 0. Light read order (v1.3; saves tokens)
1. `manifest.json`: check `layer.index.sha256` / `layer.index.aggregate_fingerprint` and per-dataset `sha256`. If all equal what you cached, stop.
2. `FILE_MAP.json`: what each file holds, its size and sha256; when to read it.
3. `index/tests_index.json`: filter by game / tier / is_live / has_results / coverage / tags / concepts. Compare each `fingerprint` with your cache; keep only the changed ones.
4. `tests/<GAME>/<test_id>.json`: only for the selected tests (`detail_file`). Each holds registry + results + 6-section Hebrew explanation (statements tagged explicit_in_source / interpretation, with source_refs) + decisions + WhatsApp refs.
5. `latest/*.json`: the full aggregates, still the basis for full-data analysis (not deprecated).
6. `latest/open_issues.json`: open decisions (status=awaiting_decision). For each one, show `display_note_he`/`_en` next to the affected `fields` / `test_ids` / `def_ids`. Never hide data because of it.
Use `docs/GLOSSARY.md` / `latest/glossary.json` for terms; never merge concepts listed in `not_same_as`. `CHANGES.md` lists what changed per run. Coverage `unclear` = 'המנגנון טרם הובהר': show it, do not fill it in.

## 1. Connect (GitHub data repo, read-only, server-side)
The data lives in the **private GitHub repo `Edenelm/superplay-ab-data`** (branch `main`; layout in UPDATE_CHANNEL.md). It is active and is updated by normal commits only (no force push). `repo_staging/` in the provider pack is a local fixture with the same layout.
1. Credential: `AB_DATA_READ_TOKEN` is a fine-grained PAT with **Contents: Read** on that repo only, or a GitHub App with Contents: read.
   - Keep it **server-side only** (backend, build step or serverless proxy).
   - **Never in the browser bundle, HTML, client JS or local storage.**
   - The browser talks only to your server or proxy.
2. Fetch `manifest.json` first, e.g. `GET /repos/{owner}/{repo}/contents/manifest.json?ref=main` with `Accept: application/vnd.github.raw+json`.
   - Send `If-None-Match: <last ETag>`. A `304` means nothing changed, so stop.
3. For each `manifest.datasets[x]`, fetch `latest/<x>.json` only if its `sha256` changed since your last good copy.
   - Verify the sha256, then cache it as the last good copy.
4. Join keys:
   - `test_id` links the registry, results, explanations and decisions.
   - `game` plus `date` keys game_metrics.
   - `definition_refs` links game_metrics to `metric_definitions.def_id`.

## 2. Validate (run on every load, in CI as well)
```
python3 validate.py <repo checkout or staging dir>          # human output
python3 validate.py <dir> --json                             # machine output (dataset_errors, datasets_passed)
```
- Exit 0 means OK. Exit 1 means contract errors, so **do not load; keep your last good copy**. Exit 2 means stale or a failed dataset, so load it and show the stale banner.
- If the `jsonschema` package is installed, it is used. Otherwise a built-in validator runs. There are no dependencies.

## 3. Health check and staleness (required UI behaviour)
- If `datasets[x].status == failed`: show "update failed — showing last good data from <last_success_at>". The file in latest/ is the last good one.
- Recompute staleness yourself: `age = now - datasets[x].last_success_at`. The data is stale if `age > stale_after_hours` (26 h), with 48 h added on Fri/Sat and Sunday before 11:00 Asia/Jerusalem, because no runs happen Fri/Sat.
- Show per dataset: "updated <last_success_at, Asia/Jerusalem>". If stale, show a stale badge. If `status != ok`, show "update failed — showing last good data from …".
- Never show `null` as 0. Show "—" with the `null_reasons` text as a tooltip.

## 4. Display rules from the contract
- Keep these four apart: **business state** (game_metrics), **measured impact** (test_results), **recommendation** and **actual decision** (decisions and explanations).
- Never imply that a game's revenue change was caused by a test.
- `outcome_label = success` comes from the board or registry decision. Show `verification` and `evidence_level` next to it.
- Label `relative_diff_pct` with "%" and `abs_diff_pp` with "pp".
- Show the Hebrew `tag`: source fact / explanation / hypothesis. Cross-studio learnings are hypotheses.
- `is_live` and `has_results` are independent.
- test_results is append-only. For each result_id, show the highest `revision`.
- Open issues: render every `open_issues` item with status=awaiting_decision as a limitation note (e.g. a badge on the metric, or a banner on the affected test). The 21-day rule (`OI-RULE-21D`) is not defined, so never use it to end or hide a test.
- Do not sum or compare game_metrics gross across games: `ALL.gross_comparability` needs approval. Solitaire gross is VAT-exclusive; Dice and Domino VAT treatment is undocumented.
- `definition_status[field] == needs_approval`: show the number with a "definition pending approval" badge, or hide it. Link to the source text in metric_definitions.
- `is_final == false`: show a "provisional" badge. Per-field detail is in `field_completeness` (`provisional_estimate` = the source says the value is usually low).
- Dates are shown exactly as the source stores them. Show `date_timezone` (UTC or "undocumented"); **do not convert**.
- `test_interim.field_definitions` keys (changed 2026-11-02): read each record's definition via `field_definitions[record.definition_refs[field]]`, with keys `DICE.<field>`, `DOM.<field>`, `DIS.<field>`. The first Dice-only version used plain keys (`revenue_gross_usd`, `revenue_net_usd`, `payers`, `active_users`, `group_size`, `is_final`). They are still there as **deprecated aliases** of `DICE.<field>` (`alias_of`, `deprecated: true`), so old readers keep working; migrate to `definition_refs`. Removal will come with a contract minor bump. test_interim rows with `scope_matches_dashboard=false` are not the test audience: show `unapplied_filters`.
- "Updated at" is `manifest.generated_at`, the actual run time. `scheduled_for` is the planned slot (null for a manual run).

## 5. Files
`manifest.json`, `data/*.json` (incl. `metric_definitions.json`, `open_issues.json`), `repo_staging/` (dry-run repo tree), `schemas/*.schema.json` (JSON Schema 2020-12), `examples/*.json` (real records), `data_dictionary.md`, `SOURCES_COVERAGE.md`, `UPDATE_CHANNEL.md`, `SECRETS_REQUIRED.md`, `METRIC_DEFINITIONS.md`, `HQ_ACCESS.md`, and `validate.py`. `tools/` holds the producer's own scripts, for reference only.
