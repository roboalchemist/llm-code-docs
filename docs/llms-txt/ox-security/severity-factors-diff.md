# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/severity-factors-diff.md

# severityFactorsDiff

Information about the difference in severity factors between scans.

### Examples

```graphql
type SeverityFactorsDiff {
  shortName: String
  change: Float
  status: SeverityFactorStatus
}
```

### Fields

| Field                                                                                                                                   | Description                                 | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ---------------- |
| shortName `String`                                                                                                                      | Short name representing the severity factor |                  |
| change `Float`                                                                                                                          | Magnitude of the change in severity factor  |                  |
| status [`SeverityFactorStatus`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/severity-factor-status) | Status of the severity factor change        |                  |

### References

#### Fields with this object

* [{} Issue.severityFactorsDiff](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
