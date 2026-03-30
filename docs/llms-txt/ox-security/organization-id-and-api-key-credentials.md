# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/organization-id-and-api-key-credentials.md

# organizationIdAndApiKeyCredentials

Credentials using organization ID and API key.

### Examples

```graphql
type OrganizationIdAndApiKeyCredentials {
  name: String
  password: String
  organizationId: String
  apiKey: String
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
| name `String`                                                                                                                              | Username for authentication                             |                  |
| password `String`                                                                                                                          | Password for authentication                             |                  |
| organizationId `String`                                                                                                                    | Organization identifier                                 |                  |
| apiKey `String`                                                                                                                            | API key                                                 |                  |
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
