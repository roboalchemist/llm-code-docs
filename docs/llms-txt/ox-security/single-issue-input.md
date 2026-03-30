# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/single-issue-input.md

# singleIssueInput

Input for retrieving information about a single security issue.

### Examples

```graphql
input SingleIssueInput {
  issueId: String!
  scanId: String
}
```

### Fields

| Field             | Description                                         | Supported fields |
| ----------------- | --------------------------------------------------- | ---------------- |
| issueId `String!` | Unique identifier of the issue to retrieve          |                  |
| scanId `String`   | Specific scan identifier to retrieve the issue from |                  |

### References

#### Queries using this object

* [\<?> getSingleIssueInfo.getSingleIssueInput](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-single-issue-info)
* [\<?> getResolvedIssue.getSingleIssueInput](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-resolved-issue)
* [\<?> getCICDIssue.getSingleIssueInput](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/queries/get-cicd-issue)
