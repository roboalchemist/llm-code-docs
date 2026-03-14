# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-status-result.md

# issueStatusResult

Result containing issue ID and its status.

### Examples

```graphql
type IssueStatusResult {
  issueId: String!
  status: IssueCollectionStatus
}
```

### Fields

| Field                                                                                                                                     | Description                    | Supported fields |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ---------------- |
| issueId `String!`                                                                                                                         | Unique identifier of the issue |                  |
| status [`IssueCollectionStatus`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issue-collection-status) | Status of the issue            |                  |

### References

#### Queries using this object

* [\<?> getIssuesStatuses](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issues-statuses)
