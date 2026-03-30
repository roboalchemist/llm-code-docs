# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/set-issue-owner-input.md

# setIssueOwnerInput

Input for setting the owner of a security issue.

### Examples

```graphql
input SetIssueOwnerInput {
  issueId: String!
  ownerName: String
  ownerEmail: String!
}
```

### Fields

| Field                | Description                              | Supported fields |
| -------------------- | ---------------------------------------- | ---------------- |
| issueId `String!`    | Unique identifier of the issue to update |                  |
| ownerName `String`   | Name of the new owner (optional)         |                  |
| ownerEmail `String!` | Email of the new owner (required)        |                  |

### References

#### Mutations using this object

* [<\~> setIssueOwner.input](https://docs.ox.security/api-documentation/api-reference/api--issue/mutations/set-issue-owner)
