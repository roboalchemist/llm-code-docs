# Source: https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/queries/get-saas-bom-items.md

# getSaasBomItems

Retrieves a paginated list of SaaS BOM items for the organization with comprehensive filtering options. Useful for displaying and managing the software inventory of SaaS applications.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetSaasBomItems($getSaasBomItemsInput: GetSaasBomItemsInput) {
  getSaasBomItems(getSaasBomItemsInput: $getSaasBomItemsInput) {
    saasBomItems {
      id
      appId
      appName
      appType
      name
      link
      category
      createdAt
      extraInfo {
        key
        link
        snippet {
          detectionType
          fileName
          snippetLineNumber
          language
          text
        }
      }
      issuesBySeverity {
        info
        low
        medium
        high
        critical
        appox
      }
    }
    total
    totalFiltered
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getSaasBomItemsInput": {
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "offset": 0,
    "limit": 100,
    "owners": ["example"],
    "tagIds": ["example"],
    "filters": {
      "apps": ["example"],
      "categories": ["example"],
      "name": ["SomeName"],
      "reachability": ["example"],
      "detectionType": ["example"]
    },
    "filterSearch": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "openItems": ["digest"],
    "orderBy": {
      "field": "example",
      "direction": "ASC"
    },
    "search": "example"
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
 "query": "query GetSaasBomItems($getSaasBomItemsInput: GetSaasBomItemsInput) { getSaasBomItems(getSaasBomItemsInput: $getSaasBomItemsInput) { saasBomItems { id appId appName appType name link category createdAt extraInfo { key link snippet { detectionType fileName snippetLineNumber language text } } issuesBySeverity { info low medium high critical appox } } total totalFiltered } }",
 "variables": {
    "getSaasBomItemsInput": {
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "offset": 0,
      "limit": 100,
      "owners": ["example"],
      "tagIds": ["example"],
      "filters": {
        "apps": ["example"],
        "categories": ["example"],
        "name": ["SomeName"],
        "reachability": ["example"],
        "detectionType": ["example"]
      },
      "filterSearch": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "openItems": ["digest"],
      "orderBy": {
        "field": "example",
        "direction": "ASC"
      },
      "search": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetSaasBomItems($getSaasBomItemsInput: GetSaasBomItemsInput) { getSaasBomItems(getSaasBomItemsInput: $getSaasBomItemsInput) { saasBomItems { id appId appName appType name link category createdAt extraInfo { key link snippet { detectionType fileName snippetLineNumber language text } } issuesBySeverity { info low medium high critical appox } } total totalFiltered } }';

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
      getSaasBomItemsInput: {
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        offset: 0,
        limit: 100,
        owners: ["example"],
        tagIds: ["example"],
        filters: {
          apps: ["example"],
          categories: ["example"],
          name: ["SomeName"],
          reachability: ["example"],
          detectionType: ["example"]
        },
        filterSearch: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        openItems: ["digest"],
        orderBy: {
          field: "example",
          direction: "ASC"
        },
        search: "example"
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

query = 'query GetSaasBomItems($getSaasBomItemsInput: GetSaasBomItemsInput) { getSaasBomItems(getSaasBomItemsInput: $getSaasBomItemsInput) { saasBomItems { id appId appName appType name link category createdAt extraInfo { key link snippet { detectionType fileName snippetLineNumber language text } } issuesBySeverity { info low medium high critical appox } } total totalFiltered } }'

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
      "getSaasBomItemsInput": {
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "offset": 0,
        "limit": 100,
        "owners": ["example"],
        "tagIds": ["example"],
        "filters": {
          "apps": ["example"],
          "categories": ["example"],
          "name": ["SomeName"],
          "reachability": ["example"],
          "detectionType": ["example"]
        },
        "filterSearch": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "openItems": ["digest"],
        "orderBy": {
          "field": "example",
          "direction": "ASC"
        },
        "search": "example"
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

You can use the following argument(s) to customize your `getSaasBomItems` query.

| Argument                                                                                                                                                     | Description                                                            | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getSaasBomItemsInput [`GetSaasBomItemsInput`](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/get-saas-bom-items-input) | Input parameters for filtering, sorting, and paginating SaaS BOM items | <p>scanId <code>String</code><br>offset <code>Int</code><br>limit <code>Int</code><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>filters <a href="../types/inputs/saas-bom-filters"><code>SaasBomFilters</code></a><br>filterSearch <a href="../../api--application/types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>orderBy <a href="../types/inputs/saas-bom-order-by"><code>SaasBomOrderBy</code></a><br>search <code>String</code></p> |

### Fields

Return type: [`SaasBomItemsResponse`](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/objects/saas-bom-items-response)

You can use the following field(s) to specify what information your `getSaasBomItems` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                               | Description                                          | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| saasBomItems [`[SaasBomItem]`](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/objects/saas-bom-item) | List of SaaS BOM items matching the query criteria   | <p>id <code>String</code><br>appId <code>String</code><br>appName <code>String</code><br>appType <code>String</code><br>name <code>String</code><br>link <code>String</code><br>category <code>String</code><br>createdAt <code>Date</code><br>extraInfo <a href="../../api--application/types/objects/application-extra-info"><code>\[ApplicationExtraInfo]</code></a><br>issuesBySeverity <a href="../../api--application/types/objects/severities"><code>Severities</code></a></p> |
| total `Int`                                                                                                                         | Total number of items in the system                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| totalFiltered `Int`                                                                                                                 | Number of items matching the current filter criteria |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
