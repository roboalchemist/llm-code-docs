# Source: https://docs.ox.security/api-documentation/api-reference/api--application/queries/get-single-application-info.md

# getSingleApplicationInfo

Retrieves detailed information about a specific application, including its metadata, security metrics, and associated resources.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetSingleApplicationInfo($getSingleApplicationInput: SingleApplicationInput) {
  getSingleApplicationInfo(getSingleApplicationInput: $getSingleApplicationInput) {
    appId
    repoName
    appName
    branch
    branchesCount
    branchesToScan
    businessPriority
    codeChanges
    commitCount
    committersCount
    createdAt
    creator
    daysSinceLastCodeChange
    daysSinceRepoCreation
    deployedProd
    filesCount
    forksCount
    hasDownloads
    hasPackageContainers
    headSha
    irrelevantReasons
    languages {
      language
      languagePercentage
    }
    lastCodeChange
    new
    overrideRelevance
    overridePriority
    originalBusinessPriority
    publicVisibility
    pullCount
    pushCount
    relevant
    risk
    scanId
    scannedAt
    secInfrastructure {
      label
      clientCoverage
      oxCoverage
      noCoverage
      notApplicable
    }
    securityPosture
    appType
    appSubtype
    size
    type
    updated
    userCount
    version
    violationCount
    watchersCount
    yamlsCount
    scoreHistory {
      appId
      appName
      score
      date
      new
      updated
      scanId
    }
    applicationFlows {
      artifacts {
        type
        name
        hashType
        system
        subType
        hash
        size
        date
        location {
          runBy
          foundBy
          foundIn
          link
        }
        linkName
        k8sType
        cluster
        region
      }
      cloudDeployments {
        type
        subType
        name
        hash
        hashType
        link
        location {
          runBy
          foundBy
          foundIn
          link
        }
        k8sType
        imageName
        date
        cluster
        region
      }
      cicdInfo {
        type
        system
        latestDate
        lastMonthJobCount
        location {
          runBy
          foundBy
          foundIn
          link
        }
      }
      orchestrators {
        type
        name
        hashType
        system
        hash
        size
        date
        location {
          runBy
          foundBy
          foundIn
          link
        }
      }
      kubernetes {
        type
        name
        hashType
        system
        hash
        subType
        size
        date
        location {
          runBy
          foundBy
          foundIn
          link
        }
      }
      repository {
        type
        system
        date
        location {
          runBy
          foundBy
          foundIn
          link
        }
      }
    }
    appOwners {
      name
      email
      roles
    }
    fakeApp
    link
    branchLink
    issues
    categories {
      categoryName
      categoryId
      catId
      severities {
        info
        low
        medium
        high
        critical
        appox
      }
      score
      severityScore
      total
      reason
    }
    toolsCoverage {
      toolName
      oxDelivered
      coverage
      type
      sources {
        match
        type
      }
    }
    pipeline {
      jobId
      jobTriggeredAt
      scanResult
      issuesCount
      jobTriggeredBy
      jobUrl
    }
    organization
    pipelineScans
    issuesBySeverity {
      info
      low
      medium
      high
      critical
      appox
    }
    pkgManagers
    sbomCount
    isMonoRepoChild
    monoRepoParent
    monorepoChildrenCount
    monorepoChildrenAppIds
    tags {
      tagId
      name
      email
      displayName
      tagType
      createdBy
      purpose
      deploymentModel
      tagCategory
    }
    dockerfiles {
      path
    }
    severityChangedReason {
      tagId
      changeNumber
      shouldBeSeverityFactor
      requiredHits
      reason
      shortName
      changeCategory
      changePlusReasonFacet
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
    }
    apiInventoriesTotal
    artifactCount
    sbomArtifactCount
    saasBomCount
    sbomRepoCount
    credentialsId
    oxInPipeline
    oxInPipelineDescription
    primaryAppReason
    primaryApp
    matchedProjects {
      toolName
      matchedProjects {
        externalToolProject
        matchMethod
      }
    }
    toolName
    createdAtOx
    irrelevantDate
    prevFullScanDate
    prevFullScanId
    lastFullScanDate
    lastFullScanId
    isFullScan
    appClassification
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getSingleApplicationInput": {
    "applicationId": "30966426",
    "limit": 0,
    "offset": 100,
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
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
 "query": "query GetSingleApplicationInfo($getSingleApplicationInput: SingleApplicationInput) { getSingleApplicationInfo(getSingleApplicationInput: $getSingleApplicationInput) { appId repoName appName branch branchesCount branchesToScan businessPriority codeChanges commitCount committersCount createdAt creator daysSinceLastCodeChange daysSinceRepoCreation deployedProd filesCount forksCount hasDownloads hasPackageContainers headSha irrelevantReasons languages { language languagePercentage } lastCodeChange new overrideRelevance overridePriority originalBusinessPriority publicVisibility pullCount pushCount relevant risk scanId scannedAt secInfrastructure { label clientCoverage oxCoverage noCoverage notApplicable } securityPosture appType appSubtype size type updated userCount version violationCount watchersCount yamlsCount scoreHistory { appId appName score date new updated scanId } applicationFlows { artifacts { type name hashType system subType hash size date location { runBy foundBy foundIn link } linkName k8sType cluster region } cloudDeployments { type subType name hash hashType link location { runBy foundBy foundIn link } k8sType imageName date cluster region } cicdInfo { type system latestDate lastMonthJobCount location { runBy foundBy foundIn link } } orchestrators { type name hashType system hash size date location { runBy foundBy foundIn link } } kubernetes { type name hashType system hash subType size date location { runBy foundBy foundIn link } } repository { type system date location { runBy foundBy foundIn link } } } appOwners { name email roles } fakeApp link branchLink issues categories { categoryName categoryId catId severities { info low medium high critical appox } score severityScore total reason } toolsCoverage { toolName oxDelivered coverage type sources { match type } } pipeline { jobId jobTriggeredAt scanResult issuesCount jobTriggeredBy jobUrl } organization pipelineScans issuesBySeverity { info low medium high critical appox } pkgManagers sbomCount isMonoRepoChild monoRepoParent monorepoChildrenCount monorepoChildrenAppIds tags { tagId name email displayName tagType createdBy purpose deploymentModel tagCategory } dockerfiles { path } severityChangedReason { tagId changeNumber shouldBeSeverityFactor requiredHits reason shortName changeCategory changePlusReasonFacet extraInfo { key link snippet { detectionType fileName snippetLineNumber language text } } } apiInventoriesTotal artifactCount sbomArtifactCount saasBomCount sbomRepoCount credentialsId oxInPipeline oxInPipelineDescription primaryAppReason primaryApp matchedProjects { toolName matchedProjects { externalToolProject matchMethod } } toolName createdAtOx irrelevantDate prevFullScanDate prevFullScanId lastFullScanDate lastFullScanId isFullScan appClassification } }",
 "variables": {
    "getSingleApplicationInput": {
      "applicationId": "30966426",
      "limit": 0,
      "offset": 100,
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetSingleApplicationInfo($getSingleApplicationInput: SingleApplicationInput) { getSingleApplicationInfo(getSingleApplicationInput: $getSingleApplicationInput) { appId repoName appName branch branchesCount branchesToScan businessPriority codeChanges commitCount committersCount createdAt creator daysSinceLastCodeChange daysSinceRepoCreation deployedProd filesCount forksCount hasDownloads hasPackageContainers headSha irrelevantReasons languages { language languagePercentage } lastCodeChange new overrideRelevance overridePriority originalBusinessPriority publicVisibility pullCount pushCount relevant risk scanId scannedAt secInfrastructure { label clientCoverage oxCoverage noCoverage notApplicable } securityPosture appType appSubtype size type updated userCount version violationCount watchersCount yamlsCount scoreHistory { appId appName score date new updated scanId } applicationFlows { artifacts { type name hashType system subType hash size date location { runBy foundBy foundIn link } linkName k8sType cluster region } cloudDeployments { type subType name hash hashType link location { runBy foundBy foundIn link } k8sType imageName date cluster region } cicdInfo { type system latestDate lastMonthJobCount location { runBy foundBy foundIn link } } orchestrators { type name hashType system hash size date location { runBy foundBy foundIn link } } kubernetes { type name hashType system hash subType size date location { runBy foundBy foundIn link } } repository { type system date location { runBy foundBy foundIn link } } } appOwners { name email roles } fakeApp link branchLink issues categories { categoryName categoryId catId severities { info low medium high critical appox } score severityScore total reason } toolsCoverage { toolName oxDelivered coverage type sources { match type } } pipeline { jobId jobTriggeredAt scanResult issuesCount jobTriggeredBy jobUrl } organization pipelineScans issuesBySeverity { info low medium high critical appox } pkgManagers sbomCount isMonoRepoChild monoRepoParent monorepoChildrenCount monorepoChildrenAppIds tags { tagId name email displayName tagType createdBy purpose deploymentModel tagCategory } dockerfiles { path } severityChangedReason { tagId changeNumber shouldBeSeverityFactor requiredHits reason shortName changeCategory changePlusReasonFacet extraInfo { key link snippet { detectionType fileName snippetLineNumber language text } } } apiInventoriesTotal artifactCount sbomArtifactCount saasBomCount sbomRepoCount credentialsId oxInPipeline oxInPipelineDescription primaryAppReason primaryApp matchedProjects { toolName matchedProjects { externalToolProject matchMethod } } toolName createdAtOx irrelevantDate prevFullScanDate prevFullScanId lastFullScanDate lastFullScanId isFullScan appClassification } }';

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
      getSingleApplicationInput: {
        applicationId: "30966426",
        limit: 0,
        offset: 100,
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
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

query = 'query GetSingleApplicationInfo($getSingleApplicationInput: SingleApplicationInput) { getSingleApplicationInfo(getSingleApplicationInput: $getSingleApplicationInput) { appId repoName appName branch branchesCount branchesToScan businessPriority codeChanges commitCount committersCount createdAt creator daysSinceLastCodeChange daysSinceRepoCreation deployedProd filesCount forksCount hasDownloads hasPackageContainers headSha irrelevantReasons languages { language languagePercentage } lastCodeChange new overrideRelevance overridePriority originalBusinessPriority publicVisibility pullCount pushCount relevant risk scanId scannedAt secInfrastructure { label clientCoverage oxCoverage noCoverage notApplicable } securityPosture appType appSubtype size type updated userCount version violationCount watchersCount yamlsCount scoreHistory { appId appName score date new updated scanId } applicationFlows { artifacts { type name hashType system subType hash size date location { runBy foundBy foundIn link } linkName k8sType cluster region } cloudDeployments { type subType name hash hashType link location { runBy foundBy foundIn link } k8sType imageName date cluster region } cicdInfo { type system latestDate lastMonthJobCount location { runBy foundBy foundIn link } } orchestrators { type name hashType system hash size date location { runBy foundBy foundIn link } } kubernetes { type name hashType system hash subType size date location { runBy foundBy foundIn link } } repository { type system date location { runBy foundBy foundIn link } } } appOwners { name email roles } fakeApp link branchLink issues categories { categoryName categoryId catId severities { info low medium high critical appox } score severityScore total reason } toolsCoverage { toolName oxDelivered coverage type sources { match type } } pipeline { jobId jobTriggeredAt scanResult issuesCount jobTriggeredBy jobUrl } organization pipelineScans issuesBySeverity { info low medium high critical appox } pkgManagers sbomCount isMonoRepoChild monoRepoParent monorepoChildrenCount monorepoChildrenAppIds tags { tagId name email displayName tagType createdBy purpose deploymentModel tagCategory } dockerfiles { path } severityChangedReason { tagId changeNumber shouldBeSeverityFactor requiredHits reason shortName changeCategory changePlusReasonFacet extraInfo { key link snippet { detectionType fileName snippetLineNumber language text } } } apiInventoriesTotal artifactCount sbomArtifactCount saasBomCount sbomRepoCount credentialsId oxInPipeline oxInPipelineDescription primaryAppReason primaryApp matchedProjects { toolName matchedProjects { externalToolProject matchMethod } } toolName createdAtOx irrelevantDate prevFullScanDate prevFullScanId lastFullScanDate lastFullScanId isFullScan appClassification } }'

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
      "getSingleApplicationInput": {
        "applicationId": "30966426",
        "limit": 0,
        "offset": 100,
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
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

You can use the following argument(s) to customize your `getSingleApplicationInfo` query.

| Argument                                                                                                                                                              | Description                                                                                                   | Supported fields                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getSingleApplicationInput [`SingleApplicationInput`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/single-application-input) | Input containing the unique identifier of the application to retrieve and optional parameters for flow items. | <p>applicationId <code>String!</code><br>limit <code>Int</code><br>offset <code>Int</code><br>dateRange <a href="../types/inputs/date-range"><code>DateRange</code></a><br>scanId <code>String</code></p> |

### Fields

Return type: [`Application`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)

You can use the following field(s) to specify what information your `getSingleApplicationInfo` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                                                                     | Description                                                | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ~~id `String`~~ ⚠️                                                                                                                                                                        | **Deprecated**: Use appId instead                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| appId `String`                                                                                                                                                                            | Application-specific identifier                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repoName `String`                                                                                                                                                                         | Name of the associated repository                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| appName `String`                                                                                                                                                                          | Display name of the application                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| branch `String`                                                                                                                                                                           | Default branch for development                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| branchesCount `Int`                                                                                                                                                                       | Total number of branches in the repository                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| branchesToScan `[String]`                                                                                                                                                                 | List of repository branches configured for scanning        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| businessPriority `Float`                                                                                                                                                                  | Business priority score assigned to the application        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| codeChanges `Int`                                                                                                                                                                         | Number of code changes recorded                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| commitCount `Int`                                                                                                                                                                         | Total number of commits in the repository                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| committersCount `Int`                                                                                                                                                                     | Total number of committers in the repository               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| createdAt `String`                                                                                                                                                                        | Timestamp of application creation                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| creator `String`                                                                                                                                                                          | User who created the application                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| daysSinceLastCodeChange `Int`                                                                                                                                                             | Number of days since the last code modification            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| daysSinceRepoCreation `Int`                                                                                                                                                               | Age of the repository in days                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| deployedProd `Boolean`                                                                                                                                                                    | Indicates if the application is deployed in production     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| filesCount `Int`                                                                                                                                                                          | Total number of files in the repository                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| forksCount `Int`                                                                                                                                                                          | Number of repository forks                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| hasDownloads `Boolean`                                                                                                                                                                    | Indicates if downloads are enabled for the repository      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| hasPackageContainers `Boolean`                                                                                                                                                            | Indicates if application has package containers            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| headSha `String`                                                                                                                                                                          | SHA hash of the latest commit                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| irrelevantReasons `[String]`                                                                                                                                                              | List of reasons why the application is marked irrelevant   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| languages [`[Language]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/language)                                                                | Programming languages used in the application              | <p>language <code>String</code><br>languagePercentage <code>Float</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| lastCodeChange `String`                                                                                                                                                                   | Timestamp of the most recent code change                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| new `Boolean`                                                                                                                                                                             | Indicates if this is a newly added application             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| overrideRelevance `String`                                                                                                                                                                | Manual override status for application relevance           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| overridePriority `Int`                                                                                                                                                                    | Manual override value for priority                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| originalBusinessPriority `Float`                                                                                                                                                          | Original business priority score calculated by the system  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| publicVisibility `Boolean`                                                                                                                                                                | Indicates if the repository is publicly accessible         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| pullCount `Int`                                                                                                                                                                           | Number of pull requests                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| pushCount `Int`                                                                                                                                                                           | Number of push events                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| relevant `Boolean`                                                                                                                                                                        | Indicates if the application is considered relevant        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| risk `Float`                                                                                                                                                                              | Security risk score                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| scanId `String`                                                                                                                                                                           | Identifier of the latest scan                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| scannedAt `Float`                                                                                                                                                                         | Timestamp of the last scan                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| secInfrastructure [`[ServerSecurityInfraItem]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/server-security-infra-item)                       | Security infrastructure components                         | <p>label <code>String</code><br>clientCoverage <code>Float</code><br>oxCoverage <code>Float</code><br>noCoverage <code>Float</code><br>notApplicable <code>Float</code></p>                                                                                                                                                                                                                                                                                                                                                                                             |
| securityPosture `Float`                                                                                                                                                                   | Overall security posture score                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| appType `String`                                                                                                                                                                          | Application type                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| appSubtype `String`                                                                                                                                                                       | Application sub type                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| size `Float`                                                                                                                                                                              | Repository size in bytes                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ~~tagsCount `Int`~~ ⚠️                                                                                                                                                                    | **Deprecated**: Use tags instead                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| type `String`                                                                                                                                                                             | Application Git vendor                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| updated `Boolean`                                                                                                                                                                         | Indicates if the application details were recently updated |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| userCount `Int`                                                                                                                                                                           | Number of unique users interacting with the application    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| version `String`                                                                                                                                                                          | Application version identifier                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| violationCount `Int`                                                                                                                                                                      | Number of security violations detected                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| watchersCount `Int`                                                                                                                                                                       | Number of repository watchers                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| yamlsCount `Int`                                                                                                                                                                          | Number of YAML configuration files                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| scoreHistory [`[ScoreHistoryItem]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/score-history-item)                                           | Historical risk score data points                          | <p>appId <code>String</code><br>appName <code>String</code><br>score <code>Float</code><br>date <code>Float</code><br>new <code>Boolean</code><br>updated <code>Boolean</code><br>scanId <code>String</code></p>                                                                                                                                                                                                                                                                                                                                                        |
| applicationFlows [`ApplicationFlow`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-flow)                                            | Application flow and dependency information                | <p>artifacts <a href="../types/objects/artifact-item"><code>\[ArtifactItem]</code></a><br>cloudDeployments <a href="../types/objects/cloud-deployment"><code>\[CloudDeployment]</code></a><br>cicdInfo <a href="../types/objects/cicd-info"><code>\[CicdInfo]</code></a><br>orchestrators <a href="../types/objects/orchestrator-item"><code>\[OrchestratorItem]</code></a><br>kubernetes <a href="../types/objects/kubernetes-item"><code>\[KubernetesItem]</code></a><br>repository <a href="../types/objects/repository-item"><code>\[RepositoryItem]</code></a></p> |
| ~~isSbomPresent `Boolean`~~ ⚠️                                                                                                                                                            | **Deprecated**: This field is not used anymore             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| appOwners [`[OwnerInfo]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/owner-info)                                                             | List of application owners and their roles                 | <p>name <code>String</code><br>email <code>String</code><br>roles <a href="../types/enums/app-owner-role"><code>\[AppOwnerRole]</code></a></p>                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ~~offset `Int`~~ ⚠️                                                                                                                                                                       | **Deprecated**: This field is not used anymore             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ~~improvement `Float`~~ ⚠️                                                                                                                                                                | **Deprecated**: This field is not used anymore             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| fakeApp `Boolean`                                                                                                                                                                         | Indicates if this is a real repository                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| link `String`                                                                                                                                                                             | URL to the repository                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| branchLink `String`                                                                                                                                                                       | URL to the specific branch                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| issues `Int`                                                                                                                                                                              | Total number of security issues                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| categories [`[AppCategories]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-categories)                                                    | Application categories and classifications                 | <p>categoryName <code>String</code><br>categoryId <code>String</code><br>catId <code>Int</code><br>severities <a href="../types/objects/app-severities"><code>AppSeverities</code></a><br>score <code>Float</code><br>severityScore <code>String</code><br>total <code>Float</code><br><del>isNa <code>Boolean</code></del> ⚠️<br>reason <code>\[String]</code></p>                                                                                                                                                                                                     |
| toolsCoverage [`[AppToolCoverage]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-tool-coverage)                                            | Security tools coverage information                        | <p>toolName <code>String</code><br>oxDelivered <code>Boolean</code><br>coverage <code>Boolean</code><br>type <code>String</code><br>sources <a href="../types/objects/tool-coverage-sources"><code>\[ToolCoverageSources]</code></a></p>                                                                                                                                                                                                                                                                                                                                |
| pipeline [`Pipeline`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/pipeline)                                                                   | Latest pipeline scan information                           | <p>jobId <code>String</code><br>jobTriggeredAt <code>Float</code><br>scanResult <a href="../types/enums/pipeline-scan-result"><code>PipelineScanResult</code></a><br>issuesCount <code>Int</code><br>jobTriggeredBy <code>String</code><br>jobUrl <code>String</code></p>                                                                                                                                                                                                                                                                                               |
| ~~isPipelineConfigured `String`~~ ⚠️                                                                                                                                                      | **Deprecated**: Use oxInPipeline instead                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| organization `String`                                                                                                                                                                     | Organization owning the repository                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ~~repoRealName `String`~~ ⚠️                                                                                                                                                              | **Deprecated**: This field is not used anymore             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ~~repoId `String`~~ ⚠️                                                                                                                                                                    | **Deprecated**: Use appId instead                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| pipelineScans `Int`                                                                                                                                                                       | Number of pipeline scan executions                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| issuesBySeverity [`Severities`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/severities)                                                       | Breakdown of issues by severity level                      | <p>info <code>Int</code><br>low <code>Int</code><br>medium <code>Int</code><br>high <code>Int</code><br>critical <code>Int</code><br>appox <code>Int</code></p>                                                                                                                                                                                                                                                                                                                                                                                                         |
| pkgManagers `[String]`                                                                                                                                                                    | Package managers used in the application                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| sbomCount `Int`                                                                                                                                                                           | Number of associated SBOMs                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| isMonoRepoChild `Boolean`                                                                                                                                                                 | Indicates if this is a child application in a monorepo     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| monoRepoParent `String`                                                                                                                                                                   | Parent application identifier in a monorepo                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| monorepoChildrenCount `Int`                                                                                                                                                               | Number of child applications in the monorepo               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| monorepoChildrenAppIds `[String]`                                                                                                                                                         | List of child application identifiers                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| tags [`[AppTag]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-tag)                                                                        | Application tags                                           | <p>tagId <code>String</code><br>name <code>String</code><br>email <code>String</code><br>displayName <code>String</code><br>tagType <a href="../types/enums/ox-tag-type"><code>OxTagType</code></a><br>createdBy <code>String</code><br>purpose <code>String</code><br>deploymentModel <code>String</code><br>tagCategory <code>String</code></p>                                                                                                                                                                                                                       |
| dockerfiles [`[Dockerfile]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/dockerfile)                                                          | List of Dockerfile locations                               | path `String`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| severityChangedReason [`[ApplicationSeverityChangedReason]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-severity-changed-reason) | Reasons for severity level changes                         | <p>tagId <code>String</code><br>changeNumber <code>Float</code><br>shouldBeSeverityFactor <code>Boolean</code><br>requiredHits <code>Int</code><br>reason <code>String</code><br>shortName <code>String</code><br>changeCategory <code>String</code><br>changePlusReasonFacet <code>String</code><br>extraInfo <a href="../types/objects/application-extra-info"><code>\[ApplicationExtraInfo]</code></a></p>                                                                                                                                                           |
| apiInventoriesTotal `Int`                                                                                                                                                                 | Total number of API inventories                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| artifactCount `Int`                                                                                                                                                                       | Total number of artifacts                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| sbomArtifactCount `Int`                                                                                                                                                                   | Total number of SBOM artifacts                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| saasBomCount `Int`                                                                                                                                                                        | Total number of SAAS BOM items                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| sbomRepoCount `Int`                                                                                                                                                                       | Total number of SBOM repositories                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| credentialsId `String`                                                                                                                                                                    | Associated credentials identifier                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| oxInPipeline `String`                                                                                                                                                                     | Integration status with Ox in the pipeline                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| oxInPipelineDescription `String`                                                                                                                                                          | Description of Ox pipeline integration                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| primaryAppReason `String`                                                                                                                                                                 | Reason for primary application designation                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| primaryApp `Boolean`                                                                                                                                                                      | Indicates if this is a primary application                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| matchedProjects [`[MatchedProjects]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/matched-projects)                                           | List of matched projects                                   | <p>toolName <code>String</code><br>matchedProjects <a href="../types/objects/matched-project"><code>\[MatchedProject]</code></a></p>                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| toolName `String`                                                                                                                                                                         | third party tool name                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| createdAtOx `String`                                                                                                                                                                      | Timestamp of application creation in Ox                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| irrelevantDate `String`                                                                                                                                                                   | Timestamp of application irrelevancy                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| prevFullScanDate `String`                                                                                                                                                                 | Timestamp of the previous full scan                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| prevFullScanId `String`                                                                                                                                                                   | ID of the previous full scan                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| lastFullScanDate `String`                                                                                                                                                                 | Timestamp of the last full scan                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| lastFullScanId `String`                                                                                                                                                                   | ID of the last full scan                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| isFullScan `Boolean`                                                                                                                                                                      | Indicated if last scan was full or delta for app           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| appClassification `[String]`                                                                                                                                                              | Application classification                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
