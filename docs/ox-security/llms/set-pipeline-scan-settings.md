# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/mutations/set-pipeline-scan-settings.md

# setPipelineScanSettings

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation SetPipelineScanSettings($input: SetPipelineScanSettingsInput!) {
  setPipelineScanSettings(input: $input) {
    success
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "appIds": ["30966426"],
    "timeout": 13.37,
    "performance": "example",
    "failOnTimeout": true,
    "failOnError": true,
    "scansEnabled": true,
    "scanSummaryAsCommentEnabled": true,
    "eventsTriggeringScansForBranches": [
      {
        "branchNamePatternBranchSelection": "example",
        "genericOptionBranchSelection": "defaultBranch",
        "events": [
          {
            "type": "pullRequest",
            "value": true
          }
        ]
      }
    ],
    "scansEnabledForBitbucketApp": true,
    "eventsTriggeringScansForBranchesForBitbucketApp": [
      {
        "branchNamePatternBranchSelection": "example",
        "genericOptionBranchSelection": "defaultBranch",
        "events": [
          {
            "type": "pullRequest",
            "value": true
          }
        ]
      }
    ],
    "scansEnabledForGitLabWebhooks": true,
    "eventsTriggeringScansForBranchesForGitLabWebhooks": [
      {
        "branchNamePatternBranchSelection": "example",
        "genericOptionBranchSelection": "defaultBranch",
        "events": [
          {
            "type": "pullRequest",
            "value": true
          }
        ]
      }
    ]
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
 "query": "mutation SetPipelineScanSettings($input: SetPipelineScanSettingsInput!) { setPipelineScanSettings(input: $input) { success } }",
 "variables": {
    "input": {
      "appIds": ["30966426"],
      "timeout": 13.37,
      "performance": "example",
      "failOnTimeout": true,
      "failOnError": true,
      "scansEnabled": true,
      "scanSummaryAsCommentEnabled": true,
      "eventsTriggeringScansForBranches": [
        {
          "branchNamePatternBranchSelection": "example",
          "genericOptionBranchSelection": "defaultBranch",
          "events": [
            {
              "type": "pullRequest",
              "value": true
            }
          ]
        }
      ],
      "scansEnabledForBitbucketApp": true,
      "eventsTriggeringScansForBranchesForBitbucketApp": [
        {
          "branchNamePatternBranchSelection": "example",
          "genericOptionBranchSelection": "defaultBranch",
          "events": [
            {
              "type": "pullRequest",
              "value": true
            }
          ]
        }
      ],
      "scansEnabledForGitLabWebhooks": true,
      "eventsTriggeringScansForBranchesForGitLabWebhooks": [
        {
          "branchNamePatternBranchSelection": "example",
          "genericOptionBranchSelection": "defaultBranch",
          "events": [
            {
              "type": "pullRequest",
              "value": true
            }
          ]
        }
      ]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation SetPipelineScanSettings($input: SetPipelineScanSettingsInput!) { setPipelineScanSettings(input: $input) { success } }';

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
        appIds: ["30966426"],
        timeout: 13.37,
        performance: "example",
        failOnTimeout: true,
        failOnError: true,
        scansEnabled: true,
        scanSummaryAsCommentEnabled: true,
        eventsTriggeringScansForBranches: [
          {
            branchNamePatternBranchSelection: "example",
            genericOptionBranchSelection: "defaultBranch",
            events: [
              {
                type: "pullRequest",
                value: true
              }
            ]
          }
        ],
        scansEnabledForBitbucketApp: true,
        eventsTriggeringScansForBranchesForBitbucketApp: [
          {
            branchNamePatternBranchSelection: "example",
            genericOptionBranchSelection: "defaultBranch",
            events: [
              {
                type: "pullRequest",
                value: true
              }
            ]
          }
        ],
        scansEnabledForGitLabWebhooks: true,
        eventsTriggeringScansForBranchesForGitLabWebhooks: [
          {
            branchNamePatternBranchSelection: "example",
            genericOptionBranchSelection: "defaultBranch",
            events: [
              {
                type: "pullRequest",
                value: true
              }
            ]
          }
        ]
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

query = 'mutation SetPipelineScanSettings($input: SetPipelineScanSettingsInput!) { setPipelineScanSettings(input: $input) { success } }'

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
        "appIds": ["30966426"],
        "timeout": 13.37,
        "performance": "example",
        "failOnTimeout": true,
        "failOnError": true,
        "scansEnabled": true,
        "scanSummaryAsCommentEnabled": true,
        "eventsTriggeringScansForBranches": [
          {
            "branchNamePatternBranchSelection": "example",
            "genericOptionBranchSelection": "defaultBranch",
            "events": [
              {
                "type": "pullRequest",
                "value": true
              }
            ]
          }
        ],
        "scansEnabledForBitbucketApp": true,
        "eventsTriggeringScansForBranchesForBitbucketApp": [
          {
            "branchNamePatternBranchSelection": "example",
            "genericOptionBranchSelection": "defaultBranch",
            "events": [
              {
                "type": "pullRequest",
                "value": true
              }
            ]
          }
        ],
        "scansEnabledForGitLabWebhooks": true,
        "eventsTriggeringScansForBranchesForGitLabWebhooks": [
          {
            "branchNamePatternBranchSelection": "example",
            "genericOptionBranchSelection": "defaultBranch",
            "events": [
              {
                "type": "pullRequest",
                "value": true
              }
            ]
          }
        ]
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

You can use the following argument(s) to customize your `setPipelineScanSettings` mutation.

| Argument                                                                                                                                                                                                                    | Description | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| input [`SetPipelineScanSettingsInput!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/set-pipeline-scan-settings-input) <mark style="color:red;background-color:red;">required</mark> |             | <p>appIds <code>\[String!]!</code><br>timeout <code>Float</code><br>performance <code>String</code><br>failOnTimeout <code>Boolean</code><br>failOnError <code>Boolean</code><br>scansEnabled <code>Boolean!</code><br>scanSummaryAsCommentEnabled <code>Boolean</code><br>eventsTriggeringScansForBranches <a href="../types/inputs/events-triggering-scans-for-branches-setting-input"><code>\[EventsTriggeringScansForBranchesSettingInput!]</code></a><br>scansEnabledForBitbucketApp <code>Boolean</code><br>eventsTriggeringScansForBranchesForBitbucketApp <a href="../types/inputs/events-triggering-scans-for-branches-setting-input"><code>\[EventsTriggeringScansForBranchesSettingInput!]</code></a><br>scansEnabledForGitLabWebhooks <code>Boolean</code><br>eventsTriggeringScansForBranchesForGitLabWebhooks <a href="../types/inputs/events-triggering-scans-for-branches-setting-input"><code>\[EventsTriggeringScansForBranchesSettingInput!]</code></a></p> |

### Fields

Return type: [`SetPipelineScanSettingsResponse!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/set-pipeline-scan-settings-response)

You can use the following field(s) to specify what information your `setPipelineScanSettings` mutation will return. Please note that some fields may have their own subfields.

| Field              | Description                                          | Supported fields |
| ------------------ | ---------------------------------------------------- | ---------------- |
| success `Boolean!` | Whether all settings updates completed successfully. |                  |
