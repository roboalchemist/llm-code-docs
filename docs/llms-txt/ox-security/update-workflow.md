# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/mutations/update-workflow.md

# updateWorkflow

Update an existing workflow policy including pipeline application selection.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation UpdateWorkflow($input: UpdateWorkflowPolicyInput!) {
  updateWorkflow(input: $input) {
    id
    isValid
    createdAt
    createdBy
    enabled
    updatedAt
    updatedBy
    name
    description
    actions {
      name
      type
    }
    triggers {
      name
      category
    }
    runs
    lastRunTime
    workflowType
    isDefault
    monitorAllNewlyCreatedRepositories
    wfPipelineSettings {
      apps {
        appName
        appType
        appId
        selected
        disabled
      }
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "id": "example",
    "name": "SomeName",
    "description": "example",
    "enabled": true,
    "pipelineSettings": {
      "apps": [
        {
          "appId": "30966426",
          "appName": "some-repo",
          "appType": "example",
          "selected": true,
          "disabled": true
        }
      ]
    },
    "isDefault": true,
    "monitorAllNewlyCreatedRepositories": 13.37,
    "monitorRepositories": "AddAll"
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
 "query": "mutation UpdateWorkflow($input: UpdateWorkflowPolicyInput!) { updateWorkflow(input: $input) { id isValid createdAt createdBy enabled updatedAt updatedBy name description actions { name type } triggers { name category } runs lastRunTime workflowType isDefault monitorAllNewlyCreatedRepositories wfPipelineSettings { apps { appName appType appId selected disabled } } } }",
 "variables": {
    "input": {
      "id": "example",
      "name": "SomeName",
      "description": "example",
      "enabled": true,
      "pipelineSettings": {
        "apps": [
          {
            "appId": "30966426",
            "appName": "some-repo",
            "appType": "example",
            "selected": true,
            "disabled": true
          }
        ]
      },
      "isDefault": true,
      "monitorAllNewlyCreatedRepositories": 13.37,
      "monitorRepositories": "AddAll"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation UpdateWorkflow($input: UpdateWorkflowPolicyInput!) { updateWorkflow(input: $input) { id isValid createdAt createdBy enabled updatedAt updatedBy name description actions { name type } triggers { name category } runs lastRunTime workflowType isDefault monitorAllNewlyCreatedRepositories wfPipelineSettings { apps { appName appType appId selected disabled } } } }';

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
        id: "example",
        name: "SomeName",
        description: "example",
        enabled: true,
        pipelineSettings: {
          apps: [
            {
              appId: "30966426",
              appName: "some-repo",
              appType: "example",
              selected: true,
              disabled: true
            }
          ]
        },
        isDefault: true,
        monitorAllNewlyCreatedRepositories: 13.37,
        monitorRepositories: "AddAll"
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

query = 'mutation UpdateWorkflow($input: UpdateWorkflowPolicyInput!) { updateWorkflow(input: $input) { id isValid createdAt createdBy enabled updatedAt updatedBy name description actions { name type } triggers { name category } runs lastRunTime workflowType isDefault monitorAllNewlyCreatedRepositories wfPipelineSettings { apps { appName appType appId selected disabled } } } }'

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
        "id": "example",
        "name": "SomeName",
        "description": "example",
        "enabled": true,
        "pipelineSettings": {
          "apps": [
            {
              "appId": "30966426",
              "appName": "some-repo",
              "appType": "example",
              "selected": true,
              "disabled": true
            }
          ]
        },
        "isDefault": true,
        "monitorAllNewlyCreatedRepositories": 13.37,
        "monitorRepositories": "AddAll"
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

You can use the following argument(s) to customize your `updateWorkflow` mutation.

| Argument                                                                                                                                                                                                                    | Description               | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| input [`UpdateWorkflowPolicyInput!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/update-workflow-policy-input) <mark style="color:red;background-color:red;">required</mark> | Workflow fields to update | <p>id <code>String!</code><br>name <code>String</code><br>description <code>String</code><br>enabled <code>Boolean</code><br>pipelineSettings <a href="../types/inputs/pipeline-settings-input"><code>PipelineSettingsInput</code></a><br>isDefault <code>Boolean</code><br>monitorAllNewlyCreatedRepositories <code>Float</code><br>monitorRepositories <a href="../types/enums/monitor-repositories"><code>MonitorRepositories</code></a></p> |

### Fields

Return type: [`WorkflowPolicy!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/workflow-policy)

You can use the following field(s) to specify what information your `updateWorkflow` mutation will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                                       | Description                                                                                  | Supported fields                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| id `String!`                                                                                                                                                | ID of the policy workflow                                                                    |                                                                                                                       |
| isValid `Boolean`                                                                                                                                           | defines if workflow is valid or not                                                          |                                                                                                                       |
| createdAt `Float!`                                                                                                                                          | Time the workflow was created                                                                |                                                                                                                       |
| createdBy `String`                                                                                                                                          | Workflow creator                                                                             |                                                                                                                       |
| enabled `Boolean`                                                                                                                                           | Enabled for evaluation                                                                       |                                                                                                                       |
| updatedAt `Float!`                                                                                                                                          | Time the workflow was updated                                                                |                                                                                                                       |
| updatedBy `String`                                                                                                                                          | Workflow last updated by                                                                     |                                                                                                                       |
| name `String!`                                                                                                                                              | Name of the workflow                                                                         |                                                                                                                       |
| description `String`                                                                                                                                        | Description of the workflow                                                                  |                                                                                                                       |
| actions [`[Action!]!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/action)                                  |                                                                                              | <p>name <code>String</code><br>type <code>String</code></p>                                                           |
| triggers [`[Trigger!]!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/trigger)                               |                                                                                              | <p>name <code>String</code><br>category <code>String</code></p>                                                       |
| runs `Int`                                                                                                                                                  | numbers of runs this workflow had                                                            |                                                                                                                       |
| lastRunTime `Float`                                                                                                                                         | last time this workflow had run                                                              |                                                                                                                       |
| workflowType [`WorkflowType!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/enums/workflow-type)                     | type of the workflow (Regular scan / Pipeline scan)                                          |                                                                                                                       |
| isDefault `Boolean!`                                                                                                                                        | If the workflow is a default one                                                             |                                                                                                                       |
| monitorAllNewlyCreatedRepositories `Float`                                                                                                                  | If this workflow should trigger for all newly created repos starting from the time it is set |                                                                                                                       |
| wfPipelineSettings [`WfPipelineSettings`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-pipeline-settings) | settings for pipeline                                                                        | apps [`[WfApp!]`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-app) |
