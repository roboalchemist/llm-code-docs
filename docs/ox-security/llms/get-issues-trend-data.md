# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issues-trend-data.md

# getIssuesTrendData

Retrieves trend data showing how issues have changed over time. Useful for tracking security posture improvements and identifying patterns.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetIssuesTrendData($getIssuesTrendInput: FetchDashboardInput) {
  getIssuesTrendData(getIssuesTrendInput: $getIssuesTrendInput) {
    scanId
    scanDate
    info
    low
    medium
    high
    critical
    appox
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getIssuesTrendInput": {
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "limit": 100,
    "orderBy": {
      "field": "BusinessPriority",
      "direction": "ASC"
    },
    "dateRange": {
      "from": 1672531200000,
      "to": 1704067199000
    },
    "filters": ["New"],
    "owners": ["example"],
    "appIds": ["30966426"],
    "tagIds": ["example"],
    "isSingleRepoScan": true,
    "apps": ["example"],
    "orgUnits": ["example"],
    "severities": [42],
    "categories": [42],
    "tags": ["example"],
    "conditionalFilters": [
      {
        "condition": "OR",
        "fieldName": "criticality",
        "values": ["example"]
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
 "query": "query GetIssuesTrendData($getIssuesTrendInput: FetchDashboardInput) { getIssuesTrendData(getIssuesTrendInput: $getIssuesTrendInput) { scanId scanDate info low medium high critical appox } }",
 "variables": {
    "getIssuesTrendInput": {
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "limit": 100,
      "orderBy": {
        "field": "BusinessPriority",
        "direction": "ASC"
      },
      "dateRange": {
        "from": 1672531200000,
        "to": 1704067199000
      },
      "filters": ["New"],
      "owners": ["example"],
      "appIds": ["30966426"],
      "tagIds": ["example"],
      "isSingleRepoScan": true,
      "apps": ["example"],
      "orgUnits": ["example"],
      "severities": [42],
      "categories": [42],
      "tags": ["example"],
      "conditionalFilters": [
        {
          "condition": "OR",
          "fieldName": "criticality",
          "values": ["example"]
        }
      ]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetIssuesTrendData($getIssuesTrendInput: FetchDashboardInput) { getIssuesTrendData(getIssuesTrendInput: $getIssuesTrendInput) { scanId scanDate info low medium high critical appox } }';

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
      getIssuesTrendInput: {
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        limit: 100,
        orderBy: {
          field: "BusinessPriority",
          direction: "ASC"
        },
        dateRange: {
          from: 1672531200000,
          to: 1704067199000
        },
        filters: ["New"],
        owners: ["example"],
        appIds: ["30966426"],
        tagIds: ["example"],
        isSingleRepoScan: true,
        apps: ["example"],
        orgUnits: ["example"],
        severities: [42],
        categories: [42],
        tags: ["example"],
        conditionalFilters: [
          {
            condition: "OR",
            fieldName: "criticality",
            values: ["example"]
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

query = 'query GetIssuesTrendData($getIssuesTrendInput: FetchDashboardInput) { getIssuesTrendData(getIssuesTrendInput: $getIssuesTrendInput) { scanId scanDate info low medium high critical appox } }'

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
      "getIssuesTrendInput": {
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "limit": 100,
        "orderBy": {
          "field": "BusinessPriority",
          "direction": "ASC"
        },
        "dateRange": {
          "from": 1672531200000,
          "to": 1704067199000
        },
        "filters": ["New"],
        "owners": ["example"],
        "appIds": ["30966426"],
        "tagIds": ["example"],
        "isSingleRepoScan": true,
        "apps": ["example"],
        "orgUnits": ["example"],
        "severities": [42],
        "categories": [42],
        "tags": ["example"],
        "conditionalFilters": [
          {
            "condition": "OR",
            "fieldName": "criticality",
            "values": ["example"]
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

You can use the following argument(s) to customize your `getIssuesTrendData` query.

| Argument                                                                                                                                            | Description                                                                | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getIssuesTrendInput [`FetchDashboardInput`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/fetch-dashboard-input) | Parameters specifying the time range and other criteria for trend analysis | <p>scanId <code>String</code><br>limit <code>Int</code><br>orderBy <a href="../types/inputs/order-by"><code>OrderBy</code></a><br>dateRange <a href="../types/inputs/date-range-filter"><code>DateRangeFilter</code></a><br>filters <a href="../types/enums/inventory-types"><code>\[InventoryTypes]</code></a><br>owners <code>\[String]</code><br>appIds <code>\[String]</code><br>tagIds <code>\[String]</code><br>isSingleRepoScan <code>Boolean</code><br>apps <code>\[String]</code><br>orgUnits <code>\[String]</code><br>severities <code>\[Int]</code><br>categories <code>\[Int]</code><br>tags <code>\[String]</code><br>conditionalFilters <a href="../types/inputs/issues-trend-data-conditional-filters"><code>\[IssuesTrendDataConditionalFilters]</code></a></p> |

### Fields

Return type: [`[IssuesTrendResponse]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issues-trend-response)

You can use the following field(s) to specify what information your `getIssuesTrendData` query will return. Please note that some fields may have their own subfields.

| Field            | Description | Supported fields |
| ---------------- | ----------- | ---------------- |
| scanId `String`  |             |                  |
| scanDate `Float` |             |                  |
| info `Int`       |             |                  |
| low `Int`        |             |                  |
| medium `Int`     |             |                  |
| high `Int`       |             |                  |
| critical `Int`   |             |                  |
| appox `Int`      |             |                  |
