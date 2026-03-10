# Source: https://docs.aws.amazon.com/detective/latest/userguide/llms.txt

# Amazon Detective User Guide

> Detective makes it easy to analyze, investigate, and identify the root cause of security findings or suspicious activities. Detective uses machine learning to build a behavior graph.

- [What is Detective?](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html)
- [Concepts and terminology](https://docs.aws.amazon.com/detective/latest/userguide/detective-terms-concepts.html)
- [Summary dashboard](https://docs.aws.amazon.com/detective/latest/userguide/summary-page.html)
- [Searching for a finding or entity](https://docs.aws.amazon.com/detective/latest/userguide/detective-search.html)
- [Logging API calls](https://docs.aws.amazon.com/detective/latest/userguide/logging-using-cloudtrail.html)
- [Regions and quotas](https://docs.aws.amazon.com/detective/latest/userguide/regions-limitations.html)
- [Managing tags](https://docs.aws.amazon.com/detective/latest/userguide/graph-tags.html)
- [Disabling Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/detective-disabling.html)
- [Document history](https://docs.aws.amazon.com/detective/latest/userguide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/detective/latest/userguide/detective-setup.html)

- [Setting up](https://docs.aws.amazon.com/detective/latest/userguide/detective-before-you-begin.html): This topic describes preliminary steps, such as creating an AWS account, to prepare you to use Amazon Detective.
- [Prerequisites](https://docs.aws.amazon.com/detective/latest/userguide/detective-prerequisites.html): This topic lists the prerequisites to enable Detective
- [Recommendations](https://docs.aws.amazon.com/detective/latest/userguide/detective-recommendations.html): This topic lists the recommendations to enable Detective
- [Enabling Detective](https://docs.aws.amazon.com/detective/latest/userguide/detective-enabling.html): Use the Amazon Detective console, Detective API, or the command line to enable Detective in a Region.


## [Data in a behavior graph](https://docs.aws.amazon.com/detective/latest/userguide/behavior-graph-data-about.html)

- [How Detective populates a behavior graph](https://docs.aws.amazon.com/detective/latest/userguide/behavior-graph-population-about.html): Discover how Amazon Detective, using a combination of extraction and analytics, uses log data and findings for member accounts to populate the behavior graph.
- [Training period for new behavior graphs](https://docs.aws.amazon.com/detective/latest/userguide/detective-data-training-period.html): Learn how Amazon Detective establishes baselines for new behavior graphs.
- [Overview of the behavior graph data structure](https://docs.aws.amazon.com/detective/latest/userguide/graph-data-structure-overview.html): Learn about the behavior graph structure.

### [Source data used in a behavior graph](https://docs.aws.amazon.com/detective/latest/userguide/detective-source-data-about.html)

Learn how Amazon Detective identifies, ingests, and stores the source data used in a behavior graph.

- [Amazon EKS audit logs](https://docs.aws.amazon.com/detective/latest/userguide/source-data-types-EKS.html): Learn about the benefits of enabling Amazon EKS audit logs as an optional data source package in Detective.
- [AWS security findings](https://docs.aws.amazon.com/detective/latest/userguide/source-data-types-asff.html): Learn about the benefits of enabling AWS security findings as an optional data source package in Detective.


## [How Detective is used for investigation](https://docs.aws.amazon.com/detective/latest/userguide/detective-investigation-about.html)

### [Detective Investigation](https://docs.aws.amazon.com/detective/latest/userguide/investigations-about.html)

You can use Amazon Detective Investigation to investigate IAM users and IAM roles using indicators of compromise, which can help you determine if a resource is involved in a security incident.

- [Running a Detective Investigation](https://docs.aws.amazon.com/detective/latest/userguide/run-investigations.html): Use Run investigation to analyze resources such as IAM users and IAM roles and to generate an investigation report.
- [Reviewing Detective Investigations reports](https://docs.aws.amazon.com/detective/latest/userguide/investigations-report.html): Investigations reports lets you review the generated Reports for investigations that you have run previously in Detective.
- [Understanding a Detective Investigations report](https://docs.aws.amazon.com/detective/latest/userguide/investigations-report-understand.html): A Detective Investigations report lists a summary of the uncommon behavior or malicious activity that indicates compromise.
- [Detective Investigations report summary](https://docs.aws.amazon.com/detective/latest/userguide/investigations-summary.html): Investigations summary highlights anomalous indicators that require attention, for the selected scope time.
- [Downloading a Detective Investigations report](https://docs.aws.amazon.com/detective/latest/userguide/download-investigation.html): You can download the Detective Investigations report in JSON format, to analyze it further or store it to your preferred storage solution such as an Amazon S3 bucket.
- [Archiving a Detective Investigations report](https://docs.aws.amazon.com/detective/latest/userguide/archive-investigation.html): When you complete your investigation in Amazon Detective, you can Archive the investigation report.


## [Analyzing findings](https://docs.aws.amazon.com/detective/latest/userguide/analyzing-findings.html)

- [Finding overview](https://docs.aws.amazon.com/detective/latest/userguide/finding-overview.html): Learn about Detective finding overviews, which contain finding details and links to involved entities.

### [Finding groups](https://docs.aws.amazon.com/detective/latest/userguide/groups-about.html)

Learn about finding groups, which are collections of related findings, entities, and evidence that are correlated to the same underlying activity or security issue.

- [Understanding the finding groups page](https://docs.aws.amazon.com/detective/latest/userguide/understanding-groups.html): Detective finding groups are collections of correlated related findings and entities.
- [Informational findings in finding groups](https://docs.aws.amazon.com/detective/latest/userguide/group-evidence.html): Amazon Detective identifies additional information related to a finding group based on data in your behavior graph collected within the last 45 days.
- [Finding group profiles](https://docs.aws.amazon.com/detective/latest/userguide/group-profile.html): When you select a group title, a finding group profile opens with additional details about that group.
- [Finding group visualization](https://docs.aws.amazon.com/detective/latest/userguide/group-visual-finding-group.html): View and interact with the entities and findings included in a finding group.
- [Finding group summary](https://docs.aws.amazon.com/detective/latest/userguide/finding-group-summary.html): Learn about finding groups, which are collections of related findings, entities, and evidence that are correlated to the same underlying activity or security issue.
- [Archiving a GuardDuty finding](https://docs.aws.amazon.com/detective/latest/userguide/finding-update-status.html): Use Amazon Detective to archive an Amazon GuardDuty finding.


## [Analyzing entities](https://docs.aws.amazon.com/detective/latest/userguide/entity-profiles.html)

- [Using entity profiles](https://docs.aws.amazon.com/detective/latest/userguide/using-entity-profiles.html): An entity profile appears when you perform one of the following actions:

### [Profile panels](https://docs.aws.amazon.com/detective/latest/userguide/profile-panels.html)

Find out about profile panels, the information they display, and how to use them.

- [Types of profile panel visualizations](https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-display-types.html): The content of a Detective profile panel shows a visualization of findings and entities in various formats.
- [Preferences for profile panels](https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-preferences.html): Customize the number of rows that appear on each page on profile panel tables and the timeâ¨ preferences.
- [Navigating to an entity profile](https://docs.aws.amazon.com/detective/latest/userguide/navigate-to-profile.html): Navigate directly to an Amazon Detective entity profile or a finding overview.
- [Pivoting to another console](https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-console-links.html): Navigate from a Detective profile panel to another console to gather additional input for your security investigation.

### [Exploring activity details](https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-drilldown.html)

Use Detective to investigate pattern of related activity.

- [Overall API call volume](https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-drilldown-overall-api-volume.html): Explore details about the API activity during a selected time interval on the Overall API call volume profile panel.
- [Geolocations](https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-drilldown-new-geolocations.html): Explore details about the API activity for a selected geolocation during the scope time.
- [Overall VPC flow volume](https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-drilldown-overall-vpc-volume.html): Explore details about inbound and outbound IP address traffic using VPC flow volume.
- [Overall Kubernetes API call volume](https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-drilldown-kubernetes-api-volume.html): Explore details about the Kubernetes API activity during a selected time interval on the Overall Kubernetes API call volume profile panel using Detective.
- [Managing the scope time](https://docs.aws.amazon.com/detective/latest/userguide/scope-time-managing.html): Customize the scope time used to limit the data displayed on entity profiles.
- [Viewing findings for an entity](https://docs.aws.amazon.com/detective/latest/userguide/entity-finding-list.html): Learn how the associated Detective findings profile panel displays a list of findings that were involved in an entity.
- [High-volume entities](https://docs.aws.amazon.com/detective/latest/userguide/high-volume-entities.html): Learn how Amazon Detective indicates that an entity has too many connections to or from other entities.


## [Managing accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts.html)

- [Restrictions and recommendations](https://docs.aws.amazon.com/detective/latest/userguide/accounts-restrictions-recommendations.html): Review some restrictions on behavior graph accounts in Detective.
- [Using Organizations to manage behavior graph accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-orgs-transition.html): Transition an existing behavior graph into your organization behavior graph.

### [Designating the Detective administrator account](https://docs.aws.amazon.com/detective/latest/userguide/accounts-designate-admin.html)

Learn how the organization management account chooses the Detective administrator account for an organization.

- [Designating a Detective administrator](https://docs.aws.amazon.com/detective/latest/userguide/accounts-designate-admin-console.html): The organization management account can use the Detective console to designate the Detective administrator account.
- [Removing the Detective administrator account](https://docs.aws.amazon.com/detective/latest/userguide/accounts-remove-admin-overview.html): The organization management account can remove the current Detective administrator account in a Region.
- [Available actions for accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-allowed-actions.html): Learn more about the available actions for administrator accounts and member accounts in Amazon Detective.
- [Viewing the list of accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-view-list.html): Use the Amazon Detective console or API to retrieve information about the accounts in a behavior graph.

### [Managing organization member accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-orgs-members.html)

Manage the membership of organization accounts in the Detective organization behavior graph.

- [Enabling new organization accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-orgs-members-autoenable.html): Automatically enable new organization accounts as member accounts in the organization behavior graph.
- [Enabling organization accounts as Detective member accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-orgs-members-enable.html): Manually enable organization accounts as member accounts in the organization behavior graph.
- [Disassociating organization accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-orgs-members-disassociate.html): Disassociate an organization account from the organization behavior graph

### [Managing invited member accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-invited-members.html)

Use the Amazon Detective console and API to invite and manage invited member accounts in your behavior graph.

- [Inviting individual accounts to a behavior graph](https://docs.aws.amazon.com/detective/latest/userguide/accounts-invited-members-add-individual.html): You can manually specify the member accounts to invite to contribute their data to a behavior graph.
- [Inviting a list of member accounts to a behavior graph](https://docs.aws.amazon.com/detective/latest/userguide/accounts-invited-members-add-csv.html): From the Detective console, you can provide a .csv file containing a list of member accounts to invite to your behavior graph.
- [Enabling a member account that is Not enabled](https://docs.aws.amazon.com/detective/latest/userguide/graph-admin-unblock-account.html): Manually enable accounts that cannot be enabled automatically.
- [Removing member accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts-invited-remove.html): Use the Amazon Detective console or API to remove invited member accounts from a behavior graph.

### [For member accounts: Managing invitations and memberships](https://docs.aws.amazon.com/detective/latest/userguide/member-account-graph-management.html)

Control your membership in behavior graphs.

- [IAM policy for a member account](https://docs.aws.amazon.com/detective/latest/userguide/member-account-iam-policy.html): Learn about the required IAM policy for member accounts in a behavior graph.
- [Viewing behavior graph invitations](https://docs.aws.amazon.com/detective/latest/userguide/member-view-graph-invitations.html): Use the Amazon Detective console, API, or command line to see your pending and accepted behavior graph invitations.
- [Responding to a behavior graph invitation](https://docs.aws.amazon.com/detective/latest/userguide/member-invitation-response.html): Use the Amazon Detective console or API to accept or decline a behavior graph invitation.
- [Removing your account from a behavior graph](https://docs.aws.amazon.com/detective/latest/userguide/member-remove-self-from-graph.html): Use the Amazon Detective console, Detective API, or AWS CLI to remove your account from a behavior graph.
- [Effect of account actions](https://docs.aws.amazon.com/detective/latest/userguide/accounts-effects.html): Learn how changes to accounts affect data in Amazon Detective.
- [Amazon Detective Python scripts](https://docs.aws.amazon.com/detective/latest/userguide/detective-github-scripts.html): Use the open source scripts provided by Amazon Detective to enable Detective, add and remove member accounts, and disable Detective.


## [Detective Integration with Security Lake](https://docs.aws.amazon.com/detective/latest/userguide/securitylake-integration.html)

### [Enabling the integration](https://docs.aws.amazon.com/detective/latest/userguide/integrating-securitylake-tutorial.html)

To integrate Detective with Security Lake, you must complete the following steps.

- [Before you begin](https://docs.aws.amazon.com/detective/latest/userguide/Prerequisites.html): This topic describes the preliminary steps such as delegating a Security Lake administrator for your organization, enabling Security Lake for your Detective administrator account, and verifying that Security Lake is collecting logs and events.
- [Step 1: Creating a Security Lake subscriber in Detective](https://docs.aws.amazon.com/detective/latest/userguide/securitylake-subscriber.html): Learn how to create a Security Lake subscriber.
- [Step 2: Adding the required IAM permissions](https://docs.aws.amazon.com/detective/latest/userguide/iam-permissions.html): Add the required IAM permissions to enable Detective integration with Security Lake.
- [Step 3: Accepting the Resource Share ARN invitation](https://docs.aws.amazon.com/detective/latest/userguide/resource-share-arn.html): Learn how to accept the Resource Share ARN invitation using a AWS CloudFormation template, which is a required step before you enable Detective integration with Security Lake.
- [Changing the Detective integration configuration](https://docs.aws.amazon.com/detective/latest/userguide/edit-integration.html): Learn how to change the integration configuration for Detective integration with Security Lake.
- [Supported AWS Regions](https://docs.aws.amazon.com/detective/latest/userguide/supported-regions.html): Learn in what AWS Regions you can integrate Detective with Security Lake.
- [Querying raw logs in Detective](https://docs.aws.amazon.com/detective/latest/userguide/query-raw-logs-detective.html): Learn how to query raw logs in Detective after integration with Security Lake related to CloudTrail management events and Amazon VPC Flow Logs.
- [Disabling the integration](https://docs.aws.amazon.com/detective/latest/userguide/disable-integration.html): Learn how to disable Detective integration with Security Lake.


## [Forecasting and monitoring costs](https://docs.aws.amazon.com/detective/latest/userguide/tracking-usage-logging.html)

- [About the free trial for behavior graphs](https://docs.aws.amazon.com/detective/latest/userguide/free-trial-overview.html): The Amazon Detective 30-day free trial starts the first time an administrator account enables Detective in a Region or when a member account is enabled for a behavior graph.
- [Administrator account usage and cost](https://docs.aws.amazon.com/detective/latest/userguide/usage-tracking-admin.html): Track the volume of data ingested into your behavior graph from each account and see a projected 30-day cost for your account and for the behavior graph.
- [Member account usage tracking](https://docs.aws.amazon.com/detective/latest/userguide/member-usage-tracking.html): Track the volume of data ingested into each behavior graph for a member account and see the projected cost for that account.
- [How Detective calculates projected cost](https://docs.aws.amazon.com/detective/latest/userguide/usage-projected-cost-calculation.html): Learn how Amazon Detective calculates the projected cost values displayed on the Usage page.


## [Security](https://docs.aws.amazon.com/detective/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/detective/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Detective.

- [Key management](https://docs.aws.amazon.com/detective/latest/userguide/key-management.html): Learn how Amazon Detective uses AWS KMS.

### [Identity and access management](https://docs.aws.amazon.com/detective/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your Detective resources.

- [How Amazon Detective works with IAM](https://docs.aws.amazon.com/detective/latest/userguide/security_iam_service-with-iam.html): By default, users and roles don't have permission to create or modify Amazon Detective resources.
- [Identity-based policy examples](https://docs.aws.amazon.com/detective/latest/userguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify Detective resources.
- [AWS managed policies](https://docs.aws.amazon.com/detective/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Detective and recent changes to these policies.
- [Using service-linked roles](https://docs.aws.amazon.com/detective/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give Detective access to resources in your AWS account.
- [Troubleshooting identity and access](https://docs.aws.amazon.com/detective/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Detective and IAM.
- [Compliance validation](https://docs.aws.amazon.com/detective/latest/userguide/detective-compliance.html): Learn about Detective compliance programs and what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/detective/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Detective features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/detective/latest/userguide/infrastructure-security.html): Learn how Amazon Detective isolates service traffic.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/detective/latest/userguide/detective-security-vpc-endpoints-privatelink.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Detective without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Security best practices](https://docs.aws.amazon.com/detective/latest/userguide/security-best-practices.html): Learn about the recommended security best practices for using Detective.
