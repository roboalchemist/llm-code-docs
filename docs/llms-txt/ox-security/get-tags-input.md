# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-tags-input.md

# getTagsInput

Input type for querying tags with pagination and filter options.

### Examples

```graphql
input GetTagsInput {
  filters: GetTagsFilters
}
```

### Fields

| Field                                                                                                                        | Description                       | Supported fields                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| filters [`GetTagsFilters`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-tags-filters) | Filter criteria for the tag query | <p>tagType <a href="../../../api--application/types/enums/ox-tag-type"><code>\[OxTagType!]</code></a><br>tagId <code>\[String!]</code></p> |

### References

#### Queries using this object

* [\<?> getAllTags.input](https://docs.ox.security/api-documentation/api-reference/api--tags/queries/get-all-tags)
