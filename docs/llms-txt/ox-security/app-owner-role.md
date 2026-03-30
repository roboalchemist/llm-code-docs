# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-owner-role.md

# appOwnerRole

Roles that can be assigned to application owners.

### Examples

```graphql
enum AppOwnerRole {
  Dev
  Business
  Security
  Watcher
}
```

### Enum values

| Enum value | Description                                                   |
| ---------- | ------------------------------------------------------------- |
| Dev        | Development team member responsible for code                  |
| Business   | Business stakeholder responsible for application requirements |
| Security   | Security team member responsible for application security     |
| Watcher    | User with read-only access to monitor the application         |

### References

#### Fields with this object

* [{} OwnerInfo.roles](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/owner-info)
* [{} GetAppsTagsInputFilter.roles](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-apps-tags-input-filter)
* [{} AppTagObject.roles](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/app-tag-object)
* [{} GetAppOwnersByAppIdsAndRoleInput.roles](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/get-app-owners-by-app-ids-and-role-input)
* [{} GetAppOwnersByAppIdsAndRoleRes.role](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/objects/get-app-owners-by-app-ids-and-role-res)
* [{} OwnersByRoleInput.role](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/owners-by-role-input)
