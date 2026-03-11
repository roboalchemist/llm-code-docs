# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/user-password-credentials.md

# userPasswordCredentials

Credentials using username and password with additional fields.

### Examples

```graphql
type UserPasswordCredentials {
  name: String
  password: String
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
| name `String`                                                                                                                                          | Username for authentication                             |                                                                                                                                                   |
| password `String`                                                                                                                                      | Password for authentication                             |                                                                                                                                                   |
| extraOptionalCreds [`ExtraOptionalCreds`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/extra-optional-creds) |                                                         | atlassian [`AtlassianCredsOutput`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/atlassian-creds-output) |
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
