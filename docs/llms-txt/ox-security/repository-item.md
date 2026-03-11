# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/repository-item.md

# repositoryItem

Represents a repository associated with the application, including its type and location.

### Examples

```graphql
type RepositoryItem {
  type: String
  system: String
  date: String
  location: [AppFlowItemLocation]
}
```

### Fields

| Field                                                                                                                                              | Description                                                           | Supported fields                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| type `String`                                                                                                                                      | Type of the repository                                                |                                                                                                                            |
| system `String`                                                                                                                                    | System associated with the repository                                 |                                                                                                                            |
| date `String`                                                                                                                                      | Timestamp indicating when the repository information was last updated |                                                                                                                            |
| location [`[AppFlowItemLocation]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-flow-item-location) | Locations where the repository is hosted or deployed                  | <p>runBy <code>String</code><br>foundBy <code>String</code><br>foundIn <code>String</code><br>link <code>String</code></p> |

### References

#### Fields with this object

* [{} ApplicationFlow.repository](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-flow)
