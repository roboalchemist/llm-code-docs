# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/code-location.md

# codeLocation

Information about where API code is located in the repository.

### Examples

```graphql
type CodeLocation {
  link: String
  callBranch: [String]
}
```

### Fields

| Field                 | Description                                                           | Supported fields |
| --------------------- | --------------------------------------------------------------------- | ---------------- |
| link `String`         | URL or path link to the relevant code location                        |                  |
| callBranch `[String]` | List of branch names where this code location is called or referenced |                  |

### References

#### Fields with this object

* [{} ExposedByApiItem.codeLocations](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/exposed-by-api-item)
* [{} ApiSecurityItem.codeLocations](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-item)
