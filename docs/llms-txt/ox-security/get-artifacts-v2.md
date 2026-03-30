# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-artifacts-v2.md

# getArtifactsV2

Retrieves artifacts with enhanced filtering and pagination support using conditional filters.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetArtifactsV2($input: GetArtifactsV2Input) {
  getArtifactsV2(input: $input) {
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
  "input": {
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "conditionalFilters": [
      {
        "condition": "AND",
        "fieldName": "digest",
        "values": ["example"],
        "greaterThan": 13.37,
        "lessThan": 13.37
      }
    ],
    "search": "example",
    "limit": 100,
    "offset": 0,
    "sort": {
      "field": ["AppName"],
      "order": ["ASC"]
    },
    "owners": ["example"],
    "tagIds": ["example"]
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
 "query": "query GetArtifactsV2($input: GetArtifactsV2Input) { getArtifactsV2(input: $input) { artifacts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues secretIssues sbomIssues counts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues vulnDepPublicImageIssues } id appDescription { appName appType appId businessPriority } artifactInfo { type name version hash artifactIntegrity registry visibility firstSeenDate runtime cloudDeployed biVisibility biName biVersion osName osVersion } categories { catId severities { info low medium high critical appox } name score } artifactCategories { catId severities { info low medium high critical appox } name score } registryDescription { type name project link hash tags username userType uploadTime lastUpdate buildTime } cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } totalIssuesBySeverity { info low medium high critical appox } packages { appId appName repoName link type } issueSeverityBreakdown { name tab severities { info low medium high critical appox } } } offset total totalFilteredArtifacts } }",
 "variables": {
    "input": {
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "conditionalFilters": [
        {
          "condition": "AND",
          "fieldName": "digest",
          "values": ["example"],
          "greaterThan": 13.37,
          "lessThan": 13.37
        }
      ],
      "search": "example",
      "limit": 100,
      "offset": 0,
      "sort": {
        "field": ["AppName"],
        "order": ["ASC"]
      },
      "owners": ["example"],
      "tagIds": ["example"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetArtifactsV2($input: GetArtifactsV2Input) { getArtifactsV2(input: $input) { artifacts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues secretIssues sbomIssues counts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues vulnDepPublicImageIssues } id appDescription { appName appType appId businessPriority } artifactInfo { type name version hash artifactIntegrity registry visibility firstSeenDate runtime cloudDeployed biVisibility biName biVersion osName osVersion } categories { catId severities { info low medium high critical appox } name score } artifactCategories { catId severities { info low medium high critical appox } name score } registryDescription { type name project link hash tags username userType uploadTime lastUpdate buildTime } cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } totalIssuesBySeverity { info low medium high critical appox } packages { appId appName repoName link type } issueSeverityBreakdown { name tab severities { info low medium high critical appox } } } offset total totalFilteredArtifacts } }';

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
      input: {
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        conditionalFilters: [
          {
            condition: "AND",
            fieldName: "digest",
            values: ["example"],
            greaterThan: 13.37,
            lessThan: 13.37
          }
        ],
        search: "example",
        limit: 100,
        offset: 0,
        sort: {
          field: ["AppName"],
          order: ["ASC"]
        },
        owners: ["example"],
        tagIds: ["example"]
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

query = 'query GetArtifactsV2($input: GetArtifactsV2Input) { getArtifactsV2(input: $input) { artifacts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues secretIssues sbomIssues counts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues vulnDepPublicImageIssues } id appDescription { appName appType appId businessPriority } artifactInfo { type name version hash artifactIntegrity registry visibility firstSeenDate runtime cloudDeployed biVisibility biName biVersion osName osVersion } categories { catId severities { info low medium high critical appox } name score } artifactCategories { catId severities { info low medium high critical appox } name score } registryDescription { type name project link hash tags username userType uploadTime lastUpdate buildTime } cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } totalIssuesBySeverity { info low medium high critical appox } packages { appId appName repoName link type } issueSeverityBreakdown { name tab severities { info low medium high critical appox } } } offset total totalFilteredArtifacts } }'

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
      "input": {
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "conditionalFilters": [
          {
            "condition": "AND",
            "fieldName": "digest",
            "values": ["example"],
            "greaterThan": 13.37,
            "lessThan": 13.37
          }
        ],
        "search": "example",
        "limit": 100,
        "offset": 0,
        "sort": {
          "field": ["AppName"],
          "order": ["ASC"]
        },
        "owners": ["example"],
        "tagIds": ["example"]
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

You can use the following argument(s) to customize your `getArtifactsV2` query.

| Argument                                                                                                                                 | Description                                             | Supported fields                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| input [`GetArtifactsV2Input`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-v2input) | Input parameters for filtering, sorting, and pagination | <p>scanId <code>String</code><br>conditionalFilters <a href="../../api--application/types/inputs/conditional-filters"><code>\[ConditionalFilters]</code></a><br>search <code>String</code><br>limit <code>Int</code><br>offset <code>Int</code><br>sort <a href="../types/inputs/artifacts-sort"><code>ArtifactsSort</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code></p> |

### Fields

Return type: [`ArtifactsResponse`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifacts-response)

You can use the following field(s) to specify what information your `getArtifactsV2` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                            | Description                                      | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| artifacts [`[ArtifactInfo]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info) | List of artifact information items               | <p>vulnDepIssues <code>\[String]</code><br>vulnDepBaseIssues <code>\[String]</code><br>vulnDepInstructionIssues <code>\[String]</code><br>secretIssues <code>\[String]</code><br>sbomIssues <code>\[String]</code><br>counts <a href="../types/objects/issue-counts"><code>IssueCounts</code></a><br>id <code>String</code><br>appDescription <a href="../types/objects/artifact-application"><code>ArtifactApplication</code></a><br>artifactInfo <a href="../types/objects/i-artifact-info"><code>IArtifactInfo</code></a><br>categories <a href="../types/objects/artifact-categories"><code>\[ArtifactCategories]</code></a><br>artifactCategories <a href="../types/objects/artifact-categories"><code>\[ArtifactCategories]</code></a><br>registryDescription <a href="../types/objects/artifact-registry-description"><code>\[ArtifactRegistryDescription]</code></a><br>cloudData <a href="../types/objects/cloud-artifact-data"><code>\[CloudArtifactData]</code></a><br>totalIssuesBySeverity <a href="../../api--application/types/objects/severities"><code>Severities</code></a><br>packages <a href="../types/objects/artifact-package"><code>\[ArtifactPackage]</code></a><br>issueSeverityBreakdown <a href="../types/objects/issue-severity-breakdown"><code>\[IssueSeverityBreakdown]</code></a></p> |
| offset `Int`                                                                                                                     | Pagination offset value for virtualization       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| total `Int`                                                                                                                      | Total number of artifacts available              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| totalFilteredArtifacts `Int`                                                                                                     | Total number of artifacts after applying filters |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
