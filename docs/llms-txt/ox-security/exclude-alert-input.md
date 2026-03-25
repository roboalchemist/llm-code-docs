# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclude-alert-input.md

# excludeAlertInput

Input for excluding an alert.

### Examples

```graphql
input ExcludeAlertInput {
  oxIssueId: String!
  rule: ExclusionRuleInput
  comment: String
  exclusionMode: ExclusionMode
  expiredAt: DateTime
}
```

### Fields

| Field                                                                                                                                   | Description                                                                 | Supported fields                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| oxIssueId `String!`                                                                                                                     | Ox-specific issue identifier                                                |                                                                                                                                                                                         |
| rule [`ExclusionRuleInput`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclusion-rule-input) | Rule configuration for the exclusion                                        | <p>oxRuleId <a href="../enums/ox-exclusion-id"><code>OxExclusionId</code></a><br>aggIds <code>\[String!]</code><br>cvesAndLibs <a href="cve-and-lib"><code>\[CveAndLib!]</code></a></p> |
| comment `String`                                                                                                                        | Comment explaining the exclusion                                            |                                                                                                                                                                                         |
| exclusionMode [`ExclusionMode`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-mode)    | Mode of operation for the exclusion, if not provided full scan mode applies |                                                                                                                                                                                         |
| expiredAt `DateTime`                                                                                                                    | Date when the exclusion expires                                             |                                                                                                                                                                                         |

### References

#### Mutations using this object

* [<\~> excludeAlert.input](https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/exclude-alert)

#### Fields with this object

* [{} ReportFalsePositiveInput.reportedAlertInput](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/report-false-positive-input)
