# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/log-type.md

# logType

Categories of audit log events in the system.

### Examples

```graphql
enum LogType {
  Authentication
  Login
  Connectors
  Scan
  ScanRepositories
  LoginOptions
  Members
  AppModification
  AppOwners
  FileDownload
  Comment
  ChatGPT
  Policies
  Settings
  Slack
  Jira
  Ticketing
  Messaging
  Exclusions
  FalsePositive
  FalseResolvedIssue
  PullRequest
  ViewCodeFix
  FixIssue
  Issue
  IssueOwner
  IssueSLA
  PipelinePolicies
  PolicyWorkflow
  WorkflowNode
  Containers
  Secrets
  Filters
  ApiKeys
  OrgUnit
  ExecutiveReport
  PipelineSettings
  SlaSettings
  BranchScanning
  Organization
  Email
  Triage
  ExportAuditLogs
  FileImport
  DastTarget
  DataRetention
  RepoScan
  CustomRoles
}
```

### Enum values

| Enum value         | Description                                   |
| ------------------ | --------------------------------------------- |
| Authentication     | User authentication related events            |
| Login              | User login/logout events                      |
| Connectors         | Events related to external service connectors |
| Scan               | Security scanning events                      |
| ScanRepositories   | Repository scanning events                    |
| LoginOptions       | Changes to login configuration                |
| Members            | Member management events                      |
| AppModification    | Application configuration changes             |
| AppOwners          | Application ownership changes                 |
| FileDownload       | File download events                          |
| Comment            | Issue comment events                          |
| ChatGPT            | AI assistant interaction events               |
| Policies           | Security policy changes                       |
| Settings           | System settings changes                       |
| Slack              | Slack integration events                      |
| Jira               | Jira integration events                       |
| Ticketing          | Ticketing system events                       |
| Messaging          | Messaging system events                       |
| Exclusions         | Security exclusion events                     |
| FalsePositive      | False positive issue reports                  |
| FalseResolvedIssue | Incorrectly resolved issue reports            |
| PullRequest        | Pull request related events                   |
| ViewCodeFix        | Code fix viewing events                       |
| FixIssue           | Issue fix events                              |
| Issue              | General issue events                          |
| IssueOwner         | Issue ownership change events                 |
| IssueSLA           | Issue SLA events                              |
| PipelinePolicies   | CI/CD pipeline policy events                  |
| PolicyWorkflow     | Policy workflow events                        |
| WorkflowNode       | Workflow node events                          |
| Containers         | Container related events                      |
| Secrets            | Secret management events                      |
| Filters            | Filter configuration events                   |
| ApiKeys            | API key management events                     |
| OrgUnit            | Organization unit events                      |
| ExecutiveReport    | Executive report events                       |
| PipelineSettings   | Pipeline configuration events                 |
| SlaSettings        | SLA configuration events                      |
| BranchScanning     | Branch scanning events                        |
| Organization       | Organization management events                |
| Email              | Email notification events                     |
| Triage             |                                               |
| ExportAuditLogs    | Export audit logs events                      |
| FileImport         | File import events                            |
| DastTarget         | Agentic Pentest target management events      |
| DataRetention      |                                               |
| RepoScan           | Repository scanning events                    |
| CustomRoles        | Custom role events                            |

### References

#### Fields with this object

* [{} GetLogsInput.logTypes](https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/get-logs-input)
* [{} AuditLog.logType](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)
