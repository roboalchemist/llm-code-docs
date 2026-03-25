# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/modify-apps-tags-input.md

# modifyAppsTagsInput

Input for modifying tags associated with applications.

### Examples

```graphql
input ModifyAppsTagsInput {
  appIds: [String!]!
  addedTagsIds: [String!]!
  removedTagsIds: [String!]!
}
```

### Fields

| Field                       | Description                                     | Supported fields |
| --------------------------- | ----------------------------------------------- | ---------------- |
| appIds `[String!]!`         | List of application IDs to modify               |                  |
| addedTagsIds `[String!]!`   | List of tag IDs to add to the applications      |                  |
| removedTagsIds `[String!]!` | List of tag IDs to remove from the applications |                  |

### References

#### Mutations using this object

* [<\~> modifyAppsTags.input](https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/modify-apps-tags)
