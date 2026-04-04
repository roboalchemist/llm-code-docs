# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/delete-tags-input.md

# deleteTagsInput

Input type for deleting tags with options.

### Examples

```graphql
input DeleteTagsInput {
  filters: DeleteTagsFilter!
}
```

### Fields

| Field                                                                                                                             | Description                                     | Supported fields  |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ----------------- |
| filters [`DeleteTagsFilter!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/delete-tags-filter) | Filter criteria specifying which tags to delete | tagId `[String!]` |

### References

#### Mutations using this object

* [<\~> removeTags.deleteTagsInput](https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/remove-tags)
