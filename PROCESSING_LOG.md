# Processing log

Run 2026-11-01T13:46:48+02:00 (run_id 20261101T134648). Baseline state: 2026-11-01T13:36:01+02:00.

## Checked against (source versions)

- `game_metrics`: {"sha256": "f2417f94dd581281e52c38b1a61661afd38c33dc53599eab078f805f7717f66c", "source_snapshot": "2026-11-01T11:45:00+02:00"}
- `test_registry`: {"sha256": "4c5bfa3d4c0d903c3eb0a6c1e5095600cd6d90557bdd8b0fac671a3486fc89cc", "source_snapshot": "2026-11-01"}
- `test_results`: {"sha256": "daa5d1d4ad5deff5b8e99a74eb80fd58705e67c8c9529115620308bae940fb18", "source_snapshot": "2026-10-18..2026-11-01"}
- `explanations_learnings_decisions`: {"sha256": "b3ac443a41130d0ae997b5e44eff1897036a30975c2854c586e2fd74991436ab", "source_snapshot": "2026-11-01"}
- `whatsapp_items`: {"sha256": "14ea414a2347165ea70289592d055035248c926a7483d0cdfadac8270a9cbb95", "source_snapshot": "2026-11-01"}
- `metric_definitions`: {"sha256": "7541232e1653e65c5d78285136cb0efb7d68c66c3bcabae76a25e4a31e5ef393", "source_snapshot": "2026-11-01T12:05:00+02:00"}
- `curated_live_understanding`: {"sha256": "ee384cab005fa900458e9a0704482e6ea50127390dc79e1ac8b4769becc5f99f"}
- `curated_extra_conflicts`: {"sha256": "5997998b247a1104f4ac35df2df7f0d980f7b1dc0f57e858a52acc2353769b8e", "file": "tools/curated/extra_conflicts.json"}
- `mixpanel_mechanism_pass`: {"sha256": "ab21b663e401310267936d2b8654de5ad8296cdbf10002b7c9a9d03a15b29213", "file": "tools/source_cache/mixpanel_mechanism_2026-11-01.json"}
- `curated_whatsapp_items_extra`: {"sha256": "fd724121bff6c39e11f84de5737aad32eafd9cbb96b3d7d17d662a27269c1c89", "file": "tools/curated/whatsapp_items_extra.json"}
- `glossary_seed`: {"sha256": "a4cdde88e99f10918940024be505682a5986aeaad1e1f16a36e1298fcc47db58"}
- `monday_live_fetch`: fetched 2026-11-01T12:30:00+02:00, 47 live items, 15 with updates; calls: get_board_items_page x3 (live items, includeItemDescription: no description blocks returned); get_updates x2 (47 live items, limit 10/item)

## Not retried (needs a permission change first)

- HQ table headquarters-dbt.50_reporting.rpt_superplay_agg query: 403 bigquery.jobs.create (HQ_ACCESS.md)
- Domino DAU source: no documented DAU field/table found (METRIC_DEFINITIONS.md (DOM.active_users_dau))

## Coverage of Hebrew explanations

- live: {'full': 7, 'partial': 31, 'unclear': 9}
- results: {'partial': 9, 'full': 19, 'unclear': 6}
- backlog: {'stub': 581}

## Regeneration

- sections regenerated: 0, reused: 3350

## Still missing

- DOM-1590-genie-new-agenda-v3: המנגנון טרם הובהר (live)
- DOM-1621-1621-trail-runner-v2: המנגנון טרם הובהר (live)
- DIS-120-rv-8box-with-purchase-v2: המנגנון טרם הובהר (live)
- DIS-123-mini-game-treatments: המנגנון טרם הובהר (live)
- DIS-125-v4-increase-by-mode: המנגנון טרם הובהר (live)
- DIS-125-zeus-launch: המנגנון טרם הובהר (live)
- DIS-125-8box-segments: המנגנון טרם הובהר (live)
- DIS-NOID-live-test: המנגנון טרם הובהר (live)
- DIS-NOID-live-test-2: המנגנון טרם הובהר (live)
- Glossary: 31 concepts `unclear` (see docs/GLOSSARY.md, column Open question).
