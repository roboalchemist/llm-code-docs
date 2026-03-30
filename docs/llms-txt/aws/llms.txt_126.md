# Source: https://docs.aws.amazon.com/aws-backup/latest/devguide/llms.txt

# AWS Backup Developer Guide

> Provides a conceptual overview of AWS Backup, detailed instructions for using the various features, and a complete API reference for developers.

- [Getting started](https://docs.aws.amazon.com/aws-backup/latest/devguide/getting-started.html)
- [Manage multiple accounts with AWS Organizations](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html)
- [AWS Backup and CloudFormation](https://docs.aws.amazon.com/aws-backup/latest/devguide/integrate-cloudformation-with-aws-backup.html)
- [Network](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-network.html)
- [Quotas](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-limits.html)
- [Troubleshooting AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/aws-backup/latest/devguide/doc-history.html)

## [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

- [AWS Backup feature availability](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html): AWS Backup features and Regional availability.


## [How it works](https://docs.aws.amazon.com/aws-backup/latest/devguide/how-it-works.html)

- [Working with supported AWS services](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-supported-services.html): Configure AWS Backup to work with other AWS services to back up your data.
- [Metering, costs, and billing](https://docs.aws.amazon.com/aws-backup/latest/devguide/metering-and-billing.html)
- [Blogs, videos, tutorials, and other resources](https://docs.aws.amazon.com/aws-backup/latest/devguide/blogs-videos.html): For more information about AWS Backup, see the following:


## [Backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html)

### [Create a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)

Create a backup plan in AWS Backup by starting from an existing plan or building a new plan.

- [Backup plan options and configuration](https://docs.aws.amazon.com/aws-backup/latest/devguide/plan-options-and-configuration.html): When you define a backup plan in the AWS Backup console, you configure the following options:
- [CloudFormation templates for backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/plan-cfn.html): We provide three sample CloudFormation templates for your reference.
- [Delete a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-a-backup-plan.html): Delete a backup plan in AWS Backup using the AWS Management Console.
- [Update a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/updating-a-backup-plan.html): Edit a backup plan in AWS Backup using the AWS Management Console.
- [Understanding backup plan summary](https://docs.aws.amazon.com/aws-backup/latest/devguide/understanding-backup-plan-summaries.html): Use backup plan summaries to validate and understand your backup plan configurations, including scheduled runs, resource assignments, and feature compatibility.

### [Opt in and assign resources](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

Automatically back up your resources by assigning them to a backup plan in AWS Backup.

- [Assign resources through console](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources-console.html)
- [Assign resources with AWS CLI](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources-json.html)
- [Assign resources with CloudFormation](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources-cfn.html): This end-to-end CloudFormation template creates a resource assignment, a backup plan, and a destination backup vault:


## [Backup vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html)

- [Backup vault creation and deletion](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-a-vault.html): Create backup vaults to manage and organize backups.

### [Logically air-gapped vault](https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html)

Details logically air-gapped vault, a secondary type of vault which can store copies of backups in other vaults.

- [Primary backups to logically air-gapped vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/lag-vault-primary-backup.html): Use primary backups to logically air-gapped vaults to eliminate the need for separate copies in both standard and logically air-gapped vaults, reducing costs while preserving security benefits.

### [Multi-party approval for logically air-gapped vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/multipartyapproval.html)

This section contains information on the integration of AWS Backup logically air-gapped vaults and AWS Organizations Multi-party approval capability.

- [Administrator tasks](https://docs.aws.amazon.com/aws-backup/latest/devguide/multipartyapproval-tasks-administrator.html): Several tasks involving AWS Backup and Multi-party overview required a user with admin permissions and access to the management account.
- [Requester tasks](https://docs.aws.amazon.com/aws-backup/latest/devguide/multipartyapproval-tasks-requester.html)
- [Approver tasks](https://docs.aws.amazon.com/aws-backup/latest/devguide/multipartyapproval-tasks-approver.html): A user who is a member of a Multi-party approval team can approve or deny requests that are part of a session.
- [Vault access policies](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-a-vault-access-policy.html): Set access policies for an AWS Backup vault and resources stored in vaults.
- [Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html): A vault lock set in compliance or governance mode can add additional security to your vault and the backups within it.


## [Backup creation, maintenance, and restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/recovery-points.html)

- [On-demand backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/recov-point-create-on-demand-backup.html): Create an on-demand backup

### [Continuous backups and PITR](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html)

For some resources, AWS Backup supports continuous backups and point-in-time recovery (PITR) in addition to snapshot backups.

- [Finding a continuous backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-finding.html): You can use the AWS Backup console to find your continuous backup.
- [Restoring a continuous backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-restoring.html)
- [Stopping or deleting continuous backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-stopping.html): You can stop the creation of continuous backups or you can delete specific backups (point-in-time-recovery or PITR points).
- [Copying continuous backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-copying.html): If a continuous backup rule also specifies a cross-account or cross-Region copy and AWS Backup supports the operation for the resource type, AWS Backup takes a snapshot of the resource and copies the snapshot to the destination vault.
- [Changing your retention period](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-retention-period.html): You can use AWS Backup to increase or decrease the retention period for your existing continuous backup rule.
- [Removing the only continuous backup rule from a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-removing_rule.html): When you create a backup plan with a continuous backup rule and then you remove that rule, AWS Backup remembers the retention period from your now-deleted rule.

### [Backup creation by resource type](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html)

Create a backup automatically or manually in AWS Backup.

- [CloudFormation stack backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/applicationstackbackups.html): How to backup up CloudFormation stack backups
- [Amazon Aurora DSQL backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-aurora.html): Backup Aurora and Aurora DSQL clusters
- [Advanced DynamoDB backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html): Understand and enable DynamoDB backups using AWS Backup advanced features.
- [Amazon EBS backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/multi-volume-crash-consistent.html): Learn about Amazon EBS snapshots and AWS Backup.
- [Amazon RDS backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/rds-backup.html): Understand and use Amazon RDS backups.
- [Amazon Redshift backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-backups.html): AWS Backup offers backup functionality for Amazon Redshift.
- [Amazon Redshift Serverless backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-serverless-backups.html): Learn how to back up Amazon Redshift Serverless namespaces using AWS Backup.
- [Amazon EKS](https://docs.aws.amazon.com/aws-backup/latest/devguide/eks-backups.html): An Amazon Elastic Kubernetes Service (Amazon EKS) cluster consists of multiple resources that you can back up as a single unit.
- [SAP HANA backup on Amazon EC2](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-saphana.html): SAP HANA backup on Amazon EC2
- [Amazon S3 backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html): AWS Backup supports centralized backup and restore of applications storing data in S3.
- [Amazon Timestream backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/timestream-backup.html): AWS Backup offers backup functionality for Amazon Timestream.

### [Virtual machine backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/vm-backups.html)

VMware virtual machine backups.

- [Backup gateway configuration](https://docs.aws.amazon.com/aws-backup/latest/devguide/configure-infrastructure-bgw.html): Learn how to configure your infrastructure to use Backup gateway
- [Working with gateways](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-gateways.html): Learn about Backup gateway
- [Working with hypervisors](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-hypervisors.html): Learn about hypervisors
- [Backing up virtual machines](https://docs.aws.amazon.com/aws-backup/latest/devguide/backing-up-vms.html): Learn about backing up virtual machines
- [Third-party source components](https://docs.aws.amazon.com/aws-backup/latest/devguide/bgw-third-party-source.html): Learn about the third-party source components for Backup gateway
- [Troubleshoot VM issues](https://docs.aws.amazon.com/aws-backup/latest/devguide/vm-troubleshooting.html): Troubleshoot VM issues for AWS Backup.
- [Create Windows VSS backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html): Create application-specific Windows backups on Amazon EC2 using AWS Backup.

### [Backup and tag copy](https://docs.aws.amazon.com/aws-backup/latest/devguide/recov-point-create-a-copy.html)

Copy a backup using AWS Backup.

- [Cross-Region backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html): Create a backup copy across Regions using AWS Backup.
- [Cross-account backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html): Create a backup copy across AWS accounts using AWS Backup.
- [Copy tags onto backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/tags-on-backups.html): You can copy tags from your source resources to your backups (recovery points).
- [Backup deletion](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html): Delete one or more backups in AWS Backup automatically using lifecycle rules or manually using the console.
- [Backup and tag edits](https://docs.aws.amazon.com/aws-backup/latest/devguide/editing-a-backup.html): Edit the tags or lifecycle of a backup job after it is created in AWS Backup.
- [Backup search](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-search.html): This page discusses backup search and backup index topics and procedures.
- [Backup tiering](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-tiering.html): Create tiering configurations to move backups to a lower cost storage tier.

### [Restore by resource type](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-a-backup.html)

Restore a backup in AWS Backup using the console, AWS CLI, or API.

- [Aurora restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-aur.html): Aurora cluster restore
- [Aurora DSQL restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-auroradsql.html): Restore Aurora DSQL cluster recovery points
- [CloudFormation restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-application-stacks.html): A CloudFormation composite backup is a combination of a CloudFormation template and all associated nested recovery points.
- [DocumentDB restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-docdb.html): Restore a Amazon DocumentDB cluster.
- [DynamoDB restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-dynamodb.html): Restore Amazon DynamoDB
- [EBS restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-ebs.html): Restore an Amazon EBS volume.
- [EC2 restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-ec2.html): Restore an Amazon EC2 instance.
- [EFS restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-efs.html): Restore an Amazon EFS file system by performing a full restore or an item-level restore in AWS Backup.
- [EKS restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-eks.html): Restore an Amazon EKS cluster.
- [FSx restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-fsx.html): Restore an Amazon FSx file system.
- [Neptune restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-nep.html): Restore a Amazon Neptune cluster.
- [RDS restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-rds.html): Restore an Amazon RDS database.
- [Redshift restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-restores.html): Restore an Amazon Redshift cluster
- [Redshift Serverless restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-serverless-restore.html): Learn how to restore manual snapshots of databases or tables from Amazon Redshift Serverless using AWS Backup.
- [SAP HANA restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/saphana-restore.html): Restore an SAP HANA database on an Amazon EC2 instance
- [S3 restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-s3.html): Amazon S3 bucket restore
- [Storage Gateway restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-storage-gateway.html): Restore an AWS Storage Gateway volume
- [Timestream restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/timestream-restore.html): Restore a Amazon Timestream table
- [VM restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-vm.html): Restore a virtual machine

### [Restore testing](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html)

Restore testing, a feature offered by AWS Backup, provides automated and periodic evaluation of restore viability, as well as the ability to monitor restore job duration times.

- [Inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html): Restoring a recovery point requires restore metadata.
- [Restore testing validation](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-validation.html): You have the option of creating an event-driven validation that runs when a restore testing job completes.
- [Stop a backup job](https://docs.aws.amazon.com/aws-backup/latest/devguide/stopping-a-backup-job.html): Stop a backup job after it has started in AWS Backup.
- [View existing backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/listing-backups.html): You can view a list of your backups using the AWS Backup console or programmatically.


## [AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html)

### [Working with audit frameworks](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-audit-frameworks.html)

Learn how to work with AWS Backup Audit Manager frameworks, controls, and parameters.

- [Choosing your controls](https://docs.aws.amazon.com/aws-backup/latest/devguide/choosing-controls.html): Choose controls for your AWS Backup Audit Manager audit frameworks.
- [Turning on resource tracking](https://docs.aws.amazon.com/aws-backup/latest/devguide/turning-on-resource-tracking.html): Turn on resource tracking to use your AWS Backup Audit Manager audit frameworks.
- [Creating frameworks using the AWS Backup console](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-frameworks-console.html): Create AWS Backup Audit Manager frameworks using the AWS Backup console.
- [Creating frameworks using the AWS Backup API](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-frameworks-api.html): Create AWS Backup Audit Manager frameworks using the AWS Backup API.
- [Viewing framework compliance status](https://docs.aws.amazon.com/aws-backup/latest/devguide/viewing-frameworks.html): View AWS Backup Audit Manager framework compliance status.
- [Finding non-compliant resources](https://docs.aws.amazon.com/aws-backup/latest/devguide/finding-non-compliant-resources.html): Find resources that are not yet compliant with AWS Backup Audit Manager frameworks.
- [Updating audit frameworks](https://docs.aws.amazon.com/aws-backup/latest/devguide/updating-frameworks.html): Update AWS Backup Audit Manager frameworks.
- [Deleting audit frameworks](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-frameworks.html): Delete AWS Backup Audit Manager frameworks.

### [Working with audit reports](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-audit-reports.html)

Work with AWS Backup Audit Manager reports.

- [Choosing your report template](https://docs.aws.amazon.com/aws-backup/latest/devguide/choosing-report-template.html): Choose the right report template for your AWS Backup Audit Manager reports.
- [Creating report plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-report-plan-console.html): Create a report plan for your AWS Backup Audit Manager reports using the AWS Backup console.
- [Creating report plans using the AWS Backup API](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-report-plan-api.html): Create a report plan for your AWS Backup Audit Manager reports using the AWS Backup API.
- [Creating on-demand reports](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-on-demand-reports.html): Create AWS Backup Audit Manager reports on-demand.
- [Viewing audit reports](https://docs.aws.amazon.com/aws-backup/latest/devguide/view-reports.html): View an AWS Backup Audit Manager report.
- [Updating report plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/update-report-plan.html): Update an AWS Backup Audit Manager report plan.
- [Deleting report plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/delete-report-plan.html): Delete an AWS Backup Audit Manager report plan.
- [Using CloudFormation to deploy AWS Backup Audit Manager resources](https://docs.aws.amazon.com/aws-backup/latest/devguide/bam-cfn-integration.html): Deploy your AWS Backup Audit Manager frameworks and report plans using CloudFormation.
- [Using AWS Backup Audit Manager with AWS Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-audit-manager-integration.html): Import your AWS Backup Audit Manager compliance findings to your AWS Audit Manager reports.
- [Controls and remediation](https://docs.aws.amazon.com/aws-backup/latest/devguide/controls-and-remediation.html): View the list of available AWS Backup Audit Manager controls and guidance to remediate resources not yet in compliance with those controls.


## [Security](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-considerations.html)

- [Compliance validation](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-compliance.html): Learn what AWS services are in scope of a specific compliance program.

### [Data protection](https://docs.aws.amazon.com/aws-backup/latest/devguide/data-protection.html)

Use and configure data protection in AWS Backup to meet the needs of your organization.

- [Encryption for backups in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html): Protect your backups by configuring encryption for various AWS services in AWS Backup.
- [Virtual machine hypervisor credential encryption](https://docs.aws.amazon.com/aws-backup/latest/devguide/bgw-hypervisor-encryption-page.html): Virtual machines managed by a hypervisor use AWS Backup Gateway to connect on-premises systems to AWS Backup.

### [Identity and access management](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-iam.html)

Access to AWS Backup requires credentials.

- [Authentication](https://docs.aws.amazon.com/aws-backup/latest/devguide/authentication.html): Overview of how to authenticate requests in AWS Backup.
- [Access control](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html): Overview of how to control access to resources in AWS Backup, including an API permissions reference and information about using managed policies.
- [IAM service roles](https://docs.aws.amazon.com/aws-backup/latest/devguide/iam-service-roles.html): Use IAM service roles to control access to backups and other resources in AWS Backup.
- [Managed policies](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Backup and recent changes to these policies.

### [Using service-linked roles](https://docs.aws.amazon.com/aws-backup/latest/devguide/using-service-linked-roles.html)

How to use service-linked roles to give AWS Backup access to resources in your AWS account.

- [Backup and copy](https://docs.aws.amazon.com/aws-backup/latest/devguide/using-service-linked-roles-AWSServiceRoleForBackup.html): How to use service-linked roles to give AWS Backup access to resources in your AWS account.
- [AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/using-service-linked-roles-AWSServiceRoleForBackupReports.html): How to use service-linked roles to give AWS Backup access to resources in your AWS account.
- [Restore testing](https://docs.aws.amazon.com/aws-backup/latest/devguide/using-service-linked-roles-AWSServiceRoleForBackupRestoreTesting.html): How to use service-linked roles to give AWS Backup access to resources in your AWS account.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Infrastructure security](https://docs.aws.amazon.com/aws-backup/latest/devguide/infrastructure-security.html): Learn how AWS Backup isolates service traffic.
- [Integrity](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-integrity.html)
- [Legal holds](https://docs.aws.amazon.com/aws-backup/latest/devguide/legalhold.html): Learn how to protect your backups from deletion using legal holds.

### [Malware protection](https://docs.aws.amazon.com/aws-backup/latest/devguide/malware-protection.html)

Protect your backups by scanning for malware using Amazon GuardDuty Malware Protection.

- [Instant access](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-instant-access.html): Overview of Access Point Permissions
- [Resilience](https://docs.aws.amazon.com/aws-backup/latest/devguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy in addition to specific AWS Backup features for data resiliency.


## [Monitoring AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html)

- [Console dashboards](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-dashboards.html): AWS Backup provides dashboards in the AWS Backup console to help you monitor the health of your backup, copy, and restore jobs to identify issues and potential problems.
- [Monitoring events using EventBridge](https://docs.aws.amazon.com/aws-backup/latest/devguide/eventbridge.html): Track changes in the AWS Backup environment using Amazon EventBridge events.
- [AWS Backup metrics with Amazon CloudWatch](https://docs.aws.amazon.com/aws-backup/latest/devguide/cloudwatch.html): Learn about the metrics that AWS Backup sends to Amazon CloudWatch.
- [Logging AWS Backup API calls with CloudTrail](https://docs.aws.amazon.com/aws-backup/latest/devguide/logging-using-cloudtrail.html): Capture detailed information about the logs and calls made to AWS Backup using AWS CloudTrail.
- [Notification options with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html): Receive notifications about AWS Backup through AWS User Notifications and Amazon Simple Notification Service.


## [AWS Backup API](https://docs.aws.amazon.com/aws-backup/latest/devguide/api-reference.html)

### [Actions](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Operations.html)

The following actions are supported by AWS Backup:

### [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Operations_AWS_Backup.html)

The following actions are supported by AWS Backup:

- [AssociateBackupVaultMpaApprovalTeam](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_AssociateBackupVaultMpaApprovalTeam.html): Associates an MPA approval team with a backup vault.
- [CancelLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CancelLegalHold.html): Removes the specified legal hold on a recovery point.
- [CreateBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateBackupPlan.html): Creates a backup plan using a backup plan name and backup rules.
- [CreateBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateBackupSelection.html): Creates a JSON document that specifies a set of resources to assign to a backup plan.
- [CreateBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateBackupVault.html): Creates a logical container where backups are stored.
- [CreateFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateFramework.html): Creates a framework with one or more controls.
- [CreateLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateLegalHold.html): Creates a legal hold on a recovery point (backup).
- [CreateLogicallyAirGappedBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateLogicallyAirGappedBackupVault.html): Creates a logical container to where backups may be copied.
- [CreateReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateReportPlan.html): Creates a report plan.
- [CreateRestoreAccessBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateRestoreAccessBackupVault.html): Creates a restore access backup vault that provides temporary access to recovery points in a logically air-gapped backup vault, subject to MPA approval.
- [CreateRestoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateRestoreTestingPlan.html): Creates a restore testing plan.
- [CreateRestoreTestingSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateRestoreTestingSelection.html): This request can be sent after CreateRestoreTestingPlan request returns successfully.
- [CreateTieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateTieringConfiguration.html): Creates a tiering configuration.
- [DeleteBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupPlan.html): Deletes a backup plan.
- [DeleteBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupSelection.html): Deletes the resource selection associated with a backup plan that is specified by the SelectionId.
- [DeleteBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupVault.html): Deletes the backup vault identified by its name.
- [DeleteBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupVaultAccessPolicy.html): Deletes the policy document that manages permissions on a backup vault.
- [DeleteBackupVaultLockConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupVaultLockConfiguration.html): Deletes AWS Backup Vault Lock from a backup vault specified by a backup vault name.
- [DeleteBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteBackupVaultNotifications.html): Deletes event notifications for the specified backup vault.
- [DeleteFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteFramework.html): Deletes the framework specified by a framework name.
- [DeleteRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteRecoveryPoint.html): Deletes the recovery point specified by a recovery point ID.
- [DeleteReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteReportPlan.html): Deletes the report plan specified by a report plan name.
- [DeleteRestoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteRestoreTestingPlan.html): This request deletes the specified restore testing plan.
- [DeleteRestoreTestingSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteRestoreTestingSelection.html): Input the Restore Testing Plan name and Restore Testing Selection name.
- [DeleteTieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DeleteTieringConfiguration.html): Deletes the tiering configuration specified by a tiering configuration name.
- [DescribeBackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeBackupJob.html): Returns backup job details for the specified BackupJobId.
- [DescribeBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeBackupVault.html): Returns metadata about a backup vault specified by its name.
- [DescribeCopyJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeCopyJob.html): Returns metadata associated with creating a copy of a resource.
- [DescribeFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeFramework.html): Returns the framework details for the specified FrameworkName.
- [DescribeGlobalSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeGlobalSettings.html): Describes whether the AWS account has enabled different cross-account management options, including cross-account backup, multi-party approval, and delegated administrator.
- [DescribeProtectedResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeProtectedResource.html): Returns information about a saved resource, including the last time it was backed up, its Amazon Resource Name (ARN), and the AWS service type of the saved resource.
- [DescribeRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRecoveryPoint.html): Returns metadata associated with a recovery point, including ID, status, encryption, and lifecycle.
- [DescribeRegionSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRegionSettings.html): Returns the current service opt-in settings for the Region.
- [DescribeReportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeReportJob.html): Returns the details associated with creating a report as specified by its ReportJobId.
- [DescribeReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeReportPlan.html): Returns a list of all report plans for an AWS account and AWS Region.
- [DescribeRestoreJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRestoreJob.html): Returns metadata associated with a restore job that is specified by a job ID.
- [DescribeScanJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeScanJob.html): Returns scan job details for the specified ScanJobID.
- [DisassociateBackupVaultMpaApprovalTeam](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DisassociateBackupVaultMpaApprovalTeam.html): Removes the association between an MPA approval team and a backup vault, disabling the MPA approval workflow for restore operations.
- [DisassociateRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DisassociateRecoveryPoint.html): Deletes the specified continuous backup recovery point from AWS Backup and releases control of that continuous backup to the source service, such as Amazon RDS.
- [DisassociateRecoveryPointFromParent](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DisassociateRecoveryPointFromParent.html): This action to a specific child (nested) recovery point removes the relationship between the specified recovery point and its parent (composite) recovery point.
- [ExportBackupPlanTemplate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ExportBackupPlanTemplate.html): Returns the backup plan that is specified by the plan ID as a backup template.
- [GetBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupPlan.html): Returns BackupPlan details for the specified BackupPlanId.
- [GetBackupPlanFromJSON](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupPlanFromJSON.html): Returns a valid JSON document specifying a backup plan or an error.
- [GetBackupPlanFromTemplate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupPlanFromTemplate.html): Returns the template specified by its templateId as a backup plan.
- [GetBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupSelection.html): Returns selection metadata and a document in JSON format that specifies a list of resources that are associated with a backup plan.
- [GetBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupVaultAccessPolicy.html): Returns the access policy document that is associated with the named backup vault.
- [GetBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetBackupVaultNotifications.html): Returns event notifications for the specified backup vault.
- [GetLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetLegalHold.html): This action returns details for a specified legal hold.
- [GetRecoveryPointIndexDetails](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRecoveryPointIndexDetails.html): This operation returns the metadata and details specific to the backup index associated with the specified recovery point.
- [GetRecoveryPointRestoreMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRecoveryPointRestoreMetadata.html): Returns a set of metadata key-value pairs that were used to create the backup.
- [GetRestoreJobMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreJobMetadata.html): This request returns the metadata for the specified restore job.
- [GetRestoreTestingInferredMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreTestingInferredMetadata.html): This request returns the minimal required set of metadata needed to start a restore job with secure default settings.
- [GetRestoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreTestingPlan.html): Returns RestoreTestingPlan details for the specified RestoreTestingPlanName.
- [GetRestoreTestingSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetRestoreTestingSelection.html): Returns RestoreTestingSelection, which displays resources and elements of the restore testing plan.
- [GetSupportedResourceTypes](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetSupportedResourceTypes.html): Returns the AWS resource types supported by AWS Backup.
- [GetTieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_GetTieringConfiguration.html): Returns TieringConfiguration details for the specified TieringConfigurationName.
- [ListBackupJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupJobs.html): Returns a list of existing backup jobs for an authenticated account for the last 30 days.
- [ListBackupJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupJobSummaries.html): This is a request for a summary of backup jobs created or running within the most recent 30 days.
- [ListBackupPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlans.html): Lists the active backup plans for the account.
- [ListBackupPlanTemplates](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlanTemplates.html): Lists the backup plan templates.
- [ListBackupPlanVersions](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlanVersions.html): Returns version metadata of your backup plans, including Amazon Resource Names (ARNs), backup plan IDs, creation and deletion dates, plan names, and version IDs.
- [ListBackupSelections](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupSelections.html): Returns an array containing metadata of the resources associated with the target backup plan.
- [ListBackupVaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupVaults.html): Returns a list of recovery point storage containers along with information about them.
- [ListCopyJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListCopyJobs.html): Returns metadata about your copy jobs.
- [ListCopyJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListCopyJobSummaries.html): This request obtains a list of copy jobs created or running within the the most recent 30 days.
- [ListFrameworks](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListFrameworks.html): Returns a list of all frameworks for an AWS account and AWS Region.
- [ListIndexedRecoveryPoints](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListIndexedRecoveryPoints.html): This operation returns a list of recovery points that have an associated index, belonging to the specified account.
- [ListLegalHolds](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListLegalHolds.html): This action returns metadata about active and previous legal holds.
- [ListProtectedResources](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListProtectedResources.html): Returns an array of resources successfully backed up by AWS Backup, including the time the resource was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.
- [ListProtectedResourcesByBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListProtectedResourcesByBackupVault.html): This request lists the protected resources corresponding to each backup vault.
- [ListRecoveryPointsByBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByBackupVault.html): Returns detailed information about the recovery points stored in a backup vault.
- [ListRecoveryPointsByLegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByLegalHold.html): This action returns recovery point ARNs (Amazon Resource Names) of the specified legal hold.
- [ListRecoveryPointsByResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRecoveryPointsByResource.html): The information about the recovery points of the type specified by a resource Amazon Resource Name (ARN).
- [ListReportJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListReportJobs.html): Returns details about your report jobs.
- [ListReportPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListReportPlans.html): Returns a list of your report plans.
- [ListRestoreAccessBackupVaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreAccessBackupVaults.html): Returns a list of restore access backup vaults associated with a specified backup vault.
- [ListRestoreJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreJobs.html): Returns a list of jobs that AWS Backup initiated to restore a saved resource, including details about the recovery process.
- [ListRestoreJobsByProtectedResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreJobsByProtectedResource.html): This returns restore jobs that contain the specified protected resource.
- [ListRestoreJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreJobSummaries.html): This request obtains a summary of restore jobs created or running within the the most recent 30 days.
- [ListRestoreTestingPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreTestingPlans.html): Returns a list of restore testing plans.
- [ListRestoreTestingSelections](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListRestoreTestingSelections.html): Returns a list of restore testing selections.
- [ListScanJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListScanJobs.html): Returns a list of existing scan jobs for an authenticated account for the last 30 days.
- [ListScanJobSummaries](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListScanJobSummaries.html): This is a request for a summary of scan jobs created or running within the most recent 30 days.
- [ListTags](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListTags.html): Returns the tags assigned to the resource, such as a target recovery point, backup plan, or backup vault.
- [ListTieringConfigurations](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListTieringConfigurations.html): Returns a list of tiering configurations.
- [PutBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultAccessPolicy.html): Sets a resource-based policy that is used to manage access permissions on the target backup vault.
- [PutBackupVaultLockConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultLockConfiguration.html): Applies AWS Backup Vault Lock to a backup vault, preventing attempts to delete any recovery point stored in or created in a backup vault.
- [PutBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultNotifications.html): Turns on notifications on a backup vault for the specified topic and events.
- [PutRestoreValidationResult](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutRestoreValidationResult.html): This request allows you to send your independent self-run restore test validation results.
- [RevokeRestoreAccessBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RevokeRestoreAccessBackupVault.html): Revokes access to a restore access backup vault, removing the ability to restore from its recovery points and permanently deleting the vault.
- [StartBackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartBackupJob.html): Starts an on-demand backup job for the specified resource.
- [StartCopyJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartCopyJob.html): Starts a job to create a one-time copy of the specified resource.
- [StartReportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartReportJob.html): Starts an on-demand report job for the specified report plan.
- [StartRestoreJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartRestoreJob.html): Recovers the saved resource identified by an Amazon Resource Name (ARN).
- [StartScanJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartScanJob.html): Starts scanning jobs for specific resources.
- [StopBackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StopBackupJob.html): Attempts to cancel a job to create a one-time backup of a resource.
- [TagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_TagResource.html): Assigns a set of key-value pairs to a resource.
- [UntagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UntagResource.html): Removes a set of key-value pairs from a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN)
- [UpdateBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateBackupPlan.html): Updates the specified backup plan.
- [UpdateFramework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateFramework.html): Updates the specified framework.
- [UpdateGlobalSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateGlobalSettings.html): Updates whether the AWS account has enabled different cross-account management options, including cross-account backup, multi-party approval, and delegated administrator.
- [UpdateRecoveryPointIndexSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRecoveryPointIndexSettings.html): This operation updates the settings of a recovery point index.
- [UpdateRecoveryPointLifecycle](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRecoveryPointLifecycle.html): Sets the transition lifecycle of a recovery point.
- [UpdateRegionSettings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRegionSettings.html): Updates the current service opt-in settings for the Region.
- [UpdateReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateReportPlan.html): Updates the specified report plan.
- [UpdateRestoreTestingPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRestoreTestingPlan.html): This request will send changes to your specified restore testing plan.
- [UpdateRestoreTestingSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRestoreTestingSelection.html): Updates the specified restore testing selection.
- [UpdateTieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateTieringConfiguration.html): This request will send changes to your specified tiering configuration.

### [AWS Backup gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Operations_AWS_Backup_Gateway.html)

The following actions are supported by AWS Backup gateway:

- [AssociateGatewayToServer](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_AssociateGatewayToServer.html): Associates a backup gateway with your server.
- [CreateGateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_CreateGateway.html): Creates a backup gateway.
- [DeleteGateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_DeleteGateway.html): Deletes a backup gateway.
- [DeleteHypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_DeleteHypervisor.html): Deletes a hypervisor.
- [DisassociateGatewayFromServer](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_DisassociateGatewayFromServer.html): Disassociates a backup gateway from the specified server.
- [GetBandwidthRateLimitSchedule](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetBandwidthRateLimitSchedule.html): Retrieves the bandwidth rate limit schedule for a specified gateway.
- [GetGateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetGateway.html): By providing the ARN (Amazon Resource Name), this API returns the gateway.
- [GetHypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetHypervisor.html): This action requests information about the specified hypervisor to which the gateway will connect.
- [GetHypervisorPropertyMappings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetHypervisorPropertyMappings.html): This action retrieves the property mappings for the specified hypervisor.
- [GetVirtualMachine](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetVirtualMachine.html): By providing the ARN (Amazon Resource Name), this API returns the virtual machine.
- [ImportHypervisorConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ImportHypervisorConfiguration.html): Connect to a hypervisor by importing its configuration.
- [ListGateways](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListGateways.html): Lists backup gateways owned by an AWS account in an AWS Region.
- [ListHypervisors](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListHypervisors.html): Lists your hypervisors.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListTagsForResource.html): Lists the tags applied to the resource identified by its Amazon Resource Name (ARN).
- [ListVirtualMachines](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListVirtualMachines.html): Lists your virtual machines.
- [PutBandwidthRateLimitSchedule](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_PutBandwidthRateLimitSchedule.html): This action sets the bandwidth rate limit schedule for a specified gateway.
- [PutHypervisorPropertyMappings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_PutHypervisorPropertyMappings.html): This action sets the property mappings for the specified hypervisor.
- [PutMaintenanceStartTime](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_PutMaintenanceStartTime.html): Set the maintenance start time for a gateway.
- [StartVirtualMachinesMetadataSync](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_StartVirtualMachinesMetadataSync.html): This action sends a request to sync metadata across the specified virtual machines.
- [TagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_TagResource.html): Tag the resource.
- [TestHypervisorConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_TestHypervisorConfiguration.html): Tests your hypervisor configuration to validate that backup gateway can connect with the hypervisor and its resources.
- [UntagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_UntagResource.html): Removes tags from the resource.
- [UpdateGatewayInformation](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_UpdateGatewayInformation.html): Updates a gateway's name.
- [UpdateGatewaySoftwareNow](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_UpdateGatewaySoftwareNow.html): Updates the gateway virtual machine (VM) software.
- [UpdateHypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_UpdateHypervisor.html): Updates a hypervisor metadata, including its host, username, and password.

### [AWS Backup search](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Operations_AWS_Backup_Search.html)

The following actions are supported by AWS Backup search:

- [GetSearchJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_GetSearchJob.html): This operation retrieves metadata of a search job, including its progress.
- [GetSearchResultExportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_GetSearchResultExportJob.html): This operation retrieves the metadata of an export job.
- [ListSearchJobBackups](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListSearchJobBackups.html): This operation returns a list of all backups (recovery points) in a paginated format that were included in the search job.
- [ListSearchJobResults](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListSearchJobResults.html): This operation returns a list of a specified search job.
- [ListSearchJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListSearchJobs.html): This operation returns a list of search jobs belonging to an account.
- [ListSearchResultExportJobs](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListSearchResultExportJobs.html): This operation exports search results of a search job to a specified destination S3 bucket.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ListTagsForResource.html): This operation returns the tags for a resource type.
- [StartSearchJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_StartSearchJob.html): This operation creates a search job which returns recovery points filtered by SearchScope and items filtered by ItemFilters.
- [StartSearchResultExportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_StartSearchResultExportJob.html): This operations starts a job to export the results of search job to a designated S3 bucket.
- [StopSearchJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_StopSearchJob.html): This operations ends a search job.
- [TagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_TagResource.html): This operation puts tags on the resource you indicate.
- [UntagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_UntagResource.html): This operation removes tags from the specified resource.

### [Data Types](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Types.html)

The following data types are supported by AWS Backup:

### [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Types_AWS_Backup.html)

The following data types are supported by AWS Backup:

- [AdvancedBackupSetting](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_AdvancedBackupSetting.html): The backup options for each resource type.
- [AggregatedScanResult](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_AggregatedScanResult.html): Contains aggregated scan results across multiple scan operations, providing a summary of scan status and findings.
- [BackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupJob.html): Contains detailed information about a backup job.
- [BackupJobSummary](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupJobSummary.html): This is a summary of jobs created or running within the most recent 30 days.
- [BackupPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupPlan.html): Contains an optional backup plan display name and an array of BackupRule objects, each of which specifies a backup rule.
- [BackupPlanInput](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupPlanInput.html): Contains an optional backup plan display name and an array of BackupRule objects, each of which specifies a backup rule.
- [BackupPlansListMember](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupPlansListMember.html): Contains metadata about a backup plan.
- [BackupPlanTemplatesListMember](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupPlanTemplatesListMember.html): An object specifying metadata associated with a backup plan template.
- [BackupRule](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupRule.html): Specifies a scheduled task used to back up a selection of resources.
- [BackupRuleInput](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupRuleInput.html): Specifies a scheduled task used to back up a selection of resources.
- [BackupSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupSelection.html): Used to specify a set of resources to a backup plan.
- [BackupSelectionsListMember](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupSelectionsListMember.html): Contains metadata about a BackupSelection object.
- [BackupVaultListMember](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupVaultListMember.html): Contains metadata about a backup vault.
- [CalculatedLifecycle](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CalculatedLifecycle.html): Contains DeleteAt and MoveToColdStorageAt timestamps, which are used to specify a lifecycle for a recovery point.
- [Condition](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Condition.html): Contains an array of triplets made up of a condition type (such as StringEquals), a key, and a value.
- [ConditionParameter](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ConditionParameter.html): Includes information about tags you define to assign tagged resources to a backup plan.
- [Conditions](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Conditions.html): Contains information about which resources to include or exclude from a backup plan using their tags.
- [ControlInputParameter](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlInputParameter.html): The parameters for a control.
- [ControlScope](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlScope.html): A framework consists of one or more controls.
- [CopyAction](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CopyAction.html): The details of the copy operation.
- [CopyJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CopyJob.html): Contains detailed information about a copy job.
- [CopyJobSummary](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CopyJobSummary.html): This is a summary of copy jobs created or running within the most recent 30 days.
- [DateRange](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DateRange.html): This is a resource filter containing FromDate: DateTime and ToDate: DateTime.
- [Framework](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Framework.html): Contains detailed information about a framework.
- [FrameworkControl](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_FrameworkControl.html): Contains detailed information about all of the controls of a framework.
- [IndexAction](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_IndexAction.html): This is an optional array within a BackupRule.
- [IndexedRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_IndexedRecoveryPoint.html): This is a recovery point that has an associated backup index.
- [KeyValue](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_KeyValue.html): Pair of two related strings.
- [LatestMpaApprovalTeamUpdate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_LatestMpaApprovalTeamUpdate.html): Contains information about the latest update to an MPA approval team association.
- [LatestRevokeRequest](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_LatestRevokeRequest.html): Contains information about the latest request to revoke access to a backup vault.
- [LegalHold](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_LegalHold.html): A legal hold is an administrative tool that helps prevent backups from being deleted while under a hold.
- [Lifecycle](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Lifecycle.html): Specifies the time period, in days, before a recovery point transitions to cold storage or is deleted.
- [ProtectedResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ProtectedResource.html): A structure that contains information about a backed-up resource.
- [ProtectedResourceConditions](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ProtectedResourceConditions.html): The conditions that you define for resources in your restore testing plan using tags.
- [RecoveryPointByBackupVault](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RecoveryPointByBackupVault.html): Contains detailed information about the recovery points stored in a backup vault.
- [RecoveryPointByResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RecoveryPointByResource.html): Contains detailed information about a saved recovery point.
- [RecoveryPointCreator](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RecoveryPointCreator.html): Contains information about the backup plan and rule that AWS Backup used to initiate the recovery point backup.
- [RecoveryPointMember](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RecoveryPointMember.html): This is a recovery point which is a child (nested) recovery point of a parent (composite) recovery point.
- [RecoveryPointSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RecoveryPointSelection.html): This specifies criteria to assign a set of resources, such as resource types or backup vaults.
- [ReportDeliveryChannel](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ReportDeliveryChannel.html): Contains information from your report plan about where to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
- [ReportDestination](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ReportDestination.html): Contains information from your report job about your report destination.
- [ReportJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ReportJob.html): Contains detailed information about a report job.
- [ReportPlan](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ReportPlan.html): Contains detailed information about a report plan.
- [ReportSetting](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ReportSetting.html): Contains detailed information about a report setting.
- [ResourceSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ResourceSelection.html): This contains metadata about resource selection for tiering configurations.
- [RestoreAccessBackupVaultListMember](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreAccessBackupVaultListMember.html): Contains information about a restore access backup vault.
- [RestoreJobCreator](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreJobCreator.html): Contains information about the restore testing plan that AWS Backup used to initiate the restore job.
- [RestoreJobsListMember](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreJobsListMember.html): Contains metadata about a restore job.
- [RestoreJobSummary](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreJobSummary.html): This is a summary of restore jobs created or running within the most recent 30 days.
- [RestoreTestingPlanForCreate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreTestingPlanForCreate.html): This contains metadata about a restore testing plan.
- [RestoreTestingPlanForGet](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreTestingPlanForGet.html): This contains metadata about a restore testing plan.
- [RestoreTestingPlanForList](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreTestingPlanForList.html): This contains metadata about a restore testing plan.
- [RestoreTestingPlanForUpdate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreTestingPlanForUpdate.html): This contains metadata about a restore testing plan.
- [RestoreTestingRecoveryPointSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreTestingRecoveryPointSelection.html): RecoveryPointSelection has five parameters (three required and two optional).
- [RestoreTestingSelectionForCreate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreTestingSelectionForCreate.html): This contains metadata about a specific restore testing selection.
- [RestoreTestingSelectionForGet](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreTestingSelectionForGet.html): This contains metadata about a restore testing selection.
- [RestoreTestingSelectionForList](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreTestingSelectionForList.html): This contains metadata about a restore testing selection.
- [RestoreTestingSelectionForUpdate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_RestoreTestingSelectionForUpdate.html): This contains metadata about a restore testing selection.
- [ScanAction](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ScanAction.html): Defines a scanning action that specifies the malware scanner and scan mode to use.
- [ScanJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ScanJob.html): Contains metadata about a scan job, including information about the scanning process, results, and associated resources.
- [ScanJobCreator](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ScanJobCreator.html): Contains identifying information about the creation of a scan job, including the backup plan and rule that initiated the scan.
- [ScanJobSummary](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ScanJobSummary.html): Contains summary information about scan jobs, including counts and metadata for a specific time period and criteria.
- [ScanResult](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ScanResult.html): Contains the results of a security scan, including scanner information, scan state, and any findings discovered.
- [ScanResultInfo](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ScanResultInfo.html): Contains information about the results of a scan job.
- [ScanSetting](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ScanSetting.html): Contains configuration settings for malware scanning, including the scanner type, target resource types, and scanner role.
- [ScheduledPlanExecutionMember](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ScheduledPlanExecutionMember.html): Contains information about a scheduled backup plan execution, including the execution time, rule type, and associated rule identifier.
- [TieringConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_TieringConfiguration.html): This contains metadata about a tiering configuration.
- [TieringConfigurationInputForCreate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_TieringConfigurationInputForCreate.html): This contains metadata about a tiering configuration for create operations.
- [TieringConfigurationInputForUpdate](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_TieringConfigurationInputForUpdate.html): This contains metadata about a tiering configuration for update operations.
- [TieringConfigurationsListMember](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_TieringConfigurationsListMember.html): This contains metadata about a tiering configuration returned in a list.

### [AWS Backup gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Types_AWS_Backup_Gateway.html)

The following data types are supported by AWS Backup gateway:

- [BandwidthRateLimitInterval](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_BandwidthRateLimitInterval.html): Describes a bandwidth rate limit interval for a gateway.
- [Gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Gateway.html): A gateway is an AWS Backup Gateway appliance that runs on the customer's network to provide seamless connectivity to backup storage in the AWS Cloud.
- [GatewayDetails](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GatewayDetails.html): The details of gateway.
- [Hypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Hypervisor.html): Represents the hypervisor's permissions to which the gateway will connect.
- [HypervisorDetails](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_HypervisorDetails.html): These are the details of the specified hypervisor.
- [MaintenanceStartTime](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_MaintenanceStartTime.html): This is your gateway's weekly maintenance start time including the day and time of the week.
- [Tag](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Tag.html): A key-value pair you can use to manage, filter, and search for your resources.
- [VirtualMachine](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_VirtualMachine.html): A virtual machine that is on a hypervisor.
- [VirtualMachineDetails](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_VirtualMachineDetails.html): Your VirtualMachine objects, ordered by their Amazon Resource Names (ARNs).
- [VmwareTag](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_VmwareTag.html): A VMware tag is a tag attached to a specific virtual machine.
- [VmwareToAwsTagMapping](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_VmwareToAwsTagMapping.html): This displays the mapping of VMware tags to the corresponding AWS tags.

### [AWS Backup search](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Types_AWS_Backup_Search.html)

The following data types are supported by AWS Backup search:

- [BackupCreationTimeFilter](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_BackupCreationTimeFilter.html): This filters by recovery points within the CreatedAfter and CreatedBefore timestamps.
- [CurrentSearchProgress](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_CurrentSearchProgress.html): This contains information results retrieved from a search job that may not have completed.
- [EBSItemFilter](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_EBSItemFilter.html): This contains arrays of objects, which may include CreationTimes time condition objects, FilePaths string objects, LastModificationTimes time condition objects,
- [EBSResultItem](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_EBSResultItem.html): These are the items returned in the results of a search of Amazon EBS backup metadata.
- [ExportJobSummary](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ExportJobSummary.html): This is the summary of an export job.
- [ExportSpecification](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ExportSpecification.html): This contains the export specification object.
- [ItemFilters](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ItemFilters.html): Item Filters represent all input item properties specified when the search was created.
- [LongCondition](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_LongCondition.html): The long condition contains a Value and can optionally contain an Operator.
- [ResultItem](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_ResultItem.html): This is an object representing the item returned in the results of a search for a specific resource type.
- [S3ExportSpecification](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_S3ExportSpecification.html): This specification contains a required string of the destination bucket; optionally, you can include the destination prefix.
- [S3ItemFilter](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_S3ItemFilter.html): This contains arrays of objects, which may include ObjectKeys, Sizes, CreationTimes, VersionIds, and/or Etags.
- [S3ResultItem](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_S3ResultItem.html): These are the items returned in the results of a search of Amazon S3 backup metadata.
- [SearchJobBackupsResult](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_SearchJobBackupsResult.html): This contains the information about recovery points returned in results of a search job.
- [SearchJobSummary](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_SearchJobSummary.html): This is information pertaining to a search job.
- [SearchScope](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_SearchScope.html): The search scope is all backup properties input into a search.
- [SearchScopeSummary](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_SearchScopeSummary.html): The summary of the specified search job scope, including:
- [StringCondition](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_StringCondition.html): This contains the value of the string and can contain one or more operators.
- [TimeCondition](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BKS_TimeCondition.html): A time condition denotes a creation time, last modification time, or other time.
- [Common Parameters](https://docs.aws.amazon.com/aws-backup/latest/devguide/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
- [Common Errors](https://docs.aws.amazon.com/aws-backup/latest/devguide/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
