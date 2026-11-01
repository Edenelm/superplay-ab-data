# Processing log

Run 2026-11-01T13:31:33+02:00 (run_id 20261101T133133). Baseline state: 2026-11-01T13:31:19+02:00.

## Checked against (source versions)

- `game_metrics`: {"sha256": "461d01c518005d28ef5ad41130a7cd8d5bf52305a71a3be38679dc63ec29f8b1", "source_snapshot": "2026-11-01T11:45:00+02:00"}
- `test_registry`: {"sha256": "99aa6f51cb3befa822b1a421626c075d770269fd4c1b2440690e3b1ebda7ee61", "source_snapshot": "2026-11-01"}
- `test_results`: {"sha256": "37d1e02f97536c733d3b3335228edb3967f697cbbc22199273503b79070709bf", "source_snapshot": "2026-10-18..2026-11-01"}
- `explanations_learnings_decisions`: {"sha256": "ad3ebed339afc52ea561e1d6ee0dea5335b4d12b30332e173adfe857eb5f3844", "source_snapshot": "2026-11-01"}
- `whatsapp_items`: {"sha256": "e4ed4733fd39e0f3948e688989b8ff54367c4204d4f78db9e56d8a4d1282a36b", "source_snapshot": "2026-11-01"}
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

- sections regenerated: 1, reused: 3349

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
