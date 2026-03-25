# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/verify-single-credentials-response.md

# verifySingleCredentialsResponse

### Examples

```graphql
type VerifySingleCredentialsResponse {
  credentialsAreValid: Boolean!
  noReposFound: Boolean!
  validationMessage: String
}
```

### Fields

| Field                          | Description | Supported fields |
| ------------------------------ | ----------- | ---------------- |
| credentialsAreValid `Boolean!` |             |                  |
| noReposFound `Boolean!`        |             |                  |
| validationMessage `String`     |             |                  |

### References

#### Mutations using this object

* [<\~> verifySingleConnectorCredentials](https://docs.ox.security/api-documentation/api-reference/api--connectors/mutations/verify-single-connector-credentials)
