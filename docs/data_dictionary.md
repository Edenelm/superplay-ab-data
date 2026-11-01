# Data dictionary — provider contract v1.1.0

**Conventions (all datasets)**
- Files are UTF-8 JSON. Each one starts with a header: `dataset`, `contract_version`, `generated_at` (ISO 8601 with offset, Asia/Jerusalem) and `timezone`.
- **Missing values are `null`, never 0.** Every null on a key field has an entry in the record's `null_reasons` object, `{field: reason}`. On Hebrew fields the reason goes in `null_reason`.
- Every record has `updated_at` and a source: `sources[]` (`{type, ref}`) or `source{}`.
- `verification` is one of `VERIFIED`, `MISMATCH` or `NOT VERIFIED`.
- **Percent vs percentage points:** `relative_diff_pct` is a relative change in % (test vs control). `abs_diff_pp` is an absolute difference in percentage points. They are never interchangeable.
- Stable ids:
  - `test_id` is `<GAME>-<board test number|NOID>-<slug>`, for example `DICE-199-dtc-from-1st-purchase-android`.
  - `metric_id` is `<GAME>-<date>`.
  - `result_id` is `<test_id>::m01`, `::p01` or `::s01`.
  - `decision_id` is `DEC-<key>`.
  - `learning_id` is `LRN-<slug>`.
- Game codes: DICE = Dice Dreams, DOM = Domino Dreams, DIS = Disney Solitaire.

## manifest.json
| Field | Meaning |
|---|---|
| run_id | Id of the run (from generated_at) |
| run_type | `manual`, `scheduled` or `dry_run` |
| scheduled_for | The planned slot this run belongs to (Sun–Thu 08:30 Asia/Jerusalem), or `null` for a manual run |
| generated_at | **Actual** time the run produced the drop (real clock, Asia/Jerusalem). Show this as "updated at" |
| schedule | Planned schedule; `active` stays false until Eden approves wiring it |
| stale_after_hours | Staleness threshold (26). The reader adds 48 h on Fri/Sat and Sunday before 11:00 |
| definitions | Pointer to `data/metric_definitions.json`, with documented / needs_approval counts and date timezones as stated by each source |
| completeness_rules | Rules behind is_final/provisional. Each rule has `rule_basis`: `source_documented`, `observed` or `default_assumption` |
| datasets.<name>.status | `ok`, `partial` or `failed` for the latest attempt |
| datasets.<name>.last_success_at | Last time this dataset passed validation and was published (last-known-good) |
| datasets.<name>.last_attempt_at | Last attempt, whether it succeeded or failed |
| datasets.<name>.error | Validation errors of the last failed attempt |
| datasets.<name>.stale | Producer's view. **The reader must recompute it** from last_success_at |
| datasets.<name>.is_final | game_metrics only: true when every record is final |
| datasets.<name>.sha256 / bytes | Integrity of the file |
| datasets.<name>.source_snapshot | Date or time of the underlying source snapshot |
| publish (repo only) | Datasets published / failed in this run, and the history folder |
| counts | Record counts |

## (a) game_metrics — `data/game_metrics.json` → `records[]`
| Field | Type | Meaning |
|---|---|---|
| metric_id | str | `DICE-2026-10-29` |
| game, date | str | Game, and the source's `date_dim`, **unconverted** |
| date_timezone | str | As stated by the source: Solitaire `UTC`; Dice and Domino `undocumented` |
| currency | `USD` | |
| revenue_gross_usd | num/null | Per-game export expression in metric_definitions (`<GAME>.revenue_gross_usd`). Definition status in `definition_status` |
| revenue_net_usd | num/null | As above (`<GAME>.revenue_net_usd`) |
| ad_revenue_usd | num/null | Ad revenue, a separate field (whether headline revenue includes ads needs approval: `ALL.revenue_includes_ads`) |
| payers | num/null | `<GAME>.payers` |
| active_users_dau | num/null | **Daily** active users (`<GAME>.active_users_dau`). Domino is null until its definition is approved |
| users_with_any_row, pau_flag_users | num | Raw alternative counts, kept for transparency |
| period_unique_users | num/null | Distinct users over a period (WAU/MAU). **Not a sum of DAU.** Currently null, because it was not queried |
| definition_refs | obj | field → `def_id` in `data/metric_definitions.json` |
| definition_status | obj | field → `documented` / `needs_approval`. **Show "definition pending approval" for needs_approval** |
| exclusions | str | User filters applied |
| source | obj | BQ project, table, exact SQL, run_at, bytes |
| field_completeness | obj | field → `{status: final / provisional / provisional_estimate, rule_id, rule_basis}` |
| is_final | bool | true only when every field is final |
| completeness | enum | `final` or `provisional` (same as is_final) |
| caveats | [str] | Known issues (observations are labelled as such) |

## metric_definitions — `data/metric_definitions.json` → `records[]`
| Field | Meaning |
|---|---|
| def_id | `DICE.payers`, `ALL.revenue_includes_ads`, ... |
| export_expression | What our export computes (our aggregation, not a source column) |
| source_texts[] | `{kind: column / table_description, ref: project.dataset.table[.column], source_text}`, copied verbatim from table metadata; `null` + `null_reason` if the source has no description |
| status | `documented` or `needs_approval` |
| questions | The open questions when status is needs_approval |
See METRIC_DEFINITIONS.md for the rendered table.

## (b) test_registry — `data/test_registry.json` → `records[]`
| Field | Meaning |
|---|---|
| test_id, legacy_keys | Stable id, plus the keys used in the current app (`dice199`, `live_…`, `bl_…`, `wab_…`) |
| board_item_id, board_test_number | Monday item id, and the number in the name. Duplicates are flagged |
| lifecycle | `has_results`, `live`, `live_with_results`, `backlog` or `completed_board_only` |
| is_live / has_results | **Independent booleans**. A live test can have results |
| board_status_raw, board_group, board_decision_raw | As written on Monday |
| outcome_label | `success`, `lost`, `running`, `stopped`, `other` or null. Set only for tests with a results tab. Rules are in `outcome_rule`. **A deploy alone does not make success** |
| business_question, hypothesis, change, audience, control_vs_test, split | Text from the source |
| start_date, end_date, phases | As in the source. `end_date` may carry a note when the board and tab differ |
| primary_kpi, guardrails | Designated KPI. Guardrails are null in all records (not designated in the sources) |
| mixpanel | `{state: matched/ambiguous/possible/none, dashboards[], possible[], board_link}` |
| conflicts[] | `{type, msg}`. Types: duplicate_test_number, board, board_live_group, mismatch_board_vs_tab, live_and_backlog |
| source_links[] | Human links (Monday, results tab, Mixpanel) |

## (c) test_results — `data/test_results.json` → `records[]` (append-only)
| Field | Meaning |
|---|---|
| result_id, revision, supersedes | A revision is never edited in place. A correction is a new revision with `supersedes` set to the old `result_id#rN` |
| record_hash | Hash of the content (excluding updated_at), used to detect real changes |
| metric | Metric label as written in the source, or null for summary-only rows |
| groups[] | `{group, value_raw, value, value_unit, population_size}`. population_size is null with a reason (not captured) |
| relative_diff_pct | Relative % change, test vs control, from the source |
| abs_diff_pp | Percentage-point difference, when the source shows it |
| uncertainty | `{p_value, ci, note}`. Only what the source shows |
| measurement_window | Start/end as written in the source |
| source | `{type: results_tab, ref: URL, tab, cell_range}` |
| verification, evidence_level, evidence_note | From the review. `directional` or `insufficient` |
| is_live, has_results | Copied from the registry |
| phase_decision | For phase rows: the decision written for that phase |
| summary_text | For summary-only rows |

## (d) explanations_learnings_decisions — `data/explanations_learnings_decisions.json`
**explanations[]** (Hebrew): `questions.{what_changed, why_tested, who, what_happened, business_meaning, limitations, recommended, decided}`. Each one is `{text_he, tag, source_refs[], null_reason}`.
- `tag` is `source_fact` (source text inside a Hebrew frame), `generated_explanation` (templated reasoning over source fields) or `hypothesis`.
- `measured_impact_ref` lists the result_ids.
- Business state (game_metrics), measured impact (test_results), recommendation and actual decision are kept separate.

**decisions[]:**
- `whatsapp_decision_latest`: the latest WhatsApp decision wins, and a launch is not a decision.
- `recommended[]`
- `board_decision`, `board_status`
- `numbers_quoted` (unverified)
- `conflicts[]` (contradicts, missing on board, not on board)
- `sources[]`: the WhatsApp file, date, time and sender

**cross_studio_learnings[]:**
- `theme`
- `per_game_evidence{game: [test_id, outcome_label, verification]}`
- `mechanism` and `conditions`: null with reasons
- `game_differences_he`
- `questions_before_porting_he[]`
- `tag: hypothesis` and `not_proof_of_transfer: true`

## whatsapp_items — `data/whatsapp_items.json` (supplementary source events)
Fields: `id` (wa001…), `game`, `group`, `date`, `time`, `sender`, `test` (as written), `decision`, `nums`, `text`, `file`, `match`, `board_item`, `poss` (possible matches, never auto-linked).
