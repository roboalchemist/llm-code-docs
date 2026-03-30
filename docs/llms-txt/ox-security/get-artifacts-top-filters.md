# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-artifacts-top-filters.md

# getArtifactsTopFilters

Retrieves artifacts top filters.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetArtifactsTopFilters($getArtifactsInput: GetArtifactsInput) {
  getArtifactsTopFilters(getArtifactsInput: $getArtifactsInput) {
    name
    label
    count
    delta
    trend
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getArtifactsInput": {
    "limit": 100,
    "offset": 0,
    "sort": {
      "field": ["AppName"],
      "order": ["ASC"]
    },
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
    "filters": {
      "apps": ["example"],
      "artifactType": ["example"],
      "artifactName": ["example"],
      "artifactFullName": ["example"],
      "version": ["example"],
      "sourceType": ["example"],
      "sourceTools": ["example"],
      "registryType": ["example"],
      "registryName": ["example"],
      "cloud": ["example"],
      "cluster": ["example"],
      "namespace": ["example"],
      "cloudDeployments": ["example"],
      "categories": ["example"],
      "issueSeverities": ["example"],
      "reachability": ["example"],
      "artifactIntegrity": ["example"],
      "artifactSha": ["example"],
      "imageSource": ["example"]
    },
    "artifactTopFilters": ["WithHighSeverityIssues"],
    "owners": ["example"],
    "tagIds": ["example"],
    "search": "example",
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
 "query": "query GetArtifactsTopFilters($getArtifactsInput: GetArtifactsInput) { getArtifactsTopFilters(getArtifactsInput: $getArtifactsInput) { name label count delta trend } }",
 "variables": {
    "getArtifactsInput": {
      "limit": 100,
      "offset": 0,
      "sort": {
        "field": ["AppName"],
        "order": ["ASC"]
      },
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
      "filters": {
        "apps": ["example"],
        "artifactType": ["example"],
        "artifactName": ["example"],
        "artifactFullName": ["example"],
        "version": ["example"],
        "sourceType": ["example"],
        "sourceTools": ["example"],
        "registryType": ["example"],
        "registryName": ["example"],
        "cloud": ["example"],
        "cluster": ["example"],
        "namespace": ["example"],
        "cloudDeployments": ["example"],
        "categories": ["example"],
        "issueSeverities": ["example"],
        "reachability": ["example"],
        "artifactIntegrity": ["example"],
        "artifactSha": ["example"],
        "imageSource": ["example"]
      },
      "artifactTopFilters": ["WithHighSeverityIssues"],
      "owners": ["example"],
      "tagIds": ["example"],
      "search": "example",
      "openItems": ["digest"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetArtifactsTopFilters($getArtifactsInput: GetArtifactsInput) { getArtifactsTopFilters(getArtifactsInput: $getArtifactsInput) { name label count delta trend } }';

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
      getArtifactsInput: {
        limit: 100,
        offset: 0,
        sort: {
          field: ["AppName"],
          order: ["ASC"]
        },
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
        filters: {
          apps: ["example"],
          artifactType: ["example"],
          artifactName: ["example"],
          artifactFullName: ["example"],
          version: ["example"],
          sourceType: ["example"],
          sourceTools: ["example"],
          registryType: ["example"],
          registryName: ["example"],
          cloud: ["example"],
          cluster: ["example"],
          namespace: ["example"],
          cloudDeployments: ["example"],
          categories: ["example"],
          issueSeverities: ["example"],
          reachability: ["example"],
          artifactIntegrity: ["example"],
          artifactSha: ["example"],
          imageSource: ["example"]
        },
        artifactTopFilters: ["WithHighSeverityIssues"],
        owners: ["example"],
        tagIds: ["example"],
        search: "example",
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

query = 'query GetArtifactsTopFilters($getArtifactsInput: GetArtifactsInput) { getArtifactsTopFilters(getArtifactsInput: $getArtifactsInput) { name label count delta trend } }'

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
      "getArtifactsInput": {
        "limit": 100,
        "offset": 0,
        "sort": {
          "field": ["AppName"],
          "order": ["ASC"]
        },
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
        "filters": {
          "apps": ["example"],
          "artifactType": ["example"],
          "artifactName": ["example"],
          "artifactFullName": ["example"],
          "version": ["example"],
          "sourceType": ["example"],
          "sourceTools": ["example"],
          "registryType": ["example"],
          "registryName": ["example"],
          "cloud": ["example"],
          "cluster": ["example"],
          "namespace": ["example"],
          "cloudDeployments": ["example"],
          "categories": ["example"],
          "issueSeverities": ["example"],
          "reachability": ["example"],
          "artifactIntegrity": ["example"],
          "artifactSha": ["example"],
          "imageSource": ["example"]
        },
        "artifactTopFilters": ["WithHighSeverityIssues"],
        "owners": ["example"],
        "tagIds": ["example"],
        "search": "example",
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

You can use the following argument(s) to customize your `getArtifactsTopFilters` query.

| Argument                                                                                                                                         | Description | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getArtifactsInput [`GetArtifactsInput`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-input) |             | <p>limit <code>Int</code><br>offset <code>Int</code><br>sort <a href="../types/inputs/artifacts-sort"><code>ArtifactsSort</code></a><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>filters <a href="../types/inputs/artifact-filters"><code>ArtifactFilters</code></a><br>artifactTopFilters <a href="../types/enums/artifact-top-filters"><code>\[ArtifactTopFilters]</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>search <code>String</code><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a></p> |

### Fields

Return type: [`[ArtifactsTopFiltersResponse]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifacts-top-filters-response)

You can use the following field(s) to specify what information your `getArtifactsTopFilters` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                | Description | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ---------------- |
| name [`ArtifactTopFilters`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/artifact-top-filters) |             |                  |
| label `String`                                                                                                                       |             |                  |
| count `Int`                                                                                                                          |             |                  |
| delta `Int`                                                                                                                          |             |                  |
| trend `String`                                                                                                                       |             |                  |
