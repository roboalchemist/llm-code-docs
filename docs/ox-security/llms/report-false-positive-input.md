# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/report-false-positive-input.md

# reportFalsePositiveInput

Input for reporting a false positive alert.

### Examples

```graphql
input ReportFalsePositiveInput {
  reportedAlertInput: ExcludeAlertInput!
  isExclude: Boolean!
}
```

### Fields

| Field                                                                                                                                                | Description                                            | Supported fields                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| reportedAlertInput [`ExcludeAlertInput!`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclude-alert-input) | Alert to report as false positive                      | <p>oxIssueId <code>String!</code><br>rule <a href="exclusion-rule-input"><code>ExclusionRuleInput</code></a><br>comment <code>String</code><br>exclusionMode <a href="../enums/exclusion-mode"><code>ExclusionMode</code></a><br>expiredAt <code>DateTime</code></p> |
| isExclude `Boolean!`                                                                                                                                 | Whether to create an exclusion for this false positive |                                                                                                                                                                                                                                                                      |

### References

#### Mutations using this object

* [<\~> reportAlertAsFalsePositiveForAggregations.input](https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/report-alert-as-false-positive-for-aggregations)
* [<\~> reportAlertAsFalsePositiveForPipelineIssues.input](https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/report-alert-as-false-positive-for-pipeline-issues)
