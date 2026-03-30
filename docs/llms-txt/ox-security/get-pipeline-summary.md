# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/queries/get-pipeline-summary.md

# getPipelineSummary

Retrieves pipeline execution summaries with security analysis results and metrics.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetPipelineSummary($getPipelineSummaryInput: GetPipelineSummaryInput) {
  getPipelineSummary(getPipelineSummaryInput: $getPipelineSummaryInput) {
    pipelineSummaries {
      apps {
        appId
        appName
        appType
      }
      sourceBranch
      targetBranch
      result
      jobId
      jobTriggeredBy
      jobTriggeredAt
      jobCompletedAt
      jobDuration
      jobTriggeredReason
      jobUrl
      totalIssues
      totalBlockingIssues
      pullRequestId
      pullRequestUrl
      tags {
        tagId
        tagType
        name
        displayName
        createdBy
        appliedBy
        tagCategory
      }
      issues {
        appox
        critical
        high
        medium
        low
        info
      }
      eventType
      cicdType
      scanCompletionStatus
      pipelineScanType
      artifactInfo {
        name
        tag
        digest
      }
      workflows {
        id
        name
      }
    }
    offset
    total
    totalFiltered
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getPipelineSummaryInput": {
    "limit": 100,
    "offset": 0,
    "owners": ["example"],
    "tagIds": ["example"],
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
    "filters": {
      "apps": ["example"],
      "result": ["example"],
      "jobTriggeredBy": ["example"],
      "sourceBranches": ["example"],
      "targetBranches": ["example"],
      "severities": ["example"],
      "eventTypes": ["example"],
      "cicdTypes": ["example"],
      "tags": ["example"],
      "jobId": ["example"],
      "scanCompletionStatus": ["example"],
      "pipelineScanType": ["example"],
      "pipelineArtifactName": ["example"],
      "pipelineArtifactTag": ["example"],
      "workflows": ["example"]
    },
    "openItems": ["digest"]
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
 "query": "query GetPipelineSummary($getPipelineSummaryInput: GetPipelineSummaryInput) { getPipelineSummary(getPipelineSummaryInput: $getPipelineSummaryInput) { pipelineSummaries { apps { appId appName appType } sourceBranch targetBranch result jobId jobTriggeredBy jobTriggeredAt jobCompletedAt jobDuration jobTriggeredReason jobUrl totalIssues totalBlockingIssues pullRequestId pullRequestUrl tags { tagId tagType name displayName createdBy appliedBy tagCategory } issues { appox critical high medium low info } eventType cicdType scanCompletionStatus pipelineScanType artifactInfo { name tag digest } workflows { id name } } offset total totalFiltered } }",
 "variables": {
    "getPipelineSummaryInput": {
      "limit": 100,
      "offset": 0,
      "owners": ["example"],
      "tagIds": ["example"],
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
      "filters": {
        "apps": ["example"],
        "result": ["example"],
        "jobTriggeredBy": ["example"],
        "sourceBranches": ["example"],
        "targetBranches": ["example"],
        "severities": ["example"],
        "eventTypes": ["example"],
        "cicdTypes": ["example"],
        "tags": ["example"],
        "jobId": ["example"],
        "scanCompletionStatus": ["example"],
        "pipelineScanType": ["example"],
        "pipelineArtifactName": ["example"],
        "pipelineArtifactTag": ["example"],
        "workflows": ["example"]
      },
      "openItems": ["digest"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetPipelineSummary($getPipelineSummaryInput: GetPipelineSummaryInput) { getPipelineSummary(getPipelineSummaryInput: $getPipelineSummaryInput) { pipelineSummaries { apps { appId appName appType } sourceBranch targetBranch result jobId jobTriggeredBy jobTriggeredAt jobCompletedAt jobDuration jobTriggeredReason jobUrl totalIssues totalBlockingIssues pullRequestId pullRequestUrl tags { tagId tagType name displayName createdBy appliedBy tagCategory } issues { appox critical high medium low info } eventType cicdType scanCompletionStatus pipelineScanType artifactInfo { name tag digest } workflows { id name } } offset total totalFiltered } }';

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
      getPipelineSummaryInput: {
        limit: 100,
        offset: 0,
        owners: ["example"],
        tagIds: ["example"],
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
        filters: {
          apps: ["example"],
          result: ["example"],
          jobTriggeredBy: ["example"],
          sourceBranches: ["example"],
          targetBranches: ["example"],
          severities: ["example"],
          eventTypes: ["example"],
          cicdTypes: ["example"],
          tags: ["example"],
          jobId: ["example"],
          scanCompletionStatus: ["example"],
          pipelineScanType: ["example"],
          pipelineArtifactName: ["example"],
          pipelineArtifactTag: ["example"],
          workflows: ["example"]
        },
        openItems: ["digest"]
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

query = 'query GetPipelineSummary($getPipelineSummaryInput: GetPipelineSummaryInput) { getPipelineSummary(getPipelineSummaryInput: $getPipelineSummaryInput) { pipelineSummaries { apps { appId appName appType } sourceBranch targetBranch result jobId jobTriggeredBy jobTriggeredAt jobCompletedAt jobDuration jobTriggeredReason jobUrl totalIssues totalBlockingIssues pullRequestId pullRequestUrl tags { tagId tagType name displayName createdBy appliedBy tagCategory } issues { appox critical high medium low info } eventType cicdType scanCompletionStatus pipelineScanType artifactInfo { name tag digest } workflows { id name } } offset total totalFiltered } }'

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
      "getPipelineSummaryInput": {
        "limit": 100,
        "offset": 0,
        "owners": ["example"],
        "tagIds": ["example"],
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
        "filters": {
          "apps": ["example"],
          "result": ["example"],
          "jobTriggeredBy": ["example"],
          "sourceBranches": ["example"],
          "targetBranches": ["example"],
          "severities": ["example"],
          "eventTypes": ["example"],
          "cicdTypes": ["example"],
          "tags": ["example"],
          "jobId": ["example"],
          "scanCompletionStatus": ["example"],
          "pipelineScanType": ["example"],
          "pipelineArtifactName": ["example"],
          "pipelineArtifactTag": ["example"],
          "workflows": ["example"]
        },
        "openItems": ["digest"]
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

You can use the following argument(s) to customize your `getPipelineSummary` query.

| Argument                                                                                                                                                            | Description                                                | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getPipelineSummaryInput [`GetPipelineSummaryInput`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/get-pipeline-summary-input) | Parameters for filtering and paginating pipeline summaries | <p>limit <code>Int</code><br>offset <code>Int</code><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>filters <a href="../types/inputs/pipeline-summary-filters"><code>PipelineSummaryFilters</code></a><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a></p> |

### Fields

Return type: [`PipelineSummaryResponse`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-summary-response)

You can use the following field(s) to specify what information your `getPipelineSummary` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                          | Description                                               | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| pipelineSummaries [`[PipelineSummary]`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-summary) | List of pipeline execution summaries                      | <p>apps <a href="../types/objects/single-app"><code>\[SingleApp]</code></a><br>sourceBranch <code>String</code><br>targetBranch <code>String</code><br>result <code>String</code><br>jobId <code>String</code><br>jobTriggeredBy <code>String</code><br>jobTriggeredAt <code>String</code><br>jobCompletedAt <code>String</code><br>jobDuration <code>Int</code><br>jobTriggeredReason <code>String</code><br>jobUrl <code>String</code><br>totalIssues <code>String</code><br>totalBlockingIssues <code>String</code><br>pullRequestId <code>String</code><br>pullRequestUrl <code>String</code><br>tags <a href="../types/objects/tag-output"><code>\[TagOutput]</code></a><br>issues <a href="../../api--issue/types/objects/issues-by-severity"><code>IssuesBySeverity</code></a><br>eventType <code>String</code><br>cicdType <code>String</code><br>scanCompletionStatus <a href="../types/enums/pipeline-scan-completion-status"><code>PipelineScanCompletionStatus</code></a><br>pipelineScanType <code>String</code><br>artifactInfo <a href="../types/objects/pipeline-artifact-info"><code>PipelineArtifactInfo</code></a><br>workflows <a href="../../api--issue/types/objects/ox-workflow"><code>\[OxWorkflow]</code></a></p> |
| offset `Int`                                                                                                                                   | Current pagination offset                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| total `Int`                                                                                                                                    | Total number of pipeline summaries available              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| totalFiltered `Int`                                                                                                                            | Total number of pipeline summaries after applying filters |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
