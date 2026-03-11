# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/add-comment-to-issue-input.md

# addCommentToIssueInput

Input for adding a comment to a security issue.

### Examples

```graphql
input addCommentToIssueInput {
  issueId: String!
  comment: String!
}
```

### Fields

| Field             | Description                                  | Supported fields |
| ----------------- | -------------------------------------------- | ---------------- |
| issueId `String!` | Unique identifier of the issue to comment on |                  |
| comment `String!` | Text content of the comment to add           |                  |

### References

#### Mutations using this object

* [<\~> addCommentToIssue.input](https://docs.ox.security/api-documentation/api-reference/api--issue/mutations/add-comment-to-issue)
