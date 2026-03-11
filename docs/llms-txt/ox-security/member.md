# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/member.md

# member

Represents a user who is a member of an organization, including their profile information and assigned roles.

### Examples

```graphql
type Member {
  user_id: String
  picture: String
  name: String
  email: String
  roles: [Role]
  scopes: String
}
```

### Fields

| Field                                                                                                           | Description                                                     | Supported fields                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| user\_id `String`                                                                                               | Unique identifier of the user                                   |                                                                                                                                   |
| picture `String`                                                                                                | URL to the user's profile picture                               |                                                                                                                                   |
| name `String`                                                                                                   | Full display name of the user                                   |                                                                                                                                   |
| email `String`                                                                                                  | Email address of the user                                       |                                                                                                                                   |
| roles [`[Role]`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/role) | List of roles assigned to this user within the organization     | <p>id <code>String!</code><br>name <code>String!</code><br>description <code>String</code><br>displayName <code>String</code></p> |
| scopes `String`                                                                                                 | Permission scopes assigned to this user within the organization |                                                                                                                                   |

### References

#### Queries using this object

* [\<?> getMembers](https://docs.ox.security/api-documentation/api-reference/api--organization/queries/get-members)
