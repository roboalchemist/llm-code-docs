# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/method-parameter.md

# methodParameter

Parameter definition for an API method.

### Examples

```graphql
type MethodParameter {
  description: String
  in: String
  name: String
  required: Boolean
}
```

### Fields

| Field                | Description                                           | Supported fields |
| -------------------- | ----------------------------------------------------- | ---------------- |
| description `String` | Description of what this parameter is used for        |                  |
| in `String`          | Location of the parameter (query, path, header, body) |                  |
| name `String`        | Name of the parameter                                 |                  |
| required `Boolean`   | Whether this parameter is required for the API call   |                  |

### References

#### Fields with this object

* [{} ApiSecurityItem.methodParameters](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-item)
