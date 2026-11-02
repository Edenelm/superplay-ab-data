# Test interim runbook (dataset `test_interim`, contract 1.5.0 additive)

What: per live test × day × group (Test / Control) raw totals from the test's linked Mixpanel dashboard: gross revenue, payers, active users. Net revenue and group size are null with reasons. No differences, uplift or normalised values are stored.

## Source and definitions (Dice)
- Template: dashboard 11602174 "1114 - Duel Time Easier Bots" tiles. Gross Revenue = sum of "Gross Revenues" on "Purchase Complete & RV" ($custom_event:2026763). PU = unique users on "purchase completed". DAU = unique users on "Activity" ($custom_event:1994644). User filter `$excluded_reason is not set`. Breakdown = the test's group property (user property named on the dashboard).
- Tool: Mixpanel `Run-Query` (insights, read-only), project 2036368, one query per test, one at a time, ≤ 20 days per query (longer ranges or parallel queries time out).
- Not applied (query tool limits): dashboard cohort filters ("Relevant users"), other dashboard filters, and "Total of User Profiles" (group size). Rows carry `scope_matches_dashboard=false` and `unapplied_filters`. The exact path is `Get-Report` on the dashboard tiles, which needs Eden's `confirm=true`. See open issue OI-INTERIM-SCOPE.
- All field definitions are `needs_approval` (field_definitions + OI-METRIC-ADS/-NET/-PAYERS/-DAU/-GROSS-VAT, OI-INTERIM-SCOPE). Revenue includes RV/ads (2026-10-21: Mixpanel 753,929 vs BigQuery gross 701,865 + ads 50,953).
- Dates are Mixpanel project dates, not converted.

## Source and definitions (Domino)
- Project 2735821. Template: dashboard 11595668 "1611 - Weekly tasks harder tasks", tiles REVENUE / PU / DAU - trend. Gross Revenue = sum of custom property "Gross Revenue" (5795608) on "purchase completed" (no ads). PU = unique users on "purchase completed". DAU = unique users on "Activity" ($custom_event:1660656). The tiles count per-user distinct days, which equals unique users at day granularity.
- Board filters applied in every query: Excluded User = false (user), Suspected Fraudulent Purchase = false (event; not on the 1581 board, so not applied there), mp_country_code not Israel and not Romania (event). Test-specific: 1590 level_id ≥ 350; 1581 "1581 DTC Remove New/Old User" = New User; 1611 move quest create_time since 2026-10-20 (the board says 10:00; day precision only, so flagged).
- Not applied: cohorts 6188702 (1581) and 6211833 (1621). Dashboards normalise by fixed bucket shares (e.g. 269/135) and add a Lift line; we store raw totals only. Group size is null (no per-group size on the board).
- Records carry `definition_refs` to `field_definitions` keys `DOM.*` (Dice: `DICE.*`). All needs_approval.
- Check 2026-10-21, all users: Mixpanel gross 343,536 vs BigQuery 344,107; payers 22,982 vs 23,086; actives 414,340 (BigQuery Domino DAU null).

## Source and definitions (Disney)
- Project 3205636. Template: dashboard 11595366 "T126 - Chef Segments", tiles "Revenues: Trend" / "Paying Users: Trend" / "DAU: Trend". Gross Revenue = sum of custom property "Purchase Amount" (5590896) on "purchase completed" (gross vs net not documented on the board). PU = unique users on "purchase completed". DAU = unique users on "Activity" ($custom_event:1804960). The tiles count per-user distinct days (= unique users per day).
- Run-Query needs `chartType: "line"` for a daily series (without it the result is a single total).
- Board filters applied: Suspected Fraudulent Purchase (cp 5685015) does not equal "True" (event; not on the AYS board 11507187, so not applied there); $country_code not Israel and not Romania (user). Opportunistic RV: user "T120 - RV 8box with purchase V2 - groups" = Test Group.
- Not applied (all Disney rows have scope_matches_dashboard=false): cohorts 5331213 "Real Players", 5669481 "Suspected Fraud Users" and each test's "Relevant / All users" cohort; T120 "New/old users" equals New User or Old User (one value per filter only).
- Group properties are formula custom properties. Query them by their current saved name: T120's board label "120 - ... groups " and Opportunistic RV's trailing-space label returned only "undefined"; the saved names worked. T124 RV bigger segment and PB level reduction ("T125 - Challenge level reduction - Groups") returned only "undefined" under every known name, so they are null (evidence in `superseded/`).
- Group size is "Total of User Profiles" (not readable with Run-Query), so null. Records reference `DIS.*` definitions, all needs_approval.

## Store and incremental runs
- Raw results: `tools/interim_store/raw/<TEST_ID>.q_<from>_<to>.txt` (DICE-*, DOM-* and DIS-*) (one Run-Query result each; verify `report_name` matches the test before saving, since results files have arrived mislabelled once). Superseded pulls are moved to `tools/interim_store/superseded/` (never deleted).
- `tools/interim_build.py` (called from `tools/build_layer.py`, i.e. by `tools/export_provider.py`) merges every raw file by (test_id, date, group); the newest file wins. Days after yesterday are dropped.
- `is_final=false` for dates ≥ UTC reference day − 7 (Dice window, assumed for Mixpanel; needs approval).
- **08:30 run:** for each test in `coverage` with status `data`: pull from the first provisional day (`window.provisional_from`) to yesterday, save as a new raw file, then run the export. For a new live test: add it to `DICE` / `DOM` / `DIS` in `tools/interim_build.py` with its dashboard id, group property and unapplied filters.
- **Backfill:** `coverage[].backfill_pending` lists days before 2026-10-13 that are not yet pulled; pull them in ≤ 20-day chunks.

## Coverage on 2026-11-02 (Dice, 17 live tests)
- Data (6): 1104 VIP push, 1108 weekly goals, 1110 RV penalty, 1113 x2 ticks (2026-10-13..11-01); 1114 duel (10-21..), 1114 tournament (10-26..).
- Null with reason (11): 1115 (group property not set on 11-01, start day), 1110 puzzle (cohort-based groups), 1106 (dashboard ends 08-13), 1104 CZ fix and 1109 whammy (ambiguous board), trail weekend recomp (possible match only), 5 without a dashboard.

## Coverage on 2026-11-02 (Domino, 9 live tests)
- Data (6): 1590 genie V3 and 1581 DTC Android (2026-10-13..11-01; earlier days backfill_pending); 1611 weekly tasks and 1611 low balance (10-19..); 1611 move quest (10-20..); 1621 trail runner V2 (10-25..).
- Null with reason (3): choose-your-trail and 1621 8-box (possible dashboard match only), ftd-offer-add-a-20 (no dashboard).
- New tests: add them to `DOM` in `tools/interim_build.py`.

## Coverage on 2026-11-02 (Disney, 22 live tests)
- Data (7): T124 AYS offer, T120 RV 8box V2, T125 Dormant CZ V3, T125 Potion Bonus (2026-10-13..11-01; earlier days backfill_pending); T126 Chef Segments (10-19..); T126 Olympus Wheel mega (10-22..); T126 Opportunistic RV (10-29..).
- Null with reason (15): T124 RV extend segment and PB level reduction (group property did not resolve, all "undefined"); T127 3po Halloween and T043 min price (cohort-only dashboards); end-of-puzzle offer and google integrity (ambiguous board); push notification, boost your puzzle mistake, dormant scene boost (possible match only); 6 without a dashboard.

## field_definitions keys (compatibility)
Keys are `DICE.<field>`, `DOM.<field>`, `DIS.<field>`; records point to them via `definition_refs`. The old plain keys (`revenue_gross_usd`, `revenue_net_usd`, `payers`, `active_users`, `group_size`, `is_final`) are kept as deprecated aliases with the Dice content plus `alias_of: "DICE.<field>"` and `deprecated: true`. They will only be removed with a contract minor bump.

## Order
`python3 tools/export_provider.py` → `python3 tools/make_file_map.py . --layout provider` → `python3 validate.py .` (exit 0) → `tools/publish_to_repo.sh`.
