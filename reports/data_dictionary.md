# Data dictionary and units

| Field | Meaning and use |
|---|---|
| plan_guid | County application identifier. Not a building identifier. |
| permit_guid | County permit identifier used for deduplication. |
| parcel_pin | Land parcel identifier. May contain multiple buildings/phases. |
| house_number | ADDRESSLINE1 from the source. Not a complete street address. |
| application_date_utc | Administrative application date, with dates before 1900 flagged and blanked. |
| application_date_source_utc | Original application date retained for audit. |
| application_date_invalid | True for a non-null application date before 1900. |
| issue_before_application_day | Issue date precedes application date by Eastern calendar day. Quarantine for timeline analysis. |
| issue_date_utc | Administrative permit issue date, not a purchasing date. |
| finalize_date_utc | Administrative finalization date. |
| snapshot_date_utc | County feed snapshot date. |
| retrieved_at_utc | Our collection timestamp. |
| historical_publication_date | Blank until independently verified. Never replace with application date. |
| current_status | Snapshot status. Not safe as a historical predictor. |
| description_current | Snapshot description. Revisions and first publication are unverified. |
| dc_keyword | Explicit data-center wording in current permit description. Discovery flag only. |
| declared_value | Source VALUE field. Not cooling revenue, RFQ value or Coco.ai market size. |
| square_feet | Source SQUAREFEET field; interpretation varies with work class. |

All derived dates use UTC to preserve source timestamps. The source may encode
local date-only values at midnight Eastern time. Use local calendar dates for
day-level comparisons once a prediction task is locked.

Sampling: first ten explicit data-center permit IDs in application-date order
are an administrative audit sample. The separate mechanical sample uses permit
number ordering. Neither is a representative project cohort or an outcome test.

Cleaning retains raw files. Conflicting cross-feed records are reported.
Issued-feed rows receive precedence when present. Duplicate address rows at the
same permit GUID do not become independent observations.
# Midterm qualification additions, October 14

Further current outputs: `watchlist_update_replay.csv` and
`watchlist_update_summary.json` record changes only on recovered document dates.
`quality_followup.csv` is a separate, manually researched three-project physical-
outcome audit. `signal_quality_audit.json` reports unresolved coverage and keeps
accuracy metrics null. Contractor engagement, conditional approval, physical
construction and completed construction are not interchangeable labels.

These qualification files describe supporting background work. The current
dated-document inputs are `data/curated/dated_projects.csv`, `dated_events.csv`
and `dated_sources.csv`. They contain manual source-fact extractions, separate
from current permit descriptions. Scope and stage are taken from the issue-era
source; later outcomes are joined only after alert decisions.

Current outputs are `early_notice_screening.csv`,
`early_notice_investigation_queue.csv`, `early_notice_timeline.csv` and
`early_notice_summary.json`. Blank approval dates mean not recovered, not failed.
Signed notice days preserve already-past milestones and negative news advantages.
An evidence document date is distinct from the event date it reports. Issue dates
are publisher-stated availability proxies, not verified delivery timestamps.

The current task and source/date interpretation are defined in
`midterm_scope.md` and `midterm_walkthrough.md`. The following files derive from
the 407-row, 2023–2025 commercial-building cohort:

- `qualification_annotations.csv`: initial AI-assisted desk labels (`positive`,
  `negative`, `unknown`), reasons and exact source evidence; human review pending.
- `qualification_predictions.csv`: one row per permit, baseline decision and
  rule decision (`qualified`, `out_of_scope`, `review`), with rule explanation.
- `qualified_filings.csv` and `review_queue.csv`: subsets of those predictions,
  not verified live leads or distinct building counts.
- `qualification_comparison.csv`: decisions joined to desk labels for auditing.
- `qualification_errors.csv`: false alerts, desk positives not auto-qualified,
  and any unresolved desk labels assigned a non-review decision.
- `qualification_metrics.json`: internal agreement metrics and application-year
  breakdown, source/annotation/rule hashes, and evaluation limitations.

`application_day_local` is the application date in America/New_York, not the
original-publication date. `parcel_pin` is one representative association per
permit. Multiple associations are retained in `audit_summary.json` under
`multi_parcel_permits`. No supplier-selection or purchasing outcome is present.
