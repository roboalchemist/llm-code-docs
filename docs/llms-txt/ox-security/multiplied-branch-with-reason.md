# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/multiplied-branch-with-reason.md

# multipliedBranchWithReason

Represents a branch selection with the reason for its inclusion in pipeline scanning.

### Examples

```graphql
type MultipliedBranchWithReason {
  branch: String!
  reason: String!
}
```

### Fields

| Field            | Description                                               | Supported fields |
| ---------------- | --------------------------------------------------------- | ---------------- |
| branch `String!` | Name or pattern of the selected branch                    |                  |
| reason `String!` | Explanation for why this branch was selected for scanning |                  |

### References

#### Fields with this object

* [{} AuditLog.branches](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)
