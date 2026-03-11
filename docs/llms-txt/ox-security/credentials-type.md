# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/credentials-type.md

# credentialsType

Type of the connector family (Code Repo etc...).

### Examples

```graphql
enum CredentialsType {
  UserPassword
  UserPasswordBothOptional
  UserPasswordOnly
  UrlOnly
  UserPasswordAndTenant
  Token
  TokenAndUser
  IdentityProvider
  BotIdentityProvider
  ClientIdSecretKey
  AWSAssumeRole
  AWSAssumeRoleCloudFormation
  AWSOrganizationConnection
  AWSAssumeRoleOnprem
  AWSAssumeRoleCloudFormationOnprem
  AWSOrganizationConnectionOnprem
  AWSAssumeRoleCodeCommit
  AWSEKS
  AWSEKSDirect
  AWSEKSPrivateLink
  AWSAssumeRoleCodeCommitOrganization
  AWSAssumeRoleCodeCommitOnprem
  AWSAssumeRoleCodeCommitOrganizationOnprem
  ApiKey
  TokenAndProjectId
  APISecretAndAccessKey
  TenantClientsubscriptionIdSecret
  TenantIdClientIdClientSecret
  None
  GitHubApp
  BitbucketApp
  OrganizationIdAndApiKey
  ClientIdSecretApiUrl
  OrganizationIdAndClientIdSecretApiUrl
  TokenOnly
  AzureCloud
  ServicePrincipal
  ClientIdClientSecret
  AppIdAndToken
  Webhook
  AksDirect
  AksRunCommand
  GKEDirect
  Broker
  K8sInspector
  ClientIdClientSecretNoHost
  RuntimeSensor
  AzureOpenAIApi
}
```

### Enum values

| Enum value                                | Description |
| ----------------------------------------- | ----------- |
| UserPassword                              |             |
| UserPasswordBothOptional                  |             |
| UserPasswordOnly                          |             |
| UrlOnly                                   |             |
| UserPasswordAndTenant                     |             |
| Token                                     |             |
| TokenAndUser                              |             |
| IdentityProvider                          |             |
| BotIdentityProvider                       |             |
| ClientIdSecretKey                         |             |
| AWSAssumeRole                             |             |
| AWSAssumeRoleCloudFormation               |             |
| AWSOrganizationConnection                 |             |
| AWSAssumeRoleOnprem                       |             |
| AWSAssumeRoleCloudFormationOnprem         |             |
| AWSOrganizationConnectionOnprem           |             |
| AWSAssumeRoleCodeCommit                   |             |
| AWSEKS                                    |             |
| AWSEKSDirect                              |             |
| AWSEKSPrivateLink                         |             |
| AWSAssumeRoleCodeCommitOrganization       |             |
| AWSAssumeRoleCodeCommitOnprem             |             |
| AWSAssumeRoleCodeCommitOrganizationOnprem |             |
| ApiKey                                    |             |
| TokenAndProjectId                         |             |
| APISecretAndAccessKey                     |             |
| TenantClientsubscriptionIdSecret          |             |
| TenantIdClientIdClientSecret              |             |
| None                                      |             |
| GitHubApp                                 |             |
| BitbucketApp                              |             |
| OrganizationIdAndApiKey                   |             |
| ClientIdSecretApiUrl                      |             |
| OrganizationIdAndClientIdSecretApiUrl     |             |
| TokenOnly                                 |             |
| AzureCloud                                |             |
| ServicePrincipal                          |             |
| ClientIdClientSecret                      |             |
| AppIdAndToken                             |             |
| Webhook                                   |             |
| AksDirect                                 |             |
| AksRunCommand                             |             |
| GKEDirect                                 |             |
| Broker                                    |             |
| K8sInspector                              |             |
| ClientIdClientSecretNoHost                |             |
| RuntimeSensor                             |             |
| AzureOpenAIApi                            |             |

### References

#### Fields with this object

* [{} Connector.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
* [{} Connector.credentialsTypes](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
* [{} Connector.brokerSupportCredentialsTypes](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
* [{} Connector.disabledMultiCredentialsTypes](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
* [{} UserPasswordOnlyCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/user-password-only-credentials)
* [{} TokenCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-credentials)
* [{} UserPasswordCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/user-password-credentials)
* [{} UrlOnlyCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/url-only-credentials)
* [{} TokenAndUserCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-and-user-credentials)
* [{} ClientIdSecretKeyCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-secret-key-credentials)
* [{} AWSAssumeRoleCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/aws-assume-role-credentials)
* [{} AWSAssumeRoleCredentialsOnprem.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/aws-assume-role-credentials-onprem)
* [{} UserPasswordAndTenantCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/user-password-and-tenant-credentials)
* [{} TokenAndProjectIdCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-and-project-id-credentials)
* [{} TenantClientsubscriptionIdSecretCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/tenant-clientsubscription-id-secret-credentials)
* [{} TenantIdClientIdClientSecretCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/tenant-id-client-id-client-secret-credentials)
* [{} GitHubAppCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/git-hub-app-credentials)
* [{} BitbucketAppCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/bitbucket-app-credentials)
* [{} APISecretAndAccessKeyCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/api-secret-and-access-key-credentials)
* [{} OrganizationIdAndApiKeyCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/organization-id-and-api-key-credentials)
* [{} ClientIdSecretApiUrlCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-secret-api-url-credentials)
* [{} OrganizationIdAndClientIdSecretApiUrlCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/organization-id-and-client-id-secret-api-url-credentials)
* [{} TokenOnlyCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-only-credentials)
* [{} AWSEKSCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/awseks-credentials)
* [{} ClientIdClientSecretCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-client-secret-credentials)
* [{} ClientIdClientSecretNoHostCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-client-secret-no-host-credentials)
* [{} AzureCloudCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/azure-cloud-credentials)
* [{} AppIdAndTokenCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/app-id-and-token-credentials)
* [{} WebhookCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/webhook-credentials)
* [{} AksCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/aks-credentials)
* [{} GKECredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/gke-credentials)
* [{} ServicePrincipalCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/service-principal-credentials)
* [{} IdentityProvider.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/identity-provider)
* [{} BrokerCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/broker-credentials)
* [{} K8sInspectorCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/k8s-inspector-credentials)
* [{} RuntimeSensor.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/runtime-sensor)
* [{} BotIdentityProvider.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/bot-identity-provider)
* [{} AzureOpenAIApiCredentials.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/azure-open-ai-api-credentials)
* [{} ConnectionInstructions.type](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connection-instructions)
* [{} OptionalConnectorInput.credsTypes](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/optional-connector-input)
* [{} AddCredentialsInput.credentialsType](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/add-credentials-input)
