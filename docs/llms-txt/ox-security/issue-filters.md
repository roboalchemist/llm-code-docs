# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issue-filters.md

# issueFilters

### Examples

```graphql
input IssueFilters {
  apps: [String]
  criticality: [CriticalityFilter]
  policies: [String]
  issueOwners: [String]
  categories: [String]
  issueNames: [String]
  sourceTools: [String]
  businessPriority: Range
  epssScore: Range
  epssPercentile: Range
  issueImportance: Range
  appId: [String]
  cwe: [String]
  severityChange: [String]
  severityChangeReasons: [String]
  issueStatus: [String]
  issueStatusVsLastScan: [String]
  issueActions: [String]
  originalSeverity: [String]
  uniqueLibs: [String]
  filePaths: [String]
  languages: [String]
  image: [String]
  artifactSha: [String]
  cbomId: [String]
  cve: [String]
  dastUrl: [String]
  codeOwners: [String]
  oscar: [String]
  complianceControl: [String]
  complianceStandard: [String]
  issuesWithout: [String]
  tags: [String]
  os: [String]
  baseImage: [String]
  resolvedReasons: [String]
  registryName: [String]
  scaFixType: [ScaFixType]
  oxuser: [String]
  issueIds: [String]
  ruleId: [String]
  appOwnersEmail: [String]
  appOwnersName: [String]
  version: [String]
  apiItem: [String]
  saasBom: [String]
  resolvedByName: [String]
}
```

### Fields

| Field                                                                                                                                   | Description                                                             | Supported fields                                        |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| apps `[String]`                                                                                                                         | Filter issues by application names                                      |                                                         |
| criticality [`[CriticalityFilter]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/criticality-filter) | Filter issues by severity levels (criticality)                          |                                                         |
| policies `[String]`                                                                                                                     | Filter issues by associated policies                                    |                                                         |
| issueOwners `[String]`                                                                                                                  | Filter issues by issue owners                                           |                                                         |
| categories `[String]`                                                                                                                   | Filter issues by categories                                             |                                                         |
| issueNames `[String]`                                                                                                                   | Filter issues by their names or titles                                  |                                                         |
| sourceTools `[String]`                                                                                                                  | Filter issues by the source tools that reported them                    |                                                         |
| businessPriority [`Range`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/range)                | Filter by business priority or importance range of repositories         | <p>from <code>Float</code><br>to <code>Float</code></p> |
| epssScore [`Range`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/range)                       | Filter by EPSS (Exploit Prediction Scoring System) score range          | <p>from <code>Float</code><br>to <code>Float</code></p> |
| epssPercentile [`Range`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/range)                  | Filter by EPSS percentile range                                         | <p>from <code>Float</code><br>to <code>Float</code></p> |
| issueImportance [`Range`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/range)                 | Filter by issue importance score range (also called appConScore)        | <p>from <code>Float</code><br>to <code>Float</code></p> |
| appId `[String]`                                                                                                                        | Filter issues by associated application IDs                             |                                                         |
| cwe `[String]`                                                                                                                          | Filter issues by CWE (Common Weakness Enumeration) identifiers          |                                                         |
| severityChange `[String]`                                                                                                               | Filter issues by severity change status                                 |                                                         |
| severityChangeReasons `[String]`                                                                                                        | Filter issues by reasons for severity changes                           |                                                         |
| issueStatus `[String]`                                                                                                                  | Filter by current issue status                                          |                                                         |
| issueStatusVsLastScan `[String]`                                                                                                        | Filter issues by status compared to the last scan                       |                                                         |
| issueActions `[String]`                                                                                                                 | Filter issues by actions taken                                          |                                                         |
| originalSeverity `[String]`                                                                                                             | Filter by the original severity level of the issue                      |                                                         |
| uniqueLibs `[String]`                                                                                                                   | Filter issues by unique libraries involved                              |                                                         |
| filePaths `[String]`                                                                                                                    | Filter issues by file paths associated with the issue                   |                                                         |
| languages `[String]`                                                                                                                    | Filter issues by programming languages                                  |                                                         |
| image `[String]`                                                                                                                        | Filter by image artifact identifiers                                    |                                                         |
| artifactSha `[String]`                                                                                                                  | Filter by artifact SHA identifiers                                      |                                                         |
| cbomId `[String]`                                                                                                                       | Filter by CBOM (Component Bill of Materials) IDs                        |                                                         |
| cve `[String]`                                                                                                                          | Filter issues by CVE (Common Vulnerabilities and Exposures) identifiers |                                                         |
| dastUrl `[String]`                                                                                                                      | Filter issues by DAST URL                                               |                                                         |
| codeOwners `[String]`                                                                                                                   | Filter issues by code owners                                            |                                                         |
| oscar `[String]`                                                                                                                        | Filter issues by OSCAR status or category                               |                                                         |
| complianceControl `[String]`                                                                                                            | Filter by compliance controls associated with issues                    |                                                         |
| complianceStandard `[String]`                                                                                                           | Filter by compliance standards                                          |                                                         |
| issuesWithout `[String]`                                                                                                                | Filter issues that do not include specified criteria                    |                                                         |
| tags `[String]`                                                                                                                         | Filter issues by associated tags                                        |                                                         |
| os `[String]`                                                                                                                           | Filter by operating systems related to the issue                        |                                                         |
| baseImage `[String]`                                                                                                                    | Filter by base image names or IDs                                       |                                                         |
| resolvedReasons `[String]`                                                                                                              | Filter by reasons why issues were resolved                              |                                                         |
| registryName `[String]`                                                                                                                 | Filter issues by registry names                                         |                                                         |
| scaFixType [`[ScaFixType]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/sca-fix-type)               | Filter by SCA (Software Composition Analysis) fix types                 |                                                         |
| oxuser `[String]`                                                                                                                       | Filter issues by associated Ox user identifiers                         |                                                         |
| issueIds `[String]`                                                                                                                     | Filter issues by issue IDs                                              |                                                         |
| ruleId `[String]`                                                                                                                       | Filter by rule IDs associated with the issues                           |                                                         |
| appOwnersEmail `[String]`                                                                                                               | Filter by email addresses of application owners                         |                                                         |
| appOwnersName `[String]`                                                                                                                | Filter by names of application owners                                   |                                                         |
| version `[String]`                                                                                                                      | Filter issues by version strings                                        |                                                         |
| apiItem `[String]`                                                                                                                      | Filter issues by API items related to the issue                         |                                                         |
| saasBom `[String]`                                                                                                                      | Filter issues by SaaS BOM (Bill of Materials) identifiers               |                                                         |
| resolvedByName `[String]`                                                                                                               | Filter issues by names of users who resolved them                       |                                                         |

### References

#### Fields with this object

* [{} IssuesInput.filters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input)
* [{} ResolvedIssuesInput.filters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-input)
* [{} ResolvedIssuesV2Input.filters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-v2input)
