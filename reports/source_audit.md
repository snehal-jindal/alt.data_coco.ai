# Source audit, October 13, 2026

## What changed since the idea pitch

The pitch identified potential signals. We have now downloaded actual official
records, examined the available fields, built a reproducible cleaning pipeline
and identified specific reasons the original RFQ prediction is not yet testable.
No customer interviews or predictive results have been added.

## Verified collection and cleaning

| Unit | Count | Interpretation |
|---|---:|---|
| Planning applications mentioning data centers | 510 | Applications, not distinct projects. Includes several administrative types. |
| Keyword permit rows across issued/submitted feeds | 1,345 | Raw rows, including repeated permit IDs. |
| Distinct permits explicitly mentioning data centers | 1,167 | Deduplicated by county PermitGUID. |
| Parcels identified by those descriptions | 140 | Current seed universe, not a historical cohort. |
| Parcel follow-up raw rows | 7,570 | All permit types at the seed parcels. |
| Distinct parcel-associated permits after deduplication | 6,858 | Includes unrelated, older and residential activity. |
| Mechanical permits at seed parcels | 454 | Candidate records, not 454 verified cooling opportunities. |
| Mechanical permits explicitly mentioning data centers | 61 | Text-confirmed context, not confirmed purchase events. |
| Unusable application date before 1900 | 1 | Source date 1753 retained; cleaned date blanked and flagged. |
| Issue dates earlier than application dates by local calendar day | 22 | Flagged for investigation before timeline use. |
| Verified cooling RFQ labels | 0 | Original purchasing target remains unavailable. |
| Independently verified historical publication dates | 0 | Historical availability remains unresolved. |

All server row counts reconcile with downloaded pagination. Planning GUIDs
are unique in this extraction. No compared cross-feed status/date/description
conflicts were found. Repeated address rows do exist within permit feeds.

## Three concrete observations

1. `MECHC-2024-061638` and `MECHC-2024-061642` describe separate AWS fit-out
   phases at the same parcel. The text names data-hall air handling units and
   rooftop exhaust arrays. This supports equipment relevance but also shows
   why a parcel cannot be treated as one purchase or one building phase.
2. `MECHC-2024-062810` describes a fourth campus building and a future
   single-tenant computer data-center use. A simple keyword match does not
   distinguish a future use from an active operating facility.
3. `MECHC-2024-064781` describes an upgrade in an existing data center and one
   energy-recovery ventilator. A data-center mention does not necessarily mean
   a large data-hall cooling opportunity.

These observations are a reading of current county descriptions. They are not
independently verified procurement timelines or seller interview findings.

## Timing and coverage findings

The permit feed snapshot is October 13, 2026. Application and issue dates can
be historical, but the snapshot does not supply historical status transitions
or description versions. Today’s description cannot be assigned to an old
application date without evidence it existed then.

The keyword seed set also uses current descriptions. It excludes unidentified
data centers and includes projects that later revealed their use. Building a
historical backtest directly from this seed set would therefore be misleading.

The planning layer has an application date and current status, but no approval
date field in the audited schema. An approval-timing feature requires documents
or another historical source.

The issued/submitted tables are not proven to contain all withdrawn or
cancelled applications. Unobserved future mechanical events are not reliable
negative outcomes. County trade-permit rules changed on March 11, 2024: trade
sub-record applications can begin when the parent building permit is applied
for. This challenges a simplistic sequential permit timeline.

## Decision

Data access is feasible. Original purchase prediction is not ready for modeling.
The next gate is a building/phase-level timeline with independently dated
records and a consistent observable outcome. Archived reports may help, but
their relevant content and publication dates remain to be recovered. If the
outcome changes to a public milestone, the research claim will change explicitly.

## Sources

- County planning API: https://logis.loudoun.gov/gis/rest/services/Projects/LOLA_DATA/MapServer/0
- County issued permits API: https://logis.loudoun.gov/gis/rest/services/LMARC/LandMARC_Permits/MapServer/1
- County submitted permits API: https://logis.loudoun.gov/gis/rest/services/LMARC/LandMARC_Permits/MapServer/2
- Public records context: https://www.loudoun.gov/landmarc
- Archived reports: https://www.loudoun.gov/1164/Issued-Building-Permit-Reports
- Trade-permit change: https://www.loudoun.gov/Blog.asp?ARC=672&IID=1300

Exact query clauses, fields, page hashes and retrieval timestamps are in the
locally retained raw responses. Counts are findings from this collected
snapshot, not county-wide data-center market estimates.
