# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connection-instructions.md

# connectionInstructions

Instructions for setting up a connector.

### Examples

```graphql
type ConnectionInstructions {
  type: CredentialsType
  title: String
  details: [String]
  linksToDocs: [LinkToDocs]
  permissions: [String]
}
```

### Fields

| Field                                                                                                                             | Description                                            | Supported fields                                               |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------- |
| type [`CredentialsType`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/credentials-type)   | Authentication type these instructions apply to        |                                                                |
| title `String`                                                                                                                    | Title of the instruction section                       |                                                                |
| details `[String]`                                                                                                                | Step-by-step setup instructions                        |                                                                |
| linksToDocs [`[LinkToDocs]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/link-to-docs) | An array of links to different releavnt documentations | <p>href <code>String!</code><br>title <code>String!</code></p> |
| permissions `[String]`                                                                                                            | An array of permissions needed for this connector      |                                                                |

### References

#### Fields with this object

* [{} Connector.connectionInstructions](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
