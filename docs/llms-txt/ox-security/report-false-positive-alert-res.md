# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/report-false-positive-alert-res.md

# reportFalsePositiveAlertRes

Response for reporting a false positive alert.

### Examples

```graphql
type ReportFalsePositiveAlertRes {
  exclusionInfo: GetExclusionsRes
  aggregationsStatus: String
}
```

### Fields

| Field                                                                                                                                         | Description                                                               | Supported fields                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| exclusionInfo [`GetExclusionsRes`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/get-exclusions-res) | Information about the created exclusion if one was created                | <p>exclusions <a href="exclusion"><code>\[Exclusion!]!</code></a><br>totalExclusions <code>Float</code><br>totalFilteredExclusions <code>Float</code></p> |
| aggregationsStatus `String`                                                                                                                   | Status of aggregations for display in UI based on enum AggregationsStatus |                                                                                                                                                           |

### References

#### Mutations using this object

* [<\~> reportAlertAsFalsePositiveForAggregations](https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/report-alert-as-false-positive-for-aggregations)
* [<\~> reportAlertAsFalsePositiveForPipelineIssues](https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/report-alert-as-false-positive-for-pipeline-issues)
