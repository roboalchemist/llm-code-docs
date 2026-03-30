# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/owner-info.md

# ownerInfo

Information about an application owner, including their roles and contact details.

### Examples

```graphql
type OwnerInfo {
  name: String
  email: String
  roles: [AppOwnerRole]
}
```

### Fields

| Field                                                                                                                          | Description                  | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ---------------- |
| name `String`                                                                                                                  | Name of the owner            |                  |
| email `String`                                                                                                                 | Email address of the owner   |                  |
| roles [`[AppOwnerRole]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-owner-role) | Roles assigned to this owner |                  |

### References

#### Queries using this object

* [\<?> getAppOwners](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/queries/get-app-owners)

#### Fields with this object

* [{} Application.appOwners](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
* [{} IAppsInfo.owners](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/i-apps-info)
