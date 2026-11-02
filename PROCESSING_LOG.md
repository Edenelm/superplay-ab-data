# Processing log

Run 2026-11-02T08:40:18+02:00 (run_id 20261102T084018). Baseline state: 2026-11-01T13:46:48+02:00.

## Checked against (source versions)

- `game_metrics`: {"sha256": "d228e47c9f171c8da80ca27d97623efbe3cdf454ef872d0d6b0bd127d71565c1", "source_snapshot": "2026-11-02T08:40:00+02:00"}
- `test_registry`: {"sha256": "89e68f1e1678f8242ba5d2cfc7467accbc54c9103270018bf17f656d441ea0f4", "source_snapshot": "2026-11-02"}
- `test_results`: {"sha256": "1abc8629e86e102c076f16b42b3a4aa9937fcc4e2e4ad57c7fe27e4c8fc130c3", "source_snapshot": "2026-10-18..2026-11-01"}
- `explanations_learnings_decisions`: {"sha256": "22ca90fb92cb63f5dcdf980d5cb8e2b4cb11ca1cbd0a7c40a3df07293d59a34c", "source_snapshot": "2026-11-02"}
- `whatsapp_items`: {"sha256": "3a1b5cb939668ad0f018e210800af1cec8564fc9c58c30c102592f46fd4cc9d7", "source_snapshot": "2026-11-02"}
- `metric_definitions`: {"sha256": "7541232e1653e65c5d78285136cb0efb7d68c66c3bcabae76a25e4a31e5ef393", "source_snapshot": "2026-11-01T12:05:00+02:00"}
- `curated_live_understanding`: {"sha256": "07bddf632ee7d21b90a7f61d9c01313652e841ecec2d34f55593ef7a9a8a1450"}
- `curated_extra_conflicts`: {"sha256": "31a493c5753754287110df56be166615ee1d9b1ddff43dba30d3dc56b4ce7efd", "file": "tools/curated/extra_conflicts.json"}
- `mixpanel_mechanism_pass`: {"sha256": "ab21b663e401310267936d2b8654de5ad8296cdbf10002b7c9a9d03a15b29213", "file": "tools/source_cache/mixpanel_mechanism_2026-11-01.json"}
- `curated_whatsapp_items_extra`: {"sha256": "e65db1c591cdc5e7310753ea7f2ede33221aa35ece5ee678fb708b0cdace35cf", "file": "tools/curated/whatsapp_items_extra.json"}
- `glossary_seed`: {"sha256": "a4cdde88e99f10918940024be505682a5986aeaad1e1f16a36e1298fcc47db58"}
- `monday_live_fetch`: fetched 2026-11-01T12:30:00+02:00, 47 live items, 15 with updates; calls: get_board_items_page x3 (live items, includeItemDescription: no description blocks returned); get_updates x2 (47 live items, limit 10/item)

## Not retried (needs a permission change first)

- HQ table headquarters-dbt.50_reporting.rpt_superplay_agg query: 403 bigquery.jobs.create (HQ_ACCESS.md)
- Domino DAU source: no documented DAU field/table found (METRIC_DEFINITIONS.md (DOM.active_users_dau))

## Coverage of Hebrew explanations

- live: {'partial': 29, 'full': 5, 'unclear': 14}
- results: {'partial': 9, 'full': 20, 'unclear': 6}
- backlog: {'stub': 598}

## Regeneration

- sections regenerated: 155, reused: 3290

## Still missing

- DICE-1115-trail-double-wheel-better-experience: המנגנון טרם הובהר (live)
- DOM-1590-genie-new-agenda-v3: המנגנון טרם הובהר (live)
- DOM-1621-1621-trail-runner-v2: המנגנון טרם הובהר (live)
- DIS-120-rv-8box-with-purchase-v2: המנגנון טרם הובהר (live)
- DIS-NOID-pb-level-reduction: המנגנון טרם הובהר (live)
- DIS-126-olympus-wheel-mega: המנגנון טרם הובהר (live)
- DIS-126-chef-segments: המנגנון טרם הובהר (live)
- DIS-127-3po-halloween: המנגנון טרם הובהר (live)
- DIS-126-es-v3: המנגנון טרם הובהר (live)
- DIS-126-wr-v3: המנגנון טרם הובהר (live)
- DIS-126-opportunistic-rv: המנגנון טרם הובהר (live)
- DIS-126-1-1-test: המנגנון טרם הובהר (live)
- DIS-NOID-live-test: המנגנון טרם הובהר (live)
- DIS-NOID-live-test-2: המנגנון טרם הובהר (live)
- Glossary: 31 concepts `unclear` (see docs/GLOSSARY.md, column Open question).

## Fixes applied in this run (2026-11-02)

- Stable test ids: ids now stay with their (game, Monday item) across renames (map in `state/test_id_map.json`, seeded from the last published registry). Without this, 21 tests would have changed id today (e.g. `DIS-125-t125-end-of-puzzle-offer` kept, not renamed).
- Carry-forward: 17 previously published tests that are no longer in the app build (7 Disney tests that left the Live group, 10 Disney/Dice backlog items) are kept with `carried_forward`; board status/decision/end date updated only from the 08:00 daily refresh diff. No 21-day rule applied.
- WhatsApp id collision: the app's new items took ids wa327–wa331, which collided with the curated extras. Curated extras renumbered wa327–wa341 → wa9327–wa9341 (refs updated in tools/curated/*). App ids unchanged.
- Business metrics: re-pulled 2026-10-29..2026-11-01 (all still provisional) from the same tables/SQL, each in its own game project; HQ table still not queried (403, not retried).
