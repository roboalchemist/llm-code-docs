# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/objects/get-app-owners-by-app-ids-and-role-res.md

# getAppOwnersByAppIdsAndRoleRes

Response type containing app owners filtered by role.

### Examples

```graphql
type GetAppOwnersByAppIdsAndRoleRes {
  role: AppOwnerRole!
  owners: [AppOwner!]!
}
```

### Fields

| Field                                                                                                                              | Description                                | Supported fields                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| role [`AppOwnerRole!`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-owner-role)       | Role for which owners were retrieved       |                                                                                                   |
| owners [`[AppOwner!]!`](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/objects/app-owner) | List of app owners with the specified role | <p>name <code>String!</code><br>email <code>String!</code><br>appIds <code>\[String!]!</code></p> |

### References

#### Queries using this object

* [\<?> getAppOwnersByAppIdsAndRole](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/queries/get-app-owners-by-app-ids-and-role)
