# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/i-owner.md

# iOwner

List of owners associated with an issue.

### Examples

```graphql
type IOwner {
  name: String
  email: String
}
```

### Fields

| Field          | Description        | Supported fields |
| -------------- | ------------------ | ---------------- |
| name `String`  | Name of the owner  |                  |
| email `String` | Email of the owner |                  |

### References

#### Fields with this object

* [{} Issue.issueOwners](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
* [{} Issue.originalIssueOwners](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
