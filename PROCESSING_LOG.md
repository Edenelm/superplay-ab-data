# Processing log

Run 2026-11-02T17:56:03+02:00 (run_id 20261102T175603). Baseline state: 2026-11-02T16:29:03+02:00.

## Checked against (source versions)

- `game_metrics`: {"sha256": "beb299381d0012b98b187f841838e0ade4d5c8a36beb0fa6b00da072a88dc87a", "source_snapshot": "2026-11-02T17:13:58+02:00"}
- `test_registry`: {"sha256": "bb9f74bce98b85fbb1d1deb397107cc3f5bd068bd0fd213bd6140c4d324e89be", "source_snapshot": "2026-11-02"}
- `test_results`: {"sha256": "f09e4a03a8837768cfbb2306351030e5d63c1686e3ccbb5bd03aff1f419130a1", "source_snapshot": "2026-10-18..2026-11-02 (diff cells re-read 2026-11-02)"}
- `explanations_learnings_decisions`: {"sha256": "64da1e9c1c285bdf2a9883f501755f1b2506932fd0cca4cf2853a1a860a69312", "source_snapshot": "2026-11-02"}
- `whatsapp_items`: {"sha256": "da4d7cc5f928acee3a74917c14be06f881dadf05d91ac08fb588ebfbfb7f794a", "source_snapshot": "2026-11-02"}
- `metric_definitions`: {"sha256": "4e05558bb6cc22f8f41987070fe236b90d5fbe0bb9575d75472668cf1e1679f3", "source_snapshot": "2026-11-01T12:05:00+02:00"}
- `game_metrics_splits`: {"sha256": "849a2543aa559f005ae5c639f6c1a7bff1aa2ac384db6152d3a52a650a4c5fee", "source_snapshot": "2026-11-02T17:13:58+02:00"}
- `game_ftd_retention`: {"sha256": "6d8c89594bdec9651154e95a387f87d1f90a109a6fbcef01bd226f874d23eea7", "source_snapshot": "2026-11-02T17:13:58+02:00"}
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

- sections regenerated: 6, reused: 3439

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
