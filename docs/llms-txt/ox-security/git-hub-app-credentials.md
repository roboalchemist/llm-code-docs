# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/git-hub-app-credentials.md

# gitHubAppCredentials

Credentials for GitHub App authentication.

### Examples

```graphql
type GitHubAppCredentials {
  gitHubAppId: String
  gitHubAppOxId: String
  installationId: Int
  installationToken: String
  token: String
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

| Field                                                                                                                                      | Description                                             | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- | ---------------- |
| gitHubAppId `String`                                                                                                                       | GitHub App identifier                                   |                  |
| gitHubAppOxId `String`                                                                                                                     | GitHub App OX identifier                                |                  |
| installationId `Int`                                                                                                                       | Installation identifier                                 |                  |
| installationToken `String`                                                                                                                 | Installation-specific token                             |                  |
| token `String`                                                                                                                             | Authentication token                                    |                  |
| credentialsId `String`                                                                                                                     |                                                         |                  |
| credentialsName `String`                                                                                                                   |                                                         |                  |
| tokenExpirationDate `String`                                                                                                               |                                                         |                  |
| credentialsType [`CredentialsType`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/credentials-type) |                                                         |                  |
| isCertChecksDisabled `Boolean`                                                                                                             | Indicates if SSL/TLS certificate validation is disabled |                  |
| hostURL `String`                                                                                                                           |                                                         |                  |
| iv `String`                                                                                                                                |                                                         |                  |
| monitoredResources `JSON`                                                                                                                  |                                                         |                  |
| monitorAllResources `Boolean`                                                                                                              |                                                         |                  |
| monitorAllNewlyCreatedResources `Float`                                                                                                    |                                                         |                  |
| brokerUsername `String`                                                                                                                    |                                                         |                  |
| brokerPassword `String`                                                                                                                    |                                                         |                  |
| brokerEnabled `Boolean`                                                                                                                    |                                                         |                  |
| brokerHost `String`                                                                                                                        |                                                         |                  |
| brokerPort `Int`                                                                                                                           |                                                         |                  |

### References

#### Fields with this object

* [{} Credential](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/unions/credential)
