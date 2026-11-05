# Processing log

Run 2026-11-05T08:48:09+02:00 (run_id 20261105T084809). Baseline state: 2026-11-04T08:53:06+02:00.

## Checked against (source versions)

- `game_metrics`: {"sha256": "b56be5b60cd3314b98c48b6eaec670c7e6d010daa251815fb452417a34a9fd58", "source_snapshot": "2026-11-05T08:34:03+02:00"}
- `test_registry`: {"sha256": "fde280a6af474e6b00997d88a6a46369a2fbba16eaab12a3d6661b17b4bce099", "source_snapshot": "2026-11-05"}
- `test_results`: {"sha256": "14755e744766c8c26e5b353aa3819bc615f1dc5d4d7653abeabc3a2017553674", "source_snapshot": "2026-10-18..2026-11-02 (diff cells re-read 2026-11-02)"}
- `explanations_learnings_decisions`: {"sha256": "56dee380450d91adb475e52e8c6275f960fe9635ed872655f3f60ea851096f83", "source_snapshot": "2026-11-05"}
- `whatsapp_items`: {"sha256": "c4d62b158d2373f243d6c0da95c37afd83901c57415557d42fa11f8b927d6923", "source_snapshot": "2026-11-05"}
- `metric_definitions`: {"sha256": "4e05558bb6cc22f8f41987070fe236b90d5fbe0bb9575d75472668cf1e1679f3", "source_snapshot": "2026-11-01T12:05:00+02:00"}
- `game_metrics_splits`: {"sha256": "c8bd263e67b1456391d0425006c1ed41166af2d4ad80524b8f887b6f5b1f2a43", "source_snapshot": "2026-11-05T08:34:03+02:00"}
- `game_ftd_retention`: {"sha256": "ab67f8a9969d37edc684d9537cf89f5b5f4bfdf306a80e66d87325c9f82c1eea", "source_snapshot": "2026-11-05T08:34:03+02:00"}
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
- backlog: {'stub': 609}

## Regeneration

- sections regenerated: 22, reused: 3473

## Still missing

- DICE-1115-trail-double-wheel-better-experience: המנגנון טרם הובהר (live)
- DICE-NOID-trail-less-coins-yeladim-ktanim: המנגנון טרם הובהר (live)
- DICE-NOID-trail-harder: המנגנון טרם הובהר (live)
- DICE-NOID-scrolling-and-6-box-later: המנגנון טרם הובהר (live)
- DOM-1590-genie-new-agenda-v3: המנגנון טרם הובהר (live)
- DOM-NOID-social-kingdom-bots: המנגנון טרם הובהר (live)
- DOM-NOID-superboost: המנגנון טרם הובהר (live)
- DOM-NOID-recompletion-for-early-finishers: המנגנון טרם הובהר (live)
- DIS-120-rv-8box-with-purchase-v2: המנגנון טרם הובהר (live)
- DIS-NOID-pb-level-reduction: המנגנון טרם הובהר (live)
- DIS-126-olympus-wheel-mega: המנגנון טרם הובהר (live)
- DIS-126-chef-segments: המנגנון טרם הובהר (live)
- DIS-127-3po-halloween: המנגנון טרם הובהר (live)
- DIS-126-es-v3: המנגנון טרם הובהר (live)
- DIS-126-wr-v3: המנגנון טרם הובהר (live)
- DIS-126-opportunistic-rv: המנגנון טרם הובהר (live)
- DIS-126-1-1-test: המנגנון טרם הובהר (live)
- Glossary: 31 concepts `unclear` (see docs/GLOSSARY.md, column Open question).

## Source pulls this run (2026-11-05 scheduled 08:30)

- 08:00 A/B app daily refresh for 2026-11-05 found and passed (daily/2026-11-05/edge_suite_out_PASS.json); built from it.
- BigQuery (read-only, dry_run then execute_query per game project): 9/9 plan queries ingested. Daily: DICE 8 dates (10-28..11-04), DOM 8 (10-28..11-04), DIS 9 (10-27..11-04). Retention cohorts: DICE 19+18, DOM 19+18, DIS 19+19. The first three dry runs were issued in parallel and one hit a client-side MCP timeout; all later calls ran one at a time and succeeded. Ingest checked the result `project` against the game.
- Mixpanel Run-Query (read-only, one at a time, chartType line): 19/19 coverage tests with status `data` pulled for 2026-10-28..2026-11-04 (DIS-126-opportunistic-rv 2026-10-29..11-04). Every report_name was checked against the test before saving (tools/interim_store/save.sh).
- Not run: the events calendar append (GAME_EVENTS_RUNBOOK: needs Eden's approval) and the test_results tab re-read (relative_diff_pct unchanged, nothing newly VERIFIED).
- Not retried: HQ headquarters-dbt (403) and the Domino DAU source (still null, needs_approval).
