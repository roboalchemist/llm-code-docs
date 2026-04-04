# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-sbom-issues-breakdown.md

# getSbomIssuesBreakdown

Gets a breakdown of security issues found in SBOM libraries by severity level.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetSbomIssuesBreakdown($getApplicationsSbom: GetApplicationsSbom) {
  getSbomIssuesBreakdown(getApplicationsSbom: $getApplicationsSbom) {
    severity
    count
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getApplicationsSbom": {
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "limit": 100,
    "offset": 0,
    "search": "example",
    "filters": {
      "libForSearch": ["example"],
      "libraryNames": ["example"],
      "libraryVersions": ["example"],
      "apps": ["example"],
      "appIds": ["30966426"],
      "source": ["example"],
      "dependencyTypes": ["example"],
      "licenses": ["example"],
      "packageNames": ["example"],
      "copyrights": ["example"],
      "severities": ["example"],
      "packageInfos": ["example"],
      "malicious": ["example"],
      "packageManagers": ["example"],
      "cve": ["example"],
      "languages": ["example"],
      "os": ["example"],
      "registryName": ["example"],
      "baseImage": ["example"],
      "image": ["example"],
      "reachability": ["example"],
      "tags": ["example"],
      "imageSource": ["example"],
      "licenseIssue": [true],
      "sbomImageTags": ["example"],
      "runtimeStatus": ["example"]
    },
    "sbomSearch": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "owners": ["example"],
    "tagIds": ["example"],
    "openItems": ["digest"],
    "sort": {
      "fields": ["LibraryName"],
      "order": ["ASC"]
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
 "query": "query GetSbomIssuesBreakdown($getApplicationsSbom: GetApplicationsSbom) { getSbomIssuesBreakdown(getApplicationsSbom: $getApplicationsSbom) { severity count } }",
 "variables": {
    "getApplicationsSbom": {
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "limit": 100,
      "offset": 0,
      "search": "example",
      "filters": {
        "libForSearch": ["example"],
        "libraryNames": ["example"],
        "libraryVersions": ["example"],
        "apps": ["example"],
        "appIds": ["30966426"],
        "source": ["example"],
        "dependencyTypes": ["example"],
        "licenses": ["example"],
        "packageNames": ["example"],
        "copyrights": ["example"],
        "severities": ["example"],
        "packageInfos": ["example"],
        "malicious": ["example"],
        "packageManagers": ["example"],
        "cve": ["example"],
        "languages": ["example"],
        "os": ["example"],
        "registryName": ["example"],
        "baseImage": ["example"],
        "image": ["example"],
        "reachability": ["example"],
        "tags": ["example"],
        "imageSource": ["example"],
        "licenseIssue": [true],
        "sbomImageTags": ["example"],
        "runtimeStatus": ["example"]
      },
      "sbomSearch": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "owners": ["example"],
      "tagIds": ["example"],
      "openItems": ["digest"],
      "sort": {
        "fields": ["LibraryName"],
        "order": ["ASC"]
      }
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetSbomIssuesBreakdown($getApplicationsSbom: GetApplicationsSbom) { getSbomIssuesBreakdown(getApplicationsSbom: $getApplicationsSbom) { severity count } }';

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
      getApplicationsSbom: {
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        limit: 100,
        offset: 0,
        search: "example",
        filters: {
          libForSearch: ["example"],
          libraryNames: ["example"],
          libraryVersions: ["example"],
          apps: ["example"],
          appIds: ["30966426"],
          source: ["example"],
          dependencyTypes: ["example"],
          licenses: ["example"],
          packageNames: ["example"],
          copyrights: ["example"],
          severities: ["example"],
          packageInfos: ["example"],
          malicious: ["example"],
          packageManagers: ["example"],
          cve: ["example"],
          languages: ["example"],
          os: ["example"],
          registryName: ["example"],
          baseImage: ["example"],
          image: ["example"],
          reachability: ["example"],
          tags: ["example"],
          imageSource: ["example"],
          licenseIssue: [true],
          sbomImageTags: ["example"],
          runtimeStatus: ["example"]
        },
        sbomSearch: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        owners: ["example"],
        tagIds: ["example"],
        openItems: ["digest"],
        sort: {
          fields: ["LibraryName"],
          order: ["ASC"]
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

query = 'query GetSbomIssuesBreakdown($getApplicationsSbom: GetApplicationsSbom) { getSbomIssuesBreakdown(getApplicationsSbom: $getApplicationsSbom) { severity count } }'

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
      "getApplicationsSbom": {
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "limit": 100,
        "offset": 0,
        "search": "example",
        "filters": {
          "libForSearch": ["example"],
          "libraryNames": ["example"],
          "libraryVersions": ["example"],
          "apps": ["example"],
          "appIds": ["30966426"],
          "source": ["example"],
          "dependencyTypes": ["example"],
          "licenses": ["example"],
          "packageNames": ["example"],
          "copyrights": ["example"],
          "severities": ["example"],
          "packageInfos": ["example"],
          "malicious": ["example"],
          "packageManagers": ["example"],
          "cve": ["example"],
          "languages": ["example"],
          "os": ["example"],
          "registryName": ["example"],
          "baseImage": ["example"],
          "image": ["example"],
          "reachability": ["example"],
          "tags": ["example"],
          "imageSource": ["example"],
          "licenseIssue": [true],
          "sbomImageTags": ["example"],
          "runtimeStatus": ["example"]
        },
        "sbomSearch": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "owners": ["example"],
        "tagIds": ["example"],
        "openItems": ["digest"],
        "sort": {
          "fields": ["LibraryName"],
          "order": ["ASC"]
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

You can use the following argument(s) to customize your `getSbomIssuesBreakdown` query.

| Argument                                                                                                                                           | Description                                                                 | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getApplicationsSbom [`GetApplicationsSbom`](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/get-applications-sbom) | Parameters for filtering which libraries to include in the issues breakdown | <p>scanId <code>String</code><br>limit <code>Int</code><br>offset <code>Int</code><br>search <code>String</code><br>filters <a href="../../api--sbom/types/inputs/sbom-lib-filters"><code>SBOMLibFilters</code></a><br>sbomSearch <a href="../../api--application/types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>sort <a href="../../api--sbom/types/inputs/sbom-lib-sort-input"><code>SbomLibSortInput</code></a></p> |

### Fields

Return type: [`[IssuesBreakdown]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issues-breakdown)

You can use the following field(s) to specify what information your `getSbomIssuesBreakdown` query will return. Please note that some fields may have their own subfields.

| Field             | Description                             | Supported fields |
| ----------------- | --------------------------------------- | ---------------- |
| severity `String` | Severity level of the issues            |                  |
| count `Int`       | Number of issues at this severity level |                  |
