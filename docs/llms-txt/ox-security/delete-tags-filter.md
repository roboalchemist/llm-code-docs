# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/delete-tags-filter.md

# deleteTagsFilter

Filter criteria for deleting tags.

### Examples

```graphql
input DeleteTagsFilter {
  tagId: [String!]
}
```

### Fields

| Field             | Description                    | Supported fields |
| ----------------- | ------------------------------ | ---------------- |
| tagId `[String!]` | Array of tag IDs to be deleted |                  |

### References

#### Fields with this object

* [{} DeleteTagsInput.filters](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/delete-tags-input)
