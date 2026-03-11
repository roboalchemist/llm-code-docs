# Source: https://docs.ox.security/api-documentation/api-reference/api--application/queries/get-applications.md

# getApplications

Provides comprehensive details about all applications within an organization. It's an effective tool for assessing the security and operational characteristics of your applications. With this information, you can prioritize your actions based on business needs and security posture.

API provides you with the following capabilities:

* Fetching a list of applications.
* Returning data about application structure, security features, deployment environments, and more.
* Filtering and sorting applications based on various attributes and metrics.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetApplications($getApplicationsInput: GetApplicationsInput) {
  getApplications(getApplicationsInput: $getApplicationsInput) {
    applications {
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
    offset
    total
    totalFilteredApps
    showHistoricalTrend
    totalIrrelevantApps
    selectedPosition
    topOffset
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getApplicationsInput": {
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "dateRange": {
      "from": 1749000000000,
      "to": 1749900000000
    },
    "orderBy": {
      "field": "BusinessPriority",
      "direction": "ASC",
      "category": "example"
    },
    "limit": 100,
    "page": 1,
    "offset": 0,
    "applicationFilters": ["New"],
    "irrelevancyFilters": ["Archived"],
    "systemFilter": {
      "name": "cicd",
      "type": "example"
    },
    "owners": ["example"],
    "tagIds": ["example"],
    "search": "example",
    "filterSearch": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "isAppIdOnly": true,
    "appId": "30966426",
    "topOffset": 42,
    "scrollDirection": "example",
    "openItems": ["digest"],
    "irrelevant": true,
    "ignoreLimit": true,
    "conditionalFilters": [
      {
        "condition": "AND",
        "fieldName": "digest",
        "values": ["example"],
        "greaterThan": 13.37,
        "lessThan": 13.37
      }
    ]
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
 "query": "query GetApplications($getApplicationsInput: GetApplicationsInput) { getApplications(getApplicationsInput: $getApplicationsInput) { applications { appId repoName appName branch branchesCount branchesToScan businessPriority codeChanges commitCount committersCount createdAt creator daysSinceLastCodeChange daysSinceRepoCreation deployedProd filesCount forksCount hasDownloads hasPackageContainers headSha irrelevantReasons languages { language languagePercentage } lastCodeChange new overrideRelevance overridePriority originalBusinessPriority publicVisibility pullCount pushCount relevant risk scanId scannedAt secInfrastructure { label clientCoverage oxCoverage noCoverage notApplicable } securityPosture appType appSubtype size type updated userCount version violationCount watchersCount yamlsCount scoreHistory { appId appName score date new updated scanId } applicationFlows { artifacts { type name hashType system subType hash size date location { runBy foundBy foundIn link } linkName k8sType cluster region } cloudDeployments { type subType name hash hashType link location { runBy foundBy foundIn link } k8sType imageName date cluster region } cicdInfo { type system latestDate lastMonthJobCount location { runBy foundBy foundIn link } } orchestrators { type name hashType system hash size date location { runBy foundBy foundIn link } } kubernetes { type name hashType system hash subType size date location { runBy foundBy foundIn link } } repository { type system date location { runBy foundBy foundIn link } } } appOwners { name email roles } fakeApp link branchLink issues categories { categoryName categoryId catId severities { info low medium high critical appox } score severityScore total reason } toolsCoverage { toolName oxDelivered coverage type sources { match type } } pipeline { jobId jobTriggeredAt scanResult issuesCount jobTriggeredBy jobUrl } organization pipelineScans issuesBySeverity { info low medium high critical appox } pkgManagers sbomCount isMonoRepoChild monoRepoParent monorepoChildrenCount monorepoChildrenAppIds tags { tagId name email displayName tagType createdBy purpose deploymentModel tagCategory } dockerfiles { path } severityChangedReason { tagId changeNumber shouldBeSeverityFactor requiredHits reason shortName changeCategory changePlusReasonFacet extraInfo { key link snippet { detectionType fileName snippetLineNumber language text } } } apiInventoriesTotal artifactCount sbomArtifactCount saasBomCount sbomRepoCount credentialsId oxInPipeline oxInPipelineDescription primaryAppReason primaryApp matchedProjects { toolName matchedProjects { externalToolProject matchMethod } } toolName createdAtOx irrelevantDate prevFullScanDate prevFullScanId lastFullScanDate lastFullScanId isFullScan appClassification } offset total totalFilteredApps showHistoricalTrend totalIrrelevantApps selectedPosition topOffset } }",
 "variables": {
    "getApplicationsInput": {
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "dateRange": {
        "from": 1749000000000,
        "to": 1749900000000
      },
      "orderBy": {
        "field": "BusinessPriority",
        "direction": "ASC",
        "category": "example"
      },
      "limit": 100,
      "page": 1,
      "offset": 0,
      "applicationFilters": ["New"],
      "irrelevancyFilters": ["Archived"],
      "systemFilter": {
        "name": "cicd",
        "type": "example"
      },
      "owners": ["example"],
      "tagIds": ["example"],
      "search": "example",
      "filterSearch": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "isAppIdOnly": true,
      "appId": "30966426",
      "topOffset": 42,
      "scrollDirection": "example",
      "openItems": ["digest"],
      "irrelevant": true,
      "ignoreLimit": true,
      "conditionalFilters": [
        {
          "condition": "AND",
          "fieldName": "digest",
          "values": ["example"],
          "greaterThan": 13.37,
          "lessThan": 13.37
        }
      ]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetApplications($getApplicationsInput: GetApplicationsInput) { getApplications(getApplicationsInput: $getApplicationsInput) { applications { appId repoName appName branch branchesCount branchesToScan businessPriority codeChanges commitCount committersCount createdAt creator daysSinceLastCodeChange daysSinceRepoCreation deployedProd filesCount forksCount hasDownloads hasPackageContainers headSha irrelevantReasons languages { language languagePercentage } lastCodeChange new overrideRelevance overridePriority originalBusinessPriority publicVisibility pullCount pushCount relevant risk scanId scannedAt secInfrastructure { label clientCoverage oxCoverage noCoverage notApplicable } securityPosture appType appSubtype size type updated userCount version violationCount watchersCount yamlsCount scoreHistory { appId appName score date new updated scanId } applicationFlows { artifacts { type name hashType system subType hash size date location { runBy foundBy foundIn link } linkName k8sType cluster region } cloudDeployments { type subType name hash hashType link location { runBy foundBy foundIn link } k8sType imageName date cluster region } cicdInfo { type system latestDate lastMonthJobCount location { runBy foundBy foundIn link } } orchestrators { type name hashType system hash size date location { runBy foundBy foundIn link } } kubernetes { type name hashType system hash subType size date location { runBy foundBy foundIn link } } repository { type system date location { runBy foundBy foundIn link } } } appOwners { name email roles } fakeApp link branchLink issues categories { categoryName categoryId catId severities { info low medium high critical appox } score severityScore total reason } toolsCoverage { toolName oxDelivered coverage type sources { match type } } pipeline { jobId jobTriggeredAt scanResult issuesCount jobTriggeredBy jobUrl } organization pipelineScans issuesBySeverity { info low medium high critical appox } pkgManagers sbomCount isMonoRepoChild monoRepoParent monorepoChildrenCount monorepoChildrenAppIds tags { tagId name email displayName tagType createdBy purpose deploymentModel tagCategory } dockerfiles { path } severityChangedReason { tagId changeNumber shouldBeSeverityFactor requiredHits reason shortName changeCategory changePlusReasonFacet extraInfo { key link snippet { detectionType fileName snippetLineNumber language text } } } apiInventoriesTotal artifactCount sbomArtifactCount saasBomCount sbomRepoCount credentialsId oxInPipeline oxInPipelineDescription primaryAppReason primaryApp matchedProjects { toolName matchedProjects { externalToolProject matchMethod } } toolName createdAtOx irrelevantDate prevFullScanDate prevFullScanId lastFullScanDate lastFullScanId isFullScan appClassification } offset total totalFilteredApps showHistoricalTrend totalIrrelevantApps selectedPosition topOffset } }';

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
      getApplicationsInput: {
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        dateRange: {
          from: 1749000000000,
          to: 1749900000000
        },
        orderBy: {
          field: "BusinessPriority",
          direction: "ASC",
          category: "example"
        },
        limit: 100,
        page: 1,
        offset: 0,
        applicationFilters: ["New"],
        irrelevancyFilters: ["Archived"],
        systemFilter: {
          name: "cicd",
          type: "example"
        },
        owners: ["example"],
        tagIds: ["example"],
        search: "example",
        filterSearch: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        isAppIdOnly: true,
        appId: "30966426",
        topOffset: 42,
        scrollDirection: "example",
        openItems: ["digest"],
        irrelevant: true,
        ignoreLimit: true,
        conditionalFilters: [
          {
            condition: "AND",
            fieldName: "digest",
            values: ["example"],
            greaterThan: 13.37,
            lessThan: 13.37
          }
        ]
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

query = 'query GetApplications($getApplicationsInput: GetApplicationsInput) { getApplications(getApplicationsInput: $getApplicationsInput) { applications { appId repoName appName branch branchesCount branchesToScan businessPriority codeChanges commitCount committersCount createdAt creator daysSinceLastCodeChange daysSinceRepoCreation deployedProd filesCount forksCount hasDownloads hasPackageContainers headSha irrelevantReasons languages { language languagePercentage } lastCodeChange new overrideRelevance overridePriority originalBusinessPriority publicVisibility pullCount pushCount relevant risk scanId scannedAt secInfrastructure { label clientCoverage oxCoverage noCoverage notApplicable } securityPosture appType appSubtype size type updated userCount version violationCount watchersCount yamlsCount scoreHistory { appId appName score date new updated scanId } applicationFlows { artifacts { type name hashType system subType hash size date location { runBy foundBy foundIn link } linkName k8sType cluster region } cloudDeployments { type subType name hash hashType link location { runBy foundBy foundIn link } k8sType imageName date cluster region } cicdInfo { type system latestDate lastMonthJobCount location { runBy foundBy foundIn link } } orchestrators { type name hashType system hash size date location { runBy foundBy foundIn link } } kubernetes { type name hashType system hash subType size date location { runBy foundBy foundIn link } } repository { type system date location { runBy foundBy foundIn link } } } appOwners { name email roles } fakeApp link branchLink issues categories { categoryName categoryId catId severities { info low medium high critical appox } score severityScore total reason } toolsCoverage { toolName oxDelivered coverage type sources { match type } } pipeline { jobId jobTriggeredAt scanResult issuesCount jobTriggeredBy jobUrl } organization pipelineScans issuesBySeverity { info low medium high critical appox } pkgManagers sbomCount isMonoRepoChild monoRepoParent monorepoChildrenCount monorepoChildrenAppIds tags { tagId name email displayName tagType createdBy purpose deploymentModel tagCategory } dockerfiles { path } severityChangedReason { tagId changeNumber shouldBeSeverityFactor requiredHits reason shortName changeCategory changePlusReasonFacet extraInfo { key link snippet { detectionType fileName snippetLineNumber language text } } } apiInventoriesTotal artifactCount sbomArtifactCount saasBomCount sbomRepoCount credentialsId oxInPipeline oxInPipelineDescription primaryAppReason primaryApp matchedProjects { toolName matchedProjects { externalToolProject matchMethod } } toolName createdAtOx irrelevantDate prevFullScanDate prevFullScanId lastFullScanDate lastFullScanId isFullScan appClassification } offset total totalFilteredApps showHistoricalTrend totalIrrelevantApps selectedPosition topOffset } }'

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
      "getApplicationsInput": {
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "dateRange": {
          "from": 1749000000000,
          "to": 1749900000000
        },
        "orderBy": {
          "field": "BusinessPriority",
          "direction": "ASC",
          "category": "example"
        },
        "limit": 100,
        "page": 1,
        "offset": 0,
        "applicationFilters": ["New"],
        "irrelevancyFilters": ["Archived"],
        "systemFilter": {
          "name": "cicd",
          "type": "example"
        },
        "owners": ["example"],
        "tagIds": ["example"],
        "search": "example",
        "filterSearch": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "isAppIdOnly": true,
        "appId": "30966426",
        "topOffset": 42,
        "scrollDirection": "example",
        "openItems": ["digest"],
        "irrelevant": true,
        "ignoreLimit": true,
        "conditionalFilters": [
          {
            "condition": "AND",
            "fieldName": "digest",
            "values": ["example"],
            "greaterThan": 13.37,
            "lessThan": 13.37
          }
        ]
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

You can use the following argument(s) to customize your `getApplications` query.

| Argument                                                                                                                                                     | Description                                                                                                                | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getApplicationsInput [`GetApplicationsInput`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input) | Parameters for filtering, sorting, and paginating the applications list, including search criteria and display preferences | <p>scanId <code>String</code><br>dateRange <a href="../types/inputs/date-range"><code>DateRange</code></a><br>orderBy <a href="../types/inputs/order-apps-by"><code>OrderAppsBy</code></a><br>limit <code>Int</code><br>page <code>Int</code><br>offset <code>Int</code><br>applicationFilters <a href="../types/enums/applications-filter"><code>\[ApplicationsFilter]</code></a><br>irrelevancyFilters <a href="../types/enums/irrelevancy-filter"><code>\[IrrelevancyFilter]</code></a><br><del>filters</del> <a href="../types/inputs/app-filters"><del><code>AppFilters</code></del></a> ⚠️<br>systemFilter <a href="../types/inputs/system-filter"><code>SystemFilter</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>search <code>String</code><br>filterSearch <a href="../types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>isAppIdOnly <code>Boolean</code><br>appId <code>String</code><br>topOffset <code>Int</code><br>scrollDirection <code>String</code><br>openItems <a href="../types/enums/filter-types"><code>\[FilterTypes]</code></a><br>irrelevant <code>Boolean</code><br>ignoreLimit <code>Boolean</code><br>conditionalFilters <a href="../types/inputs/conditional-filters"><code>\[ConditionalFilters]</code></a></p> |

### Fields

Return type: [`ApplicationsResponse`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/applications-response)

You can use the following field(s) to specify what information your `getApplications` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                               | Description                                                 | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| applications [`[Application]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application) | List of applications matching the query criteria            | <p><del>id <code>String</code></del> ⚠️<br>appId <code>String</code><br>repoName <code>String</code><br>appName <code>String</code><br>branch <code>String</code><br>branchesCount <code>Int</code><br>branchesToScan <code>\[String]</code><br>businessPriority <code>Float</code><br>codeChanges <code>Int</code><br>commitCount <code>Int</code><br>committersCount <code>Int</code><br>createdAt <code>String</code><br>creator <code>String</code><br>daysSinceLastCodeChange <code>Int</code><br>daysSinceRepoCreation <code>Int</code><br>deployedProd <code>Boolean</code><br>filesCount <code>Int</code><br>forksCount <code>Int</code><br>hasDownloads <code>Boolean</code><br>hasPackageContainers <code>Boolean</code><br>headSha <code>String</code><br>irrelevantReasons <code>\[String]</code><br>languages <a href="../types/objects/language"><code>\[Language]</code></a><br>lastCodeChange <code>String</code><br>new <code>Boolean</code><br>overrideRelevance <code>String</code><br>overridePriority <code>Int</code><br>originalBusinessPriority <code>Float</code><br>publicVisibility <code>Boolean</code><br>pullCount <code>Int</code><br>pushCount <code>Int</code><br>relevant <code>Boolean</code><br>risk <code>Float</code><br>scanId <code>String</code><br>scannedAt <code>Float</code><br>secInfrastructure <a href="../types/objects/server-security-infra-item"><code>\[ServerSecurityInfraItem]</code></a><br>securityPosture <code>Float</code><br>appType <code>String</code><br>appSubtype <code>String</code><br>size <code>Float</code><br><del>tagsCount <code>Int</code></del> ⚠️<br>type <code>String</code><br>updated <code>Boolean</code><br>userCount <code>Int</code><br>version <code>String</code><br>violationCount <code>Int</code><br>watchersCount <code>Int</code><br>yamlsCount <code>Int</code><br>scoreHistory <a href="../types/objects/score-history-item"><code>\[ScoreHistoryItem]</code></a><br>applicationFlows <a href="../types/objects/application-flow"><code>ApplicationFlow</code></a><br><del>isSbomPresent <code>Boolean</code></del> ⚠️<br>appOwners <a href="../types/objects/owner-info"><code>\[OwnerInfo]</code></a><br><del>offset <code>Int</code></del> ⚠️<br><del>improvement <code>Float</code></del> ⚠️<br>fakeApp <code>Boolean</code><br>link <code>String</code><br>branchLink <code>String</code><br>issues <code>Int</code><br>categories <a href="../types/objects/app-categories"><code>\[AppCategories]</code></a><br>toolsCoverage <a href="../types/objects/app-tool-coverage"><code>\[AppToolCoverage]</code></a><br>pipeline <a href="../types/objects/pipeline"><code>Pipeline</code></a><br><del>isPipelineConfigured <code>String</code></del> ⚠️<br>organization <code>String</code><br><del>repoRealName <code>String</code></del> ⚠️<br><del>repoId <code>String</code></del> ⚠️<br>pipelineScans <code>Int</code><br>issuesBySeverity <a href="../types/objects/severities"><code>Severities</code></a><br>pkgManagers <code>\[String]</code><br>sbomCount <code>Int</code><br>isMonoRepoChild <code>Boolean</code><br>monoRepoParent <code>String</code><br>monorepoChildrenCount <code>Int</code><br>monorepoChildrenAppIds <code>\[String]</code><br>tags <a href="../types/objects/app-tag"><code>\[AppTag]</code></a><br>dockerfiles <a href="../types/objects/dockerfile"><code>\[Dockerfile]</code></a><br>severityChangedReason <a href="../types/objects/application-severity-changed-reason"><code>\[ApplicationSeverityChangedReason]</code></a><br>apiInventoriesTotal <code>Int</code><br>artifactCount <code>Int</code><br>sbomArtifactCount <code>Int</code><br>saasBomCount <code>Int</code><br>sbomRepoCount <code>Int</code><br>credentialsId <code>String</code><br>oxInPipeline <code>String</code><br>oxInPipelineDescription <code>String</code><br>primaryAppReason <code>String</code><br>primaryApp <code>Boolean</code><br>matchedProjects <a href="../types/objects/matched-projects"><code>\[MatchedProjects]</code></a><br>toolName <code>String</code><br>createdAtOx <code>String</code><br>irrelevantDate <code>String</code><br>prevFullScanDate <code>String</code><br>prevFullScanId <code>String</code><br>lastFullScanDate <code>String</code><br>lastFullScanId <code>String</code><br>isFullScan <code>Boolean</code><br>appClassification <code>\[String]</code></p> |
| offset `Int`                                                                                                                        | Number of records skipped in the result set                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| total `Int`                                                                                                                         | Total number of applications in the system                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| totalFilteredApps `Int`                                                                                                             | Number of applications matching the current filter criteria |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| showHistoricalTrend `Boolean`                                                                                                       | Indicates if historical trend data is available             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| totalIrrelevantApps `Int`                                                                                                           | Total count of applications marked as irrelevant            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| selectedPosition `Int`                                                                                                              | Current position in the paginated result set                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| topOffset `Int`                                                                                                                     | Offset value used for top-level pagination                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
