# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/remove-credentials-input.md

# removeCredentialsInput

Input object for removing credentials from a connector.

### Examples

```graphql
input RemoveCredentialsInput {
  connectorID: String!
  credentialsIndex: Int
  credentialsId: String
}
```

### Fields

| Field                  | Description                                                   | Supported fields |
| ---------------------- | ------------------------------------------------------------- | ---------------- |
| connectorID `String!`  | Unique identifier of the connector to remove credentials from |                  |
| credentialsIndex `Int` | Index of the credentials to remove in the credentials array   |                  |
| credentialsId `String` | Unique identifier of the credentials to remove.               |                  |

### References

#### Mutations using this object

* [<\~> removeCredentials.removeCredentialsInput](https://docs.ox.security/api-documentation/api-reference/api--connectors/mutations/remove-credentials)
