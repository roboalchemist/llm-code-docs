# Source: https://docs.aws.amazon.com/resource-explorer/latest/userguide/llms.txt

# AWS Resource Explorer User Guide

> This is the official Amazon Web Services (AWS) documentation for AWS Resource Explorer. This guide explains how to use AWS Resource Explorer to provide your users with the ability to search for resources across all of the AWS Regions in your account. You can control which users can view which resources by configuring views that include filters that define which resources are visible. You then can grant your users access to the views that show only the resources they need to do their jobs.

- [Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/welcome.html)
- [Immediate resource discovery experience](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-immediate-resource-discovery-experience.html)
- [Full vs partial results by Region](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-check.html)
- [Supporting console Unified Search](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-unified-search.html)
- [Deploying to an organization](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-all-org-with-stacksets.html)
- [Supported resource types](https://docs.aws.amazon.com/resource-explorer/latest/userguide/supported-resource-types.html)
- [Searching for resources](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search.html)
- [Search query syntax](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html)
- [Example queries](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-examples.html)
- [Viewing resource details](https://docs.aws.amazon.com/resource-explorer/latest/userguide/viewing-resource-details.html)
- [Managing resources](https://docs.aws.amazon.com/resource-explorer/latest/userguide/managing-resources.html)
- [Unified Search](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-unified-search.html)
- [Working with CloudFormation](https://docs.aws.amazon.com/resource-explorer/latest/userguide/cloudformation-support.html)
- [Using Amazon Q Developer in chat applications](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-chatbot.html)
- [Turning off Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-turn-off.html)
- [Quotas](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/resource-explorer/latest/userguide/sdk-general-information-section.html)
- [Document history](https://docs.aws.amazon.com/resource-explorer/latest/userguide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started.html)

- [Terms and concepts](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started-terms-and-concepts.html): Learn terms and concepts that help you understand how Resource Explorer works and how to configure it.
- [Prerequisites](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started-setting-up-prereqs.html): Get started with Resource Explorer.
- [Setting up Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started-setting-up.html): Learn how to enhance and configure Resource Explorer in your AWS account.


## [Creating user-owned indexes](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-turn-on-region.html)

- [About opt-in Regions](https://docs.aws.amazon.com/resource-explorer/latest/userguide/opt-in-region-considerations.html): Opt-in Regions have higher security requirements than commercial Regions as it pertains to sharing IAM data through accounts in opt-in Regions.


## [Enabling cross-Region search](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html)

- [Creating the aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region-turn-on.html): For cross-region search functionality, Resource Explorer provides a streamlined banner workflow that allows you to enable cross-region search with a single click.
- [Demoting the aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region-turn-off.html): Learn how to demote the aggregator index to a local index when you no longer want to support cross-Region search, or when you want to move the aggregator index to a different AWS Region.


## [Turning on multi-account search](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-multi-account.html)

- [Effect of account actions on multi-account search](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-account-actions.html): Learn how account actions can effect multi-account search in AWS Resource Explorer.


## [Views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/views.html)

### [User views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/customer-views.html)

User views are created and managed by users or administrators.

- [Creating views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/configure-views-create.html): All searches must use a view.
- [Granting access to views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/configure-views-grant-access.html): Before users can search with a new view, you must grant access to AWS Resource Explorer views.
- [Setting a default view](https://docs.aws.amazon.com/resource-explorer/latest/userguide/configure-views-set-default.html): In AWS Resource Explorer, you can define many views in an AWS Region, where each view addresses different search requirements.
- [Tagging views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/configure-views-tag.html): You can add tags to your views to categorize them.
- [Sharing views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/configure-views-share.html): Learn how to share Resource Explorer views with other AWS accounts and attach identity-based permissions policies to roles, groups, and users.
- [Deleting views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/configure-views-delete.html): When you no longer need an AWS Resource Explorer view, you can delete it.
- [AWS service views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-service-views.html): Learn about AWS service views, pre-defined views that enable other AWS services services to access resource data through Resource Explorer.

### [AWS managed views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html)

Learn how AWS managed views work in AWS Resource Explorer as a basis for search operations.

- [Listing managed views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/listing-managed-views.html): You can see which managed views you have access to on the Views page in the Resource Explorer console.
- [Deleting managed views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/deleting-managed-views.html): Managed views can only be deleted by the AWS service that manages them.


## [Security](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security.html)

- [Upgrade IAM policies to IPv6](https://docs.aws.amazon.com/resource-explorer/latest/userguide/arex-security-ipv6-upgrade.html): Upgrading your IAM policies to include IPv6 if you use dual addressing.

### [Identity and access management](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam.html)

How to authenticate requests and manage access your Resource Explorer resources.

- [Resource Explorer and IAM](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Resource Explorer, you should understand what IAM features are available to use with Resource Explorer.
- [Identity-based policy examples](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_id-based-policy-examples.html): By default, AWS Identity and Access Management (IAM) principals, such as roles, groups, and users, don't have permission to create or modify Resource Explorer resources.
- [Example SCPs](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_scp.html): AWS Resource Explorer supports service control policies (SCPs).
- [AWS managed policies](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html): Learn about AWS managed policies for Resource Explorer and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html): Learn how to use service-linked roles to give Resource Explorer access to resources in your AWS account.
- [Troubleshooting permissions](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Resource Explorer and AWS Identity and Access Management (IAM).
- [Data protection](https://docs.aws.amazon.com/resource-explorer/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Resource Explorer.
- [Compliance validation](https://docs.aws.amazon.com/resource-explorer/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/resource-explorer/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Resource Explorer features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/resource-explorer/latest/userguide/infrastructure-security.html): Learn how Resource Explorer isolates service traffic.
- [AWS PrivateLink](https://docs.aws.amazon.com/resource-explorer/latest/userguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Resource Explorer.


## [Monitoring](https://docs.aws.amazon.com/resource-explorer/latest/userguide/monitoring-overview.html)

- [CloudTrail logs](https://docs.aws.amazon.com/resource-explorer/latest/userguide/monitoring-cloudtrail.html): Learn about logging AWS Resource Explorer with AWS CloudTrail.


## [Troubleshooting](https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting.html)

- [Setup issues](https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_setup.html): Diagnose and fix setup and configuration issues that you might encounter when working with Resource Explorer.
- [Search issues](https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_search.html): Diagnose and fix issues that you might encounter when searching for resources with Resource Explorer.
