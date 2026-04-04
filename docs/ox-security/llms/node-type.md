# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/node-type.md

# nodeType

Types of nodes in the issue graph representing different entities and their relationships.

### Examples

```graphql
enum NodeType {
  Root
  IssueOwner
  Language
  FirstSeen
  Oscar
  OscarItem
  Cwe
  CweItem
  Compliance
  ComplianceItem
  SeverityFactor
  SeverityFactorChange
  SeverityFactorCategory
  Commit
  CommitItem
  CommitItemCommitBy
  User
  UserItem
  Repos
  ReposItem
  Service
  ServiceItem
  Webhook
  SBOMRepos
  SBOMReposItem
  Artifact
  ArtifactItem
  ArtifactIntegrity
  ArtifactIntegrityItem
  WebhookItem
  CommitItemCommitDate
  CommitItemCommitReviewedBy
  CommitItemFile
  Library
  Popularity
  Maintenance
  License
  Update
  Action
  Slack
  SlackItem
  JiraTicket
  JiraTicketItem
  Pr
  PrItem
  App
  BusinessPriority
  AppLink
  AppLanguage
  Link
  Tag
  TagItem
  Cve
  CveItem
  Detection
  Intelligence
  Saas
  Api
  ApiFileName
  ApiFramework
  ApiFunction
  ApiLink
  ApiSource
  ApiCount
  Image
  ImageId
  ImageArtifact
  K8s
  K8sLink
  K8sImageId
  K8sApplication
  K8sIngress
  K8sLoadBalancer
  Cloud
  CloudRegion
  CloudDns
  CloudLink
  CloudLoadBalancer
  CloudNetworkLoadBalancer
  ApplicationLoadBalancer
  Internet
  Hub
  CBOMRoot
  Issue
  CbomIssues
  ImageRegistry
}
```

### Enum values

| Enum value                 | Description                                                   |
| -------------------------- | ------------------------------------------------------------- |
| Root                       | Root node of the issue graph serving as the main entry point  |
| IssueOwner                 | Entity responsible for managing and resolving the issue       |
| Language                   | Programming language or technology associated with the issue  |
| FirstSeen                  | Timestamp or date when the issue was first detected           |
| Oscar                      | Container for Oscar-related security findings                 |
| OscarItem                  | Specific security finding or vulnerability detected by Oscar  |
| Cwe                        | Common Weakness Enumeration category container                |
| CweItem                    | Specific CWE (Common Weakness Enumeration) vulnerability type |
| Compliance                 | Container for compliance standards and frameworks             |
| ComplianceItem             | Specific compliance requirement or control                    |
| SeverityFactor             | Container for factors affecting issue severity                |
| SeverityFactorChange       | Change in severity assessment factors                         |
| SeverityFactorCategory     | Category classification for severity factors                  |
| Commit                     | Container for code commit information                         |
| CommitItem                 | Specific code commit details                                  |
| CommitItemCommitBy         | Author or committer of the code change                        |
| User                       | Container for user-related information                        |
| UserItem                   | Specific user details and attributes                          |
| Repos                      | Container for code repositories                               |
| ReposItem                  | Specific repository information and metadata                  |
| Service                    | Container for service-related information                     |
| ServiceItem                | Specific service instance or configuration                    |
| Webhook                    | Container for webhook configurations                          |
| SBOMRepos                  | Container for Software Bill of Materials (SBOM) repositories  |
| SBOMReposItem              | Specific SBOM repository information                          |
| Artifact                   | Container for build artifacts and packages                    |
| ArtifactItem               | Specific artifact or package information                      |
| ArtifactIntegrity          | Container for artifact integrity checks                       |
| ArtifactIntegrityItem      | Specific artifact integrity verification result               |
| WebhookItem                | Specific webhook configuration and endpoint                   |
| CommitItemCommitDate       | Timestamp of when the commit was made                         |
| CommitItemCommitReviewedBy | Reviewer of the code commit                                   |
| CommitItemFile             | File affected by the commit                                   |
| Library                    | Software library or dependency                                |
| Popularity                 | Usage popularity metrics                                      |
| Maintenance                | Maintenance status and metrics                                |
| License                    | Software license information                                  |
| Update                     | Update or patch information                                   |
| Action                     | Action or task to be performed                                |
| Slack                      | Container for Slack integration information                   |
| SlackItem                  | Specific Slack notification or channel configuration          |
| JiraTicket                 | Container for Jira ticket information                         |
| JiraTicketItem             | Specific Jira ticket details                                  |
| Pr                         | Container for Pull Request information                        |
| PrItem                     | Specific Pull Request details                                 |
| App                        | Application or service instance                               |
| BusinessPriority           | Business impact and priority classification                   |
| AppLink                    | Connection between applications or services                   |
| AppLanguage                | Programming language used in the application                  |
| Link                       | Generic link or connection between nodes                      |
| Tag                        | Container for tag information                                 |
| TagItem                    | Specific tag or label                                         |
| Cve                        | Container for Common Vulnerabilities and Exposures            |
| CveItem                    | Specific CVE vulnerability information                        |
| Detection                  | Security detection or finding information                     |
| Intelligence               | Security intelligence or threat information                   |
| Saas                       | Software as a Service component or integration                |
| Api                        | API endpoint or service interface                             |
| ApiFileName                | Source file containing API definition                         |
| ApiFramework               | Framework used for API implementation                         |
| ApiFunction                | Specific API function or method                               |
| ApiLink                    | Connection between API components                             |
| ApiSource                  | Source or origin of the API                                   |
| ApiCount                   | API usage or occurrence count                                 |
| Image                      | Container image information                                   |
| ImageId                    | Unique identifier for container image                         |
| ImageArtifact              | Artifact associated with container image                      |
| K8s                        | Kubernetes resource or component                              |
| K8sLink                    | Connection between Kubernetes resources                       |
| K8sImageId                 | Container image ID used in Kubernetes                         |
| K8sApplication             | Application running on Kubernetes                             |
| K8sIngress                 | Kubernetes ingress configuration                              |
| K8sLoadBalancer            | Kubernetes load balancer service                              |
| Cloud                      | Cloud service or resource                                     |
| CloudRegion                | Geographic region of cloud resources                          |
| CloudDns                   | Cloud DNS configuration                                       |
| CloudLink                  | Connection between cloud resources                            |
| CloudLoadBalancer          | Cloud-native load balancer                                    |
| CloudNetworkLoadBalancer   | Network load balancer in cloud infrastructure                 |
| ApplicationLoadBalancer    | Application-level load balancer                               |
| Internet                   | Internet-facing or external access point                      |
| Hub                        | Central connection point for multiple components              |
| CBOMRoot                   | Root node of the cbom graph serving as the main entry point   |
| Issue                      | Container for issue information related to cbom item          |
| CbomIssues                 |                                                               |
| ImageRegistry              | Images registry                                               |

### References

#### Fields with this object

* [{} Node.type](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/node)
