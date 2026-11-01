# Processing log

Run 2026-11-01T12:35:23+02:00 (run_id 20261101T123523). Baseline state: 2026-11-01T12:35:23+02:00.

## Checked against (source versions)

- `game_metrics`: {"sha256": "dfe4b8b101281b13de113f8294a5dcb1bdee095f5396bb0b36eb3abaca4a5b39", "source_snapshot": "2026-11-01T11:45:00+02:00"}
- `test_registry`: {"sha256": "420ebcad1672a0cb08a68cec09fd01fbbdbe78aad6339936bc54e05299cb67d6", "source_snapshot": "2026-11-01"}
- `test_results`: {"sha256": "7f2a806bdcc4bac99152fce7734301288ffd1b1bb578454878f67a26dd352bfa", "source_snapshot": "2026-10-18..2026-11-01"}
- `explanations_learnings_decisions`: {"sha256": "dc24a1f45fb07a05cbca440ab68a4ecf495fadc97151a95c1ed754beea2ed694", "source_snapshot": "2026-11-01"}
- `whatsapp_items`: {"sha256": "542f28b3cb436bf227c54f5ae582c4c567234d4f3b277a1363f79e8be2bc2ae4", "source_snapshot": "2026-11-01"}
- `metric_definitions`: {"sha256": "7541232e1653e65c5d78285136cb0efb7d68c66c3bcabae76a25e4a31e5ef393", "source_snapshot": "2026-11-01T12:05:00+02:00"}
- `glossary`: {"sha256": "7bafa4f855462865cfc267340d4ae4ade40c3a00cf2b04a5daa2e565a715760a", "source_snapshot": "local sources as of 2026-11-01"}
- `curated_live_understanding`: {"sha256": "6589ba24617a9460db5b4c140401ec809757a82b4c465ec3b21e941aa9abe70d"}
- `glossary_seed`: {"sha256": "a4cdde88e99f10918940024be505682a5986aeaad1e1f16a36e1298fcc47db58"}
- `monday_live_fetch`: fetched 2026-11-01T12:30:00+02:00, 47 live items, 15 with updates; calls: get_board_items_page x3 (live items, includeItemDescription: no description blocks returned); get_updates x2 (47 live items, limit 10/item)

## Not retried (needs a permission change first)

- HQ table headquarters-dbt.50_reporting.rpt_superplay_agg query: 403 bigquery.jobs.create (HQ_ACCESS.md)
- Domino DAU source: no documented DAU field/table found (METRIC_DEFINITIONS.md (DOM.active_users_dau))

## Coverage of Hebrew explanations

- live: {'unclear': 32, 'partial': 14, 'full': 1}
- results: {'partial': 9, 'full': 19, 'unclear': 6}
- backlog: {'stub': 581}

## Regeneration

- sections regenerated: 0, reused: 3349

## Still missing

- DIS-125-make-any-purchase-new-seg: המנגנון טרם הובהר (live)
- DIS-124-ays-offer-for-ftd-and: המנגנון טרם הובהר (live)
- DICE-1104-cz-fix: המנגנון טרם הובהר (live)
- DICE-NOID-free-dream-passs-for-churners: המנגנון טרם הובהר (live)
- DICE-1110-puzzle-onboarding-gt-v4: המנגנון טרם הובהר (live)
- DOM-1590-genie-new-agenda-v3: המנגנון טרם הובהר (live)
- DOM-NOID-choose-your-trail-test: המנגנון טרם הובהר (live)
- DOM-1611-low-balance-challenge-pb-10: המנגנון טרם הובהר (live)
- DOM-1621-1621-trail-runner-v2: המנגנון טרם הובהר (live)
- DIS-125-t125-end-of-puzzle-offer: המנגנון טרם הובהר (live)
- DIS-124-trail-again-3rd-try: המנגנון טרם הובהר (live)
- DIS-120-rv-8box-with-purchase-v2: המנגנון טרם הובהר (live)
- DIS-123-mini-game-treatments: המנגנון טרם הובהר (live)
- DIS-124-rv-extend-segment: המנגנון טרם הובהר (live)
- DIS-125-v4-increase-by-mode: המנגנון טרם הובהר (live)
- DIS-125-push-notification-increase-by-lvl: המנגנון טרם הובהר (live)
- DIS-125-zeus-launch: המנגנון טרם הובהר (live)
- DIS-125-wr-v2: המנגנון טרם הובהר (live)
- DIS-125-8box-segments: המנגנון טרם הובהר (live)
- DIS-125-dormant-cz-v3: המנגנון טרם הובהר (live)
- DIS-125-potion-bonus: המנגנון טרם הובהר (live)
- DIS-125-drc-new-economy-v5-2: המנגנון טרם הובהר (live)
- DIS-112-google-integrity: המנגנון טרם הובהר (live)
- DIS-122-free-resources-pop-up: המנגנון טרם הובהר (live)
- DIS-101-boost-your-puzzle-mistake: המנגנון טרם הובהר (live)
- DICE-1109-whammy-for-dt-finishers: המנגנון טרם הובהר (live)
- DICE-NOID-pet-dynamic-requirements: המנגנון טרם הובהר (live)
- DICE-1109-limited-stock-launch-stock-progression: המנגנון טרם הובהר (live)
- DIS-118-dormant-scene-boost: המנגנון טרם הובהר (live)
- DIS-043-d01-min-price: המנגנון טרם הובהר (live)
- DIS-NOID-live-test: המנגנון טרם הובהר (live)
- DIS-NOID-live-test-2: המנגנון טרם הובהר (live)
- Glossary: 31 concepts `unclear` (see docs/GLOSSARY.md, column Open question).
