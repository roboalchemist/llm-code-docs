# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/exposed-by-api-item.md

# exposedByApiItem

Information about APIs exposing the issue.

### Examples

```graphql
type ExposedByApiItem {
  apiId: String
  codeLocations: [CodeLocation]
}
```

### Fields

| Field                                                                                                                             | Description                                     | Supported fields                                                     |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------- |
| apiId `String`                                                                                                                    | Unique identifier of the API                    |                                                                      |
| codeLocations [`[CodeLocation]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/code-location) | Code locations where the API exposure was found | <p>link <code>String</code><br>callBranch <code>\[String]</code></p> |

### References

#### Fields with this object

* [{} Issue.exposedByApiItems](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
