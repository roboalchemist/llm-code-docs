# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/queries/get-cloud-items.md

# getCloudItems

Retrieves cloud security items including cloud resources, containers, and their security posture.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetCloudItems($cloudItemsInput: CloudItemsInput) {
  getCloudItems(cloudItemsInput: $cloudItemsInput) {
    cloudItems {
      id
      assetName
      service
      resourceId
      cbomId
      cbomProvider
      resourceType
      resourceName
      accountId
      firstSeen
      cloudProvider
      serviceCategory
      applications {
        id
        name
        type
      }
      isExposed
      imageSource
      registryType
      registryName
      imageScanStatus
      exposurePath {
        type
        name
        cbomId
      }
      accountName
      subService
      region
      resourceTags
      resourceArn
      images {
        name
        hashes {
          hash
          isFromRegistry
        }
        tags
      }
      relatedIssues {
        info
        low
        medium
        high
        critical
        appox
      }
      issueSeverityBreakdown {
        name
        severities {
          info
          low
          medium
          high
          critical
          appox
        }
      }
      issuesStats {
        totalIssues
        sourceTools {
          name
          total
        }
        categories {
          name
          total
        }
        severities {
          name
          total
        }
      }
      cluster
      link
      imageHash
      workloads {
        type
        namespace
        name
        cluster
        region
        isExposed
        consoleLink
        exposurePath {
          type
          name
          cbomId
        }
      }
      artifactIds
    }
    offset
    topOffset
    total
    totalFiltered
    selectedPosition
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "cloudItemsInput": {
    "limit": 100,
    "offset": 0,
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
    "filters": {
      "apps": ["example"],
      "service": ["example"],
      "type": ["example"],
      "cloudProvider": ["example"],
      "assetName": ["example"],
      "accountId": ["example"],
      "region": ["example"],
      "serviceCategory": ["example"],
      "cluster": ["example"],
      "severities": ["example"],
      "isExposed": ["example"],
      "imageSource": ["example"],
      "registryType": ["example"],
      "registryName": ["example"],
      "imageScanStatus": ["example"],
      "artifactIds": ["example"]
    },
    "filterSearch": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "owners": ["example"],
    "tagIds": ["example"],
    "search": "example",
    "openItems": ["digest"],
    "orderBy": {
      "field": "example",
      "direction": "ASC"
    },
    "topOffset": 42,
    "scrollDirection": "example",
    "cbomId": "example"
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
 "query": "query GetCloudItems($cloudItemsInput: CloudItemsInput) { getCloudItems(cloudItemsInput: $cloudItemsInput) { cloudItems { id assetName service resourceId cbomId cbomProvider resourceType resourceName accountId firstSeen cloudProvider serviceCategory applications { id name type } isExposed imageSource registryType registryName imageScanStatus exposurePath { type name cbomId } accountName subService region resourceTags resourceArn images { name hashes { hash isFromRegistry } tags } relatedIssues { info low medium high critical appox } issueSeverityBreakdown { name severities { info low medium high critical appox } } issuesStats { totalIssues sourceTools { name total } categories { name total } severities { name total } } cluster link imageHash workloads { type namespace name cluster region isExposed consoleLink exposurePath { type name cbomId } } artifactIds } offset topOffset total totalFiltered selectedPosition } }",
 "variables": {
    "cloudItemsInput": {
      "limit": 100,
      "offset": 0,
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
      "filters": {
        "apps": ["example"],
        "service": ["example"],
        "type": ["example"],
        "cloudProvider": ["example"],
        "assetName": ["example"],
        "accountId": ["example"],
        "region": ["example"],
        "serviceCategory": ["example"],
        "cluster": ["example"],
        "severities": ["example"],
        "isExposed": ["example"],
        "imageSource": ["example"],
        "registryType": ["example"],
        "registryName": ["example"],
        "imageScanStatus": ["example"],
        "artifactIds": ["example"]
      },
      "filterSearch": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "owners": ["example"],
      "tagIds": ["example"],
      "search": "example",
      "openItems": ["digest"],
      "orderBy": {
        "field": "example",
        "direction": "ASC"
      },
      "topOffset": 42,
      "scrollDirection": "example",
      "cbomId": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetCloudItems($cloudItemsInput: CloudItemsInput) { getCloudItems(cloudItemsInput: $cloudItemsInput) { cloudItems { id assetName service resourceId cbomId cbomProvider resourceType resourceName accountId firstSeen cloudProvider serviceCategory applications { id name type } isExposed imageSource registryType registryName imageScanStatus exposurePath { type name cbomId } accountName subService region resourceTags resourceArn images { name hashes { hash isFromRegistry } tags } relatedIssues { info low medium high critical appox } issueSeverityBreakdown { name severities { info low medium high critical appox } } issuesStats { totalIssues sourceTools { name total } categories { name total } severities { name total } } cluster link imageHash workloads { type namespace name cluster region isExposed consoleLink exposurePath { type name cbomId } } artifactIds } offset topOffset total totalFiltered selectedPosition } }';

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
      cloudItemsInput: {
        limit: 100,
        offset: 0,
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
        filters: {
          apps: ["example"],
          service: ["example"],
          type: ["example"],
          cloudProvider: ["example"],
          assetName: ["example"],
          accountId: ["example"],
          region: ["example"],
          serviceCategory: ["example"],
          cluster: ["example"],
          severities: ["example"],
          isExposed: ["example"],
          imageSource: ["example"],
          registryType: ["example"],
          registryName: ["example"],
          imageScanStatus: ["example"],
          artifactIds: ["example"]
        },
        filterSearch: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        owners: ["example"],
        tagIds: ["example"],
        search: "example",
        openItems: ["digest"],
        orderBy: {
          field: "example",
          direction: "ASC"
        },
        topOffset: 42,
        scrollDirection: "example",
        cbomId: "example"
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

query = 'query GetCloudItems($cloudItemsInput: CloudItemsInput) { getCloudItems(cloudItemsInput: $cloudItemsInput) { cloudItems { id assetName service resourceId cbomId cbomProvider resourceType resourceName accountId firstSeen cloudProvider serviceCategory applications { id name type } isExposed imageSource registryType registryName imageScanStatus exposurePath { type name cbomId } accountName subService region resourceTags resourceArn images { name hashes { hash isFromRegistry } tags } relatedIssues { info low medium high critical appox } issueSeverityBreakdown { name severities { info low medium high critical appox } } issuesStats { totalIssues sourceTools { name total } categories { name total } severities { name total } } cluster link imageHash workloads { type namespace name cluster region isExposed consoleLink exposurePath { type name cbomId } } artifactIds } offset topOffset total totalFiltered selectedPosition } }'

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
      "cloudItemsInput": {
        "limit": 100,
        "offset": 0,
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
        "filters": {
          "apps": ["example"],
          "service": ["example"],
          "type": ["example"],
          "cloudProvider": ["example"],
          "assetName": ["example"],
          "accountId": ["example"],
          "region": ["example"],
          "serviceCategory": ["example"],
          "cluster": ["example"],
          "severities": ["example"],
          "isExposed": ["example"],
          "imageSource": ["example"],
          "registryType": ["example"],
          "registryName": ["example"],
          "imageScanStatus": ["example"],
          "artifactIds": ["example"]
        },
        "filterSearch": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "owners": ["example"],
        "tagIds": ["example"],
        "search": "example",
        "openItems": ["digest"],
        "orderBy": {
          "field": "example",
          "direction": "ASC"
        },
        "topOffset": 42,
        "scrollDirection": "example",
        "cbomId": "example"
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

You can use the following argument(s) to customize your `getCloudItems` query.

| Argument                                                                                                                                         | Description                                                  | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cloudItemsInput [`CloudItemsInput`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/cloud-items-input) | Parameters for filtering and paginating cloud security items | <p>limit <code>Int</code><br>offset <code>Int</code><br>scanId <code>String</code><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>filters <a href="../types/inputs/cloud-items-filters"><code>CloudItemsFilters</code></a><br>filterSearch <a href="../../api--application/types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>search <code>String</code><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>orderBy <a href="../types/inputs/cloud-items-order-by"><code>CloudItemsOrderBy</code></a><br>topOffset <code>Int</code><br>scrollDirection <code>String</code><br>cbomId <code>String</code></p> |

### Fields

Return type: [`CloudItemsResponse`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-items-response)

You can use the following field(s) to specify what information your `getCloudItems` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                             | Description                                        | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cloudItems [`[CloudItem]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item) | List of cloud security items found                 | <p>id <code>String</code><br>assetName <code>String</code><br>service <code>String</code><br>resourceId <code>String</code><br>cbomId <code>String</code><br>cbomProvider <code>String</code><br>resourceType <code>String</code><br>resourceName <code>String</code><br>accountId <code>String</code><br>firstSeen <code>String</code><br>cloudProvider <code>String</code><br>serviceCategory <code>String</code><br>applications <a href="../types/objects/app-info"><code>\[AppInfo]</code></a><br>isExposed <code>String</code><br>imageSource <code>String</code><br>registryType <code>String</code><br>registryName <code>String</code><br>imageScanStatus <code>String</code><br>exposurePath <a href="../types/objects/exposure-path-item"><code>\[ExposurePathItem]</code></a><br>accountName <code>String</code><br>subService <code>String</code><br>region <code>String</code><br>resourceTags <code>JSON</code><br>resourceArn <code>String</code><br>images <a href="../types/objects/cloud-item-image"><code>\[CloudItemImage]</code></a><br>relatedIssues <a href="../../api--application/types/objects/severities"><code>Severities</code></a><br>issueSeverityBreakdown <a href="../types/objects/cloud-issue-severity-breakdown"><code>\[CloudIssueSeverityBreakdown]</code></a><br>issuesStats <a href="../types/objects/issues-stats"><code>IssuesStats</code></a><br>cluster <code>String</code><br>link <code>String</code><br>imageHash <code>String</code><br>workloads <a href="../types/objects/workload"><code>\[Workload]</code></a><br>artifactIds <code>\[String]</code></p> |
| offset `Int`                                                                                                                      | Current pagination offset                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| topOffset `Int`                                                                                                                   | Top offset for advanced pagination                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| total `Int`                                                                                                                       | Total number of cloud items available              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| totalFiltered `Int`                                                                                                               | Total number of cloud items after applying filters |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| selectedPosition `Int`                                                                                                            | Position of the selected item in the results       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
