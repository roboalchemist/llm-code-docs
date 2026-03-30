# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/verify-credentials-input.md

# verifyCredentialsInput

Input object for verifying credentials of a connector.

### Examples

```graphql
input VerifyCredentialsInput {
  connectorID: String!
  credentialsID: String
  featureFlags: JSON
}
```

### Fields

| Field                  | Description                                               | Supported fields |
| ---------------------- | --------------------------------------------------------- | ---------------- |
| connectorID `String!`  | The id of the connector we want to verify credentials for |                  |
| credentialsID `String` |                                                           |                  |
| featureFlags `JSON`    | Object with feature flags passed from FE                  |                  |

### References

#### Mutations using this object

* [<\~> verifySingleConnectorCredentials.verifyCredentialsInput](https://docs.ox.security/api-documentation/api-reference/api--connectors/mutations/verify-single-connector-credentials)
