# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/queries/get-connectors-by-family.md

# getConnectorsByFamily

Retrieve all available connectors grouped by their family/category.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetConnectorsByFamily($family: String) {
  getConnectorsByFamily(family: $family) {
    family
    familyDisplayName
    connectors {
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
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "family": "Code Security"
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
 "query": "query GetConnectorsByFamily($family: String) { getConnectorsByFamily(family: $family) { family familyDisplayName connectors { connector { id name displayName description hostURL iconURL family credentialsType credentialsTypes brokerSupportCredentialsTypes disabledMultiCredentialsTypes credentials { ... on UserPasswordOnlyCredentials { name password credentialsId credentialsName tokenExpirationDate credentialsType isCertChecksDisabled hostURL iv monitoredResources monitorAllResources monitorAllNewlyCreatedResources brokerUsername brokerPassword brokerEnabled brokerHost brokerPort } } isConfigured isResourceAvailable ffKeyResourceAvailable resourceOptions { resourceName hideMonitorNewResourcesCheckbox showSettingsPerResource } resources { type } isOxBuiltIn isOpenSource openSourceWebsiteUrl openSourceLicense openSourceAuthor defaultEnabled comingSoon isDemoEnabled aliasFor identityProviderInfo { baseURL urlParams scope configText user_scope } gitHubAppInfo { baseURL urlPath configText } bitbucketAppInfo { baseURL queryParameters configText } awsCloudFormationInfo { baseURL urlParams } awsCloudFormationOrganizationInfo { baseURL urlParams } connectionInstructions { type title details linksToDocs { href title } permissions } isDiscovered isEmptyOfRepos isDevelopment connectorExplanation optionalInputFields { name credsTypes inputType key ffKey value } conditionalOptionalTabs { tabTitle tabInputs { inputType inputTitle inputName } } dependsOn disabledBy externalLink textExternalLink ffKey beta supportedDisabledCertChecksTypes enableMultiCredentials } } } }",
 "variables": {
    "family": "Code Security"
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetConnectorsByFamily($family: String) { getConnectorsByFamily(family: $family) { family familyDisplayName connectors { connector { id name displayName description hostURL iconURL family credentialsType credentialsTypes brokerSupportCredentialsTypes disabledMultiCredentialsTypes credentials { ... on UserPasswordOnlyCredentials { name password credentialsId credentialsName tokenExpirationDate credentialsType isCertChecksDisabled hostURL iv monitoredResources monitorAllResources monitorAllNewlyCreatedResources brokerUsername brokerPassword brokerEnabled brokerHost brokerPort } } isConfigured isResourceAvailable ffKeyResourceAvailable resourceOptions { resourceName hideMonitorNewResourcesCheckbox showSettingsPerResource } resources { type } isOxBuiltIn isOpenSource openSourceWebsiteUrl openSourceLicense openSourceAuthor defaultEnabled comingSoon isDemoEnabled aliasFor identityProviderInfo { baseURL urlParams scope configText user_scope } gitHubAppInfo { baseURL urlPath configText } bitbucketAppInfo { baseURL queryParameters configText } awsCloudFormationInfo { baseURL urlParams } awsCloudFormationOrganizationInfo { baseURL urlParams } connectionInstructions { type title details linksToDocs { href title } permissions } isDiscovered isEmptyOfRepos isDevelopment connectorExplanation optionalInputFields { name credsTypes inputType key ffKey value } conditionalOptionalTabs { tabTitle tabInputs { inputType inputTitle inputName } } dependsOn disabledBy externalLink textExternalLink ffKey beta supportedDisabledCertChecksTypes enableMultiCredentials } } } }';

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
      family: "Code Security"
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

query = 'query GetConnectorsByFamily($family: String) { getConnectorsByFamily(family: $family) { family familyDisplayName connectors { connector { id name displayName description hostURL iconURL family credentialsType credentialsTypes brokerSupportCredentialsTypes disabledMultiCredentialsTypes credentials { ... on UserPasswordOnlyCredentials { name password credentialsId credentialsName tokenExpirationDate credentialsType isCertChecksDisabled hostURL iv monitoredResources monitorAllResources monitorAllNewlyCreatedResources brokerUsername brokerPassword brokerEnabled brokerHost brokerPort } } isConfigured isResourceAvailable ffKeyResourceAvailable resourceOptions { resourceName hideMonitorNewResourcesCheckbox showSettingsPerResource } resources { type } isOxBuiltIn isOpenSource openSourceWebsiteUrl openSourceLicense openSourceAuthor defaultEnabled comingSoon isDemoEnabled aliasFor identityProviderInfo { baseURL urlParams scope configText user_scope } gitHubAppInfo { baseURL urlPath configText } bitbucketAppInfo { baseURL queryParameters configText } awsCloudFormationInfo { baseURL urlParams } awsCloudFormationOrganizationInfo { baseURL urlParams } connectionInstructions { type title details linksToDocs { href title } permissions } isDiscovered isEmptyOfRepos isDevelopment connectorExplanation optionalInputFields { name credsTypes inputType key ffKey value } conditionalOptionalTabs { tabTitle tabInputs { inputType inputTitle inputName } } dependsOn disabledBy externalLink textExternalLink ffKey beta supportedDisabledCertChecksTypes enableMultiCredentials } } } }'

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
      "family": "Code Security"
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

You can use the following argument(s) to customize your `getConnectorsByFamily` query.

| Argument        | Description | Supported fields |
| --------------- | ----------- | ---------------- |
| family `String` |             |                  |

### Fields

Return type: [`[ConnectorsByFamily]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connectors-by-family)

You can use the following field(s) to specify what information your `getConnectorsByFamily` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                         | Description                         | Supported fields                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| family `String`                                                                                                                               | Internal family identifier          |                                                                                                                           |
| familyDisplayName `String`                                                                                                                    | User-friendly family name           |                                                                                                                           |
| connectors [`[ConnectorResponse]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector-response) | Connectors belonging to this family | connector [`Connector`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector) |
