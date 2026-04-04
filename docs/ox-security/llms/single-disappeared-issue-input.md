# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/single-disappeared-issue-input.md

# singleDisappearedIssueInput

Input parameters for retrieving a single disappeared issue.

### Examples

```graphql
input SingleDisappearedIssueInput {
  issueId: String!
}
```

### Fields

| Field             | Description                                            | Supported fields |
| ----------------- | ------------------------------------------------------ | ---------------- |
| issueId `String!` | Unique identifier of the disappeared issue to retrieve |                  |

### References

#### Queries using this object

* [\<?> getRemovedIssue.getSingleRemovedIssueInput](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-removed-issue)
