# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-apps-tags-input.md

# getAppsTagsInput

Input type for querying application tags with filtering and pagination options.

### Examples

```graphql
input GetAppsTagsInput {
  filters: GetAppsTagsInputFilter
}
```

### Fields

| Field                                                                                                                                          | Description                   | Supported fields                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filters [`GetAppsTagsInputFilter`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-apps-tags-input-filter) | Filter criteria for the query | <p>appId <code>\[String!]</code><br>tagId <code>\[String!]</code><br>tagType <a href="../../../api--application/types/enums/ox-tag-type"><code>\[OxTagType!]</code></a></p> |

### References

#### Queries using this object

* [\<?> getAppTags.getAppsTagsInput](https://docs.ox.security/api-documentation/api-reference/api--tags/queries/get-app-tags)
