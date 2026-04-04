# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/get-app-owners-by-app-ids-and-role-input.md

# getAppOwnersByAppIdsAndRoleInput

Input for retrieving app owners by application IDs and roles.

### Examples

```graphql
input GetAppOwnersByAppIdsAndRoleInput {
  appIds: [String!]!
  roles: [AppOwnerRole!]!
}
```

### Fields

| Field                                                                                                                            | Description                      | Supported fields |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ---------------- |
| appIds `[String!]!`                                                                                                              | List of application IDs to query |                  |
| roles [`[AppOwnerRole!]!`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-owner-role) | List of roles to filter by       |                  |

### References

#### Queries using this object

* [\<?> getAppOwnersByAppIdsAndRole.input](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/queries/get-app-owners-by-app-ids-and-role)
