# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/queries/get-connector-resources.md

# getConnectorResources

Retrieves available resources for a connector, such as repositories, projects, or other assets that can be monitored.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetConnectorResources($getConnectorResourcesInput: GetConnectorResourcesInput!) {
  getConnectorResources(getConnectorResourcesInput: $getConnectorResourcesInput) {
    resources {
      id
      name
      resourceOrgName
      isMonitored
      resourceType
      children {
        id
        name
        resourceOrgName
        isMonitored
        resourceType
        children {
          id
          name
          resourceOrgName
          isMonitored
          resourceType
          iconName
          settingsAvailable
          credentialsId
        }
        iconName
        settingsAvailable
        credentialsId
      }
      iconName
      settingsAvailable
      credentialsId
    }
    monitorAllNewlyCreatedResources
    total
    selected
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getConnectorResourcesInput": {
    "connectorID": "2",
    "credentialsId": "example",
    "featureFlags": "example"
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
 "query": "query GetConnectorResources($getConnectorResourcesInput: GetConnectorResourcesInput!) { getConnectorResources(getConnectorResourcesInput: $getConnectorResourcesInput) { resources { id name resourceOrgName isMonitored resourceType children { id name resourceOrgName isMonitored resourceType children { id name resourceOrgName isMonitored resourceType iconName settingsAvailable credentialsId } iconName settingsAvailable credentialsId } iconName settingsAvailable credentialsId } monitorAllNewlyCreatedResources total selected } }",
 "variables": {
    "getConnectorResourcesInput": {
      "connectorID": "2",
      "credentialsId": "example",
      "featureFlags": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetConnectorResources($getConnectorResourcesInput: GetConnectorResourcesInput!) { getConnectorResources(getConnectorResourcesInput: $getConnectorResourcesInput) { resources { id name resourceOrgName isMonitored resourceType children { id name resourceOrgName isMonitored resourceType children { id name resourceOrgName isMonitored resourceType iconName settingsAvailable credentialsId } iconName settingsAvailable credentialsId } iconName settingsAvailable credentialsId } monitorAllNewlyCreatedResources total selected } }';

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
      getConnectorResourcesInput: {
        connectorID: "2",
        credentialsId: "example",
        featureFlags: "example"
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

query = 'query GetConnectorResources($getConnectorResourcesInput: GetConnectorResourcesInput!) { getConnectorResources(getConnectorResourcesInput: $getConnectorResourcesInput) { resources { id name resourceOrgName isMonitored resourceType children { id name resourceOrgName isMonitored resourceType children { id name resourceOrgName isMonitored resourceType iconName settingsAvailable credentialsId } iconName settingsAvailable credentialsId } iconName settingsAvailable credentialsId } monitorAllNewlyCreatedResources total selected } }'

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
      "getConnectorResourcesInput": {
        "connectorID": "2",
        "credentialsId": "example",
        "featureFlags": "example"
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

You can use the following argument(s) to customize your `getConnectorResources` query.

| Argument                                                                                                                                                                                                                                      | Description                                                                        | Supported fields                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| getConnectorResourcesInput [`GetConnectorResourcesInput!`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/get-connector-resources-input) <mark style="color:red;background-color:red;">required</mark> | Input parameters specifying which connector and credentials to fetch resources for | <p>connectorID <code>String!</code><br>credentialsId <code>String</code><br>featureFlags <code>JSON</code></p> |

### Fields

Return type: [`ConnectorResourceResponse`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector-resource-response)

You can use the following field(s) to specify what information your `getConnectorResources` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                     | Description                                                            | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| resources [`[Resource]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/resource) | List of resources that are available and their monitoring status       | <p>id <code>String</code><br>name <code>String</code><br>resourceOrgName <code>String</code><br>isMonitored <code>Boolean</code><br>resourceType <a href="../types/enums/resource-type"><code>ResourceType</code></a><br>children <a href="../types/objects/resource"><code>\[Resource]</code></a><br>iconName <a href="../types/enums/resource-icon"><code>ResourceIcon</code></a><br>settingsAvailable <code>Boolean</code><br>credentialsId <code>String</code></p> |
| monitorAllNewlyCreatedResources `Boolean`                                                                                 | Indicates if newly created resources should be automatically monitored |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| total `Int`                                                                                                               | Total number of available resources                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| selected `Int`                                                                                                            | Number of selected (monitored) resources                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
