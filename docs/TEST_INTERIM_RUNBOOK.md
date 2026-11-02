# Test interim runbook (dataset `test_interim`, contract 1.5.0 additive)

What: per live test × day × group (Test / Control) raw totals from the test's linked Mixpanel dashboard: gross revenue, payers, active users. Net revenue and group size are null with reasons. No differences, uplift or normalised values are stored.

## Source and definitions (Dice)
- Template: dashboard 11602174 "1114 - Duel Time Easier Bots" tiles. Gross Revenue = sum of "Gross Revenues" on "Purchase Complete & RV" ($custom_event:2026763). PU = unique users on "purchase completed". DAU = unique users on "Activity" ($custom_event:1994644). User filter `$excluded_reason is not set`. Breakdown = the test's group property (user property named on the dashboard).
- Tool: Mixpanel `Run-Query` (insights, read-only), project 2036368, one query per test, one at a time, ≤ 20 days per query (longer ranges or parallel queries time out).
- Not applied (query tool limits): dashboard cohort filters ("Relevant users"), other dashboard filters, and "Total of User Profiles" (group size). Rows carry `scope_matches_dashboard=false` and `unapplied_filters`. The exact path is `Get-Report` on the dashboard tiles, which needs Eden's `confirm=true`. See open issue OI-INTERIM-SCOPE.
- All field definitions are `needs_approval` (field_definitions + OI-METRIC-ADS/-NET/-PAYERS/-DAU/-GROSS-VAT, OI-INTERIM-SCOPE). Revenue includes RV/ads (2026-10-21: Mixpanel 753,929 vs BigQuery gross 701,865 + ads 50,953).
- Dates are Mixpanel project dates, not converted.

## Store and incremental runs
- Raw results: `tools/interim_store/raw/<TEST_ID>.q_<from>_<to>.txt` (one Run-Query result each; verify `report_name` matches the test before saving, since results files have arrived mislabelled once). Superseded pulls are moved to `tools/interim_store/superseded/` (never deleted).
- `tools/interim_build.py` (called from `tools/build_layer.py`, i.e. by `tools/export_provider.py`) merges every raw file by (test_id, date, group); the newest file wins. Days after yesterday are dropped.
- `is_final=false` for dates ≥ UTC reference day − 7 (Dice window, assumed for Mixpanel; needs approval).
- **08:30 run:** for each test in `coverage` with status `data`: pull from the first provisional day (`window.provisional_from`) to yesterday, save as a new raw file, then run the export. For a new live test: add it to `DICE` in `tools/interim_build.py` with its dashboard id, group property and unapplied filters.
- **Backfill:** `coverage[].backfill_pending` lists days before 2026-10-13 that are not yet pulled; pull them in ≤ 20-day chunks.

## Coverage on 2026-11-02 (Dice, 17 live tests)
- Data (6): 1104 VIP push, 1108 weekly goals, 1110 RV penalty, 1113 x2 ticks (2026-10-13..11-01); 1114 duel (10-21..), 1114 tournament (10-26..).
- Null with reason (11): 1115 (group property not set on 11-01, start day), 1110 puzzle (cohort-based groups), 1106 (dashboard ends 08-13), 1104 CZ fix and 1109 whammy (ambiguous board), trail weekend recomp (possible match only), 5 without a dashboard.

## Domino Dreams and Disney Solitaire: pending
Not pulled yet (`games_pending`, status `pending`, not a permanent null). Next: map each live test to its linked Mixpanel dashboard and group property, read that project's own tile definitions, then add them like Dice.

## Order
`python3 tools/export_provider.py` → `python3 tools/make_file_map.py . --layout provider` → `python3 validate.py .` (exit 0) → `tools/publish_to_repo.sh`.
