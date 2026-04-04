# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-artifact.md

# getArtifact

Retrieves detailed information about a specific artifact, including its metadata, associated packages, and deployment details for a given organization.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetArtifact($getArtifactInput: GetArtifactInput) {
  getArtifact(getArtifactInput: $getArtifactInput) {
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
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getArtifactInput": {
    "artifactId": "f01a11a3bb540707351a015edf5d8311adad31d3003bf122e1cd62cb01977b0e_some-container_*Amazon ECR"
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
 "query": "query GetArtifact($getArtifactInput: GetArtifactInput) { getArtifact(getArtifactInput: $getArtifactInput) { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues secretIssues sbomIssues counts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues vulnDepPublicImageIssues } id appDescription { appName appType appId businessPriority } artifactInfo { type name version hash artifactIntegrity registry visibility firstSeenDate runtime cloudDeployed biVisibility biName biVersion osName osVersion } categories { catId severities { info low medium high critical appox } name score } artifactCategories { catId severities { info low medium high critical appox } name score } registryDescription { type name project link hash tags username userType uploadTime lastUpdate buildTime } cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } totalIssuesBySeverity { info low medium high critical appox } packages { appId appName repoName link type } issueSeverityBreakdown { name tab severities { info low medium high critical appox } } } }",
 "variables": {
    "getArtifactInput": {
      "artifactId": "f01a11a3bb540707351a015edf5d8311adad31d3003bf122e1cd62cb01977b0e_some-container_*Amazon ECR"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetArtifact($getArtifactInput: GetArtifactInput) { getArtifact(getArtifactInput: $getArtifactInput) { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues secretIssues sbomIssues counts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues vulnDepPublicImageIssues } id appDescription { appName appType appId businessPriority } artifactInfo { type name version hash artifactIntegrity registry visibility firstSeenDate runtime cloudDeployed biVisibility biName biVersion osName osVersion } categories { catId severities { info low medium high critical appox } name score } artifactCategories { catId severities { info low medium high critical appox } name score } registryDescription { type name project link hash tags username userType uploadTime lastUpdate buildTime } cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } totalIssuesBySeverity { info low medium high critical appox } packages { appId appName repoName link type } issueSeverityBreakdown { name tab severities { info low medium high critical appox } } } }';

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
      getArtifactInput: {
        artifactId: "f01a11a3bb540707351a015edf5d8311adad31d3003bf122e1cd62cb01977b0e_some-container_*Amazon ECR"
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

query = 'query GetArtifact($getArtifactInput: GetArtifactInput) { getArtifact(getArtifactInput: $getArtifactInput) { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues secretIssues sbomIssues counts { vulnDepIssues vulnDepBaseIssues vulnDepInstructionIssues vulnDepPublicImageIssues } id appDescription { appName appType appId businessPriority } artifactInfo { type name version hash artifactIntegrity registry visibility firstSeenDate runtime cloudDeployed biVisibility biName biVersion osName osVersion } categories { catId severities { info low medium high critical appox } name score } artifactCategories { catId severities { info low medium high critical appox } name score } registryDescription { type name project link hash tags username userType uploadTime lastUpdate buildTime } cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } totalIssuesBySeverity { info low medium high critical appox } packages { appId appName repoName link type } issueSeverityBreakdown { name tab severities { info low medium high critical appox } } } }'

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
      "getArtifactInput": {
        "artifactId": "f01a11a3bb540707351a015edf5d8311adad31d3003bf122e1cd62cb01977b0e_some-container_*Amazon ECR"
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

You can use the following argument(s) to customize your `getArtifact` query.

| Argument                                                                                                                                      | Description                                                 | Supported fields    |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------- |
| getArtifactInput [`GetArtifactInput`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifact-input) | Input containing artifact identifier and additional filters | artifactId `String` |

### Fields

Return type: [`ArtifactInfo`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)

You can use the following field(s) to specify what information your `getArtifact` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                                                     | Description                                                   | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vulnDepIssues `[String]`                                                                                                                                                  | List of vulnerability dependency issue IDs                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| vulnDepBaseIssues `[String]`                                                                                                                                              | List of base vulnerability dependency issue IDs               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| vulnDepInstructionIssues `[String]`                                                                                                                                       | List of instruction-level vulnerability dependency issue IDs  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| secretIssues `[String]`                                                                                                                                                   | List of secret-related issue IDs                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| sbomIssues `[String]`                                                                                                                                                     | List of SBOM issue IDs                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| counts [`IssueCounts`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/issue-counts)                                                 | Counts of different issue types                               | <p>vulnDepIssues <code>Int</code><br>vulnDepBaseIssues <code>Int</code><br>vulnDepInstructionIssues <code>Int</code><br>vulnDepPublicImageIssues <code>Int</code></p>                                                                                                                                                                                                                                                                                                                                                                                                     |
| id `String`                                                                                                                                                               | Unique identifier of the artifact                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| appDescription [`ArtifactApplication`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-application)                         | Description of the artifact's application context             | <p>appName <code>String</code><br>appType <code>String</code><br>appId <code>String</code><br>businessPriority <code>Float</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| artifactInfo [`IArtifactInfo`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/i-artifact-info)                                      | Core artifact metadata and info                               | <p>type <a href="../types/enums/artifact-info-types"><code>ArtifactInfoTypes</code></a><br>name <code>String</code><br>version <code>String</code><br>hash <code>String</code><br>artifactIntegrity <code>String</code><br>registry <code>String</code><br>visibility <code>String</code><br>firstSeenDate <code>Float</code><br>runtime <code>Boolean</code><br>cloudDeployed <code>Boolean</code><br>biVisibility <code>String</code><br>biName <code>String</code><br>biVersion <code>String</code><br>osName <code>String</code><br>osVersion <code>String</code></p> |
| categories [`[ArtifactCategories]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-categories)                             | List of categories assigned to the artifact                   | <p>catId <code>String</code><br>severities <a href="../../api--application/types/objects/severities"><code>Severities</code></a><br>name <code>String</code><br>score <code>String</code></p>                                                                                                                                                                                                                                                                                                                                                                             |
| artifactCategories [`[ArtifactCategories]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-categories)                     | List of artifact categories (possibly duplicates or synonyms) | <p>catId <code>String</code><br>severities <a href="../../api--application/types/objects/severities"><code>Severities</code></a><br>name <code>String</code><br>score <code>String</code></p>                                                                                                                                                                                                                                                                                                                                                                             |
| registryDescription [`[ArtifactRegistryDescription]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-registry-description) | Registry descriptions related to the artifact                 | <p>type <code>String</code><br>name <code>String</code><br>project <code>String</code><br>link <code>String</code><br>hash <code>String</code><br>tags <code>\[String]</code><br>username <code>String</code><br>userType <code>String</code><br>uploadTime <code>Float</code><br>lastUpdate <code>Float</code><br>buildTime <code>Float</code></p>                                                                                                                                                                                                                       |
| cloudData [`[CloudArtifactData]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/cloud-artifact-data)                               | Cloud-related data for the artifact                           | <p>cloudIdentifier <code>String</code><br>link <code>String</code><br>lastExecutionTime <code>Float</code><br>lastModifiedTime <code>Float</code><br>account <code>String</code><br>zone <code>String</code><br>cluster <code>String</code><br>cloudDescription <a href="../types/objects/cloud-description"><code>CloudDescription</code></a></p>                                                                                                                                                                                                                        |
| totalIssuesBySeverity [`Severities`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/severities)                                  | Aggregated counts of issues by severity for the artifact      | <p>info <code>Int</code><br>low <code>Int</code><br>medium <code>Int</code><br>high <code>Int</code><br>critical <code>Int</code><br>appox <code>Int</code></p>                                                                                                                                                                                                                                                                                                                                                                                                           |
| packages [`[ArtifactPackage]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-package)                                     | List of packages included in the artifact                     | <p>appId <code>String</code><br>appName <code>String</code><br>repoName <code>String</code><br>link <code>String</code><br>type <code>String</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                   |
| issueSeverityBreakdown [`[IssueSeverityBreakdown]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/issue-severity-breakdown)        | Issue severity breakdown for the artifact                     | <p>name <code>String</code><br>tab <code>String</code><br>severities <a href="../../api--application/types/objects/severities"><code>Severities</code></a></p>                                                                                                                                                                                                                                                                                                                                                                                                            |
