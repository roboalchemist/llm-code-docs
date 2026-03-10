# Source: https://docs.aws.amazon.com/devops-guru/latest/userguide/llms.txt

# Amazon DevOps Guru User Guide

- [Setting up](https://docs.aws.amazon.com/devops-guru/latest/userguide/setting-up.html)
- [Estimating your cost](https://docs.aws.amazon.com/devops-guru/latest/userguide/cost-estimate.html)
- [Enabling AWS services for DevOpsÂ Guru analysis](https://docs.aws.amazon.com/devops-guru/latest/userguide/enable-services-for-devops-guru.html)
- [Working with insights](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html)
- [Integrating with CodeGuru Profiler](https://docs.aws.amazon.com/devops-guru/latest/userguide/integrating-with-profiler.html)
- [Working with EventBridge](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-eventbridge.html)
- [Viewing notifications](https://docs.aws.amazon.com/devops-guru/latest/userguide/notification-types.html)
- [Viewing analyzed resources](https://docs.aws.amazon.com/devops-guru/latest/userguide/view-analyzed-resources.html)
- [Best practices](https://docs.aws.amazon.com/devops-guru/latest/userguide/best-practices.html)
- [Quotas and limits](https://docs.aws.amazon.com/devops-guru/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/devops-guru/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/devops-guru/latest/userguide/glossary.html)

## [What is Amazon DevOpsÂ Guru?](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html)

### [How does DevOpsÂ Guru work?](https://docs.aws.amazon.com/devops-guru/latest/userguide/how-it-works.html)

Learn how Amazon DevOpsÂ Guru analyzes your operational system and provides recommendations to help you improve its performance.

- [High level DevOpsÂ Guru workflow](https://docs.aws.amazon.com/devops-guru/latest/userguide/high-level-workflow.html): The Amazon DevOpsÂ Guru workflow can be broken down into three high level steps.
- [Detailed DevOpsÂ Guru workflow](https://docs.aws.amazon.com/devops-guru/latest/userguide/detailed-workflow.html): The DevOpsÂ Guru workflow integrates with several AWS services, including Amazon CloudWatch, AWS CloudTrail, Amazon Simple Notification Service, and AWS Systems Manager.
- [Concepts](https://docs.aws.amazon.com/devops-guru/latest/userguide/concepts.html): Learn about concepts in DevOpsÂ Guru to help you generate insights about your applications.
- [Coverage](https://docs.aws.amazon.com/devops-guru/latest/userguide/coverage.html): Learn about coverage in DevOpsÂ Guru to help you understand what kind of insights DevOpsÂ Guru can generate about your applications.


## [Getting started](https://docs.aws.amazon.com/devops-guru/latest/userguide/getting-started.html)

- [Step 1: Get set up](https://docs.aws.amazon.com/devops-guru/latest/userguide/get-set-up.html): Before you get started, prepare by running through the steps in .

### [Step 2: Enable DevOpsÂ Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/getting-started-enable-service.html)

To configure Amazon DevOpsÂ Guru to use for the first time, you must choose how you want to set up DevOpsÂ Guru.

- [Monitor accounts across your organization](https://docs.aws.amazon.com/devops-guru/latest/userguide/getting-started-multi-account.html): If you choose to monitor applications across your organization, log into your organization management account.
- [Monitor your current account](https://docs.aws.amazon.com/devops-guru/latest/userguide/getting-started-single-account.html): If you choose to monitor applications in your current AWS account, choose which AWS resources in your account and Region are covered or analyzed and specify one or two Amazon Simple Notification Service topics that are used to notify you when an insight is created.
- [Step 3: Specify your DevOpsÂ Guru resource coverage](https://docs.aws.amazon.com/devops-guru/latest/userguide/choose-coverage.html): Learn how to configure AWS CloudFormation stacks to specify which AWS resources are analyzed by Amazon DevOpsÂ Guru.


## [Monitoring databases](https://docs.aws.amazon.com/devops-guru/latest/userguide/monitoring-databases.html)

### [Relational databases](https://docs.aws.amazon.com/devops-guru/latest/userguide/monitoring-relational-databases.html)

Learn how to use DevOpsÂ Guru to monitor databases in Amazon RDS and Amazon Redshift to discover and address anomalies and performance issues.

### [Working with anomalies in DevOpsÂ Guru for RDS](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.html)

Learn how to identify and interpret anomalies to address performance issues discovered by DevOpsÂ Guru for RDS.

### [Overview of DevOpsÂ Guru for RDS](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.overview.html)

Learn about the key features and benefits of DevOpsÂ Guru for RDS.

- [Benefits of DevOpsÂ Guru for RDS](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.overview.benefits.html): Learn about the benefits of DevOpsÂ Guru for RDS, including fast diagnosis, fast resolution, and keep knowledge.
- [Key concepts for database performance tuning](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.overview.tuning.html): Learn about a few key concepts about database performance tuning that DevOpsÂ Guru for RDS assumes that you're familiar with.
- [Key concepts for DevOpsÂ Guru for RDS](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.overview.definitions.html): Learn about key concepts for DevOpsÂ Guru for RDS.
- [How DevOpsÂ Guru for RDS works](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.overview.how-it-works.html): Learn how DevOpsÂ Guru for RDS works.
- [Supported database engines](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.overview.supported-engines.html): DevOpsÂ Guru for RDS is supported for the following database engines:
- [Enabling DevOpsÂ Guru for RDS](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.enabling.html): To allow DevOpsÂ Guru to publish insights for an Amazon Aurora database, complete these tasks.

### [Analyzing anomalies in Amazon RDS](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.analyzing.html)

When DevOpsÂ Guru for Amazon RDS publishes a performance anomaly in the dashboard, you typically perform these steps.

- [Viewing insights](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.analyzing.insights.html): View insights for DevOpsÂ Guru for RDS.
- [Viewing reactive anomalies](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.analyzing.metrics.html): View reactive anomalies in DevOpsÂ Guru for RDS
- [Viewing proactive anomalies](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.analyzing.proactive.metrics.html): View proactive anomalies in DevOpsÂ Guru for RDS
- [Responding to recommendations](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.analyzing.recommend.html): Learn how to respond to recommendations for contextual anomalies for DevOpsÂ Guru for RDS.
- [Non-relational databases](https://docs.aws.amazon.com/devops-guru/latest/userguide/monitoring-non-relational-databases.html): Learn how to use DevOpsÂ Guru to monitor databases in Amazon DynamoDB and Amazon ElastiCache to discover and address anomalies and performance issues.


## [Defining applications using AWS resources](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-resource-collections.html)

- [Using tags to identify resources in your applications](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-resource-tags.html): Learn how to use AWS tags on resources to define your application.
- [Using stacks to identify resources in your DevOpsÂ Guru applications](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-cfn-stacks.html): Describes how to use CloudFormation stacks to specify which resources you want Amazon DevOpsÂ Guru to analyze for operational insights.


## [Updating settings](https://docs.aws.amazon.com/devops-guru/latest/userguide/update-settings.html)

- [Updating your notifications](https://docs.aws.amazon.com/devops-guru/latest/userguide/update-notifications.html): Set up Amazon Simple Notification Service topics that are used to notify you about important Amazon DevOpsÂ Guru events.
- [Filtering your notifications](https://docs.aws.amazon.com/devops-guru/latest/userguide/update-notifications-filter.html): You can filter your DevOpsÂ Guru notifications by or by using a Amazon SNS subscription filter policy.


## [Security](https://docs.aws.amazon.com/devops-guru/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/devops-guru/latest/userguide/data-protection.html): Discusses data protection in DevOpsÂ Guru.

### [Identity and Access Management](https://docs.aws.amazon.com/devops-guru/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your DevOpsÂ Guru resources.

- [How Amazon DevOpsÂ Guru works with IAM](https://docs.aws.amazon.com/devops-guru/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to DevOpsÂ Guru, learn what IAM features are available to use with DevOpsÂ Guru.
- [Identity-based policies](https://docs.aws.amazon.com/devops-guru/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify DevOpsÂ Guru resources.
- [Using service-linked roles](https://docs.aws.amazon.com/devops-guru/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give Amazon DevOpsÂ Guru access to resources in your AWS account.
- [DevOpsÂ Guru permissions reference](https://docs.aws.amazon.com/devops-guru/latest/userguide/auth-and-access-control-permissions-reference.html): Describes the Amazon DevOpsÂ Guru API operations and the corresponding actions that you grant permissions to perform.
- [Permissions for Amazon SNS topics](https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html): Create a policy for an Amazon SNS topic that gives permissions to send notifications.
- [Permissions for encrypted Amazon SNS topics](https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html)
- [Troubleshooting](https://docs.aws.amazon.com/devops-guru/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with DevOpsÂ Guru and IAM.

### [Monitoring DevOpsÂ Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/monitoring-overview.html)

Monitor Amazon DevOpsÂ Guru to maintain reliability, availability, and performance.

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/devops-guru/latest/userguide/monitoring-cloudwatch.html): You can monitor DevOpsÂ Guru using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Logging DevOpsÂ Guru API calls with AWS CloudTrail](https://docs.aws.amazon.com/devops-guru/latest/userguide/logging-using-cloudtrail.html): Learn about logging Amazon DevOpsÂ Guru with AWS CloudTrail.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/devops-guru/latest/userguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon DevOpsÂ Guru without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Infrastructure security](https://docs.aws.amazon.com/devops-guru/latest/userguide/infrastructure-security.html): Learn how Amazon DevOpsÂ Guru isolates service traffic.
- [Resilience](https://docs.aws.amazon.com/devops-guru/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific DevOpsÂ Guru features for data resiliency.
