# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/excluded-issue.md

# excludedIssue

Represents a security issue that has been excluded from scanning or reporting.

### Examples

```graphql
type ExcludedIssue {
  appNames: [String!]
  issueId: String!
  issueName: String!
  categoryName: String!
  comment: String
  expiredAt: String
}
```

### Fields

| Field                  | Description                                        | Supported fields |
| ---------------------- | -------------------------------------------------- | ---------------- |
| appNames `[String!]`   | Names of applications where this issue is excluded |                  |
| issueId `String!`      | Unique identifier of the excluded issue            |                  |
| issueName `String!`    | Name or title of the excluded issue                |                  |
| categoryName `String!` | Category of the excluded issue                     |                  |
| comment `String`       | Reason or justification for excluding this issue   |                  |
| expiredAt `String`     | Date when this exclusion will expire               |                  |

### References

#### Fields with this object

* [{} AuditLog.excludedIssues](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)
