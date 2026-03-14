# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/app-tag-object.md

# appTagObject

Represents a tag associated with an application.

### Examples

```graphql
type AppTagObject {
  tagType: OxTagType!
  appId: String!
  tagId: String!
  appliedBy: String
  roles: [AppOwnerRole!]
  tag: TagObject
}
```

### Fields

| Field                                                                                                                           | Description                                              | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tagType [`OxTagType!`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/ox-tag-type)       | Type of the tag (e.g., simple, githubTopic, gitlabGroup) |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| appId `String!`                                                                                                                 | Identifier of the application                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| tagId `String!`                                                                                                                 | Identifier of the tag                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| appliedBy `String`                                                                                                              | Identifier of the user who applied the tag               |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| roles [`[AppOwnerRole!]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-owner-role) | Roles associated with this app tag                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| tag [`TagObject`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/tag-object)                  | The complete tag object with all its details             | <p>tagId <code>String!</code><br>name <code>String!</code><br>displayName <code>String!</code><br>tagType <a href="../../../api--application/types/enums/ox-tag-type"><code>OxTagType!</code></a><br>createdBy <code>String!</code><br>createdAt <code>DateTime</code><br>updatedAt <code>DateTime</code><br>tagCategory <code>String</code><br>deploymentModel <code>String</code><br>purpose <code>String</code><br>email <code>String</code></p> |

### References

#### Fields with this object

* [{} GetAppsTagsRes.appsTags](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/get-apps-tags-res)
