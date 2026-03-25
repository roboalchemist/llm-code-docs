# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-artifacts.md

# getArtifacts

Retrieves all artifacts. Artifacts are typically software components, container images, libraries, or other digital assets that have been scanned for security vulnerabilities and compliance issues. This API provides a structured way to access, filter, and analyze artifacts within your system.

With this API, you can:

* Retrieve a list of artifacts.
* Access detailed metadata for each artifact, including version, repository, associated vulnerabilities, and security posture.
* Sort and filter artifacts based on various criteria to track security risks, compliance status, and artifact integrity.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetArtifacts($getArtifactsInput: GetArtifactsInput) {
  getArtifacts(getArtifactsInput: $getArtifactsInput) {
    artifacts {
      vulnDepIssues
      vulnDepBaseIssues
      vulnDepInstructionIssues
      secretIssues
      sbomIssues
      counts {
        vulnDepIssues
        vulnDepBaseIssues
        vulnDepInstructionIssues
        vulnDepPublicImageIssues
      }
      id
      appDescription {
        appName
        appType
        appId
        businessPriority
      }
      artifactInfo {
        type
        name
        version
        hash
        artifactIntegrity
        registry
        visibility
        firstSeenDate
        runtime
        cloudDeployed
        biVisibility
        biName
        biVersion
        osName
        osVersion
      }
      categories {
        catId
        severities {
          info
          low
          medium
          high
          critical
          appox
        }
        name
        score
      }
      artifactCategories {
        catId
        severities {
          info
          low
          medium
          high
          critical
          appox
        }
        name
        score
      }
      registryDescription {
        type
        name
        project
        link
        hash
        tags
        username
        userType
        uploadTime
        lastUpdate
        buildTime
      }
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
      totalIssuesBySeverity {
        info
        low
        medium
        high
        critical
        appox
      }
      packages {
        appId
        appName
        repoName
        link
        type
      }
      issueSeverityBreakdown {
        name
        tab
        severities {
          info
          low
          medium
          high
          critical
          appox
        }
      }
    }
    offset
    total
    totalFilteredArtifacts
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
 "query": "query GetArtifacts($getArtifactsInput: GetArtifactsInput) { getArtifacts(getArtifactsInput: $getArtifactsInput) { artifacts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues secretIssues sbomIssues counts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues vulnDepPublicImageIssues } id appDescription { appName appType appId businessPriority } artifactInfo { type name version hash artifactIntegrity registry visibility firstSeenDate runtime cloudDeployed biVisibility biName biVersion osName osVersion } categories { catId severities { info low medium high critical appox } name score } artifactCategories { catId severities { info low medium high critical appox } name score } registryDescription { type name project link hash tags username userType uploadTime lastUpdate buildTime } cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } totalIssuesBySeverity { info low medium high critical appox } packages { appId appName repoName link type } issueSeverityBreakdown { name tab severities { info low medium high critical appox } } } offset total totalFilteredArtifacts } }",
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
const query = 'query GetArtifacts($getArtifactsInput: GetArtifactsInput) { getArtifacts(getArtifactsInput: $getArtifactsInput) { artifacts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues secretIssues sbomIssues counts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues vulnDepPublicImageIssues } id appDescription { appName appType appId businessPriority } artifactInfo { type name version hash artifactIntegrity registry visibility firstSeenDate runtime cloudDeployed biVisibility biName biVersion osName osVersion } categories { catId severities { info low medium high critical appox } name score } artifactCategories { catId severities { info low medium high critical appox } name score } registryDescription { type name project link hash tags username userType uploadTime lastUpdate buildTime } cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } totalIssuesBySeverity { info low medium high critical appox } packages { appId appName repoName link type } issueSeverityBreakdown { name tab severities { info low medium high critical appox } } } offset total totalFilteredArtifacts } }';

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

query = 'query GetArtifacts($getArtifactsInput: GetArtifactsInput) { getArtifacts(getArtifactsInput: $getArtifactsInput) { artifacts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues secretIssues sbomIssues counts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues vulnDepPublicImageIssues } id appDescription { appName appType appId businessPriority } artifactInfo { type name version hash artifactIntegrity registry visibility firstSeenDate runtime cloudDeployed biVisibility biName biVersion osName osVersion } categories { catId severities { info low medium high critical appox } name score } artifactCategories { catId severities { info low medium high critical appox } name score } registryDescription { type name project link hash tags username userType uploadTime lastUpdate buildTime } cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } totalIssuesBySeverity { info low medium high critical appox } packages { appId appName repoName link type } issueSeverityBreakdown { name tab severities { info low medium high critical appox } } } offset total totalFilteredArtifacts } }'

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

You can use the following argument(s) to customize your `getArtifacts` query.

| Argument                                                                                                                                         | Description                                             | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getArtifactsInput [`GetArtifactsInput`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-input) | Input parameters for filtering, sorting, and pagination | <p>limit <code>Int</code><br>offset <code>Int</code><br>sort <a href="../types/inputs/artifacts-sort"><code>ArtifactsSort</code></a><br>dateRange <a href="../../api--application/types/inputs/date-range"><code>DateRange</code></a><br>filters <a href="../types/inputs/artifact-filters"><code>ArtifactFilters</code></a><br>artifactTopFilters <a href="../types/enums/artifact-top-filters"><code>\[ArtifactTopFilters]</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>search <code>String</code><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a></p> |

### Fields

Return type: [`ArtifactsResponse`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifacts-response)

You can use the following field(s) to specify what information your `getArtifacts` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                            | Description                                      | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| artifacts [`[ArtifactInfo]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info) | List of artifact information items               | <p>vulnDepIssues <code>\[String]</code><br>vulnDepBaseIssues <code>\[String]</code><br>vulnDepInstructionIssues <code>\[String]</code><br>secretIssues <code>\[String]</code><br>sbomIssues <code>\[String]</code><br>counts <a href="../types/objects/issue-counts"><code>IssueCounts</code></a><br>id <code>String</code><br>appDescription <a href="../types/objects/artifact-application"><code>ArtifactApplication</code></a><br>artifactInfo <a href="../types/objects/i-artifact-info"><code>IArtifactInfo</code></a><br>categories <a href="../types/objects/artifact-categories"><code>\[ArtifactCategories]</code></a><br>artifactCategories <a href="../types/objects/artifact-categories"><code>\[ArtifactCategories]</code></a><br>registryDescription <a href="../types/objects/artifact-registry-description"><code>\[ArtifactRegistryDescription]</code></a><br>cloudData <a href="../types/objects/cloud-artifact-data"><code>\[CloudArtifactData]</code></a><br>totalIssuesBySeverity <a href="../../api--application/types/objects/severities"><code>Severities</code></a><br>packages <a href="../types/objects/artifact-package"><code>\[ArtifactPackage]</code></a><br>issueSeverityBreakdown <a href="../types/objects/issue-severity-breakdown"><code>\[IssueSeverityBreakdown]</code></a></p> |
| offset `Int`                                                                                                                     | Pagination offset value for virtualization       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| total `Int`                                                                                                                      | Total number of artifacts available              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| totalFilteredArtifacts `Int`                                                                                                     | Total number of artifacts after applying filters |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
