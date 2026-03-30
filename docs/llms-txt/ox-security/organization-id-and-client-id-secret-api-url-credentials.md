# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/organization-id-and-client-id-secret-api-url-credentials.md

# organizationIdAndClientIdSecretApiUrlCredentials

Credentials using Organization ID, client ID, client Secret, and API URL.

### Examples

```graphql
type OrganizationIdAndClientIdSecretApiUrlCredentials {
  clientId: String
  clientSecret: String
  apiUrl: String
  organizationId: String
  optionalFields: OptionalFields
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

| Field                                                                                                                                      | Description                                             | Supported fields                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| clientId `String`                                                                                                                          | Client identifier                                       |                                                                                                                                                  |
| clientSecret `String`                                                                                                                      | Client secret                                           |                                                                                                                                                  |
| apiUrl `String`                                                                                                                            | API endpoint URL                                        |                                                                                                                                                  |
| organizationId `String`                                                                                                                    | Organization Id                                         |                                                                                                                                                  |
| optionalFields [`OptionalFields`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/optional-fields)  | Additional optional configuration fields                | <p>SSHKey <code>String</code><br>RepoSearchQuery <code>String</code><br>Config <code>String</code><br>buildIssueToCloud <code>Boolean</code></p> |
| credentialsId `String`                                                                                                                     |                                                         |                                                                                                                                                  |
| credentialsName `String`                                                                                                                   |                                                         |                                                                                                                                                  |
| tokenExpirationDate `String`                                                                                                               |                                                         |                                                                                                                                                  |
| credentialsType [`CredentialsType`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/credentials-type) |                                                         |                                                                                                                                                  |
| isCertChecksDisabled `Boolean`                                                                                                             | Indicates if SSL/TLS certificate validation is disabled |                                                                                                                                                  |
| hostURL `String`                                                                                                                           |                                                         |                                                                                                                                                  |
| iv `String`                                                                                                                                |                                                         |                                                                                                                                                  |
| monitoredResources `JSON`                                                                                                                  |                                                         |                                                                                                                                                  |
| monitorAllResources `Boolean`                                                                                                              |                                                         |                                                                                                                                                  |
| monitorAllNewlyCreatedResources `Float`                                                                                                    |                                                         |                                                                                                                                                  |
| brokerUsername `String`                                                                                                                    |                                                         |                                                                                                                                                  |
| brokerPassword `String`                                                                                                                    |                                                         |                                                                                                                                                  |
| brokerEnabled `Boolean`                                                                                                                    |                                                         |                                                                                                                                                  |
| brokerHost `String`                                                                                                                        |                                                         |                                                                                                                                                  |
| brokerPort `Int`                                                                                                                           |                                                         |                                                                                                                                                  |

### References

#### Fields with this object

* [{} Credential](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/unions/credential)
