# Source: https://docs.ox.security/api-documentation/api-reference/api--sbom/queries/get-sbom.md

# getSbom

Retrieves SBOM libraries with filtering and pagination support.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetSbom($input: GetSbomInput) {
  getSbom(input: $input) {
    sbomLibs {
      id
      references {
        triggerPackage
        location
        locationLink
        dependencyType
        dependencyLevel
        commit {
          commitedAt
          committerName
          committerEmail
        }
        fileName
      }
      language
      libraryName
      libraryVersion
      license
      appName
      location
      dependencyType
      source
      appId
      locationLink
      appLink
      pkgName
      copyWriteInfo
      copyWriteInfoLink
      libLink
      vulnerabilityCounts {
        appox
        critical
        high
        medium
        low
        info
      }
      triggerPackage
      vulnerabilities {
        issueId
        oxSeverity
        severityNumberFromTool
        severityFromTool
        cve
        cveLink
        cvsVer
        cvssVersion
        epss
        percentile
        libName
        dependencyChain
        runtimeStatus
        libVersion
        chainDepth
        exploitInTheWild
        exploitInTheWildLink
        description
        dateDiscovered
        minorVerWithFix
        majorVerWithFix
        exploitRequirement
        exploitCode
        originalSeverity
      }
      latestVersion
      latestVersionDate
      stars
      forks
      openIssues
      packageManager
      packageManagerLink
      maintainers
      contributors
      downloads
      sourceLink
      notPopular
      licenseIssue
      malicious
      malwareType
      osVname
      notMaintained
      isDeprecated
      notImported
      notUpdated
      dependencyLevel
      requestId
      licenseLink
      artifactInSbomLibs {
        image
        imageLink
        imageCreatedAt
        sha
        os
        osVersion
        baseImage
        baseImageVersion
        tag
        layer
        registryName
        source
      }
      sha
      maintainersList {
        name
        email
      }
      runtimeStatus
      usedVersionReleaseDate
      projectDescription
    }
    total
    offset
    totalFilteredSbomLibs
    cursorValue
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
      "fields": ["LibraryName"],
      "order": ["ASC"]
    },
    "owners": ["example"],
    "tagIds": ["example"],
    "forCSV": true,
    "appPage": true,
    "cursorValue": "example"
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
 "query": "query GetSbom($input: GetSbomInput) { getSbom(input: $input) { sbomLibs { id references { triggerPackage location locationLink dependencyType dependencyLevel commit { commitedAt committerName committerEmail } fileName } language libraryName libraryVersion license appName location dependencyType source appId locationLink appLink pkgName copyWriteInfo copyWriteInfoLink libLink vulnerabilityCounts { appox critical high medium low info } triggerPackage vulnerabilities { issueId oxSeverity severityNumberFromTool severityFromTool cve cveLink cvsVer cvssVersion epss percentile libName dependencyChain runtimeStatus libVersion chainDepth exploitInTheWild exploitInTheWildLink description dateDiscovered minorVerWithFix majorVerWithFix exploitRequirement exploitCode originalSeverity } latestVersion latestVersionDate stars forks openIssues packageManager packageManagerLink maintainers contributors downloads sourceLink notPopular licenseIssue malicious malwareType osVname notMaintained isDeprecated notImported notUpdated dependencyLevel requestId licenseLink artifactInSbomLibs { image imageLink imageCreatedAt sha os osVersion baseImage baseImageVersion tag layer registryName source } sha maintainersList { name email } runtimeStatus usedVersionReleaseDate projectDescription } total offset totalFilteredSbomLibs cursorValue } }",
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
        "fields": ["LibraryName"],
        "order": ["ASC"]
      },
      "owners": ["example"],
      "tagIds": ["example"],
      "forCSV": true,
      "appPage": true,
      "cursorValue": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetSbom($input: GetSbomInput) { getSbom(input: $input) { sbomLibs { id references { triggerPackage location locationLink dependencyType dependencyLevel commit { commitedAt committerName committerEmail } fileName } language libraryName libraryVersion license appName location dependencyType source appId locationLink appLink pkgName copyWriteInfo copyWriteInfoLink libLink vulnerabilityCounts { appox critical high medium low info } triggerPackage vulnerabilities { issueId oxSeverity severityNumberFromTool severityFromTool cve cveLink cvsVer cvssVersion epss percentile libName dependencyChain runtimeStatus libVersion chainDepth exploitInTheWild exploitInTheWildLink description dateDiscovered minorVerWithFix majorVerWithFix exploitRequirement exploitCode originalSeverity } latestVersion latestVersionDate stars forks openIssues packageManager packageManagerLink maintainers contributors downloads sourceLink notPopular licenseIssue malicious malwareType osVname notMaintained isDeprecated notImported notUpdated dependencyLevel requestId licenseLink artifactInSbomLibs { image imageLink imageCreatedAt sha os osVersion baseImage baseImageVersion tag layer registryName source } sha maintainersList { name email } runtimeStatus usedVersionReleaseDate projectDescription } total offset totalFilteredSbomLibs cursorValue } }';

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
          fields: ["LibraryName"],
          order: ["ASC"]
        },
        owners: ["example"],
        tagIds: ["example"],
        forCSV: true,
        appPage: true,
        cursorValue: "example"
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

query = 'query GetSbom($input: GetSbomInput) { getSbom(input: $input) { sbomLibs { id references { triggerPackage location locationLink dependencyType dependencyLevel commit { commitedAt committerName committerEmail } fileName } language libraryName libraryVersion license appName location dependencyType source appId locationLink appLink pkgName copyWriteInfo copyWriteInfoLink libLink vulnerabilityCounts { appox critical high medium low info } triggerPackage vulnerabilities { issueId oxSeverity severityNumberFromTool severityFromTool cve cveLink cvsVer cvssVersion epss percentile libName dependencyChain runtimeStatus libVersion chainDepth exploitInTheWild exploitInTheWildLink description dateDiscovered minorVerWithFix majorVerWithFix exploitRequirement exploitCode originalSeverity } latestVersion latestVersionDate stars forks openIssues packageManager packageManagerLink maintainers contributors downloads sourceLink notPopular licenseIssue malicious malwareType osVname notMaintained isDeprecated notImported notUpdated dependencyLevel requestId licenseLink artifactInSbomLibs { image imageLink imageCreatedAt sha os osVersion baseImage baseImageVersion tag layer registryName source } sha maintainersList { name email } runtimeStatus usedVersionReleaseDate projectDescription } total offset totalFilteredSbomLibs cursorValue } }'

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
          "fields": ["LibraryName"],
          "order": ["ASC"]
        },
        "owners": ["example"],
        "tagIds": ["example"],
        "forCSV": true,
        "appPage": true,
        "cursorValue": "example"
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

You can use the following argument(s) to customize your `getSbom` query.

| Argument                                                                                                               | Description                                                | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| input [`GetSbomInput`](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/get-sbom-input) | Parameters for filtering and paginating the SBOM libraries | <p>scanId <code>String</code><br>conditionalFilters <a href="../../api--application/types/inputs/conditional-filters"><code>\[ConditionalFilters]</code></a><br>search <code>String</code><br>limit <code>Int</code><br>offset <code>Int</code><br>sort <a href="../types/inputs/sbom-lib-sort-input"><code>SbomLibSortInput</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>forCSV <code>Boolean</code><br>appPage <code>Boolean</code><br>cursorValue <code>String</code></p> |

### Fields

Return type: [`SbomLibResponse`](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/objects/sbom-lib-response)

You can use the following field(s) to specify what information your `getSbom` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                              | Description                                                                                                                                                                                                                                                                                    | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sbomLibs [`[SbomLib]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-lib) | List of SBOM libraries found in the scan                                                                                                                                                                                                                                                       | <p>id <code>String</code><br>references <a href="../../api--issue/types/objects/sbom-reference"><code>\[SbomReference]</code></a><br><del>appType <code>String</code></del> ⚠️<br>language <code>String</code><br><del>libId <code>String</code></del> ⚠️<br>libraryName <code>String</code><br>libraryVersion <code>String</code><br>license <code>String</code><br>appName <code>String</code><br>location <code>String</code><br>dependencyType <code>String</code><br>source <code>String</code><br>appId <code>String</code><br>locationLink <code>String</code><br>appLink <code>String</code><br>pkgName <code>String</code><br>copyWriteInfo <code>\[String]</code><br>copyWriteInfoLink <code>String</code><br>libLink <code>String</code><br>vulnerabilityCounts <a href="../../api--issue/types/objects/issues-by-severity"><code>IssuesBySeverity</code></a><br>triggerPackage <code>String</code><br>vulnerabilities <a href="../../api--issue/types/objects/sca-vulnerability"><code>\[SCAVulnerability]</code></a><br>latestVersion <code>String</code><br>latestVersionDate <code>String</code><br>stars <code>Int</code><br>forks <code>Int</code><br>openIssues <code>Int</code><br>packageManager <code>String</code><br>packageManagerLink <code>String</code><br>maintainers <code>Int</code><br>contributors <code>Int</code><br>downloads <code>Int</code><br>sourceLink <code>String</code><br>notPopular <code>Boolean</code><br>licenseIssue <code>Boolean</code><br>malicious <code>Boolean</code><br>malwareType <code>String</code><br>osVname <code>String</code><br>notMaintained <code>Boolean</code><br>isDeprecated <code>Boolean</code><br>notImported <code>Boolean</code><br><del>notUsed <code>Boolean</code></del> ⚠️<br>notUpdated <code>Boolean</code><br>dependencyLevel <code>Int</code><br>requestId <code>String</code><br>licenseLink <code>String</code><br>artifactInSbomLibs <a href="../../api--issue/types/objects/artifact-in-sbom-libs"><code>\[ArtifactInSbomLibs]</code></a><br>sha <code>String</code><br>maintainersList <a href="../../api--issue/types/objects/maintainer"><code>\[Maintainer]</code></a><br>runtimeStatus <code>String</code><br>usedVersionReleaseDate <code>String</code><br>projectDescription <code>String</code></p> |
| total `Int`                                                                                                        | Total number of libraries available                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| offset `Int`                                                                                                       | Current pagination offset                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| totalFilteredSbomLibs `Int`                                                                                        | Total number of libraries after applying filters                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| cursorValue `String`                                                                                               | A value returned by the API that represents the position of the last item in the previous page. Use this value to paginate efficiently through the results. Pass the cursorValue from the previous API response to fetch the next page of results. If omitted, the API returns the first page. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
