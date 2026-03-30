# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/role.md

# role

Represents a role that can be assigned to organization members, defining their permissions and access levels.

### Examples

```graphql
type Role {
  id: String!
  name: String!
  description: String
  displayName: String
}
```

### Fields

| Field                | Description                                                | Supported fields |
| -------------------- | ---------------------------------------------------------- | ---------------- |
| id `String!`         | Unique identifier of the role                              |                  |
| name `String!`       | Auth0 name of the role                                     |                  |
| description `String` | Detailed description of the role's purpose and permissions |                  |
| displayName `String` | Human-readable name of the role                            |                  |

### References

#### Queries using this object

* [\<?> getGlobalRoles](https://docs.ox.security/api-documentation/api-reference/api--organization/queries/get-global-roles)

#### Fields with this object

* [{} Member.roles](https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/member)
