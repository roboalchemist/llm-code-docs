# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/mutations/monitor-connector-resources.md

# monitorConnectorResources

Sets connector resources to monitor and replaces any existing monitoring configuration.

{% hint style="warning" %}

#### Complete replacement operation

To maintain monitoring of existing resources:

* First retrieve your current list of monitored resources
* Include ALL resources you wish to monitor in your update, both existing and new
* Any resources not included in this update will no longer be monitored
  {% endhint %}

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation MonitorConnectorResources($monitorConnectorResourceInput: MonitorConnectorResourceInput!) {
  monitorConnectorResources(monitorConnectorResourceInput: $monitorConnectorResourceInput) {
    success
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "monitorConnectorResourceInput": {
    "connectorID": "2",
    "originalConnectorID": "example",
    "credentialsId": "example",
    "credentialsType": "example",
    "resources": [
      {
        "id": "30966426",
        "name": "some-repo",
        "isMonitored": true,
        "resourceType": "edge",
        "credentialsId": "example"
      }
    ],
    "monitorAllResources": true,
    "monitorAllNewlyCreatedResources": 1749000000000,
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
 "query": "mutation MonitorConnectorResources($monitorConnectorResourceInput: MonitorConnectorResourceInput!) { monitorConnectorResources(monitorConnectorResourceInput: $monitorConnectorResourceInput) { success } }",
 "variables": {
    "monitorConnectorResourceInput": {
      "connectorID": "2",
      "originalConnectorID": "example",
      "credentialsId": "example",
      "credentialsType": "example",
      "resources": [
        {
          "id": "30966426",
          "name": "some-repo",
          "isMonitored": true,
          "resourceType": "edge",
          "credentialsId": "example"
        }
      ],
      "monitorAllResources": true,
      "monitorAllNewlyCreatedResources": 1749000000000,
      "featureFlags": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation MonitorConnectorResources($monitorConnectorResourceInput: MonitorConnectorResourceInput!) { monitorConnectorResources(monitorConnectorResourceInput: $monitorConnectorResourceInput) { success } }';

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
      monitorConnectorResourceInput: {
        connectorID: "2",
        originalConnectorID: "example",
        credentialsId: "example",
        credentialsType: "example",
        resources: [
          {
            id: "30966426",
            name: "some-repo",
            isMonitored: true,
            resourceType: "edge",
            credentialsId: "example"
          }
        ],
        monitorAllResources: true,
        monitorAllNewlyCreatedResources: 1749000000000,
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

query = 'mutation MonitorConnectorResources($monitorConnectorResourceInput: MonitorConnectorResourceInput!) { monitorConnectorResources(monitorConnectorResourceInput: $monitorConnectorResourceInput) { success } }'

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
      "monitorConnectorResourceInput": {
        "connectorID": "2",
        "originalConnectorID": "example",
        "credentialsId": "example",
        "credentialsType": "example",
        "resources": [
          {
            "id": "30966426",
            "name": "some-repo",
            "isMonitored": true,
            "resourceType": "edge",
            "credentialsId": "example"
          }
        ],
        "monitorAllResources": true,
        "monitorAllNewlyCreatedResources": 1749000000000,
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

You can use the following argument(s) to customize your `monitorConnectorResources` mutation.

| Argument                                                                                                                                                                                                                                               | Description                                                                        | Supported fields                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| monitorConnectorResourceInput [`MonitorConnectorResourceInput!`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/monitor-connector-resource-input) <mark style="color:red;background-color:red;">required</mark> | Input specifying which connector resources to monitor and monitoring configuration | <p>connectorID <code>String!</code><br>originalConnectorID <code>String</code><br>credentialsId <code>String</code><br>credentialsType <code>String</code><br>resources <a href="../types/inputs/resource-input"><code>\[ResourceInput]</code></a><br>monitorAllResources <code>Boolean</code><br>monitorAllNewlyCreatedResources <code>Float</code><br>featureFlags <code>JSON</code></p> |

### Fields

Return type: [`MonitorConnectorResourceResponse`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/monitor-connector-resource-response)

You can use the following field(s) to specify what information your `monitorConnectorResources` mutation will return. Please note that some fields may have their own subfields.

| Field             | Description                               | Supported fields |
| ----------------- | ----------------------------------------- | ---------------- |
| success `Boolean` | boolean indication if operation succeeded |                  |
