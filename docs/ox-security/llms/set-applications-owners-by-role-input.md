# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/set-applications-owners-by-role-input.md

# setApplicationsOwnersByRoleInput

Input type for setting application owners by role.

### Examples

```graphql
input SetApplicationsOwnersByRoleInput {
  ownersByRoleInput: [OwnersByRoleInput!]!
}
```

### Fields

| Field                                                                                                                                                            | Description                          | Supported fields                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ownersByRoleInput [`[OwnersByRoleInput!]!`](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/owners-by-role-input) | List of role-based owner assignments | <p>role <a href="../../../api--application/types/enums/app-owner-role"><code>AppOwnerRole!</code></a><br>owners <a href="user-input-dto"><code>\[UserInputDTO!]!</code></a></p> |

### References

#### Mutations using this object

* [<\~> setAppOwners.input](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/mutations/set-app-owners)
