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
