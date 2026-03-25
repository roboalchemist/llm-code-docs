# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/mutations/remove-credentials.md

# removeCredentials

Removes credentials from a connector and returns the updated connector configuration.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation RemoveCredentials($removeCredentialsInput: RemoveCredentialsInput!) {
  removeCredentials(removeCredentialsInput: $removeCredentialsInput) {
    connector {
      id
      name
      displayName
      description
      hostURL
      iconURL
      family
      credentialsType
      credentialsTypes
      brokerSupportCredentialsTypes
      disabledMultiCredentialsTypes
      credentials {
        ... on UserPasswordOnlyCredentials {
          name
          password
          credentialsId
          credentialsName
          tokenExpirationDate
          credentialsType
          isCertChecksDisabled
          hostURL
          iv
          monitoredResources
          monitorAllResources
          monitorAllNewlyCreatedResources
          brokerUsername
          brokerPassword
          brokerEnabled
          brokerHost
          brokerPort
        }
      }
      isConfigured
      isResourceAvailable
      ffKeyResourceAvailable
      resourceOptions {
        resourceName
        hideMonitorNewResourcesCheckbox
        showSettingsPerResource
      }
      resources {
        type
      }
      isOxBuiltIn
      isOpenSource
      openSourceWebsiteUrl
      openSourceLicense
      openSourceAuthor
      defaultEnabled
      comingSoon
      isDemoEnabled
      aliasFor
      identityProviderInfo {
        baseURL
        urlParams
        scope
        configText
        user_scope
      }
      gitHubAppInfo {
        baseURL
        urlPath
        configText
      }
      bitbucketAppInfo {
        baseURL
        queryParameters
        configText
      }
      awsCloudFormationInfo {
        baseURL
        urlParams
      }
      awsCloudFormationOrganizationInfo {
        baseURL
        urlParams
      }
      connectionInstructions {
        type
        title
        details
        linksToDocs {
          href
          title
        }
        permissions
      }
      isDiscovered
      isEmptyOfRepos
      isDevelopment
      connectorExplanation
      optionalInputFields {
        name
        credsTypes
        inputType
        key
        ffKey
        value
      }
      conditionalOptionalTabs {
        tabTitle
        tabInputs {
          inputType
          inputTitle
          inputName
        }
      }
      dependsOn
      disabledBy
      externalLink
      textExternalLink
      ffKey
      beta
      supportedDisabledCertChecksTypes
      enableMultiCredentials
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "removeCredentialsInput": {
    "connectorID": "2",
    "credentialsIndex": 42,
    "credentialsId": "example"
  }
}
```

{% endtab %}

{% tab title="cURL" %}

```shell
curl -X POST \
https://api.cloud.ox.security/api/apollo-gateway \
-H 'Content-Type: application/json' \
-H 'Authorization: YOUR_API_TOKEN' \
-d '{
 "query": "mutation RemoveCredentials($removeCredentialsInput: RemoveCredentialsInput!) { removeCredentials(removeCredentialsInput: $removeCredentialsInput) { connector { id name displayName description hostURL iconURL family credentialsType credentialsTypes brokerSupportCredentialsTypes disabledMultiCredentialsTypes credentials { ... on UserPasswordOnlyCredentials { name password credentialsId credentialsName tokenExpirationDate credentialsType isCertChecksDisabled hostURL iv monitoredResources monitorAllResources monitorAllNewlyCreatedResources brokerUsername brokerPassword brokerEnabled brokerHost brokerPort } } isConfigured isResourceAvailable ffKeyResourceAvailable resourceOptions { resourceName hideMonitorNewResourcesCheckbox showSettingsPerResource } resources { type } isOxBuiltIn isOpenSource openSourceWebsiteUrl openSourceLicense openSourceAuthor defaultEnabled comingSoon isDemoEnabled aliasFor identityProviderInfo { baseURL urlParams scope configText user_scope } gitHubAppInfo { baseURL urlPath configText } bitbucketAppInfo { baseURL queryParameters configText } awsCloudFormationInfo { baseURL urlParams } awsCloudFormationOrganizationInfo { baseURL urlParams } connectionInstructions { type title details linksToDocs { href title } permissions } isDiscovered isEmptyOfRepos isDevelopment connectorExplanation optionalInputFields { name credsTypes inputType key ffKey value } conditionalOptionalTabs { tabTitle tabInputs { inputType inputTitle inputName } } dependsOn disabledBy externalLink textExternalLink ffKey beta supportedDisabledCertChecksTypes enableMultiCredentials } } }",
 "variables": {
    "removeCredentialsInput": {
      "connectorID": "2",
      "credentialsIndex": 42,
      "credentialsId": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation RemoveCredentials($removeCredentialsInput: RemoveCredentialsInput!) { removeCredentials(removeCredentialsInput: $removeCredentialsInput) { connector { id name displayName description hostURL iconURL family credentialsType credentialsTypes brokerSupportCredentialsTypes disabledMultiCredentialsTypes credentials { ... on UserPasswordOnlyCredentials { name password credentialsId credentialsName tokenExpirationDate credentialsType isCertChecksDisabled hostURL iv monitoredResources monitorAllResources monitorAllNewlyCreatedResources brokerUsername brokerPassword brokerEnabled brokerHost brokerPort } } isConfigured isResourceAvailable ffKeyResourceAvailable resourceOptions { resourceName hideMonitorNewResourcesCheckbox showSettingsPerResource } resources { type } isOxBuiltIn isOpenSource openSourceWebsiteUrl openSourceLicense openSourceAuthor defaultEnabled comingSoon isDemoEnabled aliasFor identityProviderInfo { baseURL urlParams scope configText user_scope } gitHubAppInfo { baseURL urlPath configText } bitbucketAppInfo { baseURL queryParameters configText } awsCloudFormationInfo { baseURL urlParams } awsCloudFormationOrganizationInfo { baseURL urlParams } connectionInstructions { type title details linksToDocs { href title } permissions } isDiscovered isEmptyOfRepos isDevelopment connectorExplanation optionalInputFields { name credsTypes inputType key ffKey value } conditionalOptionalTabs { tabTitle tabInputs { inputType inputTitle inputName } } dependsOn disabledBy externalLink textExternalLink ffKey beta supportedDisabledCertChecksTypes enableMultiCredentials } } }';

fetch("https://api.cloud.ox.security/api/apollo-gateway", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  body: JSON.stringify({
    query: query,
    // This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.
    variables: {
      removeCredentialsInput: {
        connectorID: "2",
        credentialsIndex: 42,
        credentialsId: "example"
      }
    }
  })
})
.then(response => response.json())
.then(result => console.log(JSON.stringify(result, null, 2)))
.catch(error => console.error('Error:', error));
```

{% endtab %}

{% tab title="Python" %}

```python
import requests

query = 'mutation RemoveCredentials($removeCredentialsInput: RemoveCredentialsInput!) { removeCredentials(removeCredentialsInput: $removeCredentialsInput) { connector { id name displayName description hostURL iconURL family credentialsType credentialsTypes brokerSupportCredentialsTypes disabledMultiCredentialsTypes credentials { ... on UserPasswordOnlyCredentials { name password credentialsId credentialsName tokenExpirationDate credentialsType isCertChecksDisabled hostURL iv monitoredResources monitorAllResources monitorAllNewlyCreatedResources brokerUsername brokerPassword brokerEnabled brokerHost brokerPort } } isConfigured isResourceAvailable ffKeyResourceAvailable resourceOptions { resourceName hideMonitorNewResourcesCheckbox showSettingsPerResource } resources { type } isOxBuiltIn isOpenSource openSourceWebsiteUrl openSourceLicense openSourceAuthor defaultEnabled comingSoon isDemoEnabled aliasFor identityProviderInfo { baseURL urlParams scope configText user_scope } gitHubAppInfo { baseURL urlPath configText } bitbucketAppInfo { baseURL queryParameters configText } awsCloudFormationInfo { baseURL urlParams } awsCloudFormationOrganizationInfo { baseURL urlParams } connectionInstructions { type title details linksToDocs { href title } permissions } isDiscovered isEmptyOfRepos isDevelopment connectorExplanation optionalInputFields { name credsTypes inputType key ffKey value } conditionalOptionalTabs { tabTitle tabInputs { inputType inputTitle inputName } } dependsOn disabledBy externalLink textExternalLink ffKey beta supportedDisabledCertChecksTypes enableMultiCredentials } } }'

response = requests.post(
  "https://api.cloud.ox.security/api/apollo-gateway",
  headers={
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  json={
    "query": query,
    # This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.
    "variables": {
      "removeCredentialsInput": {
        "connectorID": "2",
        "credentialsIndex": 42,
        "credentialsId": "example"
      }
    }
  }
)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

{% endtab %}
{% endtabs %}

### Arguments

You can use the following argument(s) to customize your `removeCredentials` mutation.

| Argument                                                                                                                                                                                                                         | Description                                                    | Supported fields                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| removeCredentialsInput [`RemoveCredentialsInput!`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/remove-credentials-input) <mark style="color:red;background-color:red;">required</mark> | Input containing the connector ID and credentials ID to remove | <p>connectorID <code>String!</code><br>credentialsIndex <code>Int</code><br>credentialsId <code>String</code></p> |

### Fields

Return type: [`ConnectorResponse`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector-response)

You can use the following field(s) to specify what information your `removeCredentials` mutation will return. Please note that some fields may have their own subfields.

| Field                                                                                                                     | Description      | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connector [`Connector`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector) | Connector object | <p>id <code>String</code><br>name <code>String</code><br>displayName <code>String</code><br>description <code>String</code><br>hostURL <code>String</code><br>iconURL <code>String</code><br>family <code>String</code><br>credentialsType <a href="../types/enums/credentials-type"><code>CredentialsType</code></a><br>credentialsTypes <a href="../types/enums/credentials-type"><code>\[CredentialsType]</code></a><br>brokerSupportCredentialsTypes <a href="../types/enums/credentials-type"><code>\[CredentialsType]</code></a><br>disabledMultiCredentialsTypes <a href="../types/enums/credentials-type"><code>\[CredentialsType]</code></a><br>credentials <a href="../types/unions/credential"><code>\[Credential]</code></a><br>isConfigured <code>Boolean</code><br>isResourceAvailable <code>Boolean</code><br>ffKeyResourceAvailable <code>String</code><br>resourceOptions <a href="../types/objects/resource-options"><code>ResourceOptions</code></a><br>resources <a href="../types/objects/resource-item"><code>\[ResourceItem]</code></a><br>isOxBuiltIn <code>Boolean</code><br>isOpenSource <code>Boolean</code><br>openSourceWebsiteUrl <code>String</code><br>openSourceLicense <code>String</code><br>openSourceAuthor <code>String</code><br>defaultEnabled <code>Boolean</code><br>comingSoon <code>Boolean</code><br>isDemoEnabled <code>Boolean</code><br>aliasFor <code>String</code><br>identityProviderInfo <a href="../types/objects/identity-provider-info"><code>IdentityProviderInfo</code></a><br>gitHubAppInfo <a href="../types/objects/git-hub-app-info"><code>GitHubAppInfo</code></a><br>bitbucketAppInfo <a href="../types/objects/bitbucket-app-info"><code>BitbucketAppInfo</code></a><br>awsCloudFormationInfo <a href="../types/objects/aws-cloud-formation-info"><code>AWSCloudFormationInfo</code></a><br>awsCloudFormationOrganizationInfo <a href="../types/objects/aws-cloud-formation-info"><code>AWSCloudFormationInfo</code></a><br>connectionInstructions <a href="../types/objects/connection-instructions"><code>\[ConnectionInstructions]</code></a><br>isDiscovered <code>Boolean</code><br>isEmptyOfRepos <code>Boolean</code><br>isDevelopment <code>Boolean</code><br>connectorExplanation <code>String</code><br>optionalInputFields <a href="../types/objects/optional-connector-input"><code>\[OptionalConnectorInput]</code></a><br>conditionalOptionalTabs <a href="../types/objects/conditional-optional-tabs"><code>\[ConditionalOptionalTabs]</code></a><br>dependsOn <code>String</code><br>disabledBy <code>\[String]</code><br>externalLink <code>String</code><br>textExternalLink <code>String</code><br>ffKey <code>String</code><br>beta <code>Boolean</code><br>supportedDisabledCertChecksTypes <code>\[String]</code><br>enableMultiCredentials <code>Boolean</code></p> |
