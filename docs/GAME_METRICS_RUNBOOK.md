# Game metrics runbook (history, splits, FTD, retention)

Covers `data/game_metrics.json`, `data/game_metrics_splits.json`, `data/game_ftd_retention.json`.
History starts 2026-09-25 (`tools/gm_build.py` HISTORY_START). Store: `tools/gm_store/` (one JSON per game and kind; every date keeps its SQL, run_at and bytes).

## Daily (08:30 routine)
1. **Plan:** `python3 tools/gm_history.py plan`, which prints the SQL ready to run. It lists, per game, the dates that are missing or not final under `tools/completeness_rules.json` (DICE/DOM 7 days, DIS 8 days; refday = today's UTC date). Final dates are **never** re-pulled.
2. **Pull:** for each SQL in the plan (wide query, up to 19 dates per call): BigQuery MCP `dry_run`, then `execute_query` with `project=` set to the game project (dice-dreams-dbt / domino-dreams-dbt / solitaire-dreams-dbt), `write_to_file`. No SELECT *, and always keep the date_dim partition filter. HQ (headquarters-dbt) data returns 403; do not retry.
3. **Ingest:** `python3 tools/gm_history.py ingest <daily|retention> <DICE|DOM|DIS> <file>`. This checks that the result's `project` matches the game.
4. **Build:** `python3 tools/export_provider.py` (full run). It merges the store into `tools/game_metrics_queries.json`; store dates fill whatever the queries file lacks, so history persists even if only the last days were re-queried. It also re-derives splits and FTD/retention with that run's NOW, so is_final stays current. For game data only: `python3 tools/gm_history.py build`.
5. `python3 tools/make_file_map.py . --layout provider` → `python3 validate.py .` → `tools/publish_to_repo.sh` (needs AB_DATA_REPO set).

## Rules
- Approved definitions are not changed here. Every new field has definition + source + definition_status in `field_definitions`; unclear means needs_approval with a question.
- Missing values are null with `null_reasons[path]`, never 0. Immature retention days are null.
- Domino active_users is null until OI-METRIC-DAU is decided.
- Ads are separate (`revenue_channels.ads`, `included_in_iap_total: false`).
- Source timezones are kept: Disney UTC, Dice/Domino undocumented.
- **Disney filter change (2026-11-02):** the history pull used `is_special_user IS NOT TRUE`. Future pulls use the approved `is_special_user = FALSE`. They are equivalent on 09-25..11-01 (0 NULL rows on every date). Affected entries carry a caveat.
- Domino reconciliation with `prod_50_reporting.domino_daily_kpis`: `tools/source_metadata/domino_reporting_reconciliation.json`.
