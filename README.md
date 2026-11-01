# A/B test learning data (read-only feed)

Produced by Grok Bot. Do not edit by hand.

**Read order (light):** `manifest.json` → `FILE_MAP.json` → filter `index/tests_index.json` → open only `tests/<GAME>/<test_id>.json` you need. Skip anything whose sha256 / fingerprint is unchanged. See `docs/CLAUDE_CODE_README.md`, `docs/GLOSSARY.md`, `CHANGES.md`.

- `manifest.json`: start here. Per dataset: status (ok/failed), last_success_at, sha256, stale, is_final; run_type, scheduled_for, generated_at.
- `latest/*.json`: last good version of each dataset (a failed dataset keeps its previous file; check manifest status).
- `history/YYYY-MM-DD/`: copies of what was published that day (Asia/Jerusalem date of the run) + that run's manifest.
- `schemas/`: JSON Schemas (draft 2020-12). `validate.py`: `python3 validate.py .` must exit 0 (or 2 = stale/failed dataset).
- `docs/`: data dictionary, metric definitions (source text + approval status), HQ access notes.
- `latest/open_issues.json`: open decisions (metric definitions, HQ access, unclear tests, status conflicts, 21-day rule). Show them as limitations; never hide data because of them.

**App building can start now.** Open questions do not block it, because they are delivered as data (`open_issues`). Contract v1.3.0.

Times are Asia/Jerusalem unless a field says otherwise. Source dates are not converted (see docs/METRIC_DEFINITIONS.md).

## Earlier README content (kept)

# superplay-ab-data
Data-only repository for the SuperPlay CRO A/B app. Written by Grok Bot (data provider), read by the app built with Claude Code.
Contents will follow the data contract in the starter pack (manifest.json, latest/, history/, schemas/).
