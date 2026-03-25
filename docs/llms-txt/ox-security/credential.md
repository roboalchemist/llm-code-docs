# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/unions/credential.md

# credential

Represents all possible credential types that can be used for authentication.

### Examples

```graphql
union Credential = 
  | UserPasswordOnlyCredentials
  | TokenCredentials
  | UserPasswordCredentials
  | UrlOnlyCredentials
  | TokenAndUserCredentials
  | ClientIdSecretKeyCredentials
  | AWSAssumeRoleCredentials
  | AWSAssumeRoleCredentialsOnprem
  | UserPasswordAndTenantCredentials
  | TokenAndProjectIdCredentials
  | TenantClientsubscriptionIdSecretCredentials
  | TenantIdClientIdClientSecretCredentials
  | GitHubAppCredentials
  | BitbucketAppCredentials
  | APISecretAndAccessKeyCredentials
  | OrganizationIdAndApiKeyCredentials
  | ClientIdSecretApiUrlCredentials
  | OrganizationIdAndClientIdSecretApiUrlCredentials
  | TokenOnlyCredentials
  | AWSEKSCredentials
  | ClientIdClientSecretCredentials
  | ClientIdClientSecretNoHostCredentials
  | AzureCloudCredentials
  | AppIdAndTokenCredentials
  | WebhookCredentials
  | AksCredentials
  | GKECredentials
  | ServicePrincipalCredentials
  | IdentityProvider
  | BrokerCredentials
  | K8sInspectorCredentials
  | RuntimeSensor
  | BotIdentityProvider
  | AzureOpenAIApiCredentials
```

### Types

| Type                                                                                                                                                                                                  | Description                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [`UserPasswordOnlyCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/user-password-only-credentials)                                                | Credentials using username and password only                             |
| [`TokenCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-credentials)                                                                        | Credentials using a token for authentication                             |
| [`UserPasswordCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/user-password-credentials)                                                         | Credentials using username and password with additional fields           |
| [`UrlOnlyCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/url-only-credentials)                                                                   | Credentials using only a URL                                             |
| [`TokenAndUserCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-and-user-credentials)                                                        | Credentials using token and username                                     |
| [`ClientIdSecretKeyCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-secret-key-credentials)                                             | Credentials using client ID and secret key                               |
| [`AWSAssumeRoleCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/aws-assume-role-credentials)                                                      | Credentials for AWS role assumption                                      |
| [`AWSAssumeRoleCredentialsOnprem`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/aws-assume-role-credentials-onprem)                                         | Credentials for AWS role assumption in on-premises environments          |
| [`UserPasswordAndTenantCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/user-password-and-tenant-credentials)                                     | Credentials using username, password and tenant information              |
| [`TokenAndProjectIdCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-and-project-id-credentials)                                             | Credentials using token and project ID                                   |
| [`TenantClientsubscriptionIdSecretCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/tenant-clientsubscription-id-secret-credentials)               | Credentials using tenant, client, subscription ID and secret             |
| [`TenantIdClientIdClientSecretCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/tenant-id-client-id-client-secret-credentials)                     | Credentials using tenant ID, client ID and client secret                 |
| [`GitHubAppCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/git-hub-app-credentials)                                                              | Credentials for GitHub App authentication                                |
| [`BitbucketAppCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/bitbucket-app-credentials)                                                         |                                                                          |
| [`APISecretAndAccessKeyCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/api-secret-and-access-key-credentials)                                    | Credentials using API secret and access key                              |
| [`OrganizationIdAndApiKeyCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/organization-id-and-api-key-credentials)                                | Credentials using organization ID and API key                            |
| [`ClientIdSecretApiUrlCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-secret-api-url-credentials)                                      | Credentials using client ID, secret, and API URL                         |
| [`OrganizationIdAndClientIdSecretApiUrlCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/organization-id-and-client-id-secret-api-url-credentials) | Credentials using Organization ID, client ID, client Secret, and API URL |
| [`TokenOnlyCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-only-credentials)                                                               | Credentials using only a token                                           |
| [`AWSEKSCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/awseks-credentials)                                                                      | Credentials for AWS EKS authentication                                   |
| [`ClientIdClientSecretCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-client-secret-credentials)                                       | Credentials using client ID and client secret                            |
| [`ClientIdClientSecretNoHostCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-client-secret-no-host-credentials)                         | Credentials using client ID and client secret without host URL           |
| [`AzureCloudCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/azure-cloud-credentials)                                                             | Credentials for Azure Cloud authentication                               |
| [`AppIdAndTokenCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/app-id-and-token-credentials)                                                     | Credentials using application ID and token                               |
| [`WebhookCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/webhook-credentials)                                                                    | Credentials using webhook URL                                            |
| [`AksCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/aks-credentials)                                                                            | Credentials for Azure Kubernetes Service authentication                  |
| [`GKECredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/gke-credentials)                                                                            | Credentials for Google Kubernetes Engine authentication                  |
| [`ServicePrincipalCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/service-principal-credentials)                                                 | Credentials for service principal authentication                         |
| [`IdentityProvider`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/identity-provider)                                                                        | Credentials for identity provider authentication                         |
| [`BrokerCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/broker-credentials)                                                                      | Credentials for broker authentication                                    |
| [`K8sInspectorCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/k8s-inspector-credentials)                                                         | Credentials for Kubernetes inspector                                     |
| [`RuntimeSensor`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/runtime-sensor)                                                                              | Credentials for Runtime Sensor                                           |
| [`BotIdentityProvider`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/bot-identity-provider)                                                                 | Credentials for bot identity provider authentication                     |
| [`AzureOpenAIApiCredentials`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/azure-open-ai-api-credentials)                                                   | Credentials for Azure OpenAI API (token, endpoint, deployment name)      |

### References

#### Fields with this object

* [{} Connector.credentials](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
