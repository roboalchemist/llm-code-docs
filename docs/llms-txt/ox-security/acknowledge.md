# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/acknowledge.md

# acknowledge

Response type indicating successful operation completion.

### Examples

```graphql
type Acknowledge {
  acknowledge: Boolean!
}
```

### Fields

| Field                  | Description                                        | Supported fields |
| ---------------------- | -------------------------------------------------- | ---------------- |
| acknowledge `Boolean!` | Boolean indicating if the operation was successful |                  |

### References

#### Mutations using this object

* [<\~> removeTags](https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/remove-tags)
* [<\~> modifyAppsTags](https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/modify-apps-tags)
* [<\~> setAppOwners](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/mutations/set-app-owners)
