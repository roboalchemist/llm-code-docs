# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/azure-open-ai-api-credentials.md

# azureOpenAiApiCredentials

Credentials for Azure OpenAI API (token, endpoint, deployment name).

### Examples

```graphql
type AzureOpenAIApiCredentials {
  token: String
  apiUrl: String
  deploymentName: String
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
| token `String`                                                                                                                             | API key / token                                         |                  |
| apiUrl `String`                                                                                                                            | API endpoint URL                                        |                  |
| deploymentName `String`                                                                                                                    | Deployment name                                         |                  |
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
