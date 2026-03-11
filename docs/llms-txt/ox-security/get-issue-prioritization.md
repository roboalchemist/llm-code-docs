# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issue-prioritization.md

# getIssuePrioritization

Retrieves prioritization information for issues to help focus remediation efforts. Provides data about issue severity, impact, and other factors affecting priority.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetIssuePrioritization($getIssuesInput: IssuesInput) {
  getIssuePrioritization(getIssuesInput: $getIssuesInput) {
    originalSeverity {
      label
      count
    }
    oxPrioritization {
      label
      count
    }
    oxAggregation {
      label
      count
    }
    slaOverdue {
      label
      count
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getIssuesInput": {
    "scanID": "",
    "limit": 100,
    "page": 1,
    "search": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "offset": 0,
    "sort": {
      "fields": ["Category"],
      "order": ["ASC"]
    },
    "owners": ["example"],
    "tagIds": ["example"],
    "inventoryFilters": ["New"],
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
    "limitAggItems": 42,
    "offsetAggItems": 42,
    "ignoreEnvCheck": true,
    "exportsOptions": {
      "flattenAgg": true,
      "isDemoEnabled": true,
      "name": "SomeName",
      "columns": [
        {
          "key": "Severity",
          "name": "SomeName"
        }
      ],
      "rowsLimit": 42
    },
    "issueId": "30966426-oxPolicy_securityCloudScan_100-example",
    "topOffset": 42,
    "topLevelSearch": "example",
    "scrollDirection": "example",
    "openItems": ["digest"],
    "conditionalFilters": [
      {
        "condition": "AND",
        "fieldName": "digest",
        "values": ["example"],
        "greaterThan": 13.37,
        "lessThan": 13.37
      }
    ],
    "cursorValue": "example"
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
 "query": "query GetIssuePrioritization($getIssuesInput: IssuesInput) { getIssuePrioritization(getIssuesInput: $getIssuesInput) { originalSeverity { label count } oxPrioritization { label count } oxAggregation { label count } slaOverdue { label count } } }",
 "variables": {
    "getIssuesInput": {
      "scanID": "",
      "limit": 100,
      "page": 1,
      "search": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "offset": 0,
      "sort": {
        "fields": ["Category"],
        "order": ["ASC"]
      },
      "owners": ["example"],
      "tagIds": ["example"],
      "inventoryFilters": ["New"],
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
      "limitAggItems": 42,
      "offsetAggItems": 42,
      "ignoreEnvCheck": true,
      "exportsOptions": {
        "flattenAgg": true,
        "isDemoEnabled": true,
        "name": "SomeName",
        "columns": [
          {
            "key": "Severity",
            "name": "SomeName"
          }
        ],
        "rowsLimit": 42
      },
      "issueId": "30966426-oxPolicy_securityCloudScan_100-example",
      "topOffset": 42,
      "topLevelSearch": "example",
      "scrollDirection": "example",
      "openItems": ["digest"],
      "conditionalFilters": [
        {
          "condition": "AND",
          "fieldName": "digest",
          "values": ["example"],
          "greaterThan": 13.37,
          "lessThan": 13.37
        }
      ],
      "cursorValue": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetIssuePrioritization($getIssuesInput: IssuesInput) { getIssuePrioritization(getIssuesInput: $getIssuesInput) { originalSeverity { label count } oxPrioritization { label count } oxAggregation { label count } slaOverdue { label count } } }';

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
      getIssuesInput: {
        scanID: "",
        limit: 100,
        page: 1,
        search: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        offset: 0,
        sort: {
          fields: ["Category"],
          order: ["ASC"]
        },
        owners: ["example"],
        tagIds: ["example"],
        inventoryFilters: ["New"],
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
        limitAggItems: 42,
        offsetAggItems: 42,
        ignoreEnvCheck: true,
        exportsOptions: {
          flattenAgg: true,
          isDemoEnabled: true,
          name: "SomeName",
          columns: [
            {
              key: "Severity",
              name: "SomeName"
            }
          ],
          rowsLimit: 42
        },
        issueId: "30966426-oxPolicy_securityCloudScan_100-example",
        topOffset: 42,
        topLevelSearch: "example",
        scrollDirection: "example",
        openItems: ["digest"],
        conditionalFilters: [
          {
            condition: "AND",
            fieldName: "digest",
            values: ["example"],
            greaterThan: 13.37,
            lessThan: 13.37
          }
        ],
        cursorValue: "example"
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

query = 'query GetIssuePrioritization($getIssuesInput: IssuesInput) { getIssuePrioritization(getIssuesInput: $getIssuesInput) { originalSeverity { label count } oxPrioritization { label count } oxAggregation { label count } slaOverdue { label count } } }'

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
      "getIssuesInput": {
        "scanID": "",
        "limit": 100,
        "page": 1,
        "search": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "offset": 0,
        "sort": {
          "fields": ["Category"],
          "order": ["ASC"]
        },
        "owners": ["example"],
        "tagIds": ["example"],
        "inventoryFilters": ["New"],
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
        "limitAggItems": 42,
        "offsetAggItems": 42,
        "ignoreEnvCheck": true,
        "exportsOptions": {
          "flattenAgg": true,
          "isDemoEnabled": true,
          "name": "SomeName",
          "columns": [
            {
              "key": "Severity",
              "name": "SomeName"
            }
          ],
          "rowsLimit": 42
        },
        "issueId": "30966426-oxPolicy_securityCloudScan_100-example",
        "topOffset": 42,
        "topLevelSearch": "example",
        "scrollDirection": "example",
        "openItems": ["digest"],
        "conditionalFilters": [
          {
            "condition": "AND",
            "fieldName": "digest",
            "values": ["example"],
            "greaterThan": 13.37,
            "lessThan": 13.37
          }
        ],
        "cursorValue": "example"
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

You can use the following argument(s) to customize your `getIssuePrioritization` query.

| Argument                                                                                                                      | Description                                                     | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getIssuesInput [`IssuesInput`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input) | Parameters for filtering and organizing the prioritization data | <p>scanID <code>String</code><br>limit <code>Int!</code><br>page <code>Int</code><br>search <a href="../../api--application/types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>offset <code>Int</code><br><del>filters</del> <a href="../types/inputs/issue-filters"><del><code>IssueFilters</code></del></a> ⚠️<br>sort <a href="../types/inputs/issues-sort"><code>IssuesSort</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>inventoryFilters <a href="../types/enums/inventory-types"><code>\[InventoryTypes]</code></a><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>limitAggItems <code>Int</code><br>offsetAggItems <code>Int</code><br>ignoreEnvCheck <code>Boolean</code><br>exportsOptions <a href="../types/inputs/issues-export-options"><code>IssuesExportOptions</code></a><br>issueId <code>String</code><br>topOffset <code>Int</code><br>topLevelSearch <code>String</code><br>scrollDirection <code>String</code><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>conditionalFilters <a href="../../api--application/types/inputs/conditional-filters"><code>\[ConditionalFilters]</code></a><br>cursorValue <code>String</code></p> |

### Fields

Return type: [`IssuesPrioritizationResponse`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issues-prioritization-response)

You can use the following field(s) to specify what information your `getIssuePrioritization` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                            | Description | Supported fields                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ---------------------------------------------------------- |
| originalSeverity [`[PrioritizationInfo]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/prioritization-info) |             | <p>label <code>String</code><br>count <code>Int</code></p> |
| oxPrioritization [`[PrioritizationInfo]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/prioritization-info) |             | <p>label <code>String</code><br>count <code>Int</code></p> |
| oxAggregation [`[PrioritizationInfo]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/prioritization-info)    |             | <p>label <code>String</code><br>count <code>Int</code></p> |
| slaOverdue [`[PrioritizationInfo]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/prioritization-info)       |             | <p>label <code>String</code><br>count <code>Int</code></p> |
