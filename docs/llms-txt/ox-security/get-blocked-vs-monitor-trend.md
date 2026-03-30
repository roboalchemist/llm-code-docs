# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/queries/get-blocked-vs-monitor-trend.md

# getBlockedVsMonitorTrend

Retrieves trend data showing the ratio of blocked vs monitored pipeline executions over time.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetBlockedVsMonitorTrend($getPipelineSummaryInput: GetPipelineSummaryInput) {
  getBlockedVsMonitorTrend(getPipelineSummaryInput: $getPipelineSummaryInput) {
    jobTriggeredAt
    passed
    monitor
    block
    total
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
 "query": "query GetBlockedVsMonitorTrend($getPipelineSummaryInput: GetPipelineSummaryInput) { getBlockedVsMonitorTrend(getPipelineSummaryInput: $getPipelineSummaryInput) { jobTriggeredAt passed monitor block total } }",
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
const query = 'query GetBlockedVsMonitorTrend($getPipelineSummaryInput: GetPipelineSummaryInput) { getBlockedVsMonitorTrend(getPipelineSummaryInput: $getPipelineSummaryInput) { jobTriggeredAt passed monitor block total } }';

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

query = 'query GetBlockedVsMonitorTrend($getPipelineSummaryInput: GetPipelineSummaryInput) { getBlockedVsMonitorTrend(getPipelineSummaryInput: $getPipelineSummaryInput) { jobTriggeredAt passed monitor block total } }'

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

You can use the following argument(s) to customize your `getBlockedVsMonitorTrend` query.

| Argument                                                                                                                                                            | Description                                                                                      | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getPipelineSummaryInput [`GetPipelineSummaryInput`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/get-pipeline-summary-input) | Parameters for filtering which pipeline data to include in the blocked vs monitor trend analysis | <p>limit <code>Int</code><br>offset <code>Int</code><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>filters <a href="../types/inputs/pipeline-summary-filters"><code>PipelineSummaryFilters</code></a><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a></p> |

### Fields

Return type: [`[BlockedVsMonitorTrendRes]`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/blocked-vs-monitor-trend-res)

You can use the following field(s) to specify what information your `getBlockedVsMonitorTrend` query will return. Please note that some fields may have their own subfields.

| Field                   | Description                                                         | Supported fields |
| ----------------------- | ------------------------------------------------------------------- | ---------------- |
| jobTriggeredAt `String` | Timestamp when the pipeline job was triggered                       |                  |
| passed `Int`            | Number of pipelines that passed security checks                     |                  |
| monitor `Int`           | Number of pipelines in monitor mode (issues found but not blocking) |                  |
| block `Int`             | Number of pipelines blocked due to security issues                  |                  |
| total `Int`             | Total number of pipeline executions                                 |                  |
