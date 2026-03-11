# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/queries/get-pipeline-workflow-applications.md

# getPipelineWorkflowApplications

Retrieve pipeline workflows and count how many of the specified applications each contains.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetPipelineWorkflowApplications($input: getPipelineWorkflowApplicationsInput!) {
  getPipelineWorkflowApplications(input: $input) {
    workflows {
      isDefault
      workflowName
      workflowId
      count
      enabled
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "appIds": ["30966426"]
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
 "query": "query GetPipelineWorkflowApplications($input: getPipelineWorkflowApplicationsInput!) { getPipelineWorkflowApplications(input: $input) { workflows { isDefault workflowName workflowId count enabled } } }",
 "variables": {
    "input": {
      "appIds": ["30966426"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetPipelineWorkflowApplications($input: getPipelineWorkflowApplicationsInput!) { getPipelineWorkflowApplications(input: $input) { workflows { isDefault workflowName workflowId count enabled } } }';

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
        appIds: ["30966426"]
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

query = 'query GetPipelineWorkflowApplications($input: getPipelineWorkflowApplicationsInput!) { getPipelineWorkflowApplications(input: $input) { workflows { isDefault workflowName workflowId count enabled } } }'

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
        "appIds": ["30966426"]
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

You can use the following argument(s) to customize your `getPipelineWorkflowApplications` query.

| Argument                                                                                                                                                                                                                                           | Description                      | Supported fields   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------ |
| input [`getPipelineWorkflowApplicationsInput!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/get-pipeline-workflow-applications-input) <mark style="color:red;background-color:red;">required</mark> | List of application IDs to check | appIds `[String!]` |

### Fields

Return type: [`GetPipelineWorkflowApplicationsResponse!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/get-pipeline-workflow-applications-response)

You can use the following field(s) to specify what information your `getPipelineWorkflowApplications` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                                                   | Description                            | Supported fields                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| workflows [`[PipelineWorkflowApplication!]`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/pipeline-workflow-application) | List of pipeline workflow applications | <p>isDefault <code>Boolean!</code><br>workflowName <code>String!</code><br>workflowId <code>String!</code><br>count <code>Int</code><br>enabled <code>Boolean!</code></p> |
