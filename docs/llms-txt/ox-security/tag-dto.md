# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/tag-dto.md

# tagDto

Input type for creating or updating a single tag.

### Examples

```graphql
input TagDTO {
  name: String!
  displayName: String!
  tagId: String
}
```

### Fields

| Field                 | Description                                                       | Supported fields |
| --------------------- | ----------------------------------------------------------------- | ---------------- |
| name `String!`        | Internal name of the tag used for system operations               |                  |
| displayName `String!` | Human-readable name of the tag shown in the UI                    |                  |
| tagId `String`        | Unique identifier for the tag. If not provided, will be generated |                  |

### References

#### Fields with this object

* [{} AddTagInput.tagsInput](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/add-tag-input)
