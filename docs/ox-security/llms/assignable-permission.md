# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/assignable-permission.md

# assignablePermission

Represents a permission selected by user.

### Examples

```graphql
type AssignablePermission {
  name: String!
  isHidden: Boolean!
}
```

### Fields

| Field               | Description                               | Supported fields |
| ------------------- | ----------------------------------------- | ---------------- |
| name `String!`      | User friendly name of selected permission |                  |
| isHidden `Boolean!` | Auto provisioned hidden permission        |                  |

### References

#### Fields with this object

* [{} customRoleLogData.assignablePermissions](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/custom-role-log-data)
