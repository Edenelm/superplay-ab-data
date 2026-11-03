# Processing log

Run 2026-11-03T08:56:41+02:00 (run_id 20261103T085641). Baseline state: 2026-11-03T08:56:12+02:00.

## Checked against (source versions)

- `game_metrics`: {"sha256": "f17e7d6881e758c544a87c24627f8a88e99234cfb199b4b4978f37649c9f5302", "source_snapshot": "2026-11-03T08:41:22+02:00"}
- `test_registry`: {"sha256": "4afe6da57db8573cf028339a82c407c7d25274811919759a99a81f769cc2bf00", "source_snapshot": "2026-11-03"}
- `test_results`: {"sha256": "2ae11b5c4f057736b0bfc095d12de129516b5cb6341bad1aa0359423af7f2598", "source_snapshot": "2026-10-18..2026-11-02 (diff cells re-read 2026-11-02)"}
- `explanations_learnings_decisions`: {"sha256": "ac5a439438082f88939778c5152f44e43e0384494a682c729d7accef723dd01a", "source_snapshot": "2026-11-03"}
- `whatsapp_items`: {"sha256": "63289f54eed98b80196b4848d8340d3288c5220f3b92703e7c4212d980cdfee2", "source_snapshot": "2026-11-03"}
- `metric_definitions`: {"sha256": "4e05558bb6cc22f8f41987070fe236b90d5fbe0bb9575d75472668cf1e1679f3", "source_snapshot": "2026-11-01T12:05:00+02:00"}
- `game_metrics_splits`: {"sha256": "5c71e0dafd042dd43e8161f1910b2adea4fb3c9f8b29ec5a75bbbf9648485ae2", "source_snapshot": "2026-11-03T08:41:22+02:00"}
- `game_ftd_retention`: {"sha256": "6724cf0c716bd32d1ec87801a36c24ff99430e6f0f310958dd0b55d2af2a78b1", "source_snapshot": "2026-11-03T08:41:22+02:00"}
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

- live: {'partial': 28, 'full': 5, 'unclear': 14}
- results: {'partial': 9, 'full': 20, 'unclear': 6}
- backlog: {'stub': 603}

## Regeneration

- sections regenerated: 0, reused: 3465

## Still missing

- DICE-1115-trail-double-wheel-better-experience: המנגנון טרם הובהר (live)
- DICE-NOID-trail-less-coins-yeladim-ktanim: המנגנון טרם הובהר (live)
- DOM-1590-genie-new-agenda-v3: המנגנון טרם הובהר (live)
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
