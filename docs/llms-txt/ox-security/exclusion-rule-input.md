# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclusion-rule-input.md

# exclusionRuleInput

Input for exclusion rule configuration.

### Examples

```graphql
input ExclusionRuleInput {
  oxRuleId: OxExclusionId
  aggIds: [String!]
  cvesAndLibs: [CveAndLib!]
}
```

### Fields

| Field                                                                                                                            | Description                                                                                      | Supported fields                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| oxRuleId [`OxExclusionId`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/ox-exclusion-id) | Identifier for the exclusion rule type, if not provided Issue-based exclusion identifier applies |                                                                                                    |
| aggIds `[String!]`                                                                                                               | List of aggregation IDs to exclude, if not provided will exclude all the issue aggregations      |                                                                                                    |
| cvesAndLibs [`[CveAndLib!]`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/cve-and-lib)  | cves and libs to exclude                                                                         | <p>cve <code>String!</code><br>libName <code>String!</code><br>libVersion <code>String!</code></p> |

### References

#### Fields with this object

* [{} ExcludeAlertInput.rule](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclude-alert-input)
