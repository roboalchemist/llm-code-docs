# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/objects/app-owner.md

# appOwner

Represents an application owner with their associated applications.

### Examples

```graphql
type AppOwner {
  name: String!
  email: String!
  appIds: [String!]!
}
```

### Fields

| Field               | Description                                | Supported fields |
| ------------------- | ------------------------------------------ | ---------------- |
| name `String!`      | Name of the application owner              |                  |
| email `String!`     | Email address of the application owner     |                  |
| appIds `[String!]!` | List of application IDs owned by this user |                  |

### References

#### Fields with this object

* [{} GetAppOwnersByAppIdsAndRoleRes.owners](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/objects/get-app-owners-by-app-ids-and-role-res)
