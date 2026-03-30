# Source: https://docs.aws.amazon.com/fsx/latest/LustreGuide/llms.txt

# FSx for Lustre Lustre User Guide

> Amazon FSx provides fully managed third-party file systems with the native compatibility of third-party file systems with feature sets for workloads such as Microsoft Windowsâbased storage, high-performance computing, machine learning, and electronic design automation. Amazon FSx supports multiple file system types: Lustre, Windows File Server, and NetApp ONTAP. The Amazon FSx for Lustre User Guide describes key concepts for FSx for Lustre and provides instructions for launching and using your file system.

- [What is Amazon FSx for Lustre?](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)
- [Setting up](https://docs.aws.amazon.com/fsx/latest/LustreGuide/setting-up.html)
- [Getting started](https://docs.aws.amazon.com/fsx/latest/LustreGuide/getting-started.html)
- [Deployment and storage class options](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html)
- [Migrating to FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/migrating-fsx-lustre.html)
- [Service quotas](https://docs.aws.amazon.com/fsx/latest/LustreGuide/limits.html)
- [Additional information](https://docs.aws.amazon.com/fsx/latest/LustreGuide/additional-info.html)
- [Document history](https://docs.aws.amazon.com/fsx/latest/LustreGuide/doc-history.html)

## [Using data repositories](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-data-repositories.html)

- [Overview of data repositories](https://docs.aws.amazon.com/fsx/latest/LustreGuide/overview-dra-data-repo.html): Overview of using data repositories for durable data storage with Amazon FSx for Lustre.

### [POSIX metadata support](https://docs.aws.amazon.com/fsx/latest/LustreGuide/posix-metadata-support.html)

Learn about POSIX metadata support when using data repositories.

- [Exporting hard links](https://docs.aws.amazon.com/fsx/latest/LustreGuide/hard-links.html): Learn how hard links are exported to Amazon S3 when using automatic export or data repository tasks with Amazon FSx for Lustre, and understand the implications for file system imports.
- [Attaching POSIX permissions to an S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/attach-s3-posix-permissions.html): How to attach POSIX permissions when uploading objects to an Amazon S3 bucket for use with Amazon FSx for Lustre.

### [Linking your file system to an S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html)

How to link an S3 bucket to an FSx for Lustre file system

- [Creating a link to an S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-linked-dra.html): How to link an S3 bucket to an FSx for Lustre file system
- [Updating data repository association settings](https://docs.aws.amazon.com/fsx/latest/LustreGuide/update-dra-settings.html): How to update a link to an S3 bucket
- [Deleting an association to an S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/delete-linked-dra.html): How to delete a data repository association
- [Viewing data repository association details](https://docs.aws.amazon.com/fsx/latest/LustreGuide/view-dra-details.html): How to view details of a data repository association
- [Data repository association lifecycle state](https://docs.aws.amazon.com/fsx/latest/LustreGuide/dra-lifecycles.html): Lifecycle states of a data repository association
- [Working with server-side encrypted Amazon S3 buckets](https://docs.aws.amazon.com/fsx/latest/LustreGuide/s3-server-side-encryption-support.html): How to work with S3 server-side encryption on FSx for Lustre file system

### [Importing changes from your data repository](https://docs.aws.amazon.com/fsx/latest/LustreGuide/importing-files-dra.html)

How to import files to your FSx for Lustre file system from your linked S3 data repository.

- [Automatically import updates from your S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/autoimport-data-repo-dra.html): Learn how to configure Amazon FSx for Lustre to automatically import updates from your Amazon S3 bucket, including supported file changes and import policies.
- [Using data repository tasks to import changes](https://docs.aws.amazon.com/fsx/latest/LustreGuide/import-data-repo-task-dra.html): Learn how to configure Amazon FSx for Lustre to automatically import updates from your Amazon S3 bucket, including supported file changes and import policies.
- [Preloading files into your file system](https://docs.aws.amazon.com/fsx/latest/LustreGuide/preload-file-contents-hsm-dra.html): Learn how to preload files from Amazon S3 into your Amazon FSx for Lustre file system to reduce initial access latency and optimize performance for latency-sensitive applications.

### [Exporting changes to the data repository](https://docs.aws.amazon.com/fsx/latest/LustreGuide/export-changed-data-meta-dra.html)

How to import files to your FSx for Lustre file system from your linked S3 data repository.

- [Automatically export updates to your S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/autoexport-data-repo-dra.html): Configure automatic export to update your Amazon S3 bucket when files change in your Amazon FSx for Lustre file system.
- [Using data repository tasks to export changes](https://docs.aws.amazon.com/fsx/latest/LustreGuide/export-data-repo-task-dra.html): Learn how to export changes from your Amazon FSx for Lustre file system to linked Amazon S3 buckets using data repository tasks through the Amazon FSx console and CLI.
- [Exporting files using HSM commands](https://docs.aws.amazon.com/fsx/latest/LustreGuide/exporting-files-hsm.html): Learn how to export files from an Amazon FSx for Lustre file system to an Amazon S3 data repository using HSM commands and verify the export process.

### [Data repository tasks](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-repository-tasks.html)

Use FSx for Lustre data repository tasks to manage the transfer of data and metadata between your FSx for Lustre file system and its durable data repository on Amazon S3.

- [Task status and details](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-repo-task-status.html): Learn about data repository task statuses and details in Amazon FSx for Lustre, including task types, file processing information, and lifecycle statuses for effective management and troubleshooting.

### [Using data repository tasks](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-data-repo-task.html)

Learn how to manage data repository tasks in Amazon FSx for Lustre, including creating, duplicating, viewing details, and canceling tasks using the Amazon FSx console, CLI, or API.

- [Creating a data repository task](https://docs.aws.amazon.com/fsx/latest/LustreGuide/creating-data-repo-task.html): Create and manage data repository tasks to export, import, or release files between Amazon FSx for Lustre file systems and linked Amazon S3 buckets.
- [Duplicating a task](https://docs.aws.amazon.com/fsx/latest/LustreGuide/recreate-task.html): Learn how to duplicate a data repository task in Amazon FSx for Lustre, allowing you to create an exact copy of an existing task with the option to modify paths before execution.
- [Accessing data repository tasks](https://docs.aws.amazon.com/fsx/latest/LustreGuide/view-data-repo-tasks.html): Learn how to access and view data repository tasks for Amazon FSx for Lustre file systems using the console, CLI, and API.
- [Canceling a data repository task](https://docs.aws.amazon.com/fsx/latest/LustreGuide/cancel-data-repo-task.html): Learn how to cancel a data repository task in Amazon FSx for Lustre using the console or CLI, and understand the effects of cancellation on file processing.
- [Working with task completion reports](https://docs.aws.amazon.com/fsx/latest/LustreGuide/task-completion-report.html): Learn how to work with task completion reports in Amazon FSx for Lustre, including report generation, delivery, format, and encoding for export, import, and release data repository tasks.
- [Troubleshooting task failures](https://docs.aws.amazon.com/fsx/latest/LustreGuide/failed-tasks.html): Learn how to troubleshoot data repository task failures in Amazon FSx for Lustre.

### [Releasing files](https://docs.aws.amazon.com/fsx/latest/LustreGuide/file-release.html)

How to release file data from your FSx for Lustre file system to free up space for new files.

- [Using data repository tasks to release files](https://docs.aws.amazon.com/fsx/latest/LustreGuide/release-files-task.html): Learn how to release file data from Amazon FSx for Lustre file systems to free up space, while retaining file listings and metadata.
- [Using Amazon FSx with your on-premises data](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-on-premises.html): Learn how to use Amazon FSx for Lustre to process on-premises data with in-cloud compute instances, including steps for creating, mounting, and managing file systems.
- [Data repository event logs](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-repo-event-logs.html): Describes what the CloudWatch Logs logs for data repository events.
- [Working with older deployment types](https://docs.aws.amazon.com/fsx/latest/LustreGuide/older-deployment-types.html): Describes how to use FSx for Lustre with the older, legacy deployment types


## [Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html)

- [SSD and HDD storage classes](https://docs.aws.amazon.com/fsx/latest/LustreGuide/ssd-storage.html): Learn about the SSD storage class on FSx for Lustre file systems.
- [Intelligent-Tiering storage class](https://docs.aws.amazon.com/fsx/latest/LustreGuide/intelligent-tiering-file-systems.html): The FSx for Lustre Intelligent-Tiering storage class offers elastic, cost-optimized storage for workloads that traditionally run on HDD-based or mixed HDD-/SDD-based high-performance file storage file systems.
- [Performance tips](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance-tips.html): When using Amazon FSx for Lustre, keep the following performance tips in mind.


## [Accessing file systems](https://docs.aws.amazon.com/fsx/latest/LustreGuide/accessing-fs.html)

- [Lustre file system and client kernel compatibility](https://docs.aws.amazon.com/fsx/latest/LustreGuide/lustre-client-matrix.html): Use this matrix to make sure the Lustre version for your FSx for Lustre file system is compatible with the Linux kernel versions of your client instances.
- [Installing the Lustre client](https://docs.aws.amazon.com/fsx/latest/LustreGuide/install-lustre-client.html): Mount your FSx for Lustre file system by first installing the open-source Lustre client on your compute instance, including Amazon Linux, CentOS, Red Hat, Rocky Linux, Ubuntu, and SUSE Linux.
- [Mount from Amazon EC2](https://docs.aws.amazon.com/fsx/latest/LustreGuide/mounting-ec2-instance.html): Learn how to mount an FSx for Lustre file system from an Amazon EC2 instance.
- [Configure EFA clients](https://docs.aws.amazon.com/fsx/latest/LustreGuide/configure-efa-clients.html): Describes how to configure Elastic Fabric Adapter (EFA) clients on an FSx for Lustre file system.
- [Mounting from Amazon ECS](https://docs.aws.amazon.com/fsx/latest/LustreGuide/mounting-ecs.html): Learn how to mount an FSx for Lustre file system from an Amazon Elastic Container Service Docker container on an Amazon EC2 instance.
- [Mounting from on-premises or another VPC](https://docs.aws.amazon.com/fsx/latest/LustreGuide/mounting-on-premises.html): Learn how to mount an FSx for Lustre file system from on-premises or a peered Amazon VPC
- [Mounting Amazon FSx automatically](https://docs.aws.amazon.com/fsx/latest/LustreGuide/mount-fs-auto-mount-onreboot.html): How to mount your Amazon FSx file system automatically.
- [Mounting specific filesets](https://docs.aws.amazon.com/fsx/latest/LustreGuide/mounting-from-fileset.html): Learn how to use the Lustre fileset feature.
- [Unmounting file systems](https://docs.aws.amazon.com/fsx/latest/LustreGuide/unmounting-fs.html): Unmount an FSx for Lustre file system.
- [Using EC2 Spot Instances](https://docs.aws.amazon.com/fsx/latest/LustreGuide/working-with-ec2-spot-instances.html): Considerations for working with Amazon EC2 Spot Instances in FSx for Lustre.


## [Administering file systems](https://docs.aws.amazon.com/fsx/latest/LustreGuide/administer-lustre-file-systems.html)

- [EFA-enabled file systems](https://docs.aws.amazon.com/fsx/latest/LustreGuide/efa-file-systems.html): Learn how FSx for Lustre supports Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS).
- [Storage quotas](https://docs.aws.amazon.com/fsx/latest/LustreGuide/lustre-quotas.html): Limit the amount of disk space that a user, group, or project can consume by creating storage quotas on FSx for Lustre file systems.

### [Storage capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html)

Learn how to increase the storage capacity configured on your Amazon FSx for Lustre file system when you need additional storage.

- [Increasing storage capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/increase-storage-capacity.html): Learn how to increase the storage capacity of your Amazon FSx for Lustre file system, and understand the process of storage scaling and optimization.
- [Monitoring storage capacity increases](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-storage-capacity-increase.html): Monitor storage capacity increases for Amazon FSx for Lustre file systems using the Amazon FSx console, CLI, or API.
- [SSD read caches](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-ssd-read-cache.html): Learn how to modify your provisioned SSD data read cache.

### [Manage metadata performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-metadata-performance.html)

Learn about the FSx for Lustre metadata configuration and how to increase the metadata performance on your file system.

- [Increasing metadata performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/modify-metadata-performance.html): How to increase the metadata performance on your FSx for Lustre file system.
- [Changing the metadata configuration mode](https://docs.aws.amazon.com/fsx/latest/LustreGuide/switch-provisioning-mode.html): How to change the FSx for Lustre metadata configuration mode.
- [Monitoring metadata configuration updates](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-metadata-performance-increase.html): How to monitor FSx for Lustre metadata configuration increases on your file system.

### [Throughput capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-throughput-capacity.html)

Learn how to modify the throughput capacity configured on your FSx for Lustre file system when you need additional performance.

- [Modifying throughput capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/increase-throughput-capacity.html): Learn how to manage and modify throughput capacity for FSx for Lustre file systems, using the Amazon FSx console, CLI, or API.
- [Monitoring throughput capacity changes](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-throughput-capacity-changes.html): Monitor storage capacity increases for Amazon FSx for Lustre file systems using the Amazon FSx console, CLI, or API.
- [Data compression](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html): Save on storage costs and increase throughput capacity on your file systems with data compression for Amazon FSx for Lustre.
- [Root squash](https://docs.aws.amazon.com/fsx/latest/LustreGuide/root-squash.html): Describes the Lustre root squash feature.
- [File system status](https://docs.aws.amazon.com/fsx/latest/LustreGuide/file-system-lifecycle-states.html): You can view the status of your file system by using the Amazon FSx console, the AWS CLI, or the Amazon FSx API.
- [Tag your resources](https://docs.aws.amazon.com/fsx/latest/LustreGuide/tag-resources.html): Working with tags to create metadata for your Amazon FSx resources.
- [Maintenance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/maintenance-windows.html): Describes what maintenance windows are and how to use them.
- [Lustre versions](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-lustre-version.html): How to update your file system's Lustre version.
- [Deleting a file system](https://docs.aws.amazon.com/fsx/latest/LustreGuide/delete-file-system.html): Learn how to delete an Amazon FSx for Lustre file system using the Amazon FSx console, CLI, or API, and understand the steps to ensure data integrity before deletion.


## [Backups](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html)

- [Copying backups](https://docs.aws.amazon.com/fsx/latest/LustreGuide/copy-backups.html): Learn how to copy Amazon FSx for Lustre backups within the same AWS Region or across Regions for disaster recovery and data protection.
- [Copying backups within the same AWS account](https://docs.aws.amazon.com/fsx/latest/LustreGuide/copying-backups-same-account.html): Describes how to copy FSx for Lustre backups within the same AWS account.
- [Restoring backups](https://docs.aws.amazon.com/fsx/latest/LustreGuide/restoring-backups.html): Learn how to restore an Amazon FSx for Lustre file system from a backup using the Amazon FSx console, CLI, or SDKs.
- [Deleting backups](https://docs.aws.amazon.com/fsx/latest/LustreGuide/delete-backups.html): Learn how to permanently delete Amazon FSx for Lustre backups using the Amazon FSx console, CLI, and API, and understand the implications of this irreversible action.


## [Monitoring file systems](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring_overview.html)

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-cloudwatch.html)

Learn how to monitor Amazon FSx for Lustre with Amazon CloudWatch metrics.

- [Using CloudWatch metrics](https://docs.aws.amazon.com/fsx/latest/LustreGuide/how_to_use_metrics.html): Learn how to use FSx for Lustre metrics to monitor your file system.
- [Accessing CloudWatch metrics](https://docs.aws.amazon.com/fsx/latest/LustreGuide/accessingmetrics.html): Learn how to access Amazon FSx for Lustre metrics for CloudWatch.
- [Metrics and dimensions](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fs-metrics.html): Find the metrics published in the AWS/FSx namespace in Amazon CloudWatch for all FSx for Lustre file systems.
- [Performance warnings and recommendations](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance-insights.html): Performance warnings that you might see from CloudWatch metrics, and recommendations to resolve them.
- [Creating CloudWatch alarms](https://docs.aws.amazon.com/fsx/latest/LustreGuide/creating_alarms.html): Learn how to create CloudWatch alarms to monitor Amazon FSx for Lustre.
- [Logging with CloudWatch Logs](https://docs.aws.amazon.com/fsx/latest/LustreGuide/cw-event-logging.html): Describes how to use Lustre event logging.
- [Logging with AWS CloudTrail](https://docs.aws.amazon.com/fsx/latest/LustreGuide/logging-using-cloudtrail.html): Learn about logging Amazon FSx for Lustre with AWS CloudTrail.


## [Security](https://docs.aws.amazon.com/fsx/latest/LustreGuide/security.html)

### [Data protection](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon FSx for Lustre.

### [Data encryption](https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-fsxl.html)

Learn about data encryption options in Amazon FSx for Lustre file systems, including automatic encryption at rest and in-transit encryption when accessing from supported Amazon EC2 instances.

- [Encrypting data at rest](https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-at-rest.html): Learn about encryption of data at rest.
- [Encrypting data in transit](https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-in-transit-fsxl.html): Learn about encryption in transit.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/fsx/latest/LustreGuide/internetwork-privacy.html): Learn about network traffic privacy for Amazon FSx for Lustre, including connectivity options, API encryption requirements, and data encryption in transit between Amazon FSx and on-premises clients.

### [Identity and access management](https://docs.aws.amazon.com/fsx/latest/LustreGuide/security-iam.html)

How to authenticate requests and manage access your Amazon FSx resources.

- [FSx for Lustre and IAM](https://docs.aws.amazon.com/fsx/latest/LustreGuide/security_iam_service-with-iam.html): Learn how Amazon FSx for Lustre integrates with AWS Identity and Access Management, including supported features like identity-based policies, policy actions, and condition keys for managing access to your file systems.
- [Identity-based policy examples](https://docs.aws.amazon.com/fsx/latest/LustreGuide/security_iam_id-based-policy-examples.html): Learn how to create identity-based IAM policies for Amazon FSx for Lustre to grant users permissions to perform actions on Amazon FSx resources using the console, CLI, or API.
- [AWS managed policies](https://docs.aws.amazon.com/fsx/latest/LustreGuide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon FSx and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/fsx/latest/LustreGuide/security_iam_troubleshoot.html): Learn how to troubleshoot common identity and access issues in Amazon FSx for Lustre file systems, including unauthorized actions, IAM role permissions, and cross-account resource access.
- [Using tags with Amazon FSx](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-tags-fsx.html): Create AWS Identity and Access Management (IAM) policies to allow users to tag Amazon FSx for Lustre resources on creation.
- [Using service-linked roles](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-service-linked-roles.html): How to use service-linked roles to give Amazon FSx access to resources in your AWS account.
- [File system access control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/LustreGuide/limit-access-security-groups.html): Learn how to control access to your Amazon FSx for Lustre file system using Amazon VPC security groups and understand the network interface configuration for secure file system access.
- [Amazon VPC network ACLs](https://docs.aws.amazon.com/fsx/latest/LustreGuide/limit-access-acl.html): Learn how to control access to your Amazon FSx for Lustre file system using Amazon VPC security groups and understand the network interface configuration for secure file system access.
- [Compliance Validation](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-lustre-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Interface VPC endpoints](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-vpc-endpoints.html): You can use interface VPC endpoints (AWS PrivateLink) to access the Amazon FSx API from your VPC without sending traffic over the internet.


## [Troubleshooting](https://docs.aws.amazon.com/fsx/latest/LustreGuide/troubleshooting.html)

- [Creating a file system fails](https://docs.aws.amazon.com/fsx/latest/LustreGuide/cannot-create-fs.html): Troubleshooting why creating an FSx for Lustre file system fails.
- [File system mount fails](https://docs.aws.amazon.com/fsx/latest/LustreGuide/mount-troubleshooting.html): Troubleshooting why mounting an FSx for OpenZFS volume fails.
- [You cannot access your file system](https://docs.aws.amazon.com/fsx/latest/LustreGuide/cant-access-fs.html): Use this troubleshooting information if you cannot access your Amazon FSx for Lustre file system.
- [Creating a DRA fails](https://docs.aws.amazon.com/fsx/latest/LustreGuide/s3-validation-error.html): Use this troubleshooting information if you cannot link to an S3 bucket.
- [Renaming directories takes a long time](https://docs.aws.amazon.com/fsx/latest/LustreGuide/rename-directory-time.html): Use this troubleshooting information if renaming directories takes a long time.
- [Misconfigured linked S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/troubleshooting-misconfigured-data-repository.html): Use this troubleshooting information if you encounter misconfigured links to S3 buckets.
- [Storage issues](https://docs.aws.amazon.com/fsx/latest/LustreGuide/lfs-migrate-ts.html): Use this troubleshooting information if you have storage issues.
- [CSI driver issues](https://docs.aws.amazon.com/fsx/latest/LustreGuide/csi-driver-issues.html): Use this troubleshooting information if you have CSI driver issues.
