# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/recipient.md

# recipient

Recipient of messages related to an issue.

### Examples

```graphql
type Recipient {
  name: String!
  id: String!
  type: String!
}
```

### Fields

| Field          | Description                        | Supported fields |
| -------------- | ---------------------------------- | ---------------- |
| name `String!` | Name of the recipient              |                  |
| id `String!`   | Unique identifier of the recipient |                  |
| type `String!` | Type of recipient                  |                  |

### References

#### Fields with this object

* [{} IssueMessage.recipients](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-message)
