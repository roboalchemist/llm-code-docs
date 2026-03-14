# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/add-tag-input.md

# addTagInput

Input type for creating multiple tags in a single operation.

### Examples

```graphql
input AddTagInput {
  tagsInput: [TagDTO!]!
}
```

### Fields

| Field                                                                                                             | Description                        | Supported fields                                                                                  |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------- |
| tagsInput [`[TagDTO!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/tag-dto) | Array of tag objects to be created | <p>name <code>String!</code><br>displayName <code>String!</code><br>tagId <code>String</code></p> |

### References

#### Mutations using this object

* [<\~> addTags.input](https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/add-tags)
