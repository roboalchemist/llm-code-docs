# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-definitions.md

# apiDefinitions

API definition details including source files and AI-generated documentation.

### Examples

```graphql
type APIDefinitions {
  source: String
  fileName: String
  link: String
  llmTitle: String
  llmDescription: String
  functions: [ApiSecurityItemFunction]
}
```

### Fields

| Field                                                                                                                                                        | Description                                       | Supported fields                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| source `String`                                                                                                                                              | Source of the API definition                      |                                                                                                                                                         |
| fileName `String`                                                                                                                                            | Name of the file containing the API definition    |                                                                                                                                                         |
| link `String`                                                                                                                                                | URL link to the API definition file               |                                                                                                                                                         |
| llmTitle `String`                                                                                                                                            | AI-generated title for the API                    |                                                                                                                                                         |
| llmDescription `String`                                                                                                                                      | AI-generated description of the API functionality |                                                                                                                                                         |
| functions [`[ApiSecurityItemFunction]`](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-item-function) | List of functions that implement this API         | <p>function <code>String</code><br>line <code>Int</code><br>snippet <code>String</code><br>filepath <code>String</code><br>link <code>String</code></p> |

### References

#### Fields with this object

* [{} ApiSecurityItem.definitions](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-item)
