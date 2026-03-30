# Source: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/llms.txt

# AWS Migration Hub Orchestrator User Guide

> Use AWS Migration Hub Orchestrator to simplify and automate the migration of servers and enterprise applications to AWS

- [What is AWS Migration Hub Orchestrator?](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/what-is-migrationhub-orchestrator.html)
- [AWS Migration Hub availability change](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migrationhub-availability-change.html)
- [Setting up](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/setting-up.html)
- [How it works](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/how-mho-works.html)
- [Configure plugin](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/configure-plugin.html)
- [Migration workflows](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migration-workflows.html)
- [Quotas](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/load-balancer-limits.html)
- [Version history](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/version-history.html)
- [Document history](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/doc-history.html)

## [Templates](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/templates.html)

- [Migrate SAP applications and databases](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migrate-sap.html): With this template, you can automate the migration of your SAP NetWeaver based applications along with SAP HANA databases, or SAP HANA databases only to AWS.
- [Rehost on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-on-ec2.html): Rehost on Amazon EC2 with Migration Hub Orchestrator.
- [Rehost SQL Server on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-sql-ec2.html): With Rehost SQL server on Amazon EC2 template, you can rehost your SQL Server databases on an instance to Amazon EC2 using automated SQL Server backup and restore.
- [Replatform SQL on Amazon RDS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/replatform-sql-rds.html): With Replatform SQL server on Amazon RDS template, you can replatform your SQL Server databases on an instance to Amazon RDS using native backup and restore.

### [Replatform applications to Amazon ECS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/replatform-to-ecs.html)

Describes how to replatform applications to Amazon ECS with AWS Migration Hub Orchestrator.

- [Combining applications](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/replatform-to-ecs-combining-applications.html): If you are combining multiple applications from your source server to one container, there are additional requirements for the workflow.
- [Import virtual machine images](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/import-vm-images.html): >Import virtual machine images to AWS with Migration Hub Orchestrator.
- [Custom templates](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/custom-templates.html): Describes how to save a custom workflow created from an AWS managed template as a custom template for later use.


## [Security](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Migration Hub Orchestrator.
- [AWS managed policies](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Migration Hub Orchestrator and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give Migration Hub Orchestrator access to resources in your AWS account.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create private connections between your VPC and Migration Hub Orchestrator.
- [Compliance validation](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Migration Hub Orchestrator features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/infrastructure-security.html): Learn how Migration Hub Orchestrator isolates service traffic.


## [Logging and monitoring](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/logging-and-monitoring.html)

- [CloudTrail logs](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/logging-using-cloudtrail.html): Learn about logging Migration Hub Orchestrator with AWS CloudTrail.

### [Migration Hub Orchestrator events in EventBridge](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/event-bridge.html)

Understand how AWS Migration Hub Orchestrator generates status change events in Amazon EventBridge and the event structure that is delivered in JSON.

- [Configure notifications for status change events](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/event-bridge-notifications.html): Understand how AWS Migration Hub Orchestrator status change events in Amazon EventBridge can be used to configure notifications.
