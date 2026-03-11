# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/log-name.md

# logName

Specific actions recorded in audit logs.

### Examples

```graphql
enum LogName {
  AddCredentials
  RemoveCredentials
  UpdateCredentials
  EnableConnector
  DisableConnector
  ScanNow
  ScheduledScan
  CancelScan
  AddLoginOption
  RevokeLoginOption
  UpdateLoginOption
  SendInvitation
  RevokeInvitation
  ResendInvitation
  MemberAcceptInvitation
  RemoveMember
  UpdateMemberRoles
  UpdateMemberScopes
  UpdateMember
  UpdateMonitorResources
  AddAppBranchesToMonitor
  RemovedMonitoredAppBranches
  UpdateMonitorAppBranches
  AddResourcesToMonitor
  RemovedMonitoredResources
  UpdateMonitorBranches
  AddBranchesToMonitor
  RemovedMonitoredBranches
  Login
  Logout
  ChatGPTDisclaimerAccepted
  ModifiedBusinessPriority
  DownloadSBOM
  DownloadReportSBOM
  CommentCreated
  CommentDeleted
  CommentEdited
  AssignedOwners
  ModifiedAppOwner
  DeletedAppOwner
  ChatGPTCreated
  ModifiedPolicies
  SplitMonorepo
  AlertSlackSent
  AlertSent
  JiraTicketOpened
  JiraTicketLinked
  JiraTicketUnlinked
  TicketingTicketCreated
  TicketingTicketLinked
  TicketingTicketUnlinked
  TicketClosed
  TicketReopened
  TicketingSettingsUpdated
  ScanSettings
  IssueExcluded
  AllApplicationsExclusion
  SingleApplicationExclusion
  BulkIssuesExcluded
  BulkIssuesExcludedRemoved
  BulkUpdatedExclusionExpiryDate
  BulkPoliciesEnabled
  FalsePositive
  FalseResolvedIssue
  ExclusionRemoved
  UpdatedExclusionExpiryDate
  ViewCodeFix
  PullRequestOpened
  PullRequestDeleted
  FixApplied
  ChangedSeverity
  SetSLA
  ResetSLA
  DismissSLA
  IssueSeverityReset
  ChangedIssueOwner
  ResetIssueOwner
  BusinessPriorityReset
  MakeAppIrrelevant
  MakeAppRelevant
  ModifiedAppTags
  ModifiedPipelinePolicies
  ChatGPT
  ChatGPTCodeSnippet
  PRChatGPT
  Monorepo
  GithubTopics
  ScheduleScan
  ScheduledScanHour
  AdvancedOptionsToolTip
  ConfiguredIrrelevantAppsTime
  ConfiguredAdvancedOptionsToolTipTime
  TextArr
  PolicyWorkflowCreated
  PolicyWorkflowManualExecution
  PolicyWorkflowDeleted
  PolicyWorkflowUpdated
  PolicyWorkflowDisabled
  PolicyWorkflowEnabled
  PolicyWorkflowNodeCreated
  PolicyWorkflowNodeUpdated
  PolicyWorkflowNodeDeleted
  ApplicationContainerAssigned
  ApplicationContainerUnassigned
  ApplicationContainerRestored
  ContainersRestored
  SecretCreated
  SecretDeleted
  SaveSharedFilter
  DeleteSharedFilter
  UpdateSharedFilter
  ConfiguredIrrelevantImagesTime
  DefineBranch
  ApiKeyCreate
  ApiKeyDelete
  ApiKeyEnable
  ApiKeyDisable
  ApiKeySetExpiration
  DefineBranchPerRepo
  DisableCodeSmellIssues
  ConfigureIssuesTime
  ConfigureIssuesScanTime
  ScanImagesByTags
  ScanOnlySelectedImagesFromRuntime
  ScanImagesFromK8sNodes
  OrgUnitCreated
  OrgUnitUpdated
  OrgUnitDeleted
  OrgUnitHierarchyUpdated
  TagExclusionUpdatedForExecutiveReport
  PipelineSettingsSaved
  MonorepoSplitBy
  ConfiguredToolTipTime
  ExcludeFiles
  ExcludeUrls
  GitlabGroups
  GitlabTopics
  ScanRuntimeImagesBasedOnArtifactMatch
  GitPosture
  CicdPosture
  CallGraph
  AppTags
  SaasBom
  ApiBom
  AttackPath
  ApiBomOnly
  Dashboard
  Applications
  Issues
  ToggleManualScanning
  DefineMultiBranchSplit
  DefineMultiBranchDefaultBranch
  DefineMultiBranchList
  SlaSettingsChanged
  MultiBranchScanningApplied
  MultiBranchScanningFailed
  BitbucketWorkspace
  BitbucketProjects
  AIBasedMatching
  IrrelevantPublicRepos
  SecretsValidator
  ScanRepositories
  CreateOrganization
  UpdateOrganization
  DeleteOrganization
  EmailNotification
  DownloadReportSlaTopBusinessUnitsCSV
  AIRemediationIDE
  AIRemediationPRs
  AIRemediationUI
  AuditLogsExportEnabled
  AuditLogsExportDisabled
  AuditLogsExportBucketName
  AuditLogsExportS3Region
  AuditLogsExportBucketPrefix
  AuditLogsExportInvocationFrequencyHours
  AuditLogsExportSettingUpdated
  ValidateS3BucketConnection
  ScheduledAuditLogsExportCompleted
  ScheduledAuditLogsExportFailed
  CustomScannerTag
  IssueTriaged
  FileImportUploaded
  FileImportRemoved
  AISummaryIssue
  CreateDastTarget
  EditDastTarget
  DeleteDastTarget
  AuditLogsRetentionDays
  ResolvedIssuesRetentionDays
  RemovedIssuesRetentionDays
  ScanSummariesRetentionDays
  CicdIssuesRetentionDays
  PipelineSummariesRetentionDays
  RepoScan
  CustomRoleCreated
  CustomRoleUpdated
  CustomRoleDeleted
}
```

### Enum values

| Enum value                              | Description                                                      |
| --------------------------------------- | ---------------------------------------------------------------- |
| AddCredentials                          | Addition of new authentication credentials to the system         |
| RemoveCredentials                       | Removal of existing authentication credentials from the system   |
| UpdateCredentials                       | Update of existing authentication credentials in the system      |
| EnableConnector                         | Activation of an external service connector integration          |
| DisableConnector                        | Deactivation of an external service connector integration        |
| ScanNow                                 | Manual initiation of an immediate security scan                  |
| ScheduledScan                           | Automatic execution of a pre-scheduled security scan             |
| CancelScan                              | Manual cancellation of an ongoing security scan                  |
| AddLoginOption                          | Addition of a new authentication method or login option          |
| RevokeLoginOption                       | Removal of an existing authentication method                     |
| UpdateLoginOption                       | Modification of existing login settings or options               |
| SendInvitation                          | Sending of a new member invitation                               |
| RevokeInvitation                        | Cancellation of a pending member invitation                      |
| ResendInvitation                        | Resending an invitation to a pending member                      |
| MemberAcceptInvitation                  | Acceptance of an invitation by a new member                      |
| RemoveMember                            | Removal of an existing member from the organization              |
| UpdateMemberRoles                       | Modification of a member's assigned roles                        |
| UpdateMemberScopes                      | Changes to a member's permission scopes                          |
| UpdateMember                            | General updates to member information or settings                |
| UpdateMonitorResources                  | Modification of resources being monitored                        |
| AddAppBranchesToMonitor                 |                                                                  |
| RemovedMonitoredAppBranches             |                                                                  |
| UpdateMonitorAppBranches                |                                                                  |
| AddResourcesToMonitor                   | Addition of new resources to monitoring scope                    |
| RemovedMonitoredResources               | Removal of resources from monitoring scope                       |
| UpdateMonitorBranches                   | Updates to branch monitoring configuration                       |
| AddBranchesToMonitor                    | Addition of new branches to monitoring scope                     |
| RemovedMonitoredBranches                | Removal of branches from monitoring scope                        |
| Login                                   | Successful user authentication and login                         |
| Logout                                  | User session termination and logout                              |
| ChatGPTDisclaimerAccepted               | User acceptance of AI assistant usage terms                      |
| ModifiedBusinessPriority                | Changes to application business priority level                   |
| DownloadSBOM                            | Download of Software Bill of Materials report                    |
| DownloadReportSBOM                      | Download of detailed SBOM analysis report                        |
| CommentCreated                          | Creation of a new comment on an issue                            |
| CommentDeleted                          | Deletion of an existing comment                                  |
| CommentEdited                           | Modification of an existing comment                              |
| AssignedOwners                          | Assignment of owners to an application                           |
| ModifiedAppOwner                        | Changes to application ownership settings                        |
| DeletedAppOwner                         | Removal of an owner from an application                          |
| ChatGPTCreated                          | New interaction initiated with AI assistant                      |
| ModifiedPolicies                        | Changes to security policy configurations                        |
| SplitMonorepo                           |                                                                  |
| AlertSlackSent                          |                                                                  |
| AlertSent                               |                                                                  |
| JiraTicketOpened                        |                                                                  |
| JiraTicketLinked                        |                                                                  |
| JiraTicketUnlinked                      |                                                                  |
| TicketingTicketCreated                  |                                                                  |
| TicketingTicketLinked                   |                                                                  |
| TicketingTicketUnlinked                 |                                                                  |
| TicketClosed                            |                                                                  |
| TicketReopened                          |                                                                  |
| TicketingSettingsUpdated                | Ticketing system settings were updated                           |
| ScanSettings                            |                                                                  |
| IssueExcluded                           |                                                                  |
| AllApplicationsExclusion                |                                                                  |
| SingleApplicationExclusion              |                                                                  |
| BulkIssuesExcluded                      |                                                                  |
| BulkIssuesExcludedRemoved               |                                                                  |
| BulkUpdatedExclusionExpiryDate          |                                                                  |
| BulkPoliciesEnabled                     |                                                                  |
| FalsePositive                           | Issue marked as false positive                                   |
| FalseResolvedIssue                      | Issue marked as incorrectly resolved                             |
| ExclusionRemoved                        |                                                                  |
| UpdatedExclusionExpiryDate              |                                                                  |
| ViewCodeFix                             | Viewing of suggested code fixes                                  |
| PullRequestOpened                       |                                                                  |
| PullRequestDeleted                      |                                                                  |
| FixApplied                              |                                                                  |
| ChangedSeverity                         |                                                                  |
| SetSLA                                  |                                                                  |
| ResetSLA                                |                                                                  |
| DismissSLA                              |                                                                  |
| IssueSeverityReset                      |                                                                  |
| ChangedIssueOwner                       | Issue owner was changed                                          |
| ResetIssueOwner                         | Issue owner was reset                                            |
| BusinessPriorityReset                   |                                                                  |
| MakeAppIrrelevant                       |                                                                  |
| MakeAppRelevant                         |                                                                  |
| ModifiedAppTags                         |                                                                  |
| ModifiedPipelinePolicies                | Updates to CI/CD pipeline security policies                      |
| ChatGPT                                 | General AI assistant interactions                                |
| ChatGPTCodeSnippet                      |                                                                  |
| PRChatGPT                               |                                                                  |
| Monorepo                                |                                                                  |
| GithubTopics                            |                                                                  |
| ScheduleScan                            |                                                                  |
| ScheduledScanHour                       |                                                                  |
| AdvancedOptionsToolTip                  |                                                                  |
| ConfiguredIrrelevantAppsTime            |                                                                  |
| ConfiguredAdvancedOptionsToolTipTime    |                                                                  |
| TextArr                                 |                                                                  |
| PolicyWorkflowCreated                   |                                                                  |
| PolicyWorkflowManualExecution           |                                                                  |
| PolicyWorkflowDeleted                   |                                                                  |
| PolicyWorkflowUpdated                   |                                                                  |
| PolicyWorkflowDisabled                  |                                                                  |
| PolicyWorkflowEnabled                   |                                                                  |
| PolicyWorkflowNodeCreated               |                                                                  |
| PolicyWorkflowNodeUpdated               |                                                                  |
| PolicyWorkflowNodeDeleted               |                                                                  |
| ApplicationContainerAssigned            |                                                                  |
| ApplicationContainerUnassigned          |                                                                  |
| ApplicationContainerRestored            |                                                                  |
| ContainersRestored                      |                                                                  |
| SecretCreated                           |                                                                  |
| SecretDeleted                           |                                                                  |
| SaveSharedFilter                        |                                                                  |
| DeleteSharedFilter                      |                                                                  |
| UpdateSharedFilter                      |                                                                  |
| ConfiguredIrrelevantImagesTime          |                                                                  |
| DefineBranch                            |                                                                  |
| ApiKeyCreate                            |                                                                  |
| ApiKeyDelete                            |                                                                  |
| ApiKeyEnable                            |                                                                  |
| ApiKeyDisable                           |                                                                  |
| ApiKeySetExpiration                     |                                                                  |
| DefineBranchPerRepo                     |                                                                  |
| DisableCodeSmellIssues                  |                                                                  |
| ConfigureIssuesTime                     |                                                                  |
| ConfigureIssuesScanTime                 |                                                                  |
| ScanImagesByTags                        |                                                                  |
| ScanOnlySelectedImagesFromRuntime       |                                                                  |
| ScanImagesFromK8sNodes                  |                                                                  |
| OrgUnitCreated                          | Creation of a new organizational unit                            |
| OrgUnitUpdated                          | Updates to organizational unit settings                          |
| OrgUnitDeleted                          | Deletion of an organizational unit                               |
| OrgUnitHierarchyUpdated                 |                                                                  |
| TagExclusionUpdatedForExecutiveReport   |                                                                  |
| PipelineSettingsSaved                   | Saving of CI/CD pipeline configuration changes                   |
| MonorepoSplitBy                         |                                                                  |
| ConfiguredToolTipTime                   |                                                                  |
| ExcludeFiles                            |                                                                  |
| ExcludeUrls                             |                                                                  |
| GitlabGroups                            |                                                                  |
| GitlabTopics                            |                                                                  |
| ScanRuntimeImagesBasedOnArtifactMatch   |                                                                  |
| GitPosture                              |                                                                  |
| CicdPosture                             |                                                                  |
| CallGraph                               |                                                                  |
| AppTags                                 |                                                                  |
| SaasBom                                 |                                                                  |
| ApiBom                                  |                                                                  |
| AttackPath                              |                                                                  |
| ApiBomOnly                              |                                                                  |
| Dashboard                               |                                                                  |
| Applications                            |                                                                  |
| Issues                                  |                                                                  |
| ToggleManualScanning                    |                                                                  |
| DefineMultiBranchSplit                  |                                                                  |
| DefineMultiBranchDefaultBranch          |                                                                  |
| DefineMultiBranchList                   |                                                                  |
| SlaSettingsChanged                      |                                                                  |
| MultiBranchScanningApplied              |                                                                  |
| MultiBranchScanningFailed               |                                                                  |
| BitbucketWorkspace                      |                                                                  |
| BitbucketProjects                       |                                                                  |
| AIBasedMatching                         |                                                                  |
| IrrelevantPublicRepos                   |                                                                  |
| SecretsValidator                        |                                                                  |
| ScanRepositories                        | Scanning of source code repositories                             |
| CreateOrganization                      | Creation of a new organization                                   |
| UpdateOrganization                      | Modification of organization settings                            |
| DeleteOrganization                      | Deletion of an organization                                      |
| EmailNotification                       | Sending of system email notifications                            |
| DownloadReportSlaTopBusinessUnitsCSV    |                                                                  |
| AIRemediationIDE                        |                                                                  |
| AIRemediationPRs                        |                                                                  |
| AIRemediationUI                         |                                                                  |
| AuditLogsExportEnabled                  |                                                                  |
| AuditLogsExportDisabled                 |                                                                  |
| AuditLogsExportBucketName               |                                                                  |
| AuditLogsExportS3Region                 |                                                                  |
| AuditLogsExportBucketPrefix             |                                                                  |
| AuditLogsExportInvocationFrequencyHours |                                                                  |
| AuditLogsExportSettingUpdated           |                                                                  |
| ValidateS3BucketConnection              |                                                                  |
| ScheduledAuditLogsExportCompleted       |                                                                  |
| ScheduledAuditLogsExportFailed          |                                                                  |
| CustomScannerTag                        |                                                                  |
| IssueTriaged                            |                                                                  |
| FileImportUploaded                      | Upload of a file for import                                      |
| FileImportRemoved                       | Removal of an uploaded file                                      |
| AISummaryIssue                          | AI summary of an issues                                          |
| CreateDastTarget                        | Creation of a new Agentic Pentest scanning target                |
| EditDastTarget                          | Modification of an existing Agentic Pentest target configuration |
| DeleteDastTarget                        | Deletion of a Agentic Pentest scanning target                    |
| AuditLogsRetentionDays                  |                                                                  |
| ResolvedIssuesRetentionDays             |                                                                  |
| RemovedIssuesRetentionDays              |                                                                  |
| ScanSummariesRetentionDays              |                                                                  |
| CicdIssuesRetentionDays                 |                                                                  |
| PipelineSummariesRetentionDays          |                                                                  |
| RepoScan                                | Repository was scanned                                           |
| CustomRoleCreated                       | Custom Role Created                                              |
| CustomRoleUpdated                       | Custom Role Updated                                              |
| CustomRoleDeleted                       | Custom Role Deleted                                              |

### References

#### Fields with this object

* [{} GetLogsInput.logNames](https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/get-logs-input)
* [{} AuditLog.logName](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)
