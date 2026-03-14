# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/reset-issue-owner-input.md

# resetIssueOwnerInput

Input for resetting the owner of a security issue back to the original automatically calculated owner.

### Examples

```graphql
input ResetIssueOwnerInput {
  issueId: String!
}
```

### Fields

| Field             | Description                                           | Supported fields |
| ----------------- | ----------------------------------------------------- | ---------------- |
| issueId `String!` | Unique identifier of the issue to reset the owner for |                  |

### References

#### Mutations using this object

* [<\~> resetIssueOwner.input](https://docs.ox.security/api-documentation/api-reference/api--issue/mutations/reset-issue-owner)
