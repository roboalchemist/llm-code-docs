# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-unscanned-artifacts.md

# getUnscannedArtifacts

Retrieves unscanned artifacts with filtering and pagination support.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetUnscannedArtifacts($getUnscannedArtifactsInput: GetUnscannedArtifactsInput) {
  getUnscannedArtifacts(getUnscannedArtifactsInput: $getUnscannedArtifactsInput) {
    unscannedArtifacts {
      id
      artifactId
      registryType
      registryName
      registryLink
      imageName
      imageTags
      imageCreationDate
      imageDigest
      reason
      error
      scanId
      cloudData {
        cloudIdentifier
        link
        lastExecutionTime
        lastModifiedTime
        account
        zone
        cluster
        cloudDescription {
          type
          subType
          cloudEntityAttributes {
            ... on ECS {
              os
              cpu
              memory
              containers
              registeredAt
              registeredBy
              account
              zone
            }
          }
        }
      }
    }
    offset
    total
    totalFilteredUnscannedArtifacts
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getUnscannedArtifactsInput": {
    "limit": 100,
    "offset": 0,
    "sort": {
      "field": ["createdAt"],
      "order": ["ASC"]
    },
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
    "filters": {
      "reason": ["example"],
      "registryType": ["example"],
      "registryName": ["example"],
      "imageName": ["example"],
      "imageDigest": ["example"],
      "imageTags": ["example"],
      "cloudDeployments": ["example"],
      "cluster": ["example"],
      "namespace": ["example"],
      "reachability": ["example"],
      "imageSource": ["example"]
    },
    "owners": ["example"],
    "search": "example",
    "openItems": ["digest"],
    "topFilters": ["DeployedToCloud"]
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
 "query": "query GetUnscannedArtifacts($getUnscannedArtifactsInput: GetUnscannedArtifactsInput) { getUnscannedArtifacts(getUnscannedArtifactsInput: $getUnscannedArtifactsInput) { unscannedArtifacts { id artifactId registryType registryName registryLink imageName imageTags imageCreationDate imageDigest reason error scanId cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } } offset total totalFilteredUnscannedArtifacts } }",
 "variables": {
    "getUnscannedArtifactsInput": {
      "limit": 100,
      "offset": 0,
      "sort": {
        "field": ["createdAt"],
        "order": ["ASC"]
      },
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
      "filters": {
        "reason": ["example"],
        "registryType": ["example"],
        "registryName": ["example"],
        "imageName": ["example"],
        "imageDigest": ["example"],
        "imageTags": ["example"],
        "cloudDeployments": ["example"],
        "cluster": ["example"],
        "namespace": ["example"],
        "reachability": ["example"],
        "imageSource": ["example"]
      },
      "owners": ["example"],
      "search": "example",
      "openItems": ["digest"],
      "topFilters": ["DeployedToCloud"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetUnscannedArtifacts($getUnscannedArtifactsInput: GetUnscannedArtifactsInput) { getUnscannedArtifacts(getUnscannedArtifactsInput: $getUnscannedArtifactsInput) { unscannedArtifacts { id artifactId registryType registryName registryLink imageName imageTags imageCreationDate imageDigest reason error scanId cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } } offset total totalFilteredUnscannedArtifacts } }';

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
      getUnscannedArtifactsInput: {
        limit: 100,
        offset: 0,
        sort: {
          field: ["createdAt"],
          order: ["ASC"]
        },
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
        filters: {
          reason: ["example"],
          registryType: ["example"],
          registryName: ["example"],
          imageName: ["example"],
          imageDigest: ["example"],
          imageTags: ["example"],
          cloudDeployments: ["example"],
          cluster: ["example"],
          namespace: ["example"],
          reachability: ["example"],
          imageSource: ["example"]
        },
        owners: ["example"],
        search: "example",
        openItems: ["digest"],
        topFilters: ["DeployedToCloud"]
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

query = 'query GetUnscannedArtifacts($getUnscannedArtifactsInput: GetUnscannedArtifactsInput) { getUnscannedArtifacts(getUnscannedArtifactsInput: $getUnscannedArtifactsInput) { unscannedArtifacts { id artifactId registryType registryName registryLink imageName imageTags imageCreationDate imageDigest reason error scanId cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } } offset total totalFilteredUnscannedArtifacts } }'

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
      "getUnscannedArtifactsInput": {
        "limit": 100,
        "offset": 0,
        "sort": {
          "field": ["createdAt"],
          "order": ["ASC"]
        },
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
        "filters": {
          "reason": ["example"],
          "registryType": ["example"],
          "registryName": ["example"],
          "imageName": ["example"],
          "imageDigest": ["example"],
          "imageTags": ["example"],
          "cloudDeployments": ["example"],
          "cluster": ["example"],
          "namespace": ["example"],
          "reachability": ["example"],
          "imageSource": ["example"]
        },
        "owners": ["example"],
        "search": "example",
        "openItems": ["digest"],
        "topFilters": ["DeployedToCloud"]
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

You can use the following argument(s) to customize your `getUnscannedArtifacts` query.

| Argument                                                                                                                                                                     | Description                                             | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getUnscannedArtifactsInput [`GetUnscannedArtifactsInput`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-unscanned-artifacts-input) | Input parameters for filtering, sorting, and pagination | <p>limit <code>Int</code><br>offset <code>Int</code><br>sort <a href="../types/inputs/unscanned-artifact-sort"><code>UnscannedArtifactSort</code></a><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>filters <a href="../types/inputs/unscanned-artifact-filters"><code>UnscannedArtifactFilters</code></a><br>owners <code>\[String]</code><br>search <code>String</code><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>topFilters <a href="../types/enums/unscanned-artifact-top-filters"><code>\[UnscannedArtifactTopFilters]</code></a></p> |

### Fields

Return type: [`UnscannedArtifactsResponse`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/unscanned-artifacts-response)

You can use the following field(s) to specify what information your `getUnscannedArtifacts` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                               | Description                              | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| unscannedArtifacts [`[UnscannedArtifact]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/unscanned-artifact) | Unscanned Artifacts                      | <p>id <code>String</code><br>artifactId <code>String</code><br>registryType <code>String</code><br>registryName <code>String</code><br>registryLink <code>String</code><br>imageName <code>String</code><br>imageTags <code>\[String]</code><br>imageCreationDate <code>String</code><br>imageDigest <code>String</code><br>reason <code>String</code><br>error <code>String</code><br>scanId <code>String</code><br>cloudData <a href="../types/objects/cloud-artifact-data"><code>\[CloudArtifactData]</code></a></p> |
| offset `Int`                                                                                                                                        | Offset Value for Virtualization          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| total `Int`                                                                                                                                         | Total Unscanned Artifacts Count          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| totalFilteredUnscannedArtifacts `Int`                                                                                                               | Total Filtered Unscanned Artifacts Count |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
