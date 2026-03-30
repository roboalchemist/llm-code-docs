# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-apps-tags-input-filter.md

# getAppsTagsInputFilter

Filter criteria for querying application tags.

### Examples

```graphql
input GetAppsTagsInputFilter {
  appId: [String!]
  tagId: [String!]
  tagType: [OxTagType!]
}
```

### Fields

| Field                                                                                                                       | Description                 | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ---------------- |
| appId `[String!]`                                                                                                           | Filter by application ID(s) |                  |
| tagId `[String!]`                                                                                                           | Filter by tag ID(s)         |                  |
| tagType [`[OxTagType!]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/ox-tag-type) | Filter by tag type(s)       |                  |

### References

#### Fields with this object

* [{} GetAppsTagsInput.filters](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-apps-tags-input)
