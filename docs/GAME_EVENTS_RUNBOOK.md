# GAME_EVENTS_RUNBOOK — `game_events` (v1.5 additive)

Events calendar per game (Dice Dreams, Domino Dreams, Disney Solitaire): albums, sales/offers, price changes, feature launches and A/B test windows. Each event has start/end dates, a source link, `definition_refs`, and `null_reasons` for every null. Dates are never guessed. Each record keeps its source's timezone in `date_timezone`.

## Sources (read-only, approved by Eden)
| system | what | verification | link |
|---|---|---|---|
| Monday board 9494658232 (Dice "AB Test Dashboard") | Start Date / End Date (test window); Type; Status; Decision; "Date Implemented" | `board` | `source.url` = pulse URL |
| Monday board 18416650776 (Domino "AB Tests Dashboard 2026") | Start / End; Type; Status | `board` | pulse URL |
| Monday board 18435634714 (Disney "AB Tests Disney") | start_date / end_date; test_status; decision (no Type column) | `board` | pulse URL |
| WhatsApp extracts (`data/whatsapp_items.json` ← `/workspace/pilot/whatsapp/`) | decision `launched` → launch_message (start = message date); deploy decisions → deploy_message (start null, `announced_on`) | `whatsapp_unverified` | `source.file` + `source.item_id` |
| BigQuery `dice-dreams-dbt.20_core.dim_album_season` | Dice album seasons (MIN/MAX of event album dates; album 63 end hardcoded in dbt) | `bigquery_dbt` | `source.table` + album_id |
| BigQuery `solitaire-dreams-dbt.30_intermediate.int_album_season` | Disney album windows (from int_album_config) | `bigquery_dbt` | `source.table` + album_id |

No authoritative source was found for these (see `missing_sources[]` and OI-EVENTS-CALENDAR):
- Domino album calendar.
- An all-player sales/offers calendar.
- A price-change log.
- A release/deploy log.

The Domino and Disney boards have no deploy-date column. Board Pricing/Offer/Album items are **test windows** (`scope: test_population`). They are not live-ops events for all players.

## Category rules
- **Board items:** category comes from the Type label only:
  - Album → `album`
  - OFFER/Offers → `sale_offer`
  - Pricing → `price_change`
  - Feature Launch → `feature_launch`
  - any other or empty Type → `ab_test`
- **WhatsApp:** category comes from explicit words (`whatsapp_keyword_category`, needs approval).
- **BigQuery album tables:** `album`.

## What Eden needs to provide to close the gaps
1. The Domino album calendar (id/name, start, end), or the name of the table or sheet that holds it.
2. A sales/offers calendar per game (name, start, end, segment).
3. A price-change log per game (SKU/package, old/new price, effective date).
4. A release/deploy log per game (feature, version, rollout date, % rollout), or a deploy-date column on the boards.
5. Approval of the `needs_approval` definitions:
   - `bq_album_season` as the official album calendar
   - `whatsapp_launch`
   - `whatsapp_keyword_category`
   - `board_date_implemented`

## Rebuild
`python3 tools/export_provider.py` runs `tools/build_layer.py`, which loads `tools/events_build.py`. Then run:

```
python3 tools/make_file_map.py . --layout provider
python3 validate.py .
```

## Incremental 08:30 append (Asia/Jerusalem). Not scheduled; any automation needs Eden's approval of location and scope.
1. **Monday:** re-read the 3 boards read-only with `get_board_items_page` (limit 2000, the columns listed in `tools/events_store/progress.json`). Overwrite `tools/events_store/raw/items_<board>.txt` with the new snapshot.
2. **WhatsApp:** append the new day's extract under `/workspace/pilot/whatsapp/` and refresh `data/whatsapp_items.json` with the existing extractor. Only new messages are added.
3. **BigQuery (optional, weekly is enough):** re-run the two album-season SELECTs. Each is about 1 KB; run `dry_run` first. Write the results to `tools/events_store/raw/bq_*.txt`.
4. Rebuild, then validate. The validator must exit 0.
5. **Append semantics:**
   - `event_id` is a stable hash of (game, event_kind, source system, item id, start_date).
   - Unchanged events keep their id.
   - An event whose start date changes on the board gets a new id. Readers should treat the item id plus `source.url` as the identity.
   - Never delete history from the raw snapshots. Previous snapshots can be kept as `items_<board>.<YYYYMMDD>.txt`.
6. Add a CHANGES.md entry: `game_events: +N events`, coverage changes.
7. Publish with `tools/publish_to_repo.sh`: pull/rebase first, never force.

## Validator rules (validate.py)
- Every null in start_date/end_date/date_basis/name has a reason in `null_reasons`.
- end ≥ start.
- WhatsApp events are always `whatsapp_unverified`.
- Board events carry a Monday pulse URL. BigQuery events carry a table.
- `definition_refs` resolve.
- A `needs_approval` definition has a question.
- Coverage counts match the records. Any coverage status other than `ok` has a `null_reason`.
- The global phone-number scan applies.
