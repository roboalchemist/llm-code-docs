# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/filter-types.md

# filterTypes

Types of filters that can be applied to narrow down and organize security findings and resources.

### Examples

```graphql
enum FilterTypes {
  digest
  expiry
  fakeApp
  apps
  criticality
  policies
  issueOwners
  codeOwners
  categories
  issueNames
  appId
  sourceTools
  cwe
  originBranchName
  businessPriority
  cvss
  severityChange
  severityChangeReasons
  issueStatus
  issueStatusVsLastScan
  issueActions
  originalSeverity
  filePaths
  uniqueLibs
  languages
  cve
  dastUrl
  oscar
  oscarTactic
  complianceControl
  complianceStandard
  tags
  tagIds
  issuesWithout
  image
  resolvedReasons
  os
  baseImage
  registryName
  artifactSha
  workflows
  scaFixType
  oxuser
  issueIds
  firstSeen
  daysPastSLA
  slaStatus
  credentialsName
  credentialsId
  issueUpdatedAt
  commitDate
  orgUnit
  azureResourceGroup
  applicationSource
  libraryNames
  libraryVersions
  appIds
  source
  licenses
  dependencyTypes
  packageNames
  copyrights
  severities
  packageInfos
  packageManagers
  ruleId
  licenseIssue
  malicious
  cicd
  repoTypes
  appApplicationSource
  orchestrators
  artifacts
  artifactsSystem
  cloudDeployments
  kubernetes
  sast
  sca
  iac
  secretSearch
  securityToolSource
  oxInPipeline
  oxInPipelineV2
  pkgManagers
  isMonoRepoChild
  appClassification
  appOwners
  ticketStatus
  resolvedReason
  disappearedReason
  disappearedType
  enforcement
  cicdIssueStatus
  jobNumber
  pullRequests
  eventTypes
  targetBranches
  sourceBranches
  jobTriggeredBy
  result
  cicdTypes
  jobId
  sourceBranch
  cicdEventType
  scanCompletionStatus
  pipelineScanType
  pipelineArtifactName
  pipelineArtifactTag
  artifactName
  artifactFullName
  artifactType
  environment
  issueSeverities
  registryType
  version
  user
  region
  accountId
  cloudRegion
  cloudAccountId
  cloudResource
  cloudResourceTag
  namespace
  artifactIntegrity
  artifactTag
  artifactSignStatus
  appTags
  artifactSignatureTag
  signerProfileVersion
  imageName
  reason
  imageTags
  imageDigest
  apiId
  titles
  endpoints
  methods
  framework
  appOwnersName
  appOwnersEmail
  apiItem
  irrelevantReasons
  severityChangeHistory
  reachability
  exposureByApi
  name
  detectionType
  saasBom
  type
  service
  cloudProvider
  assetName
  serviceCategory
  isLegitimatelyDisappeared
  cbomId
  cluster
  isExposed
  epssPercentile
  epssScore
  imageSource
  imageScanStatus
  resolvedByName
  sbomImageTags
  libForSearch
  runtimeStatus
  fixedByVibeSecOxMind
  cspmEnhanced
  packageVisibility
  triageStatus
  severityChangeReasonsV2
}
```

### Enum values

| Enum value                | Description                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| digest                    | Filter by Signature Time                                                                              |
| expiry                    | Filter by Expiration Time                                                                             |
| fakeApp                   | Filter test/demo applications                                                                         |
| apps                      | Filter by Application                                                                                 |
| criticality               | Filter by Severity                                                                                    |
| policies                  | Filter by Policy                                                                                      |
| issueOwners               | Filter by Issue Owner                                                                                 |
| codeOwners                | Filter by Code Owners                                                                                 |
| categories                | Filter by Category                                                                                    |
| issueNames                | Filter by Issue Name                                                                                  |
| appId                     | Filter by application identifier                                                                      |
| sourceTools               | Filter by Source Tool                                                                                 |
| cwe                       | Filter by CWE                                                                                         |
| originBranchName          | Filter by repository branch names                                                                     |
| businessPriority          | Filter by Business Priority                                                                           |
| cvss                      | Filter by CVSS Base Score                                                                             |
| severityChange            | Filter by Severity Reprioritized                                                                      |
| severityChangeReasons     | Filter by Severity Factor                                                                             |
| issueStatus               | Filter by Issue Status Over Time                                                                      |
| issueStatusVsLastScan     | Filter by Issue Status vs Last Scan                                                                   |
| issueActions              | Filter by Actions                                                                                     |
| originalSeverity          | Filter by Severity Before Prioritization                                                              |
| filePaths                 | Filter by Files With Issues                                                                           |
| uniqueLibs                | Filter by Vulnerable Library                                                                          |
| languages                 | Filter by Languages                                                                                   |
| cve                       | Filter by CVE                                                                                         |
| dastUrl                   | Filter by DAST URL                                                                                    |
| oscar                     | Filter by OSC\&R Technique                                                                            |
| oscarTactic               | Filter by OSC\&R Tactic                                                                               |
| complianceControl         | Filter by Compliance Control                                                                          |
| complianceStandard        | Filter by Compliance Standard                                                                         |
| tags                      | Filter by App Tag                                                                                     |
| tagIds                    | Filter by tag identifiers                                                                             |
| issuesWithout             | Filter by Issues Without                                                                              |
| image                     | Filter by Artifact Image                                                                              |
| resolvedReasons           | Filter by Resolved Reasons                                                                            |
| os                        | Filter by Artifact OS Image                                                                           |
| baseImage                 | Filter by Artifact Base Image                                                                         |
| registryName              | Filter by Registry Name                                                                               |
| artifactSha               | Filter by Artifact SHA                                                                                |
| workflows                 | Filter by Workflow Name                                                                               |
| scaFixType                | Filter by software composition analysis fix types                                                     |
| oxuser                    | Filter by Ox user references                                                                          |
| issueIds                  | Filter by issue identifiers                                                                           |
| firstSeen                 | Filter by First Seen                                                                                  |
| daysPastSLA               | Filter by SLA                                                                                         |
| slaStatus                 | Filter by SLA status                                                                                  |
| credentialsName           | Filter by Connection Name                                                                             |
| credentialsId             | Filter by credentials ID                                                                              |
| issueUpdatedAt            | Filter by Issue Updated At                                                                            |
| commitDate                | Filter by Commit Date                                                                                 |
| orgUnit                   | Filter by Business Unit                                                                               |
| azureResourceGroup        | Filter by Resource Group                                                                              |
| applicationSource         | Filter by Application Source                                                                          |
| libraryNames              | Filter by Library Name                                                                                |
| libraryVersions           | Filter by Library Version                                                                             |
| appIds                    | Filter by application identifiers                                                                     |
| source                    | Filter by Source                                                                                      |
| licenses                  | Filter by License                                                                                     |
| dependencyTypes           | Filter by Dependency                                                                                  |
| packageNames              | Filter by Package Name                                                                                |
| copyrights                | Filter by Copyright                                                                                   |
| severities                | Filter by Vulnerability Severity                                                                      |
| packageInfos              | Filter by Issues                                                                                      |
| packageManagers           | Filter by Package Manager                                                                             |
| ruleId                    | Filter by Rule ID                                                                                     |
| licenseIssue              | Filter by license compliance issues                                                                   |
| malicious                 | Filter by Malicious                                                                                   |
| cicd                      | Filter by CI/CD                                                                                       |
| repoTypes                 | Filter by Source Control                                                                              |
| appApplicationSource      | Filter by Application Source                                                                          |
| orchestrators             | Filter by Orchestrator                                                                                |
| artifacts                 | Filter by Artifact Type                                                                               |
| artifactsSystem           | Filter by Registry                                                                                    |
| cloudDeployments          | Filter by Cloud Deployment                                                                            |
| kubernetes                | Filter by Container as a Service                                                                      |
| sast                      | Filter by SAST Coverage                                                                               |
| sca                       | Filter by SCA Coverage                                                                                |
| iac                       | Filter by IAC Coverage                                                                                |
| secretSearch              | Filter by Secret Coverage                                                                             |
| securityToolSource        | Filter by Security Tool Source                                                                        |
| oxInPipeline              | Filter by OX In Pipeline                                                                              |
| oxInPipelineV2            | Filter by OX In Pipeline                                                                              |
| pkgManagers               | Filter by Package Manager                                                                             |
| isMonoRepoChild           | Filter by monorepo child status                                                                       |
| appClassification         | Filter by App Classification                                                                          |
| appOwners                 | Filter by application owners                                                                          |
| ticketStatus              | Filter by Ticket Status                                                                               |
| resolvedReason            | Filter by issue resolution reason                                                                     |
| disappearedReason         | Filter by Removed Reasons                                                                             |
| disappearedType           | Filter by type of disappearance                                                                       |
| enforcement               | Filter by Result                                                                                      |
| cicdIssueStatus           | Filter by Pipeline Issue Status                                                                       |
| jobNumber                 | Filter by Job Number                                                                                  |
| pullRequests              | Filter by Pull Request                                                                                |
| eventTypes                | Filter by Event Type                                                                                  |
| targetBranches            | Filter by Target Branch                                                                               |
| sourceBranches            | Filter by Scanned Branch                                                                              |
| jobTriggeredBy            | Filter by Job Triggered By                                                                            |
| result                    | Filter by Result                                                                                      |
| cicdTypes                 | Filter by CI/CD Type                                                                                  |
| jobId                     | Filter by Job ID                                                                                      |
| sourceBranch              | Filter by source branch                                                                               |
| cicdEventType             | Filter by CI/CD event type                                                                            |
| scanCompletionStatus      | Filter by Scan Completion Status                                                                      |
| pipelineScanType          | Filter by Scan Type                                                                                   |
| pipelineArtifactName      | Filter by pipeline artifact name                                                                      |
| pipelineArtifactTag       | Filter by pipeline artifact tag                                                                       |
| artifactName              | Filter by Artifact                                                                                    |
| artifactFullName          | Filter by full artifact name                                                                          |
| artifactType              | Filter by Artifact Type                                                                               |
| environment               | Filter by Environment                                                                                 |
| issueSeverities           | Filter by issue severity levels                                                                       |
| registryType              | Filter by Registry Type                                                                               |
| version                   | Filter by Version                                                                                     |
| user                      | Filter by User                                                                                        |
| region                    | Filter by Region                                                                                      |
| accountId                 | Filter by Account                                                                                     |
| cloudRegion               | Filter by Cloud Region                                                                                |
| cloudAccountId            | Filter by Cloud Account                                                                               |
| cloudResource             | Filter by Cloud Resource                                                                              |
| cloudResourceTag          | Filter by Cloud Resource Tag                                                                          |
| namespace                 | Filter by Kubernetes Namespace                                                                        |
| artifactIntegrity         | Filter by Artifact Integrity                                                                          |
| artifactTag               | Filter by Artifact Tag                                                                                |
| artifactSignStatus        | Filter by artifact signature status                                                                   |
| appTags                   | Filter by application tags                                                                            |
| artifactSignatureTag      | Filter by Signature Tag                                                                               |
| signerProfileVersion      | Filter by Signing Profile                                                                             |
| imageName                 | Filter by Image Name                                                                                  |
| reason                    | Filter by Reason                                                                                      |
| imageTags                 | Filter by Image Tags                                                                                  |
| imageDigest               | Filter by image digest                                                                                |
| apiId                     | Filter by API identifier                                                                              |
| titles                    | Filter by Title                                                                                       |
| endpoints                 | Filter by Endpoint                                                                                    |
| methods                   | Filter by Method                                                                                      |
| framework                 | Filter by Framework                                                                                   |
| appOwnersName             | Filter by application owner name                                                                      |
| appOwnersEmail            | Filter by application owner email                                                                     |
| apiItem                   | Filter by API item                                                                                    |
| irrelevantReasons         | Filter by irrelevant reasons                                                                          |
| severityChangeHistory     | Filter by Severity Change Log                                                                         |
| reachability              | Filter by Code-to-Cloud Exposure (Available values: Code)                                             |
| exposureByApi             | Filter by Exposure by API (Available values: "Exposed + internet exposure", "Exposed", "Not exposed") |
| name                      | Filter by name                                                                                        |
| detectionType             | Filter by Detection Type                                                                              |
| saasBom                   | Filter by SaaS Bill of Materials                                                                      |
| type                      | Filter by Type                                                                                        |
| service                   | Filter by Cloud Service                                                                               |
| cloudProvider             | Filter by Cloud Provider                                                                              |
| assetName                 | Filter by Asset Name                                                                                  |
| serviceCategory           | Filter by Service Category                                                                            |
| isLegitimatelyDisappeared | Filter by Is Legitimately Removed                                                                     |
| cbomId                    | Filter by Cloud Bill of Materials identifier                                                          |
| cluster                   | Filter by Kubernetes Cluster                                                                          |
| isExposed                 | Filter by Is Internet Exposed                                                                         |
| epssPercentile            | Filter by EPSS percentile                                                                             |
| epssScore                 | Filter by EPSS score                                                                                  |
| imageSource               | Filter by Image Source                                                                                |
| imageScanStatus           | Filter by Image Scan Status                                                                           |
| resolvedByName            | Filter by Resolved By                                                                                 |
| sbomImageTags             | Filter by Artifact Image Tag                                                                          |
| libForSearch              | Filter by Library                                                                                     |
| runtimeStatus             | Filter by Runtime Status                                                                              |
| fixedByVibeSecOxMind      | Filter by Fixed by VibeSec OxMind                                                                     |
| cspmEnhanced              | Filter by CSPM Enhanced Issues                                                                        |
| packageVisibility         | Filter by Visibility                                                                                  |
| triageStatus              | Filter by Triage Status                                                                               |
| severityChangeReasonsV2   |                                                                                                       |

### References

#### Fields with this object

* [{} GetApplicationsInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input)
* [{} ConditionalFilters.fieldName](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/conditional-filters)
* [{} FilterLazy.type](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy)
* [{} IssuesInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input)
* [{} GetIssuesConditionalFiltersInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/get-issues-conditional-filters-input)
* [{} GetApplicationsSbom.openItems](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/get-applications-sbom)
* [{} ResolvedIssuesInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-input)
* [{} ResolvedIssuesV2Input.openItems](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-v2input)
* [{} DisappearedIssuesInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/disappeared-issues-input)
* [{} CICDIssuesInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-input)
* [{} GetArtifactsInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-input)
* [{} GetUnscannedArtifactsInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-unscanned-artifacts-input)
* [{} GetPipelineSummaryInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/get-pipeline-summary-input)
* [{} GetApiSecurityInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/inputs/get-api-security-input)
* [{} GetSaasBomItemsInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/get-saas-bom-items-input)
* [{} CloudItemsInput.openItems](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/cloud-items-input)
