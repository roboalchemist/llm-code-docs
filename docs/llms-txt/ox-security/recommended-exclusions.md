# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/recommended-exclusions.md

# recommendedExclusions

Details about recommended exclusions for issues, including reasons, scope, and flags.

### Examples

```graphql
type RecommendedExclusions {
  label: String
  recommended: Boolean
  tooltip: String
  type: String
  id: String
  oxRuleId: String
  level: String
  excludeBy: [String]
  uidOnly: Boolean
  isDefault: Boolean
  ffKey: String
  exclusionScope: String
}
```

### Fields

| Field                   | Description                                                           | Supported fields |
| ----------------------- | --------------------------------------------------------------------- | ---------------- |
| label `String`          | Label or name of the exclusion                                        |                  |
| recommended `Boolean`   | Indicates if the exclusion is recommended                             |                  |
| tooltip `String`        | Tooltip description for the exclusion                                 |                  |
| type `String`           | Type or category of the exclusion                                     |                  |
| id `String`             | Unique identifier of the exclusion                                    |                  |
| oxRuleId `String`       | Rule ID associated with the exclusion                                 |                  |
| level `String`          | Level of exclusion severity or priority                               |                  |
| excludeBy `[String]`    | List of identifiers that exclude this exclusion                       |                  |
| uidOnly `Boolean`       | Indicates if the exclusion is applied only by unique identifier (UID) |                  |
| isDefault `Boolean`     | Indicates if this exclusion is the default                            |                  |
| ffKey `String`          | Feature flag key controlling this exclusion                           |                  |
| exclusionScope `String` | Scope or boundary where this exclusion applies                        |                  |

### References

#### Fields with this object

* [{} Issue.exclusions](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
* [{} Issue.cveExclusions](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
