# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/queries/get-logs.md

# getLogs

Retrieve audit logs based on specified filters and criteria.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetLogs($input: GetLogsInput) {
  getLogs(input: $input) {
    id
    date
    logType
    logName
    userId
    userEmail
    name
    appId
    appName
    registry
    dockerfile
    connector
    credentialsType
    credentialName
    resourceCount
    resources
    branches {
      branch
      reason
    }
    repoName
    reposCount
    hostUrl
    monitorAllResources
    scanId
    enabledConnectors
    loginType
    domain
    memberEmail
    disclaimerType
    memberRoles
    memberScopes
    appNames
    businessPriority
    owners
    ownersWithRoles {
      owner
      email
      roles
    }
    roles
    generatedForOrg
    downloadFormat
    generatedFrom
    comment
    excluded
    removed
    issueName
    issueId
    profileId
    profileName
    activeProfile
    settingsType
    disabled
    configured
    textArr
    policies {
      policyId
      policyName
      categoryName
      enabled
      severity
      oldIssues
      newIssues
      args
    }
    slackUser
    channel
    key
    ticketId
    ticketingVendor
    messagingVendor
    user
    link
    categoryName
    categoryId
    expiredAt
    prId
    prURL
    sourceControlType
    aggItems
    excludedIssues {
      appNames
      issueId
      issueName
      categoryName
      comment
      expiredAt
    }
    fixTitle
    severity
    oldSeverity
    newOwnerName
    newOwnerEmail
    oldOwnerName
    oldOwnerEmail
    tagsAdded
    tagsRemoved
    workflowType
    workflowName
    nodeName
    nodeType
    workflowId
    description
    enabled
    monitorAllNewlyCreatedRepositories
    monitoredApps
    secretName
    filterName
    pageName
    apiKeyName
    apiKeyType
    createdBy
    apiKeyCreatedAt
    apiKeyExpiredAt
    orgUnitName
    orgUnitId
    tags
    pipelineSettingsV2 {
      isDefaultSettings
      isGithubConnected
      isBitbucketConnected
      isGitlabConnected
      apps
      settings
      branchSettings
    }
    children
    updateSlaSettings
    irrelevantComment
    sla
    emailType
    emailSubject
    triageStatus
    actionType
    changes
    fileName
    fileType
    title
    domainType
    targetUrl
    env
    authMethod
    previousValues {
      title
      domainType
      targetUrl
      env
      authMethod
    }
    branch
    customRoleLogData {
      name
      displayName
      assignablePermissions {
        name
        isHidden
      }
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "logTypes": ["Authentication"],
    "logNames": ["AddCredentials"],
    "userEmails": ["example"],
    "limit": 100,
    "skip": 0,
    "orderBy": {
      "field": "example",
      "direction": "ASC"
    },
    "dateRange": {
      "from": "1672531200000",
      "to": "1704067199000"
    }
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
 "query": "query GetLogs($input: GetLogsInput) { getLogs(input: $input) { id date logType logName userId userEmail name appId appName registry dockerfile connector credentialsType credentialName resourceCount resources branches { branch reason } repoName reposCount hostUrl monitorAllResources scanId enabledConnectors loginType domain memberEmail disclaimerType memberRoles memberScopes appNames businessPriority owners ownersWithRoles { owner email roles } roles generatedForOrg downloadFormat generatedFrom comment excluded removed issueName issueId profileId profileName activeProfile settingsType disabled configured textArr policies { policyId policyName categoryName enabled severity oldIssues newIssues args } slackUser channel key ticketId ticketingVendor messagingVendor user link categoryName categoryId expiredAt prId prURL sourceControlType aggItems excludedIssues { appNames issueId issueName categoryName comment expiredAt } fixTitle severity oldSeverity newOwnerName newOwnerEmail oldOwnerName oldOwnerEmail tagsAdded tagsRemoved workflowType workflowName nodeName nodeType workflowId description enabled monitorAllNewlyCreatedRepositories monitoredApps secretName filterName pageName apiKeyName apiKeyType createdBy apiKeyCreatedAt apiKeyExpiredAt orgUnitName orgUnitId tags pipelineSettingsV2 { isDefaultSettings isGithubConnected isBitbucketConnected isGitlabConnected apps settings branchSettings } children updateSlaSettings irrelevantComment sla emailType emailSubject triageStatus actionType changes fileName fileType title domainType targetUrl env authMethod previousValues { title domainType targetUrl env authMethod } branch customRoleLogData { name displayName assignablePermissions { name isHidden } } } }",
 "variables": {
    "input": {
      "logTypes": ["Authentication"],
      "logNames": ["AddCredentials"],
      "userEmails": ["example"],
      "limit": 100,
      "skip": 0,
      "orderBy": {
        "field": "example",
        "direction": "ASC"
      },
      "dateRange": {
        "from": "1672531200000",
        "to": "1704067199000"
      }
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetLogs($input: GetLogsInput) { getLogs(input: $input) { id date logType logName userId userEmail name appId appName registry dockerfile connector credentialsType credentialName resourceCount resources branches { branch reason } repoName reposCount hostUrl monitorAllResources scanId enabledConnectors loginType domain memberEmail disclaimerType memberRoles memberScopes appNames businessPriority owners ownersWithRoles { owner email roles } roles generatedForOrg downloadFormat generatedFrom comment excluded removed issueName issueId profileId profileName activeProfile settingsType disabled configured textArr policies { policyId policyName categoryName enabled severity oldIssues newIssues args } slackUser channel key ticketId ticketingVendor messagingVendor user link categoryName categoryId expiredAt prId prURL sourceControlType aggItems excludedIssues { appNames issueId issueName categoryName comment expiredAt } fixTitle severity oldSeverity newOwnerName newOwnerEmail oldOwnerName oldOwnerEmail tagsAdded tagsRemoved workflowType workflowName nodeName nodeType workflowId description enabled monitorAllNewlyCreatedRepositories monitoredApps secretName filterName pageName apiKeyName apiKeyType createdBy apiKeyCreatedAt apiKeyExpiredAt orgUnitName orgUnitId tags pipelineSettingsV2 { isDefaultSettings isGithubConnected isBitbucketConnected isGitlabConnected apps settings branchSettings } children updateSlaSettings irrelevantComment sla emailType emailSubject triageStatus actionType changes fileName fileType title domainType targetUrl env authMethod previousValues { title domainType targetUrl env authMethod } branch customRoleLogData { name displayName assignablePermissions { name isHidden } } } }';

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
        logTypes: ["Authentication"],
        logNames: ["AddCredentials"],
        userEmails: ["example"],
        limit: 100,
        skip: 0,
        orderBy: {
          field: "example",
          direction: "ASC"
        },
        dateRange: {
          from: "1672531200000",
          to: "1704067199000"
        }
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

query = 'query GetLogs($input: GetLogsInput) { getLogs(input: $input) { id date logType logName userId userEmail name appId appName registry dockerfile connector credentialsType credentialName resourceCount resources branches { branch reason } repoName reposCount hostUrl monitorAllResources scanId enabledConnectors loginType domain memberEmail disclaimerType memberRoles memberScopes appNames businessPriority owners ownersWithRoles { owner email roles } roles generatedForOrg downloadFormat generatedFrom comment excluded removed issueName issueId profileId profileName activeProfile settingsType disabled configured textArr policies { policyId policyName categoryName enabled severity oldIssues newIssues args } slackUser channel key ticketId ticketingVendor messagingVendor user link categoryName categoryId expiredAt prId prURL sourceControlType aggItems excludedIssues { appNames issueId issueName categoryName comment expiredAt } fixTitle severity oldSeverity newOwnerName newOwnerEmail oldOwnerName oldOwnerEmail tagsAdded tagsRemoved workflowType workflowName nodeName nodeType workflowId description enabled monitorAllNewlyCreatedRepositories monitoredApps secretName filterName pageName apiKeyName apiKeyType createdBy apiKeyCreatedAt apiKeyExpiredAt orgUnitName orgUnitId tags pipelineSettingsV2 { isDefaultSettings isGithubConnected isBitbucketConnected isGitlabConnected apps settings branchSettings } children updateSlaSettings irrelevantComment sla emailType emailSubject triageStatus actionType changes fileName fileType title domainType targetUrl env authMethod previousValues { title domainType targetUrl env authMethod } branch customRoleLogData { name displayName assignablePermissions { name isHidden } } } }'

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
        "logTypes": ["Authentication"],
        "logNames": ["AddCredentials"],
        "userEmails": ["example"],
        "limit": 100,
        "skip": 0,
        "orderBy": {
          "field": "example",
          "direction": "ASC"
        },
        "dateRange": {
          "from": "1672531200000",
          "to": "1704067199000"
        }
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

You can use the following argument(s) to customize your `getLogs` query.

| Argument                                                                                                                | Description                                                | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| input [`GetLogsInput`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/get-logs-input) | Filter and pagination parameters for retrieving audit logs | <p>logTypes <a href="../types/enums/log-type"><code>\[LogType!]</code></a><br>logNames <a href="../types/enums/log-name"><code>\[LogName!]</code></a><br>userEmails <code>\[String!]</code><br>limit <code>Float</code><br>skip <code>Float</code><br>orderBy <a href="../types/inputs/log-order-by"><code>LogOrderBy</code></a><br>dateRange <a href="../types/inputs/log-date-range"><code>LogDateRange</code></a></p> |

### Fields

Return type: [`[AuditLog!]!`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log)

You can use the following field(s) to specify what information your `getLogs` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                                       | Description                                                                               | Supported fields                                                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id `String!`                                                                                                                                                | Unique identifier of the audit log entry                                                  |                                                                                                                                                                                                                                                                                               |
| date `DateTime!`                                                                                                                                            | Timestamp when the event occurred. Records are automatically expired after 365 days       |                                                                                                                                                                                                                                                                                               |
| logType [`LogType!`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/log-type)                                              | Category of the event (e.g., Authentication, Login, Scan)                                 |                                                                                                                                                                                                                                                                                               |
| logName [`LogName!`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/log-name)                                              | Specific action or event name within the category                                         |                                                                                                                                                                                                                                                                                               |
| userId `String!`                                                                                                                                            | Unique identifier of the user who performed the action                                    |                                                                                                                                                                                                                                                                                               |
| userEmail `String!`                                                                                                                                         | Email address of the user who performed the action                                        |                                                                                                                                                                                                                                                                                               |
| name `String`                                                                                                                                               | Name of the container or organization involved in the event                               |                                                                                                                                                                                                                                                                                               |
| appId `String`                                                                                                                                              | Unique identifier of the application associated with the container                        |                                                                                                                                                                                                                                                                                               |
| appName `String`                                                                                                                                            | Name of the application associated with the container                                     |                                                                                                                                                                                                                                                                                               |
| registry `String`                                                                                                                                           | Container registry information                                                            |                                                                                                                                                                                                                                                                                               |
| dockerfile `String`                                                                                                                                         | Path or content of the Dockerfile used                                                    |                                                                                                                                                                                                                                                                                               |
| connector `String`                                                                                                                                          | Name or identifier of the external service connector                                      |                                                                                                                                                                                                                                                                                               |
| credentialsType `String`                                                                                                                                    | Type of credentials used for authentication                                               |                                                                                                                                                                                                                                                                                               |
| credentialName `String`                                                                                                                                     | Name of the credential used for the connector                                             |                                                                                                                                                                                                                                                                                               |
| resourceCount `Float`                                                                                                                                       | Number of resources affected or monitored                                                 |                                                                                                                                                                                                                                                                                               |
| resources `[String!]`                                                                                                                                       | List of resource identifiers being monitored                                              |                                                                                                                                                                                                                                                                                               |
| branches [`[MultipliedBranchWithReason!]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/multiplied-branch-with-reason) | List of branches selected for scanning with their selection reasons                       | <p>branch <code>String!</code><br>reason <code>String!</code></p>                                                                                                                                                                                                                             |
| repoName `String`                                                                                                                                           | Name of the repository being scanned                                                      |                                                                                                                                                                                                                                                                                               |
| reposCount `Float`                                                                                                                                          | Total number of repositories affected                                                     |                                                                                                                                                                                                                                                                                               |
| hostUrl `String`                                                                                                                                            | URL of the external service or repository host                                            |                                                                                                                                                                                                                                                                                               |
| monitorAllResources `Boolean`                                                                                                                               | Whether all available resources are being monitored                                       |                                                                                                                                                                                                                                                                                               |
| scanId `String`                                                                                                                                             | Unique identifier of the security scan                                                    |                                                                                                                                                                                                                                                                                               |
| enabledConnectors `[String!]`                                                                                                                               | List of connectors enabled for the scan                                                   |                                                                                                                                                                                                                                                                                               |
| loginType `String`                                                                                                                                          | Authentication method used for login                                                      |                                                                                                                                                                                                                                                                                               |
| domain `String`                                                                                                                                             | Domain associated with the authentication or login event                                  |                                                                                                                                                                                                                                                                                               |
| memberEmail `String`                                                                                                                                        | Email address of the member involved in the event                                         |                                                                                                                                                                                                                                                                                               |
| disclaimerType `String`                                                                                                                                     | Type of disclaimer that was accepted                                                      |                                                                                                                                                                                                                                                                                               |
| memberRoles `[String!]`                                                                                                                                     | Roles assigned to the member                                                              |                                                                                                                                                                                                                                                                                               |
| memberScopes `String`                                                                                                                                       | Permission scopes granted to the member                                                   |                                                                                                                                                                                                                                                                                               |
| appNames `[String]`                                                                                                                                         | Names of applications involved in the event                                               |                                                                                                                                                                                                                                                                                               |
| businessPriority `Float`                                                                                                                                    | Business priority level assigned to the application                                       |                                                                                                                                                                                                                                                                                               |
| owners `[String!]`                                                                                                                                          | List of application owner identifiers                                                     |                                                                                                                                                                                                                                                                                               |
| ownersWithRoles [`[Owner!]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/owner)                                       | Detailed information about application owners including their roles                       | <p>owner <code>String</code><br>email <code>String</code><br>roles <code>\[String!]</code></p>                                                                                                                                                                                                |
| roles `[String!]`                                                                                                                                           | List of roles associated with the event                                                   |                                                                                                                                                                                                                                                                                               |
| generatedForOrg `Boolean`                                                                                                                                   | Indicates if the file was generated for the entire organization                           |                                                                                                                                                                                                                                                                                               |
| downloadFormat `String`                                                                                                                                     | Format of the downloaded file (e.g., JSON, CSV)                                           |                                                                                                                                                                                                                                                                                               |
| generatedFrom `String`                                                                                                                                      | Source or context from which the file was generated                                       |                                                                                                                                                                                                                                                                                               |
| comment `String`                                                                                                                                            | User-provided comment or explanation for the action                                       |                                                                                                                                                                                                                                                                                               |
| excluded `Boolean`                                                                                                                                          | Indicates if an issue was marked as a false positive                                      |                                                                                                                                                                                                                                                                                               |
| removed `Boolean`                                                                                                                                           | Indicates if a resolved issue was marked as incorrectly resolved                          |                                                                                                                                                                                                                                                                                               |
| issueName `String`                                                                                                                                          | Name or title of the security issue                                                       |                                                                                                                                                                                                                                                                                               |
| issueId `String`                                                                                                                                            | Unique identifier of the security issue                                                   |                                                                                                                                                                                                                                                                                               |
| profileId `String`                                                                                                                                          | Identifier of the security policy profile                                                 |                                                                                                                                                                                                                                                                                               |
| profileName `String`                                                                                                                                        | Name of the security policy profile                                                       |                                                                                                                                                                                                                                                                                               |
| activeProfile `Boolean`                                                                                                                                     | Indicates if this is the active security policy profile                                   |                                                                                                                                                                                                                                                                                               |
| settingsType `String`                                                                                                                                       | Type of system settings being modified                                                    |                                                                                                                                                                                                                                                                                               |
| disabled `Boolean`                                                                                                                                          | Indicates if the feature or setting is disabled                                           |                                                                                                                                                                                                                                                                                               |
| configured `Float`                                                                                                                                          | Configuration value or count                                                              |                                                                                                                                                                                                                                                                                               |
| textArr `String`                                                                                                                                            | Array of text values in string format                                                     |                                                                                                                                                                                                                                                                                               |
| policies [`[LogPolicy!]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/log-policy)                                     | List of security policies affected by the event                                           | <p>policyId <code>String</code><br>policyName <code>String</code><br>categoryName <code>String</code><br>enabled <code>Boolean</code><br>severity <code>String</code><br>oldIssues <code>String</code><br>newIssues <code>String</code><br>args <code>String</code></p>                       |
| slackUser `String`                                                                                                                                          | Slack username associated with the event                                                  |                                                                                                                                                                                                                                                                                               |
| channel `String`                                                                                                                                            | Slack channel where the notification was sent                                             |                                                                                                                                                                                                                                                                                               |
| key `String`                                                                                                                                                | Unique key or identifier in the external system                                           |                                                                                                                                                                                                                                                                                               |
| ticketId `String`                                                                                                                                           | Ticket identifier in the external ticketing system                                        |                                                                                                                                                                                                                                                                                               |
| ticketingVendor `String`                                                                                                                                    | Name of the ticketing system vendor (e.g., Jira, ServiceNow)                              |                                                                                                                                                                                                                                                                                               |
| messagingVendor `String`                                                                                                                                    | Name of the messaging system vendor                                                       |                                                                                                                                                                                                                                                                                               |
| user `String`                                                                                                                                               | Username in the external system                                                           |                                                                                                                                                                                                                                                                                               |
| link `String`                                                                                                                                               | URL or link to the external resource                                                      |                                                                                                                                                                                                                                                                                               |
| categoryName `String`                                                                                                                                       | Category name of the security issue or code fix                                           |                                                                                                                                                                                                                                                                                               |
| categoryId `Float`                                                                                                                                          | Numeric identifier of the issue category                                                  |                                                                                                                                                                                                                                                                                               |
| expiredAt `DateTime`                                                                                                                                        | Expiration date of the exclusion                                                          |                                                                                                                                                                                                                                                                                               |
| prId `String`                                                                                                                                               | Pull request identifier                                                                   |                                                                                                                                                                                                                                                                                               |
| prURL `String`                                                                                                                                              | URL of the pull request                                                                   |                                                                                                                                                                                                                                                                                               |
| sourceControlType `String`                                                                                                                                  | Type of source control system (e.g., GitHub, GitLab)                                      |                                                                                                                                                                                                                                                                                               |
| aggItems `String`                                                                                                                                           | Aggregated items in string format                                                         |                                                                                                                                                                                                                                                                                               |
| excludedIssues [`[ExcludedIssue!]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/excluded-issue)                       | List of issues excluded from security scanning                                            | <p>appNames <code>\[String!]</code><br>issueId <code>String!</code><br>issueName <code>String!</code><br>categoryName <code>String!</code><br>comment <code>String</code><br>expiredAt <code>String</code></p>                                                                                |
| fixTitle `String`                                                                                                                                           | Title of the applied fix                                                                  |                                                                                                                                                                                                                                                                                               |
| severity `String`                                                                                                                                           | Current severity level of the issue                                                       |                                                                                                                                                                                                                                                                                               |
| oldSeverity `String`                                                                                                                                        | Previous severity level of the issue                                                      |                                                                                                                                                                                                                                                                                               |
| newOwnerName `String`                                                                                                                                       | Name of the new issue owner                                                               |                                                                                                                                                                                                                                                                                               |
| newOwnerEmail `String`                                                                                                                                      | Email of the new issue owner                                                              |                                                                                                                                                                                                                                                                                               |
| oldOwnerName `String`                                                                                                                                       | Name of the previous issue owner                                                          |                                                                                                                                                                                                                                                                                               |
| oldOwnerEmail `String`                                                                                                                                      | Email of the previous issue owner                                                         |                                                                                                                                                                                                                                                                                               |
| tagsAdded `[String!]`                                                                                                                                       | Tags added to the application                                                             |                                                                                                                                                                                                                                                                                               |
| tagsRemoved `[String!]`                                                                                                                                     | Tags removed from the application                                                         |                                                                                                                                                                                                                                                                                               |
| workflowType `String`                                                                                                                                       | Type of the policy workflow                                                               |                                                                                                                                                                                                                                                                                               |
| workflowName `String`                                                                                                                                       | Name of the policy workflow                                                               |                                                                                                                                                                                                                                                                                               |
| nodeName `String`                                                                                                                                           | Name of the workflow node                                                                 |                                                                                                                                                                                                                                                                                               |
| nodeType `String`                                                                                                                                           | Type of the workflow node                                                                 |                                                                                                                                                                                                                                                                                               |
| workflowId `String`                                                                                                                                         | Unique identifier of the workflow                                                         |                                                                                                                                                                                                                                                                                               |
| description `String`                                                                                                                                        | Description of the workflow                                                               |                                                                                                                                                                                                                                                                                               |
| enabled `Boolean`                                                                                                                                           | Indicates if the workflow is enabled                                                      |                                                                                                                                                                                                                                                                                               |
| monitorAllNewlyCreatedRepositories `Float`                                                                                                                  | Number of newly created repositories to monitor                                           |                                                                                                                                                                                                                                                                                               |
| monitoredApps `[String!]`                                                                                                                                   | List of applications being monitored by the workflow                                      |                                                                                                                                                                                                                                                                                               |
| secretName `String`                                                                                                                                         | Name of the secret                                                                        |                                                                                                                                                                                                                                                                                               |
| filterName `String`                                                                                                                                         | Name of the saved filter                                                                  |                                                                                                                                                                                                                                                                                               |
| pageName `String`                                                                                                                                           | Page where the filter is applied                                                          |                                                                                                                                                                                                                                                                                               |
| apiKeyName `String`                                                                                                                                         | Name of the API key                                                                       |                                                                                                                                                                                                                                                                                               |
| apiKeyType `String`                                                                                                                                         | Type of the API key                                                                       |                                                                                                                                                                                                                                                                                               |
| createdBy `String`                                                                                                                                          | User who created the API key                                                              |                                                                                                                                                                                                                                                                                               |
| apiKeyCreatedAt `DateTime`                                                                                                                                  | Creation date of the API key                                                              |                                                                                                                                                                                                                                                                                               |
| apiKeyExpiredAt `DateTime`                                                                                                                                  | Expiration date of the API key                                                            |                                                                                                                                                                                                                                                                                               |
| orgUnitName `String`                                                                                                                                        | Name of the organization unit                                                             |                                                                                                                                                                                                                                                                                               |
| orgUnitId `ID`                                                                                                                                              | Unique identifier of the organization unit                                                |                                                                                                                                                                                                                                                                                               |
| tags `[String!]`                                                                                                                                            | Tags associated with the organization unit                                                |                                                                                                                                                                                                                                                                                               |
| pipelineSettingsV2 [`PipelineSettingsV2`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/pipeline-settings-v2)           | Enhanced CI/CD pipeline configuration settings                                            | <p>isDefaultSettings <code>Boolean!</code><br>isGithubConnected <code>Boolean</code><br>isBitbucketConnected <code>Boolean</code><br>isGitlabConnected <code>Boolean</code><br>apps <code>JSONObject</code><br>settings <code>JSONObject</code><br>branchSettings <code>JSONObject</code></p> |
| children `[ID!]`                                                                                                                                            | Child organization unit identifiers                                                       |                                                                                                                                                                                                                                                                                               |
| updateSlaSettings `String`                                                                                                                                  | Changes made to SLA settings                                                              |                                                                                                                                                                                                                                                                                               |
| irrelevantComment `String`                                                                                                                                  | Reason for marking an application as irrelevant                                           |                                                                                                                                                                                                                                                                                               |
| sla `Float`                                                                                                                                                 | SLA time value in hours                                                                   |                                                                                                                                                                                                                                                                                               |
| emailType `String`                                                                                                                                          | Type of email notification sent                                                           |                                                                                                                                                                                                                                                                                               |
| emailSubject `String`                                                                                                                                       | Subject line of the email notification                                                    |                                                                                                                                                                                                                                                                                               |
| triageStatus `String`                                                                                                                                       | Triage status of the issue                                                                |                                                                                                                                                                                                                                                                                               |
| actionType `String`                                                                                                                                         | Action type of the audit logs export                                                      |                                                                                                                                                                                                                                                                                               |
| changes `[String!]`                                                                                                                                         | Changes made to the audit logs export                                                     |                                                                                                                                                                                                                                                                                               |
| fileName `String`                                                                                                                                           | Imported File Name                                                                        |                                                                                                                                                                                                                                                                                               |
| fileType `String`                                                                                                                                           | Imported File Type                                                                        |                                                                                                                                                                                                                                                                                               |
| title `String`                                                                                                                                              | Title or name of the Agentic Pentest scanning target                                      |                                                                                                                                                                                                                                                                                               |
| domainType `String`                                                                                                                                         | Type or classification of the domain being scanned                                        |                                                                                                                                                                                                                                                                                               |
| targetUrl `String`                                                                                                                                          | URL of the target being scanned by Agentic Pentest                                        |                                                                                                                                                                                                                                                                                               |
| env `String`                                                                                                                                                | Environment classification of the target (e.g., production, staging, development)         |                                                                                                                                                                                                                                                                                               |
| authMethod `String`                                                                                                                                         | Authentication method used to access the Agentic Pentest target                           |                                                                                                                                                                                                                                                                                               |
| previousValues [`PreviousTargetValues`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/previous-target-values)           | Previous values of the target configuration before modification (used in Edit operations) | <p>title <code>String</code><br>domainType <code>String</code><br>targetUrl <code>String</code><br>env <code>String</code><br>authMethod <code>String</code></p>                                                                                                                              |
| branch `String`                                                                                                                                             | Name of the branch being scanned                                                          |                                                                                                                                                                                                                                                                                               |
| customRoleLogData [`customRoleLogData`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/custom-role-log-data)             | Custom Role details                                                                       | <p>name <code>String!</code><br>displayName <code>String!</code><br>assignablePermissions <a href="../types/objects/assignable-permission"><code>\[AssignablePermission!]</code></a></p>                                                                                                      |
