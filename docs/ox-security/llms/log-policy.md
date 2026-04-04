# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/log-policy.md

# logPolicy

Represents a security policy configuration and its current state.

### Examples

```graphql
type LogPolicy {
  policyId: String
  policyName: String
  categoryName: String
  enabled: Boolean
  severity: String
  oldIssues: String
  newIssues: String
  args: String
}
```

### Fields

| Field                 | Description                                         | Supported fields |
| --------------------- | --------------------------------------------------- | ---------------- |
| policyId `String`     | Unique identifier of the security policy            |                  |
| policyName `String`   | Human-readable name of the security policy          |                  |
| categoryName `String` | Category or group this policy belongs to            |                  |
| enabled `Boolean`     | Whether this policy is currently active             |                  |
| severity `String`     | Severity level of policy violations                 |                  |
| oldIssues `String`    | Previous security issues before policy modification |                  |
| newIssues `String`    | Current security issues after policy modification   |                  |
| args `String`         | Policy configuration arguments                      |                  |

### References

#### Fields with this object

* [{} AuditLog.policies](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)
