# Source: https://docs.ox.security/api-documentation/api-reference/api--application/queries/get-applications-conditional-filters.md

# getApplicationsConditionalFilters

Retrieves available conditional filters for applications based on current data. Helps users understand what filter options are available for refining application lists.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetApplicationsConditionalFilters($getApplicationsInput: GetApplicationsInput) {
  getApplicationsConditionalFilters(getApplicationsInput: $getApplicationsInput) {
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
  "getApplicationsInput": {
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
    "orderBy": {
      "field": "BusinessPriority",
      "direction": "ASC",
      "category": "example"
    },
    "limit": 100,
    "page": 1,
    "offset": 0,
    "applicationFilters": ["New"],
    "irrelevancyFilters": ["Archived"],
    "systemFilter": {
      "name": "cicd",
      "type": "example"
    },
    "owners": ["example"],
    "tagIds": ["example"],
    "search": "example",
    "filterSearch": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "isAppIdOnly": true,
    "appId": "30966426",
    "topOffset": 42,
    "scrollDirection": "example",
    "openItems": ["digest"],
    "irrelevant": true,
    "ignoreLimit": true,
    "conditionalFilters": [
      {
        "condition": "AND",
        "fieldName": "digest",
        "values": ["example"],
        "greaterThan": 13.37,
        "lessThan": 13.37
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
 "query": "query GetApplicationsConditionalFilters($getApplicationsInput: GetApplicationsInput) { getApplicationsConditionalFilters(getApplicationsInput: $getApplicationsInput) { total totalFiltered filters { type items { id filterId label count percent changeNumber policyId extraInfo { key value } } } } }",
 "variables": {
    "getApplicationsInput": {
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
      "orderBy": {
        "field": "BusinessPriority",
        "direction": "ASC",
        "category": "example"
      },
      "limit": 100,
      "page": 1,
      "offset": 0,
      "applicationFilters": ["New"],
      "irrelevancyFilters": ["Archived"],
      "systemFilter": {
        "name": "cicd",
        "type": "example"
      },
      "owners": ["example"],
      "tagIds": ["example"],
      "search": "example",
      "filterSearch": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "isAppIdOnly": true,
      "appId": "30966426",
      "topOffset": 42,
      "scrollDirection": "example",
      "openItems": ["digest"],
      "irrelevant": true,
      "ignoreLimit": true,
      "conditionalFilters": [
        {
          "condition": "AND",
          "fieldName": "digest",
          "values": ["example"],
          "greaterThan": 13.37,
          "lessThan": 13.37
        }
      ]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetApplicationsConditionalFilters($getApplicationsInput: GetApplicationsInput) { getApplicationsConditionalFilters(getApplicationsInput: $getApplicationsInput) { total totalFiltered filters { type items { id filterId label count percent changeNumber policyId extraInfo { key value } } } } }';

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
      getApplicationsInput: {
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
        orderBy: {
          field: "BusinessPriority",
          direction: "ASC",
          category: "example"
        },
        limit: 100,
        page: 1,
        offset: 0,
        applicationFilters: ["New"],
        irrelevancyFilters: ["Archived"],
        systemFilter: {
          name: "cicd",
          type: "example"
        },
        owners: ["example"],
        tagIds: ["example"],
        search: "example",
        filterSearch: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        isAppIdOnly: true,
        appId: "30966426",
        topOffset: 42,
        scrollDirection: "example",
        openItems: ["digest"],
        irrelevant: true,
        ignoreLimit: true,
        conditionalFilters: [
          {
            condition: "AND",
            fieldName: "digest",
            values: ["example"],
            greaterThan: 13.37,
            lessThan: 13.37
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

query = 'query GetApplicationsConditionalFilters($getApplicationsInput: GetApplicationsInput) { getApplicationsConditionalFilters(getApplicationsInput: $getApplicationsInput) { total totalFiltered filters { type items { id filterId label count percent changeNumber policyId extraInfo { key value } } } } }'

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
      "getApplicationsInput": {
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
        "orderBy": {
          "field": "BusinessPriority",
          "direction": "ASC",
          "category": "example"
        },
        "limit": 100,
        "page": 1,
        "offset": 0,
        "applicationFilters": ["New"],
        "irrelevancyFilters": ["Archived"],
        "systemFilter": {
          "name": "cicd",
          "type": "example"
        },
        "owners": ["example"],
        "tagIds": ["example"],
        "search": "example",
        "filterSearch": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "isAppIdOnly": true,
        "appId": "30966426",
        "topOffset": 42,
        "scrollDirection": "example",
        "openItems": ["digest"],
        "irrelevant": true,
        "ignoreLimit": true,
        "conditionalFilters": [
          {
            "condition": "AND",
            "fieldName": "digest",
            "values": ["example"],
            "greaterThan": 13.37,
            "lessThan": 13.37
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

You can use the following argument(s) to customize your `getApplicationsConditionalFilters` query.

| Argument                                                                                                                                                     | Description                                                                                                         | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getApplicationsInput [`GetApplicationsInput`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input) | Parameters to determine which filters should be available based on current search criteria and organization context | <p>scanId <code>String</code><br>dateRange <a href="../types/inputs/date-range"><code>DateRange</code></a><br>orderBy <a href="../types/inputs/order-apps-by"><code>OrderAppsBy</code></a><br>limit <code>Int</code><br>page <code>Int</code><br>offset <code>Int</code><br>applicationFilters <a href="../types/enums/applications-filter"><code>\[ApplicationsFilter]</code></a><br>irrelevancyFilters <a href="../types/enums/irrelevancy-filter"><code>\[IrrelevancyFilter]</code></a><br><del>filters</del> <a href="../types/inputs/app-filters"><del><code>AppFilters</code></del></a> ⚠️<br>systemFilter <a href="../types/inputs/system-filter"><code>SystemFilter</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>search <code>String</code><br>filterSearch <a href="../types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>isAppIdOnly <code>Boolean</code><br>appId <code>String</code><br>topOffset <code>Int</code><br>scrollDirection <code>String</code><br>openItems <a href="../types/enums/filter-types"><code>\[FilterTypes]</code></a><br>irrelevant <code>Boolean</code><br>ignoreLimit <code>Boolean</code><br>conditionalFilters <a href="../types/inputs/conditional-filters"><code>\[ConditionalFilters]</code></a></p> |

### Fields

Return type: [`FilterLazyResponse`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy-response)

You can use the following field(s) to specify what information your `getApplicationsConditionalFilters` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                         | Description                                  | Supported fields                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| total `Int`                                                                                                                   | Total number of items available              |                                                                                                                                                               |
| totalFiltered `Int`                                                                                                           | Total number of items after applying filters |                                                                                                                                                               |
| filters [`[FilterLazy]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy) | List of filter categories with their items   | <p>type <a href="../types/enums/filter-types"><code>FilterTypes</code></a><br>items <a href="../types/objects/filter-info"><code>\[FilterInfo]</code></a></p> |
