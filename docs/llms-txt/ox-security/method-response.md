# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/method-response.md

# methodResponse

HTTP response definition for an API method.

### Examples

```graphql
type MethodResponse {
  description: String
  code: String
}
```

### Fields

| Field                | Description                                  | Supported fields |
| -------------------- | -------------------------------------------- | ---------------- |
| description `String` | Description of what this response represents |                  |
| code `String`        | HTTP status code for this response           |                  |

### References

#### Fields with this object

* [{} ApiSecurityItem.methodResponses](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-item)
