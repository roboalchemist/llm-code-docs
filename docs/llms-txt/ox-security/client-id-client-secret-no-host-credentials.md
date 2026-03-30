# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-client-secret-no-host-credentials.md

# clientIdClientSecretNoHostCredentials

Credentials using client ID and client secret without host URL.

### Examples

```graphql
type ClientIdClientSecretNoHostCredentials {
  clientId: String
  clientSecret: String
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
| clientId `String`                                                                                                                          | Client identifier                                       |                  |
| clientSecret `String`                                                                                                                      | Client secret                                           |                  |
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
