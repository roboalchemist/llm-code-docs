# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/owner.md

# owner

Represents an application owner with their associated roles and permissions.

### Examples

```graphql
type Owner {
  owner: String
  email: String
  roles: [String!]
}
```

### Fields

| Field             | Description                          | Supported fields |
| ----------------- | ------------------------------------ | ---------------- |
| owner `String`    | Identifier of the owner              |                  |
| email `String`    | Email address of the owner           |                  |
| roles `[String!]` | List of roles assigned to this owner |                  |

### References

#### Fields with this object

* [{} AuditLog.ownersWithRoles](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)
