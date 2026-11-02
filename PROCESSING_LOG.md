# Processing log

Run 2026-11-02T18:27:08+02:00 (run_id 20261102T182708). Baseline state: 2026-11-02T18:07:49+02:00.

## Checked against (source versions)

- `game_metrics`: {"sha256": "10123725983918510cdc28806a9e1b9f6452a0e82cde80f6fa0938d02e992a41", "source_snapshot": "2026-11-02T17:13:58+02:00"}
- `test_registry`: {"sha256": "576b8571ac2bda967f3bc0b8813fcac0a402d62b9fd9c32201f19c27ffba9ee2", "source_snapshot": "2026-11-02"}
- `test_results`: {"sha256": "3e2885b32f2ec6fec25f0ef27f9c570118f90bb6dd8117d8b1843ceebe11d3ea", "source_snapshot": "2026-10-18..2026-11-02 (diff cells re-read 2026-11-02)"}
- `explanations_learnings_decisions`: {"sha256": "7a084f837754a0f4e2e5bf93124f2dddb33e53f9e58490000ac5648e20d46d0a", "source_snapshot": "2026-11-02"}
- `whatsapp_items`: {"sha256": "5d26e21dd66a07bec732e4e8f1108da794c109556366f9d0739c43d4d2e06263", "source_snapshot": "2026-11-02"}
- `metric_definitions`: {"sha256": "4e05558bb6cc22f8f41987070fe236b90d5fbe0bb9575d75472668cf1e1679f3", "source_snapshot": "2026-11-01T12:05:00+02:00"}
- `game_metrics_splits`: {"sha256": "be0f4f32697e3e4545bda2cc268afd6f48450103233eb55c3f8604acfc48c919", "source_snapshot": "2026-11-02T17:13:58+02:00"}
- `game_ftd_retention`: {"sha256": "e2dba11969a1e09412389e1d65012f37b188fa2b531ff64c10023a9767d3385f", "source_snapshot": "2026-11-02T17:13:58+02:00"}
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

- sections regenerated: 0, reused: 3445

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
