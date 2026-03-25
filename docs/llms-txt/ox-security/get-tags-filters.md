# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-tags-filters.md

# getTagsFilters

Filter criteria for querying tags.

### Examples

```graphql
input GetTagsFilters {
  tagType: [OxTagType!]
  tagId: [String!]
}
```

### Fields

| Field                                                                                                                       | Description                  | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------- |
| tagType [`[OxTagType!]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/ox-tag-type) | Filter by tag type(s)        |                  |
| tagId `[String!]`                                                                                                           | Filter by specific tag ID(s) |                  |

### References

#### Fields with this object

* [{} GetTagsInput.filters](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-tags-input)
