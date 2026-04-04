# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/queries/get-pipeline-applications.md

# getPipelineApplications

Retrieve pipeline applications with their selection state for a specific workflow.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetPipelineApplications($input: GetPipelineApplicationsInput!) {
  getPipelineApplications(input: $input) {
    total
    offset
    totalFilteredApps
    applications {
      appName
      appType
      appId
      selected
      disabled
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "isDefault": true,
    "policyWorkflowId": "example",
    "searchValue": "example",
    "offset": 0,
    "limit": 100
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
 "query": "query GetPipelineApplications($input: GetPipelineApplicationsInput!) { getPipelineApplications(input: $input) { total offset totalFilteredApps applications { appName appType appId selected disabled } } }",
 "variables": {
    "input": {
      "isDefault": true,
      "policyWorkflowId": "example",
      "searchValue": "example",
      "offset": 0,
      "limit": 100
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetPipelineApplications($input: GetPipelineApplicationsInput!) { getPipelineApplications(input: $input) { total offset totalFilteredApps applications { appName appType appId selected disabled } } }';

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
      input: {
        isDefault: true,
        policyWorkflowId: "example",
        searchValue: "example",
        offset: 0,
        limit: 100
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

query = 'query GetPipelineApplications($input: GetPipelineApplicationsInput!) { getPipelineApplications(input: $input) { total offset totalFilteredApps applications { appName appType appId selected disabled } } }'

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
      "input": {
        "isDefault": true,
        "policyWorkflowId": "example",
        "searchValue": "example",
        "offset": 0,
        "limit": 100
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

You can use the following argument(s) to customize your `getPipelineApplications` query.

| Argument                                                                                                                                                                                                                          | Description                                                | Supported fields                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| input [`GetPipelineApplicationsInput!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/get-pipeline-applications-input) <mark style="color:red;background-color:red;">required</mark> | Filter and pagination parameters for pipeline applications | <p>isDefault <code>Boolean</code><br>policyWorkflowId <code>String</code><br>searchValue <code>String</code><br>offset <code>Float</code><br>limit <code>Float</code></p> |

### Fields

Return type: [`GetPipelineApplicationsResponse!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/get-pipeline-applications-response)

You can use the following field(s) to specify what information your `getPipelineApplications` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                         | Description                           | Supported fields                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| total `Int`                                                                                                                   | Total number of applications          |                                                                                                                                                                  |
| offset `Int`                                                                                                                  | Pagination offset                     |                                                                                                                                                                  |
| totalFilteredApps `Int`                                                                                                       | Total number of filtered applications |                                                                                                                                                                  |
| applications [`[WfApp!]`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-app) | List of applications                  | <p>appName <code>String</code><br>appType <code>String</code><br>appId <code>String</code><br>selected <code>Boolean</code><br>disabled <code>Boolean</code></p> |
