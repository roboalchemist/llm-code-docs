# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-credentials.md

# tokenCredentials

Credentials using a token for authentication.

### Examples

```graphql
type TokenCredentials {
  token: String
  optionalFields: OptionalFields
  extraOptionalCreds: ExtraOptionalCreds
  credentialsId: String
  credentialsName: String
  tokenExpirationDate: String
  credentialsType: CredentialsType
  isCertChecksDisabled: Boolean
  hostURL: String
  iv: String
  monitoredResources: JSON
  monitorAllResources: Boolean
  monitorAllNewlyCreatedResources: Float
  brokerUsername: String
  brokerPassword: String
  brokerEnabled: Boolean
  brokerHost: String
  brokerPort: Int
}
```

### Fields

| Field                                                                                                                                                  | Description                                             | Supported fields                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| token `String`                                                                                                                                         | Authentication token                                    |                                                                                                                                                   |
| optionalFields [`OptionalFields`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/optional-fields)              | Additional optional configuration fields                | <p>SSHKey <code>String</code><br>RepoSearchQuery <code>String</code><br>Config <code>String</code><br>buildIssueToCloud <code>Boolean</code></p>  |
| extraOptionalCreds [`ExtraOptionalCreds`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/extra-optional-creds) | Extra optional credentials for specific services        | atlassian [`AtlassianCredsOutput`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/atlassian-creds-output) |
| credentialsId `String`                                                                                                                                 |                                                         |                                                                                                                                                   |
| credentialsName `String`                                                                                                                               |                                                         |                                                                                                                                                   |
| tokenExpirationDate `String`                                                                                                                           |                                                         |                                                                                                                                                   |
| credentialsType [`CredentialsType`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/credentials-type)             |                                                         |                                                                                                                                                   |
| isCertChecksDisabled `Boolean`                                                                                                                         | Indicates if SSL/TLS certificate validation is disabled |                                                                                                                                                   |
| hostURL `String`                                                                                                                                       |                                                         |                                                                                                                                                   |
| iv `String`                                                                                                                                            |                                                         |                                                                                                                                                   |
| monitoredResources `JSON`                                                                                                                              |                                                         |                                                                                                                                                   |
| monitorAllResources `Boolean`                                                                                                                          |                                                         |                                                                                                                                                   |
| monitorAllNewlyCreatedResources `Float`                                                                                                                |                                                         |                                                                                                                                                   |
| brokerUsername `String`                                                                                                                                |                                                         |                                                                                                                                                   |
| brokerPassword `String`                                                                                                                                |                                                         |                                                                                                                                                   |
| brokerEnabled `Boolean`                                                                                                                                |                                                         |                                                                                                                                                   |
| brokerHost `String`                                                                                                                                    |                                                         |                                                                                                                                                   |
| brokerPort `Int`                                                                                                                                       |                                                         |                                                                                                                                                   |

### References

#### Fields with this object

* [{} Credential](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/unions/credential)
