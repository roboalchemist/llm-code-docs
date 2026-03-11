# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/update-member-response.md

# updateMemberResponse

### Examples

```graphql
type UpdateMemberResponse {
  userId: String!
  roleIDs: [String]
  scopes: String
}
```

### Fields

| Field              | Description                                    | Supported fields |
| ------------------ | ---------------------------------------------- | ---------------- |
| userId `String!`   | user ID                                        |                  |
| roleIDs `[String]` | list of roles assigned for the user            |                  |
| scopes `String`    | list of scopes assigned for the user as string |                  |

### References

#### Mutations using this object

* [<\~> updateMember](https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/update-member)
