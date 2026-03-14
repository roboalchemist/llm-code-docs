# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-tag.md

# appTag

Represents a tag associated with an application, including user and system-generated tags.

### Examples

```graphql
type AppTag {
  tagId: String
  name: String
  email: String
  displayName: String
  tagType: OxTagType
  createdBy: String
  purpose: String
  deploymentModel: String
  tagCategory: String
}
```

### Fields

| Field                                                                                                                    | Description                                                      | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- | ---------------- |
| tagId `String`                                                                                                           | The unique identifier of the tag                                 |                  |
| name `String`                                                                                                            | The name of the tag                                              |                  |
| email `String`                                                                                                           | The email of the user associated with the tag                    |                  |
| displayName `String`                                                                                                     | The display name of the tag                                      |                  |
| tagType [`OxTagType`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/ox-tag-type) | The type of the tag as defined by Ox                             |                  |
| createdBy `String`                                                                                                       | The user who created the tag                                     |                  |
| purpose `String`                                                                                                         | The purpose of the tag, such as 'Classification' or 'Monitoring' |                  |
| deploymentModel `String`                                                                                                 | The deployment model associated with the tag                     |                  |
| tagCategory `String`                                                                                                     | The category of the tag                                          |                  |

### References

#### Fields with this object

* [{} Application.tags](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
* [{} Issue.tags](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
