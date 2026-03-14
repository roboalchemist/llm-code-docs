# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/tag-object.md

# tagObject

Represents a tag entity with its complete metadata including type, category, and ownership information.

### Examples

```graphql
type TagObject {
  tagId: String!
  name: String!
  displayName: String!
  tagType: OxTagType!
  createdBy: String!
  createdAt: DateTime
  updatedAt: DateTime
  tagCategory: String
  deploymentModel: String
  purpose: String
  email: String
}
```

### Fields

| Field                                                                                                                     | Description                                              | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ---------------- |
| tagId `String!`                                                                                                           | Unique identifier for the tag used across the system     |                  |
| name `String!`                                                                                                            | Internal name of the tag used for system operations      |                  |
| displayName `String!`                                                                                                     | Human-readable name of the tag shown in the UI           |                  |
| tagType [`OxTagType!`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/ox-tag-type) | Type of the tag (e.g., simple, githubTopic, gitlabGroup) |                  |
| createdBy `String!`                                                                                                       | Identifier of the user who created the tag               |                  |
| createdAt `DateTime`                                                                                                      | Timestamp when the tag was created                       |                  |
| updatedAt `DateTime`                                                                                                      | Timestamp when the tag was last updated                  |                  |
| tagCategory `String`                                                                                                      | Category classification of the tag                       |                  |
| deploymentModel `String`                                                                                                  | Deployment model associated with the tag                 |                  |
| purpose `String`                                                                                                          | Purpose or intended use of the tag                       |                  |
| email `String`                                                                                                            | Email address associated with the tag owner              |                  |

### References

#### Fields with this object

* [{} GetAllTagsResponse.tags](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/get-all-tags-response)
* [{} AppTagObject.tag](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/app-tag-object)
* [{} AddTagRes.tags](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/add-tag-res)
