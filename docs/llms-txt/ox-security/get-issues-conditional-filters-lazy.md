# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issues-conditional-filters-lazy.md

# getIssuesConditionalFiltersLazy

Retrieves available filters and their values for conditional filtering of issues. Helps users understand what filter options are available based on their current data.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetIssuesConditionalFiltersLazy($getIssuesInput: IssuesInput, $getIssuesConditionalFiltersInput: GetIssuesConditionalFiltersInput) {
  getIssuesConditionalFiltersLazy(getIssuesInput: $getIssuesInput, getIssuesConditionalFiltersInput: $getIssuesConditionalFiltersInput) {
    total
    totalFiltered
    filters {
      type
      items {
        id
        filterId
        label
        count
        percent
        changeNumber
        policyId
        extraInfo {
          key
          value
        }
      }
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getIssuesConditionalFiltersInput": {
    "scanID": "e2ae1e94-eeee-4444-aaaa-0000ccccf660",
    "limit": 100,
    "search": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "owners": ["example"],
    "tagIds": ["example"],
    "inventoryFilters": ["New"],
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
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
    "topLevelSearch": "example"
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
 "query": "query GetIssuesConditionalFiltersLazy($getIssuesInput: IssuesInput, $getIssuesConditionalFiltersInput: GetIssuesConditionalFiltersInput) { getIssuesConditionalFiltersLazy(getIssuesInput: $getIssuesInput, getIssuesConditionalFiltersInput: $getIssuesConditionalFiltersInput) { total totalFiltered filters { type items { id filterId label count percent changeNumber policyId extraInfo { key value } } } } }",
 "variables": {
    "getIssuesConditionalFiltersInput": {
      "scanID": "e2ae1e94-eeee-4444-aaaa-0000ccccf660",
      "limit": 100,
      "search": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "owners": ["example"],
      "tagIds": ["example"],
      "inventoryFilters": ["New"],
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
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
      "topLevelSearch": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetIssuesConditionalFiltersLazy($getIssuesInput: IssuesInput, $getIssuesConditionalFiltersInput: GetIssuesConditionalFiltersInput) { getIssuesConditionalFiltersLazy(getIssuesInput: $getIssuesInput, getIssuesConditionalFiltersInput: $getIssuesConditionalFiltersInput) { total totalFiltered filters { type items { id filterId label count percent changeNumber policyId extraInfo { key value } } } } }';

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
      getIssuesConditionalFiltersInput: {
        scanID: "e2ae1e94-eeee-4444-aaaa-0000ccccf660",
        limit: 100,
        search: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        owners: ["example"],
        tagIds: ["example"],
        inventoryFilters: ["New"],
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
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
        topLevelSearch: "example"
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

query = 'query GetIssuesConditionalFiltersLazy($getIssuesInput: IssuesInput, $getIssuesConditionalFiltersInput: GetIssuesConditionalFiltersInput) { getIssuesConditionalFiltersLazy(getIssuesInput: $getIssuesInput, getIssuesConditionalFiltersInput: $getIssuesConditionalFiltersInput) { total totalFiltered filters { type items { id filterId label count percent changeNumber policyId extraInfo { key value } } } } }'

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
      "getIssuesConditionalFiltersInput": {
        "scanID": "e2ae1e94-eeee-4444-aaaa-0000ccccf660",
        "limit": 100,
        "search": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "owners": ["example"],
        "tagIds": ["example"],
        "inventoryFilters": ["New"],
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
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
        "topLevelSearch": "example"
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

You can use the following argument(s) to customize your `getIssuesConditionalFiltersLazy` query.

| Argument                                                                                                                                                                                     | Description                                                                                                         | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getIssuesInput [`IssuesInput`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input)                                                                | Deprecated: Use getIssuesConditionalFiltersInput instead                                                            | <p>scanID <code>String</code><br>limit <code>Int!</code><br>page <code>Int</code><br>search <a href="../../api--application/types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>offset <code>Int</code><br><del>filters</del> <a href="../types/inputs/issue-filters"><del><code>IssueFilters</code></del></a> ⚠️<br>sort <a href="../types/inputs/issues-sort"><code>IssuesSort</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>inventoryFilters <a href="../types/enums/inventory-types"><code>\[InventoryTypes]</code></a><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>limitAggItems <code>Int</code><br>offsetAggItems <code>Int</code><br>ignoreEnvCheck <code>Boolean</code><br>exportsOptions <a href="../types/inputs/issues-export-options"><code>IssuesExportOptions</code></a><br>issueId <code>String</code><br>topOffset <code>Int</code><br>topLevelSearch <code>String</code><br>scrollDirection <code>String</code><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>conditionalFilters <a href="../../api--application/types/inputs/conditional-filters"><code>\[ConditionalFilters]</code></a><br>cursorValue <code>String</code></p> |
| getIssuesConditionalFiltersInput [`GetIssuesConditionalFiltersInput`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/get-issues-conditional-filters-input) | Parameters to determine which filters should be available based on current search criteria and organization context | <p>scanID <code>String</code><br>limit <code>Int</code><br>search <a href="../../api--application/types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>inventoryFilters <a href="../types/enums/inventory-types"><code>\[InventoryTypes]</code></a><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>conditionalFilters <a href="../../api--application/types/inputs/conditional-filters"><code>\[ConditionalFilters]</code></a><br>topLevelSearch <code>String</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### Fields

Return type: [`FilterLazyResponse`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy-response)

You can use the following field(s) to specify what information your `getIssuesConditionalFiltersLazy` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                         | Description                                  | Supported fields                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| total `Int`                                                                                                                   | Total number of items available              |                                                                                                                                                                                                       |
| totalFiltered `Int`                                                                                                           | Total number of items after applying filters |                                                                                                                                                                                                       |
| filters [`[FilterLazy]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy) | List of filter categories with their items   | <p>type <a href="../../api--application/types/enums/filter-types"><code>FilterTypes</code></a><br>items <a href="../../api--application/types/objects/filter-info"><code>\[FilterInfo]</code></a></p> |
