# Source: https://docs.aws.amazon.com/awssupport/latest/user/llms.txt

# AWS Support User Guide

> Describes AWS Support, a one-on-one, fast-response support channel that is staffed with experienced support personnel. This guide explains the components and features that AWS Support provides and how to use them. Also shows you how to access AWS Support through a web-based UI, command-line tools, and the AWS Support API.

- [About the AWS Support API](https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html)
- [Troubleshooting resources](https://docs.aws.amazon.com/awssupport/latest/user/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/awssupport/latest/user/History.html)

## [Get started with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html)

### [AI-enhanced troubleshooting in Support Center Console](https://docs.aws.amazon.com/awssupport/latest/user/ai-enhanced-support.html)

AI-enhanced troubleshooting with AWS Support to get help with AWS.

### [Set up permissions to use AI-enhanced troubleshooting](https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-perm.html)

To access AI-enhanced troubleshooting capabilities in Support Center, you need specific AWS Identity and Access Management permissions.

- [Option 1: Use the AWS managed policy (recommended)](https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-perm-man-policy.html): If you currently have the AWSSupportAccess managed policy attached, no additional permissions are required.
- [Option 2: Create a custom policy with minimum required permissions](https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-perm-custom-policy.html): You can explicitly allow-list specific actions instead of using wildcards.
- [Required permissions for Amazon Q integration](https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-perm-q-required-perm.html): To use the Amazon Q conversation import feature in Support Center, IAM identities need permissions for the following Amazon Q Developer actions:
- [Applying required permissions for support interactions](https://docs.aws.amazon.com/awssupport/latest/user/support-interaction-apply-permissions.html): To apply permissions to your IAM users, complete the following steps:
- [Create a support interaction](https://docs.aws.amazon.com/awssupport/latest/user/create-support-interaction.html): A support interaction is how you begin your engagement with AWS Support.
- [Create a support case from a support interaction](https://docs.aws.amazon.com/awssupport/latest/user/create-support-case-from-interaction.html): When you select Create case during your support interaction, a support case is created for you with many of the case details, such as the Subject, Description, Case type Service, Category, and Severity level populated for you.
- [View support interactions](https://docs.aws.amazon.com/awssupport/latest/user/view-support-interactions.html): Past interactions with AWS Support are saved for 10 years.
- [Troubleshooting](https://docs.aws.amazon.com/awssupport/latest/user/troubleshooting-support-cases.html): Find common ways to troubleshoot your cases in Support Center.
- [Virtual meetings with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/virtual-meetings-support.html): Learn about how to join a virtual meeting and screenshare with an AWS Supportengineer directly from the Support Center console.
- [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html): Manage support cases AWS Support to get help with AWS.
- [Request a service quota increase](https://docs.aws.amazon.com/awssupport/latest/user/create-service-quota-increase.html): Request a service quota increase for your AWS account to use with your AWS services.

### [Legacy method: Create support cases and case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management-legacy.html)

Create cases in AWS Support to get help with AWS.

- [Example: Create a support case for account and billing](https://docs.aws.amazon.com/awssupport/latest/user/case-example.html): See the following example for creating a support case for an AWS account issue.
- [Legacy experience: Update, resolve, and reopen your cases](https://docs.aws.amazon.com/awssupport/latest/user/monitoring-your-case.html): Maintain your Support case to receive updates and changes.
- [Working with AWS SDKs](https://docs.aws.amazon.com/awssupport/latest/user/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [About the Support Center Console API](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-console.html)

- [Adding IAM policies for the Support Center Console API operations](https://docs.aws.amazon.com/awssupport/latest/user/support-console-access-control.html): Onboard the Support Center Console API by using the AWS Identity and Access Management console to add IAM policies.
- [Testing Support Center Console API calls](https://docs.aws.amazon.com/awssupport/latest/user/support-console-access-control-test.html): Test the Support Center Console API calls using Amazon CloudWatch.


## [AWS Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html)

### [What is AWS Unified Operations](https://docs.aws.amazon.com/awssupport/latest/user/unified-operations-intro.html)

Learn about the AWS Unified Operations Support plan

- [Benefits of Unified Operations](https://docs.aws.amazon.com/awssupport/latest/user/unified-operations-benefits.html): Unified Operations offers several key benefits.
- [Unified Operations Team](https://docs.aws.amazon.com/awssupport/latest/user/unified-operations-team.html): AWS Unified Operations brings together a designated team of specialized experts who work together to support your cloud journey.

### [Unified Operations life cycle](https://docs.aws.amazon.com/awssupport/latest/user/unified-operations-phases.html)

Learn about the Unified Operations Support plan life cycle, from pre-onboarding through continuous improvement

- [Pre-onboarding](https://docs.aws.amazon.com/awssupport/latest/user/uops-pre-onboarding.html): Learn about the pre-onboarding stage for Unified Operations
- [Unified Operations onboarding](https://docs.aws.amazon.com/awssupport/latest/user/uops-onboarding.html): Onboarding kickoff
- [Pre-event or migration planning](https://docs.aws.amazon.com/awssupport/latest/user/uops-pre-event-planning.html): Pre-event or migration planning in AWS Unified Operations includes the following key elements.
- [Event migration or cutover](https://docs.aws.amazon.com/awssupport/latest/user/uops-event-migration-cutover.html): Event migration or cutover in Unified Operations includes the following key elements.
- [Post Go-live or event](https://docs.aws.amazon.com/awssupport/latest/user/uops-event-post-golive.html): The post go-live or post event process in Unified Operations includes the following key elements:
- [Workload incident management](https://docs.aws.amazon.com/awssupport/latest/user/uops-workload-inc-management.html): Workload incident management includes the following key elements:
- [Post incident](https://docs.aws.amazon.com/awssupport/latest/user/uops-post-incident.html): Post-incident analysis for critical incidents is conducted by the assigned Domain Specialist Engineer (DSE).
- [Continuous improvement](https://docs.aws.amazon.com/awssupport/latest/user/uops-continuous-improvement.html): Continuous improvement includes the following key elements:

### [Getting started with Unified Operations](https://docs.aws.amazon.com/awssupport/latest/user/unified-operations-getting-started.html)

Learn how to get started with the Unified Operations Support plan

- [Prerequisites](https://docs.aws.amazon.com/awssupport/latest/user/uops-gs-prerequisites.html): Learn about the Prerequisites for Unified Operations
- [Onboard critical alarms to rapid incident management](https://docs.aws.amazon.com/awssupport/latest/user/uops-gs-onboard-alarms.html): To help quickly notify you of critical incidents, complete the following steps to onboard your alarms to AWS Incident Detection and Response
- [Request 5-minute incident response](https://docs.aws.amazon.com/awssupport/latest/user/uo-gs-incident-response.html): AWS Unified Operations offers 5-minute incident response for your critical incidents.
- [Plan for domain coverage](https://docs.aws.amazon.com/awssupport/latest/user/uo-gs-domain-coverage.html): AWS Unified Operations provides specialized expertise through a domain-based coverage approach.
- [Onboard your account to proactive security incident management](https://docs.aws.amazon.com/awssupport/latest/user/uops-gs-proactive-sec-man.html): Unified Operations entitles you to AWS Security Incident Response to help you quickly prepare for, respond to, and recover from security incidents, such as account takeovers, data breaches, and ransomware attacks.
- [AWS expectations from you](https://docs.aws.amazon.com/awssupport/latest/user/uops-gs-expectations-customers.html): For Unified Operations to deliver maximum value, we recommend the following collaborative approach:
- [What you can expect from AWS](https://docs.aws.amazon.com/awssupport/latest/user/uops-gs-aws-expectations.html): When you onboard to Unified Operations, you can expect the following from AWS.
- [Change AWS Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/changing-support-plans.html): Use the AWS Support Plans console to change your AWS support plan.
- [Configure promotional plan expiration notifications](https://docs.aws.amazon.com/awssupport/latest/user/configure-promo-plan-notifications.html): Configure User notifications to learn when your promotional plan is nearing expiration.
- [Developer, Business, and Enterprise On-Ramp end of support](https://docs.aws.amazon.com/awssupport/latest/user/support-plans-eos.html): Information regarding the end of support for the existing Developer and Business AWS Support plans.


## [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)

- [Get started with Trusted Advisor Recommendations](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html): Use the AWS Trusted Advisor console to review checks for your AWS account.
- [Get started with the Trusted Advisor API](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor-api.html): Use the AWS Trusted Advisor console to review checks for your AWS account.
- [Using Trusted Advisor as a web service](https://docs.aws.amazon.com/awssupport/latest/user/trustedadvisor.html): Write applications that interact with AWS Trusted Advisor to get a list of Trusted Advisor checks and obtain the detailed results for a check.

### [Organizational view for AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/organizational-view.html)

Create reports for AWS Trusted Advisor checks for all accounts in AWS Organizations.

- [Using IAM policies to allow access to organizational view](https://docs.aws.amazon.com/awssupport/latest/user/organizational-view-iam-policies.html): Add IAM policies to your users to grant them permission to the AWS Trusted Advisor organizational view feature.
- [Using other AWS services to view Trusted Advisor reports](https://docs.aws.amazon.com/awssupport/latest/user/use-other-aws-services-with-trusted-advisor-reports.html): Import your AWS Trusted Advisor check results to Amazon Athena and Quick.
- [View Trusted Advisor checks powered by AWS Config](https://docs.aws.amazon.com/awssupport/latest/user/aws-config-integration-with-ta.html): View checks powered by AWS Config in the Trusted Advisor console.
- [View your Security Hub CSPM controls in Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/security-hub-controls-with-trusted-advisor.html): Enable AWS Security Hub CSPM in your AWS account so that you can view your Security Hub CSPM findings in the Trusted Advisor console.
- [Opt in AWS Compute Optimizer for Trusted Advisor checks](https://docs.aws.amazon.com/awssupport/latest/user/compute-optimizer-with-trusted-advisor.html): Opt-in your AWS account with Compute Optimizer to get Trusted Advisor checks for your Amazon EBS volumes and AWS Lambda functions.
- [Get started with AWS Trusted Advisor Priority](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-priority.html): You can use Trusted Advisor Priority to view critical recommendations that your technical account management team identified for your AWS account.

### [Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html)

You can use the following Trusted Advisor checks to monitor your services and operations for your AWS account.

- [Cost optimization](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html): View the available cost optimization checks from AWS Trusted Advisor to help save you money.
- [Performance](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html): View the available performance checks from AWS Trusted Advisor to help optimize your resources and services.
- [Security](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html): View the available security checks from AWS Trusted Advisor to help secure your account.
- [Fault tolerance](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html): View the available fault tolerance checks from AWS Trusted Advisor to help optimize your applications and prevent issues.
- [Service limits](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html): View the available service limit checks from AWS Trusted Advisor to determine if you're exceeding any quotas.
- [Operational Excellence](https://docs.aws.amazon.com/awssupport/latest/user/operational-excellence-checks.html): View the available operational excellence checks from AWS Trusted Advisor to help secure your account.
- [Change log for AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/aws-trusted-advisor-change-log.html): Learn more about changes to checks and check categories for Trusted Advisor.


## [AWS Support App in Slack](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html)

### [Prerequisites](https://docs.aws.amazon.com/awssupport/latest/user/prerequisites-support-app-for-slack.html)

Follow the requirements to use the AWS Support App for your AWS account.

- [Manage access to the AWS Support App widget](https://docs.aws.amazon.com/awssupport/latest/user/slack-authorization-permissions.html): Use the following IAM policy so that users can add a Slack workspace to your AWS account.
- [Manage access to the AWS Support App](https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html): Learn about the required AWS permissions for the AWS Support App in Slack.
- [Authorize a Slack workspace](https://docs.aws.amazon.com/awssupport/latest/user/authorize-slack-workspace.html): Authorize your Slack workspace to use the AWS Support App.
- [Configure a Slack channel](https://docs.aws.amazon.com/awssupport/latest/user/add-your-slack-channel.html): Configure your Slack channel to the AWS Support App.
- [Create support cases in Slack](https://docs.aws.amazon.com/awssupport/latest/user/create-case-in-slack.html): Use the AWS Support App to create support cases in Slack.
- [Reply to support cases in Slack](https://docs.aws.amazon.com/awssupport/latest/user/replying-to-support-cases-in-slack.html): Use the AWS Support App to reply to your support cases in Slack.
- [Join a live chat session with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/joining-a-live-chat-session.html): Join a live chat session in Slack so that you can work with a AWS Support agent to resolve your support case.
- [Search for support cases in Slack](https://docs.aws.amazon.com/awssupport/latest/user/search-case.html): Use the AWS Support App to search for cases in the Slack channel.
- [Resolve support cases in Slack](https://docs.aws.amazon.com/awssupport/latest/user/resolve-support-cases.html): Use the AWS Support App to resolve a case in Slack.
- [Reopen support cases in Slack](https://docs.aws.amazon.com/awssupport/latest/user/reopen-a-support-case.html): You can reopen an AWS Support case in a Slack channel to add correspondences and attachments if the issue isn't resolved.
- [Delete a Slack channel configuration from the AWS Support App](https://docs.aws.amazon.com/awssupport/latest/user/delete-a-channel.html): Delete a Slack channel from the AWS Support App page.
- [Delete a Slack workspace configuration from the AWS Support App](https://docs.aws.amazon.com/awssupport/latest/user/delete-a-workspace.html): Delete a Slack workspace configuration from the AWS Support Center Console.
- [AWS Support App in Slack commands](https://docs.aws.amazon.com/awssupport/latest/user/support-app-commands.html): Use the following command line reference for the AWS Support App.
- [View AWS Support App correspondences in the AWS Support Center Console](https://docs.aws.amazon.com/awssupport/latest/user/view-slack-updates-in-support-center.html): View correspondences from Slack in the AWS Support Center Console.
- [Create AWS CloudFormation resources for the AWS Support App in Slack](https://docs.aws.amazon.com/awssupport/latest/user/creating-resources-with-cloudformation.html): Create resources for AWS Support App in Slack using an AWS CloudFormation template.


## [Security](https://docs.aws.amazon.com/awssupport/latest/user/security.html)

- [Data protection](https://docs.aws.amazon.com/awssupport/latest/user/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Support.
- [Security for support cases](https://docs.aws.amazon.com/awssupport/latest/user/security-for-support-cases.html): Learn how AWS keeps your AWS Support cases secure .

### [Identity and access management](https://docs.aws.amazon.com/awssupport/latest/user/security-iam.html)

How to authenticate requests and manage access your Support resources.

- [How AWS Support works with IAM](https://docs.aws.amazon.com/awssupport/latest/user/security_iam_service-with-iam.html): Use IAM users, policies, and roles to manage access AWS Support.
- [Identity-based policy examples](https://docs.aws.amazon.com/awssupport/latest/user/security_iam_id-based-policy-examples.html): Use AWS Support identity-based policies to allow or restrict access to the AWS Support Center page or the API operations.

### [Using service-linked roles](https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-intro.html)

Use the built-in service-linked role to manage your interaction with AWS Support and Trusted Advisor.

- [Using service-linked roles for AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-sup.html): Use the built-in service-linked role to manage your interaction with AWS Support.
- [Using service-linked roles for Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/using-service-linked-roles-ta.html): Use service-linked roles to give AWS Trusted Advisor access to resources in your AWS account.

### [AWS managed policies](https://docs.aws.amazon.com/awssupport/latest/user/security-iam-awsmanpol.html)

Learn about AWS managed policies for AWS Support, AWS Support Plans Trusted Advisor, and recent changes to those policies.

### [AWS managed policies for AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/aws-managed-policies-aws-support.html)

Learn about AWS managed policies for AWS Support and recent changes to those policies.

- [Permission changes for AWSSupportServiceRolePolicy](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-service-link-role-updates.html): Learn more about detailed changes to the service-linked role for AWS Support.
- [AWS managed policies for AWS Support App in Slack](https://docs.aws.amazon.com/awssupport/latest/user/support-app-managed-policies.html): Learn about AWS managed policies for AWS Support App and recent changes to those policies.
- [AWS managed policies for AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/aws-managed-policies-for-trusted-advisor.html): Learn about AWS managed policies for Trusted Advisor and recent changes to those policies.
- [AWS managed policies for AWS Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/managed-policies-aws-support-plans.html): Learn about AWS managed policies for AWS Support Plans and recent changes to those policies.
- [AWS managed policies for AWS Partner-Led Support](https://docs.aws.amazon.com/awssupport/latest/user/managed-policies-partner-led-support.html): Learn about AWS managed policies for AWS Partner-Led Support and recent changes to those policies.
- [Manage access to AWS Support Center](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html): Create IAM users and attach policies to access Support and create cases.
- [Manage access to AWS Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html): Grant IAM users permission to view and change the support plan for your AWS account.
- [Manage access to AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/security-trusted-advisor.html): Authenticate requests and manage access for your AWS Trusted Advisor resources.
- [Example Service Control Policies for AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/example-scps-for-aws-trusted-advisor.html): You can use Service Control Policies to manage access to AWS Trusted Advisor features.
- [Troubleshooting](https://docs.aws.amazon.com/awssupport/latest/user/security_iam_troubleshoot.html): Identify and fix common issues for working with AWS Support and IAM.
- [Incident response](https://docs.aws.amazon.com/awssupport/latest/user/incident-response.html): Learn about how Support responds to events that might affect your account.
- [Logging and monitoring in AWS Support and AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/monitoring-security.html): Monitor and log AWS Support and AWS Trusted Advisor events that occur in your AWS account.
- [Compliance validation](https://docs.aws.amazon.com/awssupport/latest/user/support-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/awssupport/latest/user/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Support features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/awssupport/latest/user/infrastructure-security.html): Learn how AWS Support isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/awssupport/latest/user/vulnerability-analysis-and-management.html): Learn how the AWS shared responsibility model applies to vulnerability analysis and management in Support.


## [Code examples](https://docs.aws.amazon.com/awssupport/latest/user/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/awssupport/latest/user/service_code_examples_basics.html)

The following code examples show how to use the basics of Support with AWS SDKs.

- [Hello Support](https://docs.aws.amazon.com/awssupport/latest/user/example_support_Hello_section.html): Hello Support
- [Learn the basics](https://docs.aws.amazon.com/awssupport/latest/user/example_support_Scenario_GetStartedSupportCases_section.html): Learn the basics of Support with an AWS SDK

### [Actions](https://docs.aws.amazon.com/awssupport/latest/user/service_code_examples_actions.html)

The following code examples show how to use Support with AWS SDKs.

- [AddAttachmentsToSet](https://docs.aws.amazon.com/awssupport/latest/user/example_support_AddAttachmentsToSet_section.html): Use AddAttachmentsToSet with an AWS SDK or CLI
- [AddCommunicationToCase](https://docs.aws.amazon.com/awssupport/latest/user/example_support_AddCommunicationToCase_section.html): Use AddCommunicationToCase with an AWS SDK or CLI
- [CreateCase](https://docs.aws.amazon.com/awssupport/latest/user/example_support_CreateCase_section.html): Use CreateCase with an AWS SDK or CLI
- [DescribeAttachment](https://docs.aws.amazon.com/awssupport/latest/user/example_support_DescribeAttachment_section.html): Use DescribeAttachment with an AWS SDK or CLI
- [DescribeCases](https://docs.aws.amazon.com/awssupport/latest/user/example_support_DescribeCases_section.html): Use DescribeCases with an AWS SDK or CLI
- [DescribeCommunications](https://docs.aws.amazon.com/awssupport/latest/user/example_support_DescribeCommunications_section.html): Use DescribeCommunications with an AWS SDK or CLI
- [DescribeServices](https://docs.aws.amazon.com/awssupport/latest/user/example_support_DescribeServices_section.html): Use DescribeServices with an AWS SDK or CLI
- [DescribeSeverityLevels](https://docs.aws.amazon.com/awssupport/latest/user/example_support_DescribeSeverityLevels_section.html): Use DescribeSeverityLevels with an AWS SDK or CLI
- [DescribeTrustedAdvisorCheckRefreshStatuses](https://docs.aws.amazon.com/awssupport/latest/user/example_support_DescribeTrustedAdvisorCheckRefreshStatuses_section.html): Use DescribeTrustedAdvisorCheckRefreshStatuses with a CLI
- [DescribeTrustedAdvisorCheckResult](https://docs.aws.amazon.com/awssupport/latest/user/example_support_DescribeTrustedAdvisorCheckResult_section.html): Use DescribeTrustedAdvisorCheckResult with a CLI
- [DescribeTrustedAdvisorCheckSummaries](https://docs.aws.amazon.com/awssupport/latest/user/example_support_DescribeTrustedAdvisorCheckSummaries_section.html): Use DescribeTrustedAdvisorCheckSummaries with a CLI
- [DescribeTrustedAdvisorChecks](https://docs.aws.amazon.com/awssupport/latest/user/example_support_DescribeTrustedAdvisorChecks_section.html): Use DescribeTrustedAdvisorChecks with a CLI
- [RefreshTrustedAdvisorCheck](https://docs.aws.amazon.com/awssupport/latest/user/example_support_RefreshTrustedAdvisorCheck_section.html): Use RefreshTrustedAdvisorCheck with a CLI
- [ResolveCase](https://docs.aws.amazon.com/awssupport/latest/user/example_support_ResolveCase_section.html): Use ResolveCase with an AWS SDK or CLI


## [Monitoring and logging for Support](https://docs.aws.amazon.com/awssupport/latest/user/monitoring-overview.html)

### [Integrating AWS Support into EDAs](https://docs.aws.amazon.com/awssupport/latest/user/eventbridge-integration.html)

Receive notifications when specific AWS Support events occur in an AWS Support with EventBridge.

- [Support Case Update event](https://docs.aws.amazon.com/awssupport/latest/user/event-detail-support-case-update.html): Includes reference information about fields in the AWS Support support-case-update event .
- [Logging AWS Support API calls with AWS CloudTrail](https://docs.aws.amazon.com/awssupport/latest/user/logging-using-cloudtrail.html): Use AWS CloudTrail logging for support case management operations, such as creating and updating support cases.
- [Logging AWS Support App API calls with CloudTrail](https://docs.aws.amazon.com/awssupport/latest/user/logging-using-cloudtrail-support-app.html): Learn about logging AWS Support App in Slack with AWS CloudTrail.


## [Monitoring and logging for Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/monitoring-overview-support-plans.html)

- [Logging AWS Support Plans API calls with AWS CloudTrail](https://docs.aws.amazon.com/awssupport/latest/user/logging-using-cloudtrail-support-plans.html): Use AWS CloudTrail logging for support case management operations, such as creating and updating support cases.


## [Monitoring and logging for Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-ta.html)

- [Monitoring Trusted Advisor check results with EventBridge](https://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html): Use an EventBridge rule to monitor changes to your Trusted Advisor checks.
- [Creating CloudWatch alarms to monitor Trusted Advisor metrics](https://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-metrics-ta.html): Use CloudWatch to create alarms for Trusted Advisor metrics for check status changes, resource status changes, and service quota usage.
- [Logging AWS Trusted Advisor console actions with AWS CloudTrail](https://docs.aws.amazon.com/awssupport/latest/user/logging-using-cloudtrail-for-aws-trusted-advisor.html): Use AWS CloudTrail to log console actions for Trusted Advisor that occur in your AWS account.
