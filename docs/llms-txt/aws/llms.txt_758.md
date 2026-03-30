# Source: https://docs.aws.amazon.com/security-lake/latest/userguide/llms.txt

# Amazon Security Lake User Guide

- [What is Amazon Security Lake?](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html)
- [Concepts and terminology](https://docs.aws.amazon.com/security-lake/latest/userguide/service-concepts.html)
- [Managing multiple accounts](https://docs.aws.amazon.com/security-lake/latest/userguide/multi-account-management.html)
- [Lifecycle management](https://docs.aws.amazon.com/security-lake/latest/userguide/lifecycle-management.html)
- [Open Cybersecurity Schema Framework (OCSF)](https://docs.aws.amazon.com/security-lake/latest/userguide/open-cybersecurity-schema-framework.html)
- [Logging API calls](https://docs.aws.amazon.com/security-lake/latest/userguide/securitylake-cloudtrail.html)
- [Supported Regions and endpoints](https://docs.aws.amazon.com/security-lake/latest/userguide/supported-regions.html)
- [Disabling Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/disable-security-lake.html)
- [Document history](https://docs.aws.amazon.com/security-lake/latest/userguide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html)

- [Setting up your AWS account](https://docs.aws.amazon.com/security-lake/latest/userguide/initial-account-setup.html): Before you can enable Amazon Security Lake, you must have an AWS account.
- [Considerations when enabling Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/enable-securitylake-considerations.html): Before enabling Security Lake, consider the following:
- [Using the console](https://docs.aws.amazon.com/security-lake/latest/userguide/get-started-console.html): This tutorial explains how to enable and configure Security Lake through the AWS Management Console.
- [Using the AWS CLI or API](https://docs.aws.amazon.com/security-lake/latest/userguide/get-started-programmatic.html): This tutorial explains how to enable and start using Security Lake programmatically.


## [Managing Regions](https://docs.aws.amazon.com/security-lake/latest/userguide/manage-regions.html)

- [Configuring rollup Regions](https://docs.aws.amazon.com/security-lake/latest/userguide/add-rollup-region.html): A rollup Region consolidates data from one or more contributing Regions.


## [Source management](https://docs.aws.amazon.com/security-lake/latest/userguide/source-management.html)

### [Collecting data from AWS services](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html)

Learn about collecting security logs and events in Security Lake from supported AWS services.

- [Updating role permissions](https://docs.aws.amazon.com/security-lake/latest/userguide/update-role-permissions.html): If you don't have the required role permissions or resourcesânew AWS Lambda function and Amazon Simple Queue Service (Amazon SQS) queueâto ingest data from a new version of the data source, you must update your AmazonSecurityLakeMetaStoreManagerV2 role permissions and create a new set of resources to process data from your sources.
- [Removing an AWS service as a source](https://docs.aws.amazon.com/security-lake/latest/userguide/remove-internal-sources.html): Choose your access method, and follow these steps to remove a natively-supported AWS service as a Security Lake source.
- [CloudTrail event logs](https://docs.aws.amazon.com/security-lake/latest/userguide/cloudtrail-event-logs.html): AWS CloudTrail provides you with a history of AWS API calls for your account, including API calls made using the AWS Management Console, the AWS SDKs, the command line tools, and certain AWS services.
- [Amazon EKS Audit Logs](https://docs.aws.amazon.com/security-lake/latest/userguide/eks-audit-logs.html): When you add Amazon EKS Audit Logs as a source, Security Lake starts collecting in-depth information about the activities performed on the Kubernetes resources running in your Elastic Kubernetes Service (EKS) clusters.
- [RouteÂ 53 resolver query logs](https://docs.aws.amazon.com/security-lake/latest/userguide/route-53-logs.html): RouteÂ 53 resolver query logs track DNS queries made by resources within your Amazon Virtual Private Cloud (Amazon VPC).
- [Security Hub CSPM findings](https://docs.aws.amazon.com/security-lake/latest/userguide/security-hub-findings.html): Security Hub CSPM findings help you understand your security posture in AWS and let you check your environment against security industry standards and best practices.
- [VPC Flow Logs](https://docs.aws.amazon.com/security-lake/latest/userguide/vpc-flow-logs.html): The VPC Flow Logs feature of Amazon VPC captures information about the IP traffic going to and from network interfaces within your environment.
- [AWS WAF logs](https://docs.aws.amazon.com/security-lake/latest/userguide/aws-waf.html): When you add AWS WAF as a log source in Security Lake, Security Lake immediately starts collecting the logs.

### [Collecting data from custom sources](https://docs.aws.amazon.com/security-lake/latest/userguide/custom-sources.html)

Learn about collecting security logs and events in Security Lake from custom, third-party sources.

- [Adding a custom source](https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html): After creating the IAM role to invoke the AWS Glue crawler, follow these steps to add a custom source in Security Lake.
- [Deleting a custom source](https://docs.aws.amazon.com/security-lake/latest/userguide/delete-custom-source.html): Delete a custom source to stop sending data from the source to Security Lake.


## [Subscriber management](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html)

### [Subscriber data access](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-data-access.html)

Learn about how to set up data access for subscribers in Security Lake.

- [Prerequisites](https://docs.aws.amazon.com/security-lake/latest/userguide/prereqs-creating-subscriber.html): You must complete the following prerequisites before you can create a subscriber with data access in Security Lake.
- [Creating a subscriber with data access](https://docs.aws.amazon.com/security-lake/latest/userguide/create-subscriber-data-access.html): Choose one of the following access methods to create a subscriber with access to data in the current AWS Region.
- [Updating a data subscriber](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-update.html): You can update a subscriber by changing the sources from which the subscriber consumes.
- [Removing a data subscriber](https://docs.aws.amazon.com/security-lake/latest/userguide/remove-data-access-subscriber.html): If you no longer want a subscriber to consume data from Security Lake, you can remove the subscriber by following these steps.

### [Subscriber query access](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-access.html)

Learn about how to set up query access for subscribers in Security Lake.

- [Prerequisites](https://docs.aws.amazon.com/security-lake/latest/userguide/prereqs-query-subscriber.html): You must complete the following prerequisites before you can create a subscriber with data access in Security Lake.
- [Creating a subscriber with query access](https://docs.aws.amazon.com/security-lake/latest/userguide/create-query-subscriber-procedures.html): Choose your preferred method to create a subscriber with query access in the current AWS Region.
- [Editing a subscriber with query access](https://docs.aws.amazon.com/security-lake/latest/userguide/editing-query-access-subscriber.html): Security Lake supports making edits to a subscriber with query access.


## [Security Lake queries](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-examples.html)

### [Security Lake queries source version 1](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-examples1.html)

Get querying guidance and example queries for subscribers that have query access in Security Lake.

- [Queries for CloudTrail data](https://docs.aws.amazon.com/security-lake/latest/userguide/cloudtrail-query-examples.html): Get example queries for AWS CloudTrail data that is stored in Security Lake.
- [Queries for RouteÂ 53 resolver query logs](https://docs.aws.amazon.com/security-lake/latest/userguide/route53_1_0-query-examples.html): Get example queries for Amazon RouteÂ 53 resolver query logs that are stored in Security Lake.
- [Queries for Security Hub CSPM findings](https://docs.aws.amazon.com/security-lake/latest/userguide/security-hub-query-examples.html): Here are some example queries for Security Hub CSPM findings that are stored in Security Lake for AWS source version 1.
- [Queries for Amazon VPC Flow Logs](https://docs.aws.amazon.com/security-lake/latest/userguide/vpc-query-examples.html): Here are some example queries for Amazon VPC Flow Logs that are stored in Security Lake for AWS source version 1.

### [Security Lake queries source version 2](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-examples2.html)

Get querying guidance and example queries for subscribers that have query access in Security Lake.

- [Queries for CloudTrail data](https://docs.aws.amazon.com/security-lake/latest/userguide/cloudtrail-query-examples-sourceversion2.html): Here are some example queries for AWS CloudTrail data that is stored in Security Lake for AWS source version 2.
- [Queries for RouteÂ 53 resolver query logs](https://docs.aws.amazon.com/security-lake/latest/userguide/route53_1_0-query-examples-sourceversion2.html): Here are some example queries for Amazon RouteÂ 53 resolver query logs that are stored in Security Lake for AWS source version 2.
- [Queries for Security Hub CSPM findings](https://docs.aws.amazon.com/security-lake/latest/userguide/security-hub-query-examples-sourceversion2.html): Here are some example queries for Security Hub CSPM findings that are stored in Security Lake for AWS source version 2.
- [Queries for Amazon VPC Flow Logs](https://docs.aws.amazon.com/security-lake/latest/userguide/vpc-query-examples-sourceversion2.html): Here are some example queries for Amazon VPC Flow Logs that are stored in Security Lake for AWS source version 2.
- [Queries for AWS WAFv2 logs](https://docs.aws.amazon.com/security-lake/latest/userguide/example-queries-waf-sourceversion2.html): Here are some example queries for AWS WAFv2 logs that are stored in Security Lake for AWS source version 2.


## [Integrations](https://docs.aws.amazon.com/security-lake/latest/userguide/integrations-overview.html)

### [AWS service integrations](https://docs.aws.amazon.com/security-lake/latest/userguide/aws-integrations.html)

Learn how to use Amazon Security Lake with other AWS services.

- [Amazon Bedrock integration](https://docs.aws.amazon.com/security-lake/latest/userguide/bedrock-integration.html): Learn how to use the Amazon Security Lake integration with Amazon Bedrock.
- [Amazon Detective integration](https://docs.aws.amazon.com/security-lake/latest/userguide/detective-integration.html): Learn how to use the Security Lake integration with Amazon Detective.
- [Amazon OpenSearch Service integration](https://docs.aws.amazon.com/security-lake/latest/userguide/opensearch-integration.html): Learn how to use Amazon Security Lake integration with Amazon OpenSearch Service
- [Amazon OpenSearch Service Ingestion pipeline integration](https://docs.aws.amazon.com/security-lake/latest/userguide/opensearch-ingestion-pipeline-integration.html): Integration type:Subscriber, Source
- [Amazon OpenSearch Service zero-ETL direct query integration](https://docs.aws.amazon.com/security-lake/latest/userguide/opensearch-datasource-integration.html): Integration type: Subscriber (Query)
- [Quick integration](https://docs.aws.amazon.com/security-lake/latest/userguide/quicksight-integration.html): Learn how to use the Security Lake integration with Amazon Quick
- [Amazon SageMaker AI integration](https://docs.aws.amazon.com/security-lake/latest/userguide/sagemaker-integration.html): Learn how to use the Security Lake integration with Amazon SageMaker AI
- [AWS AppFabric integration](https://docs.aws.amazon.com/security-lake/latest/userguide/appfabric-integration.html): Learn how to use the Amazon Security Lake integration with AWS AppFabric.
- [AWS Security Hub CSPM integration](https://docs.aws.amazon.com/security-lake/latest/userguide/securityhub-integration.html): Learn how to use the Amazon Security Lake integration with AWS Security Hub CSPM.
- [Third-party integrations](https://docs.aws.amazon.com/security-lake/latest/userguide/integrations-third-party.html): Learn about third-party integrations with Security Lake.


## [Security](https://docs.aws.amazon.com/security-lake/latest/userguide/security.html)

### [Identity and access management](https://docs.aws.amazon.com/security-lake/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Security Lake resources.

- [How Security Lake works with IAM](https://docs.aws.amazon.com/security-lake/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Security Lake, learn what IAM features are available to use with Security Lake.
- [Identity-based policy examples](https://docs.aws.amazon.com/security-lake/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Security Lake resources.
- [AWS managed policies](https://docs.aws.amazon.com/security-lake/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Security Lake and recent changes to those policies.

### [Using service-linked roles](https://docs.aws.amazon.com/security-lake/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give Security Lake access to resources in your AWS account.

- [SLR permissions for Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/slr-permissions.html): Security Lake uses the service-linked role named AWSServiceRoleForSecurityLake.
- [SLR permissions for resource management](https://docs.aws.amazon.com/security-lake/latest/userguide/AWSServiceRoleForSecurityLakeResourceManagement.html): Learn how Security Lake uses a service-linked role to manage the metadata and resources in your AWS account.

### [Data protection](https://docs.aws.amazon.com/security-lake/latest/userguide/data-protection.html)

Learn about how the AWS shared responsibility model applies to data protection in Security Lake.

- [Opting out of using your data for service improvement](https://docs.aws.amazon.com/security-lake/latest/userguide/opting-out-of-using-your-data.html): Learn how you can opt-out of using your data for Security Lake improvement.
- [Compliance validation](https://docs.aws.amazon.com/security-lake/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Security best practices for Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/best-practices-overview.html): Learn about Security Lake security best practices.
- [Resilience](https://docs.aws.amazon.com/security-lake/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Security Lake features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/security-lake/latest/userguide/infrastructure-security.html): Learn how Security Lake isolates service traffic.
- [Configuration and vulnerability analysis in Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/configuration-vulnerability-analysis.html): Learn about Security Lake configuration and vulnerability analysis.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/security-lake/latest/userguide/security-vpc-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Security Lake without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.

### [Monitoring](https://docs.aws.amazon.com/security-lake/latest/userguide/monitoring-overview.html)

Monitor Security Lake to maintain reliability, availability, and performance.

- [CloudWatch metrics for Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/cloudwatch-metrics.html): Monitor Security Lake in CloudWatch to maintain reliability, availability, and performance.


## [Tagging resources](https://docs.aws.amazon.com/security-lake/latest/userguide/tagging-resources.html)

- [Tagging fundamentals](https://docs.aws.amazon.com/security-lake/latest/userguide/tags-basics.html): A resource can have as many as 50 tags.
- [Using tags in IAM policies](https://docs.aws.amazon.com/security-lake/latest/userguide/tags-iam.html): After you start tagging resources, you can define tag-based, resource-level permissions in AWS Identity and Access Management (IAM) policies.
- [Adding tags to resources](https://docs.aws.amazon.com/security-lake/latest/userguide/tags-add.html): To add tags to an Amazon Security Lake resource, you can use the Security Lake console or the Security Lake API.
- [Editing tags for resources](https://docs.aws.amazon.com/security-lake/latest/userguide/tags-update.html): To edit the tags (tag keys or tag values) for an Amazon Security Lake resource, you can use the Security Lake console or the Security Lake API.
- [Removing tags from resources](https://docs.aws.amazon.com/security-lake/latest/userguide/tags-remove.html): To remove tags from an Amazon Security Lake resource, you can use the Security Lake console or the Security Lake API.


## [Troubleshooting](https://docs.aws.amazon.com/security-lake/latest/userguide/security-lake-troubleshoot.html)

- [Troubleshooting data lake status](https://docs.aws.amazon.com/security-lake/latest/userguide/securitylake-data-lake-troubleshoot.html): The Issues page of the Security Lake console shows you a summary of issues that are affecting your data lake.
- [Troubleshooting Lake Formation issues](https://docs.aws.amazon.com/security-lake/latest/userguide/securitylake-lf-troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Security Lake and AWS Lake Formation databases or tables.
- [Troubleshooting querying in Amazon Athena](https://docs.aws.amazon.com/security-lake/latest/userguide/querying-troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when using Athena to query objects that are stored in your Security Lake S3 bucket.
- [Troubleshooting Organizations issues](https://docs.aws.amazon.com/security-lake/latest/userguide/securitylake-orgs-troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Security Lake and AWS Organizations.
- [Troubleshooting IAM issues](https://docs.aws.amazon.com/security-lake/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Security Lake and IAM.


## [Security Lake pricing](https://docs.aws.amazon.com/security-lake/latest/userguide/estimating-costs.html)

- [Reviewing usage and estimated costs](https://docs.aws.amazon.com/security-lake/latest/userguide/reviewing-usage-costs.html): Learn how to review your Security Lake usage and estimate costs.
