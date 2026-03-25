# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issue-collection-status.md

# issueCollectionStatus

Status of an issue based on which collection it exists in.

### Examples

```graphql
enum IssueCollectionStatus {
  Active
  Resolved
}
```

### Enum values

| Enum value | Description                               |
| ---------- | ----------------------------------------- |
| Active     | Issue is in the current issues collection |
| Resolved   | Issue is in the fixed issues collection   |

### References

#### Fields with this object

* [{} IssueStatusResult.status](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-status-result)
