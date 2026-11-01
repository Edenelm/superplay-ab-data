# HQ KPI table: access status (checked 2026-11-01 ~12:03 Asia/Jerusalem, read-only)

## The table
`headquarters-dbt.50_reporting.rpt_superplay_agg` (the HQ KPI report source, dashboard 2055).

Schema metadata **is visible** through the Bifrost Looker connection (studio "Headquarters", billing project `headquarters-dbt`). Full copy: `tools/source_metadata/headquarters-dbt.50_reporting.rpt_superplay_agg.json`.
- Table description (verbatim): "Superplay aggregate by date_dim, studio. Incremental insert_overwrite. Grain: date_dim, studio. Sources: mrt_daily_agg_dice, mrt_daily_agg_domino, mrt_daily_agg_solitaire, mrt_playtika_est_dice, mrt_playtika_est_domino, mrt_playtika_est_solitaire"
- Partition `date_dim` (DAY), clustered by `studio`, 32 columns, 4,801 rows, 1,226,207 bytes (metadata).
- The `date_dim` column description does not state a timezone ("date dim. Granularity: date_dim, studio. Source: mrt_daily_agg_dice.date_dim").

## The exact error (data query)
A **dry run** (no execution, no bytes billed) of a 3-day query on the table via the Bifrost Looker connection returned:

```
403 POST https://bigquery.googleapis.com/bigquery/v2/projects/headquarters-dbt/jobs?prettyPrint=false: Access Denied: Project headquarters-dbt: User does not have bigquery.jobs.create permission in project headquarters-dbt.
Location: US
```
error_type `Forbidden`. (Job ID omitted here; available in the run log.) The Bifrost BigQuery connection also lists `headquarters-dbt` with `can_query: false`.

What this does and does not tell us:
- Missing for sure: `bigquery.jobs.create` in project `headquarters-dbt` (you cannot start a query job billed there).
- Unknown: whether the identity can read the table's rows (`bigquery.tables.getData`). That can't be tested until a job can be created.

## What it would provide / reconcile (per its column descriptions)
| HQ column | Source description (verbatim, abridged to the first sentence) | Reconciles our field |
|---|---|---|
| `total_revenues` | "Total gross revenue including gross IAP and net ads." | ALL.revenue_includes_ads (HQ headline = gross IAP + net ads) |
| `gross_revenues` | "gross revenues." | revenue_gross_usd (Dice, Domino; VAT question) |
| `net_revenues` | "net revenues." | revenue_net_usd |
| `ads_net_revenues` | "ads net revenues." | ad_revenue_usd (gross vs net of ad share) |
| `dau` | "dau." | active_users_dau (**resolves Domino DAU**, Dice DAU rule) |
| `paying_users` | "paying users." | payers |
| `pau` | "Paying active users." | Domino `pau_flag` wording conflict |
| `mau` | "mau." | period_unique_users (currently null) |
| `installs`, `ftd`, `arppu`, `arpdau` | as described in the metadata file | not exported today |
| channel splits (`apple_store_*`, `google_store_*`, `*_stripe_*`, `dice_plus_stripe_*`, `other_*`, `total_dtc_*`, `net_dtc`) | gross/net per channel | Dice channel inclusion question |

Note: several HQ descriptions are only a column name ("dau.", "gross revenues."). Even with access, the definitions of HQ dau / paying_users stay undocumented in the metadata. Reconciling against them shows which game-level rule matches HQ. It does not document the rule.

## Access to request (phrase for the data/infra owner; NOT requested by Grok Bot)
For the principal the Bifrost BigQuery/Looker connection runs as (the error says "User"; the Bifrost admin should confirm which account or service account that is):
1. **`roles/bigquery.jobUser` on project `headquarters-dbt`**: gives `bigquery.jobs.create`, which is the missing permission in the error.
   *Alternative:* allow running the query billed to an already-allowed studio project (e.g. `dice-dreams-dbt`) and grant only (2).
2. **`roles/bigquery.dataViewer` on dataset `headquarters-dbt.50_reporting`** (or only on table `rpt_superplay_agg`): read rows. It may already be partly in place, since metadata is visible; this can't be verified yet.
3. **Bifrost BigQuery connection:** add `headquarters-dbt` to the queryable projects (today `can_query: false`).

Until then, every game_metrics record keeps `verification = NOT VERIFIED` with this reason.
