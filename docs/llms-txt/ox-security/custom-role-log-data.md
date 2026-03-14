# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/custom-role-log-data.md

# customRoleLogData

Custom Role audit log event details.

### Examples

```graphql
type customRoleLogData {
  name: String!
  displayName: String!
  assignablePermissions: [AssignablePermission!]
}
```

### Fields

| Field                                                                                                                                                      | Description                                       | Supported fields                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------ |
| name `String!`                                                                                                                                             | Auth0 role name                                   |                                                                    |
| displayName `String!`                                                                                                                                      | Role name provided by user                        |                                                                    |
| assignablePermissions [`[AssignablePermission!]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/assignable-permission) | List of permissions assignable to the custom role | <p>name <code>String!</code><br>isHidden <code>Boolean!</code></p> |

### References

#### Fields with this object

* [{} AuditLog.customRoleLogData](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)
