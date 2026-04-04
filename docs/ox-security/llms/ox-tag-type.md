# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/ox-tag-type.md

# oxTagType

Types of tags that can be applied to applications.

### Examples

```graphql
enum OxTagType {
  simple
  owner
  ox
  githubTopic
  gitlabGroup
  bitbucketProject
}
```

### Enum values

| Enum value       | Description                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------ |
| simple           | User-defined tags that can be freely created and managed by users                                            |
| owner            | Represents ownership of an application, used to associate users with specific roles to applications          |
| ox               | System-defined tags managed by the OX platform, used for categorizing applications, frameworks, and services |
| githubTopic      | Tags imported from GitHub repository topics, used for repository categorization                              |
| gitlabGroup      | Tags representing GitLab group associations, used for organizing repositories                                |
| bitbucketProject | Tags representing Bitbucket project associations, used for project organization                              |

### References

#### Fields with this object

* [{} AppTag.tagType](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-tag)
* [{} GetTagsFilters.tagType](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-tags-filters)
* [{} TagObject.tagType](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/tag-object)
* [{} GetAppsTagsInputFilter.tagType](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-apps-tags-input-filter)
* [{} AppTagObject.tagType](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/app-tag-object)
* [{} TagDTO.tagType](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/tag-dto)
