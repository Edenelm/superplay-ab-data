# Processing log

Run 2026-11-04T08:53:06+02:00 (run_id 20261104T085306). Baseline state: 2026-11-03T08:56:41+02:00.

## Checked against (source versions)

- `game_metrics`: {"sha256": "045de1b5931a285af6d391ed5e285d2ba1d9e31dacc566639fd944dfc0d00f5f", "source_snapshot": "2026-11-04T08:40:01+02:00"}
- `test_registry`: {"sha256": "f4207fc448a2c7f346e62fa2c38e3e49960351961c59768b2517a207c2d9a437", "source_snapshot": "2026-11-04"}
- `test_results`: {"sha256": "5f1619d00a49bce321fc2a5022354653d86f423f7d7bfb7ea5387d360e484901", "source_snapshot": "2026-10-18..2026-11-02 (diff cells re-read 2026-11-02)"}
- `explanations_learnings_decisions`: {"sha256": "ec33a9cc9dc0d5324935a8bc3850bb21baba37fbdddd074aca7e7fc083094032", "source_snapshot": "2026-11-04"}
- `whatsapp_items`: {"sha256": "43141303bb3545d754d08f31a4a81c927cbad4be590012ad9c0225e67bbd06c2", "source_snapshot": "2026-11-04"}
- `metric_definitions`: {"sha256": "4e05558bb6cc22f8f41987070fe236b90d5fbe0bb9575d75472668cf1e1679f3", "source_snapshot": "2026-11-01T12:05:00+02:00"}
- `game_metrics_splits`: {"sha256": "6b239fe564a523f4638fb4e751d5dac8c4fa59ba959d0a795f93ace8c6485389", "source_snapshot": "2026-11-04T08:40:01+02:00"}
- `game_ftd_retention`: {"sha256": "7a50e67ac85ac3f18af07b351110157221121b378b7314f5cabf02c2e0f476e3", "source_snapshot": "2026-11-04T08:40:01+02:00"}
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

- live: {'partial': 25, 'full': 5, 'unclear': 17}
- results: {'partial': 9, 'full': 20, 'unclear': 6}
- backlog: {'stub': 607}

## Regeneration

- sections regenerated: 44, reused: 3441

## Still missing

- DICE-1115-trail-double-wheel-better-experience: המנגנון טרם הובהר (live)
- DICE-NOID-trail-less-coins-yeladim-ktanim: המנגנון טרם הובהר (live)
- DICE-NOID-trail-harder: המנגנון טרם הובהר (live)
- DICE-NOID-scrolling-and-6-box-later: המנגנון טרם הובהר (live)
- DOM-1590-genie-new-agenda-v3: המנגנון טרם הובהר (live)
- DOM-NOID-social-kingdom-bots: המנגנון טרם הובהר (live)
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

## Source pulls this run (2026-11-04 scheduled 08:30)

- BigQuery (read-only, dry_run then execute_query per game project): 9/9 plan queries ingested. Daily: DICE 8 dates (10-27..11-03), DOM 8 (10-27..11-03), DIS 9 (10-26..11-03). Retention cohorts: DICE 19+18, DOM 19+18, DIS 19+19. Two retention queries (DICE 10-16..11-02, DIS 10-15..11-02) hit a client-side MCP timeout when issued in parallel; each was re-run once on its own and succeeded. Results were matched to games by the `project` field and date range, not by call order.
- Mixpanel Run-Query (read-only, one at a time, qspec shapes from tools/interim_build.py, chartType line): 19/19 coverage tests with status `data` pulled for 2026-10-27..2026-11-03 (DIS-126-opportunistic-rv 2026-10-29..11-03, its start). Every report_name was checked against the test before saving (tools/interim_store/save.sh).
- Not run: the events calendar append (GAME_EVENTS_RUNBOOK: not scheduled, needs Eden's approval) and the test_results tab re-read (no new diff-cell read; relative_diff_pct unchanged, nothing newly VERIFIED).
- Not retried: HQ headquarters-dbt (403) and the Domino DAU source (still null, needs_approval).
