# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/get-issue-status-input.md

# getIssueStatusInput

Input for getting the status of issues.

### Examples

```graphql
input GetIssueStatusInput {
  issueIds: [String!]!
}
```

### Fields

| Field                 | Description                               | Supported fields |
| --------------------- | ----------------------------------------- | ---------------- |
| issueIds `[String!]!` | Array of unique identifiers of the issues |                  |

### References

#### Queries using this object

* [\<?> getIssuesStatuses.getIssuesStatusesInput](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issues-statuses)
