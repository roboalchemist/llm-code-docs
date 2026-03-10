# Source: https://docs.aws.amazon.com/odb/latest/UserGuide/llms.txt

# Oracle Database@AWS Oracle Database@AWS User Guide

> With Oracle Database@AWS, you can access Oracle Exadata infrastructure managed by Oracle Cloud Infrastructure (OCI) inside AWS data centers. You migrate your on-premises Oracle Exadata workloads, establish low-latency connectivity with applications running on AWS, and integrate with AWS services.

- [What is Oracle Database@AWS?](https://docs.aws.amazon.com/odb/latest/UserGuide/what-is-odb.html)
- [How it works](https://docs.aws.amazon.com/odb/latest/UserGuide/how-it-works.html)
- [Onboarding](https://docs.aws.amazon.com/odb/latest/UserGuide/setting-up.html)
- [Getting started](https://docs.aws.amazon.com/odb/latest/UserGuide/getting-started.html)
- [ODB peering](https://docs.aws.amazon.com/odb/latest/UserGuide/configuring.html)
- [Managing](https://docs.aws.amazon.com/odb/latest/UserGuide/managing.html)
- [Backing up](https://docs.aws.amazon.com/odb/latest/UserGuide/managing-backups.html)
- [Troubleshooting](https://docs.aws.amazon.com/odb/latest/UserGuide/odb-troubleshooting-overview.html)
- [Quotas](https://docs.aws.amazon.com/odb/latest/UserGuide/quotas.html)
- [Document history](https://docs.aws.amazon.com/odb/latest/UserGuide/doc-history.html)

## [Entitlement sharing](https://docs.aws.amazon.com/odb/latest/UserGuide/entitlement-sharing.html)

- [Sharing entitlements across accounts](https://docs.aws.amazon.com/odb/latest/UserGuide/sharing-entitlement-task.html): Learn how to share Oracle Database@AWS entitlements with other AWS accounts within the same organization using AWS License Manager.


## [Resource sharing](https://docs.aws.amazon.com/odb/latest/UserGuide/resource-sharing.html)

- [Sharing resources across accounts](https://docs.aws.amazon.com/odb/latest/UserGuide/sharing-resources-task.html): Learn how to share Oracle Database@AWS resources with other AWS accounts within the same organization using AWS Resource Access Manager (AWS RAM).
- [Initializing the service](https://docs.aws.amazon.com/odb/latest/UserGuide/initialize-service-task.html): Learn how to initialize Oracle Database@AWS in a trusted account to establish the connection between your AWS account and Oracle Cloud Infrastructure for resource sharing.
- [Working with shared resources in a trusted account](https://docs.aws.amazon.com/odb/latest/UserGuide/working-with-shared-resources.html): Learn how to view and use shared Oracle Database@AWS resources in a trusted account after resource sharing has been established.


## [Zero-ETL integration with Redshift](https://docs.aws.amazon.com/odb/latest/UserGuide/zero-etl-integration.html)

- [Prerequisites](https://docs.aws.amazon.com/odb/latest/UserGuide/zero-etl-prerequisites.html): Learn about the requirements and prerequisites needed before setting up zero-ETL integration between Oracle Database@AWS and Amazon Redshift.
- [Considerations](https://docs.aws.amazon.com/odb/latest/UserGuide/zero-etl-operational-considerations.html): Learn about important considerations and best practices when setting up Zero-ETL integration between Oracle Database@AWS and Amazon Redshift.
- [Limitations](https://docs.aws.amazon.com/odb/latest/UserGuide/zero-etl-limitations.html): Learn about the limitations and constraints when using zero-ETL integration between Oracle Database@AWS and Amazon Redshift.
- [Setting up](https://docs.aws.amazon.com/odb/latest/UserGuide/setting-up-zero-etl.html): Learn how to set up and configure zero-ETL integration between your Oracle Database@AWS database and Amazon Redshift for real-time data replication.
- [Data filtering](https://docs.aws.amazon.com/odb/latest/UserGuide/filtering-zero-etl.html): Learn how to manage zero-ETL integrations between Oracle Database@AWS and Amazon Redshift, including monitoring (describing), modifying, and deleting integration configurations.
- [Monitoring](https://docs.aws.amazon.com/odb/latest/UserGuide/monitoring-zero-etl.html): Learn how to monitor zero-ETL integrations between Oracle Database@AWS and Amazon Redshift, including status monitoring and performance tracking.
- [Managing](https://docs.aws.amazon.com/odb/latest/UserGuide/managing-zero-etl.html): Learn how to manage zero-ETL integrations between Oracle Database@AWS and Amazon Redshift, including modifying and deleting integration configurations.
- [Troubleshooting](https://docs.aws.amazon.com/odb/latest/UserGuide/troubleshooting-zero-etl.html): Learn how to diagnose and resolve common issues with zero-ETL integration between Oracle Database@AWS and Amazon Redshift.


## [Security](https://docs.aws.amazon.com/odb/latest/UserGuide/security.html)

- [Data protection](https://docs.aws.amazon.com/odb/latest/UserGuide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Oracle Database@AWS.

### [Identity and access management](https://docs.aws.amazon.com/odb/latest/UserGuide/security-iam.html)

Learn how to authenticate requests and manage access to your Oracle Database@AWS resources using AWS Identity and Access Management policies and permissions.

- [How Oracle Database@AWS works with IAM](https://docs.aws.amazon.com/odb/latest/UserGuide/security_iam_service-with-iam.html): Before you use IAM to manage access to Oracle Database@AWS, learn what IAM features are available to use with Oracle Database@AWS.
- [Identity-based policies](https://docs.aws.amazon.com/odb/latest/UserGuide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Oracle Database@AWS resources.
- [AWS managed policies](https://docs.aws.amazon.com/odb/latest/UserGuide/odb-security-iam-awsmanpol.html): Learn about AWS managed policies for Oracle Database@AWS and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/odb/latest/UserGuide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Oracle Database@AWS and IAM.
- [Compliance validation](https://docs.aws.amazon.com/odb/latest/UserGuide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program and how Oracle Database@AWS meets regulatory requirements and industry standards.
- [Resilience](https://docs.aws.amazon.com/odb/latest/UserGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Oracle Database@AWS features for data resiliency and disaster recovery.
- [Service-linked roles](https://docs.aws.amazon.com/odb/latest/UserGuide/odb-SLR.html): Learn how to use service-linked roles with Oracle Database@AWS to allow the service to access resources on your behalf.
- [Policy updates](https://docs.aws.amazon.com/odb/latest/UserGuide/odb-manpol-updates.html): View details about updates to AWS managed policies for Oracle Database@AWS since RDS began tracking these changes.


## [Monitoring](https://docs.aws.amazon.com/odb/latest/UserGuide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/odb/latest/UserGuide/monitoring-cloudwatch.html): You can monitor Oracle Database@AWS using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Monitoring events](https://docs.aws.amazon.com/odb/latest/UserGuide/monitoring-events.html): Learn how to monitor Oracle Database@AWS events in Amazon EventBridge and route real-time data to targets such as AWS Lambda and Amazon Simple Notification Service.
- [CloudTrail logs](https://docs.aws.amazon.com/odb/latest/UserGuide/logging-using-cloudtrail.html): Learn how to log and monitor Oracle Database@AWS API calls with AWS CloudTrail for security analysis, resource change tracking, and compliance auditing.
