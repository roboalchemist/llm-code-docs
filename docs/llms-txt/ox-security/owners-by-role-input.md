# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/owners-by-role-input.md

# ownersByRoleInput

Input type defining owners for a specific role.

### Examples

```graphql
input OwnersByRoleInput {
  role: AppOwnerRole!
  owners: [UserInputDTO!]!
}
```

### Fields

| Field                                                                                                                                      | Description                         | Supported fields                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ----------------------------------------------------------------------------------------------- |
| role [`AppOwnerRole!`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-owner-role)               | Role to assign to the owners        |                                                                                                 |
| owners [`[UserInputDTO!]!`](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/user-input-dto) | List of users to assign to the role | <p>name <code>String</code><br>email <code>String</code><br>appIds <code>\[String!]!</code></p> |

### References

#### Fields with this object

* [{} SetApplicationsOwnersByRoleInput.ownersByRoleInput](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/set-applications-owners-by-role-input)
