# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/prev-severity.md

# prevSeverity

Previous severity data of the issue before it was changed.

### Examples

```graphql
type PrevSeverity {
  severity: String
  severityChangedDate: Date
}
```

### Fields

| Field                      | Description                            | Supported fields |
| -------------------------- | -------------------------------------- | ---------------- |
| severity `String`          | Severity level before the change       |                  |
| severityChangedDate `Date` | Date when the severity change occurred |                  |

### References

#### Fields with this object

* [{} Issue.previousSeverity](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
