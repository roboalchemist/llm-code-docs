# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/bot-identity-provider.md

# botIdentityProvider

Credentials for bot identity provider authentication.

### Examples

```graphql
type BotIdentityProvider {
  idpToken: String
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
| idpToken `String`                                                                                                                          | Token received from bot identity provider               |                  |
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
