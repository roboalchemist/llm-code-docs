# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/queries/get-api-security-filters-lazy.md

# getApiSecurityFiltersLazy

Retrieves filter options with lazy loading support for better performance.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetApiSecurityFiltersLazy($getApiSecurityInput: GetApiSecurityInput) {
  getApiSecurityFiltersLazy(getApiSecurityInput: $getApiSecurityInput) {
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
  "getApiSecurityInput": {
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "offset": 0,
    "limit": 100,
    "owners": ["example"],
    "tagIds": ["example"],
    "search": "/api/v2/",
    "filters": {
      "apps": ["repo-name"],
      "appIds": ["1234567890"],
      "titles": ["Kubernetes"],
      "endpoints": ["/api/v1/some/endpoint"],
      "methods": ["GET"],
      "framework": ["OpenAPI"],
      "languages": ["OpenAPI"],
      "issueIds": ["30966426-oxPolicy_securityCloudScan_100-example"],
      "apiId": ["ceb76dd8-7c11-448c-9056-17c5b5bfa361"],
      "source": ["OpenAPI"],
      "severities": ["2"],
      "reachability": ["Code"],
      "appTags": ["Private repo"]
    },
    "filterSearch": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "openItems": ["digest"],
    "orderBy": {
      "field": "title",
      "direction": "ASC"
    }
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
 "query": "query GetApiSecurityFiltersLazy($getApiSecurityInput: GetApiSecurityInput) { getApiSecurityFiltersLazy(getApiSecurityInput: $getApiSecurityInput) { total totalFiltered filters { type items { id filterId label count percent changeNumber policyId extraInfo { key value } } } } }",
 "variables": {
    "getApiSecurityInput": {
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "offset": 0,
      "limit": 100,
      "owners": ["example"],
      "tagIds": ["example"],
      "search": "/api/v2/",
      "filters": {
        "apps": ["repo-name"],
        "appIds": ["1234567890"],
        "titles": ["Kubernetes"],
        "endpoints": ["/api/v1/some/endpoint"],
        "methods": ["GET"],
        "framework": ["OpenAPI"],
        "languages": ["OpenAPI"],
        "issueIds": ["30966426-oxPolicy_securityCloudScan_100-example"],
        "apiId": ["ceb76dd8-7c11-448c-9056-17c5b5bfa361"],
        "source": ["OpenAPI"],
        "severities": ["2"],
        "reachability": ["Code"],
        "appTags": ["Private repo"]
      },
      "filterSearch": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "openItems": ["digest"],
      "orderBy": {
        "field": "title",
        "direction": "ASC"
      }
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetApiSecurityFiltersLazy($getApiSecurityInput: GetApiSecurityInput) { getApiSecurityFiltersLazy(getApiSecurityInput: $getApiSecurityInput) { total totalFiltered filters { type items { id filterId label count percent changeNumber policyId extraInfo { key value } } } } }';

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
      getApiSecurityInput: {
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        offset: 0,
        limit: 100,
        owners: ["example"],
        tagIds: ["example"],
        search: "/api/v2/",
        filters: {
          apps: ["repo-name"],
          appIds: ["1234567890"],
          titles: ["Kubernetes"],
          endpoints: ["/api/v1/some/endpoint"],
          methods: ["GET"],
          framework: ["OpenAPI"],
          languages: ["OpenAPI"],
          issueIds: ["30966426-oxPolicy_securityCloudScan_100-example"],
          apiId: ["ceb76dd8-7c11-448c-9056-17c5b5bfa361"],
          source: ["OpenAPI"],
          severities: ["2"],
          reachability: ["Code"],
          appTags: ["Private repo"]
        },
        filterSearch: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        openItems: ["digest"],
        orderBy: {
          field: "title",
          direction: "ASC"
        }
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

query = 'query GetApiSecurityFiltersLazy($getApiSecurityInput: GetApiSecurityInput) { getApiSecurityFiltersLazy(getApiSecurityInput: $getApiSecurityInput) { total totalFiltered filters { type items { id filterId label count percent changeNumber policyId extraInfo { key value } } } } }'

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
      "getApiSecurityInput": {
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "offset": 0,
        "limit": 100,
        "owners": ["example"],
        "tagIds": ["example"],
        "search": "/api/v2/",
        "filters": {
          "apps": ["repo-name"],
          "appIds": ["1234567890"],
          "titles": ["Kubernetes"],
          "endpoints": ["/api/v1/some/endpoint"],
          "methods": ["GET"],
          "framework": ["OpenAPI"],
          "languages": ["OpenAPI"],
          "issueIds": ["30966426-oxPolicy_securityCloudScan_100-example"],
          "apiId": ["ceb76dd8-7c11-448c-9056-17c5b5bfa361"],
          "source": ["OpenAPI"],
          "severities": ["2"],
          "reachability": ["Code"],
          "appTags": ["Private repo"]
        },
        "filterSearch": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "openItems": ["digest"],
        "orderBy": {
          "field": "title",
          "direction": "ASC"
        }
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

You can use the following argument(s) to customize your `getApiSecurityFiltersLazy` query.

| Argument                                                                                                                                                    | Description                                    | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getApiSecurityInput [`GetApiSecurityInput`](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/inputs/get-api-security-input) | Parameters for the lazy-loaded filter options. | <p>scanId <code>String</code><br>offset <code>Int</code><br>limit <code>Int</code><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>search <code>String</code><br>filters <a href="../types/inputs/api-sec-filters"><code>ApiSecFilters</code></a><br>filterSearch <a href="../../api--application/types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>orderBy <a href="../types/inputs/api-security-order-by"><code>ApiSecurityOrderBy</code></a></p> |

### Fields

Return type: [`FilterLazyResponse`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy-response)

You can use the following field(s) to specify what information your `getApiSecurityFiltersLazy` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                         | Description                                  | Supported fields                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| total `Int`                                                                                                                   | Total number of items available              |                                                                                                                                                                                                       |
| totalFiltered `Int`                                                                                                           | Total number of items after applying filters |                                                                                                                                                                                                       |
| filters [`[FilterLazy]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy) | List of filter categories with their items   | <p>type <a href="../../api--application/types/enums/filter-types"><code>FilterTypes</code></a><br>items <a href="../../api--application/types/objects/filter-info"><code>\[FilterInfo]</code></a></p> |
