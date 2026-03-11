# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-item-function.md

# apiSecurityItemFunction

Function-level information for API implementations.

### Examples

```graphql
type ApiSecurityItemFunction {
  function: String
  line: Int
  snippet: String
  filepath: String
  link: String
}
```

### Fields

| Field             | Description                                      | Supported fields |
| ----------------- | ------------------------------------------------ | ---------------- |
| function `String` | Name of the function implementing the API        |                  |
| line `Int`        | Line number where the function is defined        |                  |
| snippet `String`  | Code snippet showing the function implementation |                  |
| filepath `String` | File path where the function is located          |                  |
| link `String`     | URL link to view the function in the repository  |                  |

### References

#### Fields with this object

* [{} APIDefinitions.functions](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-definitions)
