# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/get-single-cloud-bom-item.md

# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/queries/get-single-cloud-bom-item.md

# getSingleCloudBomItem

Retrieves detailed information about a specific cloud BOM item.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetSingleCloudBomItem($getSingleCloudBomItemInput: GetSingleCloudBomItem!) {
  getSingleCloudBomItem(getSingleCloudBomItemInput: $getSingleCloudBomItemInput) {
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
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getSingleCloudBomItemInput": {
    "id": "example",
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99"
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
 "query": "query GetSingleCloudBomItem($getSingleCloudBomItemInput: GetSingleCloudBomItem!) { getSingleCloudBomItem(getSingleCloudBomItemInput: $getSingleCloudBomItemInput) { id assetName service resourceId cbomId cbomProvider resourceType resourceName accountId firstSeen cloudProvider serviceCategory applications { id name type } isExposed imageSource registryType registryName imageScanStatus exposurePath { type name cbomId } accountName subService region resourceTags resourceArn images { name hashes { hash isFromRegistry } tags } relatedIssues { info low medium high critical appox } issueSeverityBreakdown { name severities { info low medium high critical appox } } issuesStats { totalIssues sourceTools { name total } categories { name total } severities { name total } } cluster link imageHash workloads { type namespace name cluster region isExposed consoleLink exposurePath { type name cbomId } } artifactIds } }",
 "variables": {
    "getSingleCloudBomItemInput": {
      "id": "example",
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetSingleCloudBomItem($getSingleCloudBomItemInput: GetSingleCloudBomItem!) { getSingleCloudBomItem(getSingleCloudBomItemInput: $getSingleCloudBomItemInput) { id assetName service resourceId cbomId cbomProvider resourceType resourceName accountId firstSeen cloudProvider serviceCategory applications { id name type } isExposed imageSource registryType registryName imageScanStatus exposurePath { type name cbomId } accountName subService region resourceTags resourceArn images { name hashes { hash isFromRegistry } tags } relatedIssues { info low medium high critical appox } issueSeverityBreakdown { name severities { info low medium high critical appox } } issuesStats { totalIssues sourceTools { name total } categories { name total } severities { name total } } cluster link imageHash workloads { type namespace name cluster region isExposed consoleLink exposurePath { type name cbomId } } artifactIds } }';

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
      getSingleCloudBomItemInput: {
        id: "example",
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99"
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

query = 'query GetSingleCloudBomItem($getSingleCloudBomItemInput: GetSingleCloudBomItem!) { getSingleCloudBomItem(getSingleCloudBomItemInput: $getSingleCloudBomItemInput) { id assetName service resourceId cbomId cbomProvider resourceType resourceName accountId firstSeen cloudProvider serviceCategory applications { id name type } isExposed imageSource registryType registryName imageScanStatus exposurePath { type name cbomId } accountName subService region resourceTags resourceArn images { name hashes { hash isFromRegistry } tags } relatedIssues { info low medium high critical appox } issueSeverityBreakdown { name severities { info low medium high critical appox } } issuesStats { totalIssues sourceTools { name total } categories { name total } severities { name total } } cluster link imageHash workloads { type namespace name cluster region isExposed consoleLink exposurePath { type name cbomId } } artifactIds } }'

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
      "getSingleCloudBomItemInput": {
        "id": "example",
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99"
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

You can use the following argument(s) to customize your `getSingleCloudBomItem` query.

| Argument                                                                                                                                                                                                                                 | Description                                                      | Supported fields                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------ |
| getSingleCloudBomItemInput [`GetSingleCloudBomItem!`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/get-single-cloud-bom-item) <mark style="color:red;background-color:red;">required</mark> | Parameters identifying which specific cloud BOM item to retrieve | <p>id <code>String!</code><br>scanId <code>String</code></p> |

### Fields

Return type: [`CloudItem`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item)

You can use the following field(s) to specify what information your `getSingleCloudBomItem` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                                                               | Description                                                     | Supported fields                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id `String`                                                                                                                                                                         | Unique identifier for the cloud item                            |                                                                                                                                                                                                                                                                                                                                  |
| assetName `String`                                                                                                                                                                  | Name of the cloud asset or resource                             |                                                                                                                                                                                                                                                                                                                                  |
| service `String`                                                                                                                                                                    | Cloud service type (EC2, S3, Lambda, etc.)                      |                                                                                                                                                                                                                                                                                                                                  |
| resourceId `String`                                                                                                                                                                 | Cloud provider's resource identifier                            |                                                                                                                                                                                                                                                                                                                                  |
| cbomId `String`                                                                                                                                                                     | Cloud Bill of Materials identifier                              |                                                                                                                                                                                                                                                                                                                                  |
| cbomProvider `String`                                                                                                                                                               | Cloud provider name                                             |                                                                                                                                                                                                                                                                                                                                  |
| resourceType `String`                                                                                                                                                               | Type of cloud resource                                          |                                                                                                                                                                                                                                                                                                                                  |
| resourceName `String`                                                                                                                                                               | Name of the cloud resource                                      |                                                                                                                                                                                                                                                                                                                                  |
| accountId `String`                                                                                                                                                                  | Cloud account identifier                                        |                                                                                                                                                                                                                                                                                                                                  |
| firstSeen `String`                                                                                                                                                                  | Date when the resource was first discovered                     |                                                                                                                                                                                                                                                                                                                                  |
| cloudProvider `String`                                                                                                                                                              | Cloud provider (AWS, Azure, GCP, etc.)                          |                                                                                                                                                                                                                                                                                                                                  |
| serviceCategory `String`                                                                                                                                                            | Category of the cloud service                                   |                                                                                                                                                                                                                                                                                                                                  |
| applications [`[AppInfo]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/app-info)                                                     | Applications associated with this cloud resource                | <p>id <code>String</code><br>name <code>String</code><br>type <code>String</code></p>                                                                                                                                                                                                                                            |
| isExposed `String`                                                                                                                                                                  | Whether the resource is exposed to the internet                 |                                                                                                                                                                                                                                                                                                                                  |
| imageSource `String`                                                                                                                                                                | Source of the container image if applicable                     |                                                                                                                                                                                                                                                                                                                                  |
| registryType `String`                                                                                                                                                               | Type of container registry                                      |                                                                                                                                                                                                                                                                                                                                  |
| registryName `String`                                                                                                                                                               | Name of the container registry                                  |                                                                                                                                                                                                                                                                                                                                  |
| imageScanStatus `String`                                                                                                                                                            | Status of the image security scan                               |                                                                                                                                                                                                                                                                                                                                  |
| exposurePath [`[ExposurePathItem]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/exposure-path-item)                                  | Path showing how the resource is exposed                        | <p>type <code>String</code><br>name <code>String</code><br>cbomId <code>String</code></p>                                                                                                                                                                                                                                        |
| accountName `String`                                                                                                                                                                | Human-readable name of the cloud account                        |                                                                                                                                                                                                                                                                                                                                  |
| subService `String`                                                                                                                                                                 | Sub-service or component within the main service                |                                                                                                                                                                                                                                                                                                                                  |
| region `String`                                                                                                                                                                     | Cloud region where the resource is located                      |                                                                                                                                                                                                                                                                                                                                  |
| resourceTags `JSON`                                                                                                                                                                 | Tags associated with the cloud resource                         |                                                                                                                                                                                                                                                                                                                                  |
| resourceArn `String`                                                                                                                                                                | Amazon Resource Name (ARN) for AWS resources                    |                                                                                                                                                                                                                                                                                                                                  |
| images [`[CloudItemImage]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item-image)                                            | Container images associated with this resource                  | <p>name <code>String</code><br>hashes <a href="../types/objects/cloud-item-image-hash"><code>\[CloudItemImageHash]</code></a><br>tags <code>\[String]</code></p>                                                                                                                                                                 |
| relatedIssues [`Severities`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/severities)                                                    | Security issues found in this resource, categorized by severity | <p>info <code>Int</code><br>low <code>Int</code><br>medium <code>Int</code><br>high <code>Int</code><br>critical <code>Int</code><br>appox <code>Int</code></p>                                                                                                                                                                  |
| issueSeverityBreakdown [`[CloudIssueSeverityBreakdown]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-issue-severity-breakdown) | Breakdown of issues by policy category with severity details    | <p>name <code>String</code><br>severities <a href="../../api--application/types/objects/severities"><code>Severities</code></a></p>                                                                                                                                                                                              |
| issuesStats [`IssuesStats`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/issues-stats)                                                | Statistics about security issues found                          | <p>totalIssues <code>Int</code><br>sourceTools <a href="../types/objects/issue-stat"><code>\[IssueStat]</code></a><br>categories <a href="../types/objects/issue-stat"><code>\[IssueStat]</code></a><br>severities <a href="../types/objects/issue-stat"><code>\[IssueStat]</code></a></p>                                       |
| cluster `String`                                                                                                                                                                    | Kubernetes cluster name if applicable                           |                                                                                                                                                                                                                                                                                                                                  |
| link `String`                                                                                                                                                                       | URL link to view the resource in the cloud console              |                                                                                                                                                                                                                                                                                                                                  |
| imageHash `String`                                                                                                                                                                  | Hash of the container image                                     |                                                                                                                                                                                                                                                                                                                                  |
| workloads [`[Workload]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/workload)                                                       | Kubernetes workloads associated with this resource              | <p>type <code>String</code><br>namespace <code>String</code><br>name <code>String</code><br>cluster <code>String</code><br>region <code>String</code><br>isExposed <code>String</code><br>consoleLink <code>String</code><br>exposurePath <a href="../types/objects/exposure-path-item"><code>\[ExposurePathItem]</code></a></p> |
| artifactIds `[String]`                                                                                                                                                              | List of artifact identifiers associated with this resource      |                                                                                                                                                                                                                                                                                                                                  |
