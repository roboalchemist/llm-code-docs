# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/queries/get-pipeline-scan-settings.md

# getPipelineScanSettings

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetPipelineScanSettings($input: GetPipelineScanSettingsInput!) {
  getPipelineScanSettings(input: $input) {
    timeout {
      option
      count
    }
    failOnTimeout {
      true
      false
    }
    failOnError {
      true
      false
    }
    performance {
      type
      count
      tooltip
    }
    scansEnabled {
      true
      false
    }
    scanSummaryAsCommentEnabled {
      true
      false
    }
    eventsTriggeringScansForBranches {
      branchNamePatternBranchSelection
      genericOptionBranchSelection
      events {
        type
        value {
          true
          false
        }
        label
      }
    }
    scansEnabledForBitbucketApp {
      true
      false
    }
    eventsTriggeringScansForBranchesForBitbucketApp {
      branchNamePatternBranchSelection
      genericOptionBranchSelection
      events {
        type
        value {
          true
          false
        }
        label
      }
    }
    scansEnabledForGitLabWebhooks {
      true
      false
    }
    eventsTriggeringScansForBranchesForGitLabWebhooks {
      branchNamePatternBranchSelection
      genericOptionBranchSelection
      events {
        type
        value {
          true
          false
        }
        label
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
 "query": "query GetPipelineScanSettings($input: GetPipelineScanSettingsInput!) { getPipelineScanSettings(input: $input) { timeout { option count } failOnTimeout { true false } failOnError { true false } performance { type count tooltip } scansEnabled { true false } scanSummaryAsCommentEnabled { true false } eventsTriggeringScansForBranches { branchNamePatternBranchSelection genericOptionBranchSelection events { type value { true false } label } } scansEnabledForBitbucketApp { true false } eventsTriggeringScansForBranchesForBitbucketApp { branchNamePatternBranchSelection genericOptionBranchSelection events { type value { true false } label } } scansEnabledForGitLabWebhooks { true false } eventsTriggeringScansForBranchesForGitLabWebhooks { branchNamePatternBranchSelection genericOptionBranchSelection events { type value { true false } label } } } }",
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
const query = 'query GetPipelineScanSettings($input: GetPipelineScanSettingsInput!) { getPipelineScanSettings(input: $input) { timeout { option count } failOnTimeout { true false } failOnError { true false } performance { type count tooltip } scansEnabled { true false } scanSummaryAsCommentEnabled { true false } eventsTriggeringScansForBranches { branchNamePatternBranchSelection genericOptionBranchSelection events { type value { true false } label } } scansEnabledForBitbucketApp { true false } eventsTriggeringScansForBranchesForBitbucketApp { branchNamePatternBranchSelection genericOptionBranchSelection events { type value { true false } label } } scansEnabledForGitLabWebhooks { true false } eventsTriggeringScansForBranchesForGitLabWebhooks { branchNamePatternBranchSelection genericOptionBranchSelection events { type value { true false } label } } } }';

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

query = 'query GetPipelineScanSettings($input: GetPipelineScanSettingsInput!) { getPipelineScanSettings(input: $input) { timeout { option count } failOnTimeout { true false } failOnError { true false } performance { type count tooltip } scansEnabled { true false } scanSummaryAsCommentEnabled { true false } eventsTriggeringScansForBranches { branchNamePatternBranchSelection genericOptionBranchSelection events { type value { true false } label } } scansEnabledForBitbucketApp { true false } eventsTriggeringScansForBranchesForBitbucketApp { branchNamePatternBranchSelection genericOptionBranchSelection events { type value { true false } label } } scansEnabledForGitLabWebhooks { true false } eventsTriggeringScansForBranchesForGitLabWebhooks { branchNamePatternBranchSelection genericOptionBranchSelection events { type value { true false } label } } } }'

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

You can use the following argument(s) to customize your `getPipelineScanSettings` query.

| Argument                                                                                                                                                                                                                    | Description | Supported fields    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------- |
| input [`GetPipelineScanSettingsInput!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/get-pipeline-scan-settings-input) <mark style="color:red;background-color:red;">required</mark> |             | appIds `[String!]!` |

### Fields

Return type: [`GetPipelineScanSettingsResponse!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)

You can use the following field(s) to specify what information your `getPipelineScanSettings` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                                                                                                                                 | Description                                                                                                               | Supported fields                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| timeout [`[NumericSettingResponse!]!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/numeric-setting-response)                                                                                                 | General Setting. Scan timeout value in minutes                                                                            | <p>option <code>Float!</code><br>count <code>Float!</code></p>                                                                                                                                                                                                                                                           |
| failOnTimeout [`BooleanSettingResponse!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/boolean-setting-response)                                                                                              | General Setting. Whether or not a scan timeout causes a scan to fail (block)                                              | <p>true <code>Float!</code><br>false <code>Float!</code></p>                                                                                                                                                                                                                                                             |
| failOnError [`BooleanSettingResponse!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/boolean-setting-response)                                                                                                | General Setting. Whether or not an error (i.e. network, infrastructure) causes a scan to fail (block)                     | <p>true <code>Float!</code><br>false <code>Float!</code></p>                                                                                                                                                                                                                                                             |
| performance [`[ScanTypeSettingResponse!]!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/scan-type-setting-response)                                                                                          | General Setting. Scan speed                                                                                               | <p>type <code>String!</code><br>count <code>Float!</code><br>tooltip <code>String!</code></p>                                                                                                                                                                                                                            |
| scansEnabled [`BooleanSettingResponse!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/boolean-setting-response)                                                                                               | GitHub App Setting. Whether or not GitHub Checks should be run for the repository (application)                           | <p>true <code>Float!</code><br>false <code>Float!</code></p>                                                                                                                                                                                                                                                             |
| scanSummaryAsCommentEnabled [`BooleanSettingResponse!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/boolean-setting-response)                                                                                | GitHub App Setting. Whether or not GitHub Checks results should be published in a pull request comments                   | <p>true <code>Float!</code><br>false <code>Float!</code></p>                                                                                                                                                                                                                                                             |
| eventsTriggeringScansForBranches [`[EventsTriggeringScansForBranchesSettingResponse!]!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/events-triggering-scans-for-branches-setting-response)                  | GitHub App Setting. Which events for which branches should trigger GitHub Checks                                          | <p>branchNamePatternBranchSelection <code>String</code><br>genericOptionBranchSelection <a href="../types/enums/generic-option-branch-selection-type"><code>GenericOptionBranchSelectionType</code></a><br>events <a href="../types/objects/triggering-event-response"><code>\[TriggeringEventResponse!]!</code></a></p> |
| scansEnabledForBitbucketApp [`BooleanSettingResponse!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/boolean-setting-response)                                                                                | Bitbucket App Setting. Whether or not scans should be run and reported to Bitbucket APIs for the repository (application) | <p>true <code>Float!</code><br>false <code>Float!</code></p>                                                                                                                                                                                                                                                             |
| eventsTriggeringScansForBranchesForBitbucketApp [`[EventsTriggeringScansForBranchesSettingResponse!]!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/events-triggering-scans-for-branches-setting-response)   | Bitbucket App Setting. Which events for which branches should trigger scans                                               | <p>branchNamePatternBranchSelection <code>String</code><br>genericOptionBranchSelection <a href="../types/enums/generic-option-branch-selection-type"><code>GenericOptionBranchSelectionType</code></a><br>events <a href="../types/objects/triggering-event-response"><code>\[TriggeringEventResponse!]!</code></a></p> |
| scansEnabledForGitLabWebhooks [`BooleanSettingResponse!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/boolean-setting-response)                                                                              | GitLab Webhooks Setting. Whether or not scans should be run and reported to GitLab APIs for the project (application)     | <p>true <code>Float!</code><br>false <code>Float!</code></p>                                                                                                                                                                                                                                                             |
| eventsTriggeringScansForBranchesForGitLabWebhooks [`[EventsTriggeringScansForBranchesSettingResponse!]!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/events-triggering-scans-for-branches-setting-response) | GitLab Webhooks Setting. Which events for which branches should trigger scans                                             | <p>branchNamePatternBranchSelection <code>String</code><br>genericOptionBranchSelection <a href="../types/enums/generic-option-branch-selection-type"><code>GenericOptionBranchSelectionType</code></a><br>events <a href="../types/objects/triggering-event-response"><code>\[TriggeringEventResponse!]!</code></a></p> |
