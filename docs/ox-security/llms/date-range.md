# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/date-range.md

# dateRange

Date range filter for time-based report queries.

### Examples

```graphql
input DateRange {
  from: Float
  to: Float
}
```

### Fields

| Field        | Description                                       | Supported fields |
| ------------ | ------------------------------------------------- | ---------------- |
| from `Float` | Start timestamp (UTC epoch, default: 0)           |                  |
| to `Float`   | End timestamp (UTC epoch, default: maximum value) |                  |

### References

#### Fields with this object

* [{} GetApplicationsInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input)
* [{} SingleApplicationInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/single-application-input)
* [{} IssuesInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input)
* [{} GetIssuesConditionalFiltersInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/get-issues-conditional-filters-input)
* [{} ResolvedIssuesInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-input)
* [{} ResolvedIssuesV2Input.dateRange](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-v2input)
* [{} DisappearedIssuesInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/disappeared-issues-input)
* [{} CICDIssuesInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-input)
* [{} GetArtifactsInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-input)
* [{} GetUnscannedArtifactsInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-unscanned-artifacts-input)
* [{} GetPipelineSummaryInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/get-pipeline-summary-input)
* [{} CloudItemsInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/cloud-items-input)
