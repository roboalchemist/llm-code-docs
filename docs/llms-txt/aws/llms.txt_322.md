# Source: https://docs.aws.amazon.com/efs/latest/ug/llms.txt

# Amazon Elastic File System User Guide

> Use Amazon Elastic File System (Amazon EFS) to set up, operate, and scale shared file storage in the AWS cloud.

- [Getting started](https://docs.aws.amazon.com/efs/latest/ug/getting-started.html)
- [Document history](https://docs.aws.amazon.com/efs/latest/ug/document-history.html)

## [What is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

- [How it works](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html): Overview of how Amazon EFS works with other AWS services.
- [Features](https://docs.aws.amazon.com/efs/latest/ug/features.html): Learn about key Amazon EFS features including storage classes, replication, data consistency, authentication, and access control for managing your file systems in the cloud.


## [Installing the EFS client](https://docs.aws.amazon.com/efs/latest/ug/using-amazon-efs-utils.html)

- [Manually installing the EFS client](https://docs.aws.amazon.com/efs/latest/ug/installing-amazon-efs-utils.html): Manually install the Amazon EFS client on your EC2 Linux instances, other supported Linux distributions, and on EC2 Mac instances running macOS.

### [Automatically installing the EFS client](https://docs.aws.amazon.com/efs/latest/ug/manage-efs-utils-with-aws-sys-manager.html)

There are two steps in setting up AWS Systems Manager, which automates tasks required to install or update the amazon-efs-utils package on your EC2 instances.

- [Configuring AWS Systems Manager to install the EFS client](https://docs.aws.amazon.com/efs/latest/ug/setting-up-aws-sys-mgr.html): Learn how to configure AWS Systems Manager to automatically install and update the Amazon EFS client on your EC2 instances using IAM profiles and State Manager associations.
- [Installing and upgrading botocore](https://docs.aws.amazon.com/efs/latest/ug/install-botocore.html): The Amazon EFS client uses botocore to interact with other AWS services and is required to monitor mount attempts for your EFS file systems in CloudWatch Logs.

### [Upgrading stunnel](https://docs.aws.amazon.com/efs/latest/ug/upgrading-stunnel.html)

EFS mount helper requires a version of stunnel that supports both Online Certificate Status Protocol (OCSP) and certificate hostname checking.

- [Resolving issues with installing stunnel](https://docs.aws.amazon.com/efs/latest/ug/stunnel-issues.html): If you are unable to install stunnel, try disabling certificate hostname checking.
- [Enabling FIPS mode](https://docs.aws.amazon.com/efs/latest/ug/fips-enabling.html): Learn how to enable FIPS mode in the Amazon EFS client by modifying the efs-utils.conf file when your system requires FIPS-compliant endpoints.


## [Creating and managing resources](https://docs.aws.amazon.com/efs/latest/ug/creating-using.html)

- [Implementation summary](https://docs.aws.amazon.com/efs/latest/ug/how-it-works-implementation.html): Understand the key Amazon EFS resources including file systems, mount targets, and access points, and learn how to create and manage them using the console, AWS CLI, or API.
- [Creating file systems](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html): Required AWS Identity and Access Management (IAM) permissions for creating file systems and the configuration options available when creating the file systems.
- [Deleting file systems](https://docs.aws.amazon.com/efs/latest/ug/delete-efs-fs.html): Permanently delete an EFS file system to make the file system data rendered unusable.
- [Creating file system policies](https://docs.aws.amazon.com/efs/latest/ug/create-file-system-policy.html): Create a file system policy for your EFS file system by setting policy options and customizing a preconfigured policy or creating your own file system policy.
- [Creating access points](https://docs.aws.amazon.com/efs/latest/ug/create-access-point.html): Create access points for your EFS file system.
- [Deleting access points](https://docs.aws.amazon.com/efs/latest/ug/delete-access-point.html): Delete access points.
- [Tagging resources](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-tags.html): Add tags to Amazon EFS file systems and access points to make managing them easier and to implement attribute-based access control (ABAC).
- [Tutorial: Creating writable per-user subdirectories](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs-nfs-permissions-per-user-subdirs.html): Learn how to create a user-specific subdirectory in an Amazon EFS file system, grant ownership, and mount it to the user's home directory on an EC2 instance.


## [Mounting file systems](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs.html)

- [Mounting considerations for Linux](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-general.html): Certain values for mount options in Linux are recommended.

### [Using the EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html)

The EFS mount helper (part of the amazon-efs-utils package) simplifies mounting EFS file systems on EC2 Linux and Mac instances running supported distributions.

- [Mount settings used by EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/mount-helper-setting.html): Learn about the optimized mount options that the Amazon EFS mount helper automatically uses when mounting file systems on EC2 Linux and Mac instances.
- [Getting support logs](https://docs.aws.amazon.com/efs/latest/ug/mount-helper-logs.html): Access and configure logging for the EFS mount helper, stunnel process, and watchdog process to help troubleshoot mount issues with AWS Support.
- [Prerequisites](https://docs.aws.amazon.com/efs/latest/ug/mount-helper-prerequisites.html): Review the requirements for mounting an Amazon EFS file system using the mount helper, including file system ID, mount targets, and supported EC2 instances.
- [Mounting on EC2 Linux](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-helper-ec2-linux.html): Mount your EFS file system on Amazon EC2 instances using the EFS mount helper.
- [Mounting on EC2 Mac](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-helper-ec2-mac.html): Mount Amazon EFS file systems on EC2 Mac instances running macOS Big Sur, Monterey, or Ventura using the EFS mount helper with encryption in transit.
- [Mounting from a different Region](https://docs.aws.amazon.com/efs/latest/ug/mount-different-region.html): To mount your EFS file system from an EC2 instance that is in a different AWS Region than the file system, you must edit the region property value in the efs-utils.conf file.
- [Mounting One Zone file systems](https://docs.aws.amazon.com/efs/latest/ug/mounting-one-zone.html): Considerations apply when mounting One Zone file systems in different Availability Zones and when mounting One Zone file systems on other AWS compute instances.
- [Mounting with IAM authorization](https://docs.aws.amazon.com/efs/latest/ug/mounting-IAM-option.html): Mount to an Amazon EC2 instance that has an instance profile by using AWS Identity and Access Management (IAM) authorization, using IAM credentials, or using AWS CLI config file.
- [Mounting with EFS access points](https://docs.aws.amazon.com/efs/latest/ug/mounting-access-points.html): Mount file systems using access points by using the EFS mount helper.
- [Mounting multiple EC2 instances](https://docs.aws.amazon.com/efs/latest/ug/mount-multiple-ec2-instances.html): Mount EFS file systems to multiple Amazon EC2 instances remotely and securely by using the AWS Systems Manager Run Command.

### [Mounting from another account or VPC](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-vpc-peering.html)

Mount your EFS file system using IAM or access points from another account or VPC.

- [Mounting from another AWS account](https://docs.aws.amazon.com/efs/latest/ug/mount-fs-diff-account-same-vpc.html): Mount EFS file systems owned by one AWS account from EC2 instances owned by a different account using shared Amazon VPCs and DNS name resolution.
- [Mounting from another VPC](https://docs.aws.amazon.com/efs/latest/ug/mount-fs-different-vpc.html): Use a VPC peering connection or transit gateway to connect VPCs in different accounts.

### [Using NFS](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-old.html)

Install the Network File System (NFS) client and use it to mount an EFS file system on an EC2 instance.

- [Installing the NFS client](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-install-nfsclient.html): To mount your EFS file system on your Amazon EC2 instance, you first must install an NFS client.
- [Recommended NFS mount settings](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-nfs-mount-settings.html): Use recommended values for mount settings when mounting your EFS file systems with Network File System (NFS).
- [Mounting on EC2 with DNS](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html): Mount your EFS file system using the DNS name for the file system or mount target.
- [Mounting with an IP address](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-ip-addr.html): Mount your EFS file system using the mount targetâs IP address.

### [Automatically mounting file systems](https://docs.aws.amazon.com/efs/latest/ug/mount-fs-auto-mount-onreboot.html)

Configure Amazon EFS to automatically mount file systems on restart

- [New EC2 Linux instances](https://docs.aws.amazon.com/efs/latest/ug/mount-fs-auto-mount-on-creation.html): When you create a new Amazon EC2 Linux instance using the EC2 launch instance wizard, you can configure it to mount your EFS file system automatically.
- [Existing EC2 Linux instances](https://docs.aws.amazon.com/efs/latest/ug/mount-fs-auto-mount-update-fstab.html): Manually update the /etc/fstab on an Amazon EC2 Linux instance so that the instance uses the EFS mount helper to automatically remount an EFS file system when the instance restarts.
- [Linux and Mac instances using NFS](https://docs.aws.amazon.com/efs/latest/ug/nfs-automount-efs.html): Use the NFS to configure the /etc/fstab on Amazon EC2 instances to automatically remount your EFS file systems when the instance re-starts.
- [Unmounting file systems](https://docs.aws.amazon.com/efs/latest/ug/unmounting-fs.html): Before you delete a file system, unmount it from every Amazon EC2 instance that it's connected to.
- [Tutorial: Create and mount a file system using the AWS CLI](https://docs.aws.amazon.com/efs/latest/ug/wt1-getting-started.html): In this tutorial, use the AWS CLI to create EC2 and EFS resources, mount the EC2 file system to the EC2 instance, and then test the setup.
- [Tutorial: Mounting with on-premises clients](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-helper-direct.html): Mount your EFS file system with on-premises clients using the EFS mount helper over Direct Connect and VPN.
- [Tutorial: Mount a file system from a different VPC](https://docs.aws.amazon.com/efs/latest/ug/efs-different-vpc.html): Set up an EC2 instance to mount an EFS file system that is in a different virtual private cloud (VPC).
- [Troubleshooting mount issues](https://docs.aws.amazon.com/efs/latest/ug/troubleshooting-efs-mounting.html): Find information about troubleshooting EFS file system mounting issues.


## [Transferring data](https://docs.aws.amazon.com/efs/latest/ug/transfer-data-to-efs.html)

- [Using AWS DataSync](https://docs.aws.amazon.com/efs/latest/ug/trnsfr-data-using-datasync.html): Use AWS DataSync to enable secure, automated transfer and replication of data between on-premises storage systems, and also between AWS storage services.
- [Using AWS Transfer Family](https://docs.aws.amazon.com/efs/latest/ug/using-aws-transfer-integration.html): Use AWS Transfer Family to transfer files into and out of Amazon EFS file systems over certain protocols, such as Secure Shell (SSH) File Transfer Protocol (SFTP) (AWS Transfer for SFTP) and File Transfer Protocol Secure (FTPS) (AWS Transfer for FTPS).


## [Managing file systems](https://docs.aws.amazon.com/efs/latest/ug/managing.html)

- [Understanding file system status](https://docs.aws.amazon.com/efs/latest/ug/file-system-state.html): View the status of EFS file systems using the Amazon EFS console or the AWS CLI.

### [Managing mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)

Mount your file system on Amazon EC2 or other AWS compute instance in your virtual private cloud (VPC) using a mount target that you create for the file system.

- [Creating mount targets](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-create-delete-mount-targets.html): Create Amazon EFS mount targets to access an EFS file system in a VPC.
- [Deleting mount targets](https://docs.aws.amazon.com/efs/latest/ug/mount-target-delete.html): Learn how to delete mount targets
- [Changing mount target VPC](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-change-vpc.html): Changing the VPC for your mount target.
- [Changing mount target security groups](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-update-mount-target-config-sg.html): Security groups define inbound and outbound access.
- [Managing throughput](https://docs.aws.amazon.com/efs/latest/ug/managing-throughput.html): Learn how to manage mount targets for EFS file systems, including creating, deleting, and modifying mount targets in your VPC.

### [Managing storage lifecycle](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

Use lifecycle management to automatically transition data between storage classes according to lifecycle policies that you define for the file system.

- [Configuring lifecycle policies](https://docs.aws.amazon.com/efs/latest/ug/enable-lifecycle-management.html): When you create an EFS file system that has the recommended settings using the AWS Management Console, the file system is automatically configured with the following default lifecycle configuration:


## [Monitoring](https://docs.aws.amazon.com/efs/latest/ug/monitoring_overview.html)

- [Monitoring tools](https://docs.aws.amazon.com/efs/latest/ug/monitoring_automated_manual.html): AWS provides various tools that you can use to monitor Amazon EFS.
- [File system metering](https://docs.aws.amazon.com/efs/latest/ug/metered-sizes.html): Learn how Amazon EFS reports file system sizes, sizes of objects within a file system, and file system throughput.
- [Viewing storage class size](https://docs.aws.amazon.com/efs/latest/ug/view-storage-class-size.html): View how much data is stored in each storage class of your Amazon EFS file system using the AWS Management Console, AWS CLI, or EFS API.

### [Monitoring metrics with CloudWatch](https://docs.aws.amazon.com/efs/latest/ug/monitoring-cloudwatch.html)

Monitor EFS file systems using EFS metrics in Amazon CloudWatch.

- [CloudWatch metrics](https://docs.aws.amazon.com/efs/latest/ug/efs-metrics.html): Use Amazon EFS metrics to monitor file systems in CloudWatch.
- [Accessing CloudWatch metrics](https://docs.aws.amazon.com/efs/latest/ug/accessingmetrics.html): View Amazon CloudWatch metrics for EFS in the CloudWatch console, AWS CLI, and API.
- [Using CloudWatch metrics](https://docs.aws.amazon.com/efs/latest/ug/how_to_use_metrics.html): Common uses for using CloudWatch metrics.
- [Using metric math with CloudWatch metrics](https://docs.aws.amazon.com/efs/latest/ug/monitoring-metric-math.html): Query multiple Amazon CloudWatch metrics and use math expressions to create time series based on the metrics.
- [Monitoring mount attempt successes and failures](https://docs.aws.amazon.com/efs/latest/ug/how-to-monitor-mount-status.html): Configure your EC2 instance to use Amazon CloudWatch Logs to monitor the success or failure of its file system mount attempts.
- [Creating alarms](https://docs.aws.amazon.com/efs/latest/ug/creating_alarms.html): Create alarms that send Amazon SNS messages when a metric changes values.
- [Logging API calls with CloudTrail](https://docs.aws.amazon.com/efs/latest/ug/logging-using-cloudtrail.html): Use AWS CloudTrail to record actions taken by a user, role, or an AWS service in Amazon EFS.


## [Using billing and usage reports](https://docs.aws.amazon.com/efs/latest/ug/billing-usage-reporting.html)

- [Using cost allocation tags](https://docs.aws.amazon.com/efs/latest/ug/CostAllocTagging.html): Label Amazon EFS file systems with cost allocation tags to track the storage cost or other criteria for individual files or groups of files.
- [Billing reports](https://docs.aws.amazon.com/efs/latest/ug/aws-billing-report.html): Learn about the AWS charges for using Amazon EFS.
- [Usage reports](https://docs.aws.amazon.com/efs/latest/ug/aws-usage-report.html): Create and download AWS usage reports for Amazon EFS.
- [Understanding billing and usage reports](https://docs.aws.amazon.com/efs/latest/ug/billing-usage-reports-understand.html): Understand your AWS usage bill and report for Amazon EFS.


## [Performance specifications](https://docs.aws.amazon.com/efs/latest/ug/performance.html)

- [Performance tips](https://docs.aws.amazon.com/efs/latest/ug/performance-tips.html): Learn useful tips for optimizing the performance for your EFS file systems.
- [Troubleshooting performance issues](https://docs.aws.amazon.com/efs/latest/ug/troubleshooting-efs-general.html): Troubleshoot general performance issues Amazon EFS, including access denied to allowed files on NFS file system, errors when accessing the Amazon EFS console, and the Amazon EC2 instance not responding.
- [Troubleshooting AMI and kernel issues](https://docs.aws.amazon.com/efs/latest/ug/troubleshooting-efs-ami-kernel.html): Troubleshoot performance issues related to Amazon Machine Images (AMIs) and Amazon EFS kernels, such as unable to chown and having a deadlocked client.


## [Backing up and replicating data](https://docs.aws.amazon.com/efs/latest/ug/backup-replication.html)

### [Backing up file systems](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html)

Use AWS Backup to back up and restore EFS file systems.

- [Managing automatic backups](https://docs.aws.amazon.com/efs/latest/ug/automatic-backups.html): When you create a file system using the Amazon EFS console, automatic backups are turned on by default.

### [Replicating file systems](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html)

Replicate EFS file systems for resilience and data protection.

- [Configuring replication to new file system](https://docs.aws.amazon.com/efs/latest/ug/create-replication.html): When replicating to a new EFS file system, choose the file system type and AWS key.
- [Configuring replication to existing file system](https://docs.aws.amazon.com/efs/latest/ug/replicate-existing-destination.html): When replicating to an existing EFS file system, first disable the file system's replication overwrite protection.
- [Replicating across AWS accounts](https://docs.aws.amazon.com/efs/latest/ug/cross-account-replication.html): Replicate across AWS accounts within your organization.
- [Viewing replication details](https://docs.aws.amazon.com/efs/latest/ug/monitoring-replication-status.html): Learn about the options for monitoring replication status.
- [Deleting replication configurations](https://docs.aws.amazon.com/efs/latest/ug/delete-replications.html): Delete an EFS replication configuration from the source or destination file system.
- [Using the replica](https://docs.aws.amazon.com/efs/latest/ug/replication-fail-over.html): To use the replica file system, delete the replication configuration.


## [Securing your data](https://docs.aws.amazon.com/efs/latest/ug/security-considerations.html)

### [Data protection](https://docs.aws.amazon.com/efs/latest/ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon EFS.

### [Data encryption](https://docs.aws.amazon.com/efs/latest/ug/encryption.html)

Amazon EFS provides comprehensive encryption capabilities to protect your data both at rest and in transit.

- [Encrypting data at rest](https://docs.aws.amazon.com/efs/latest/ug/encryption-at-rest.html): Protect your file system data with automatic encryption at rest using AWS KMS keys.
- [Encrypting data in transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html): Amazon EFS supports encryption of data in transit with Transport Layer Security (TLS).
- [Using AWS KMS keys](https://docs.aws.amazon.com/efs/latest/ug/EFSKMS.html): Amazon EFS integrates with AWS Key Management Service (AWS KMS) to encrypt your file systems using customer managed keys.
- [Troubleshooting encryption](https://docs.aws.amazon.com/efs/latest/ug/troubleshooting-efs-encryption.html): Resolve common encryption issues with Amazon EFS, including TLS mount failures, interrupted connections, AWS KMS key problems, and encryption-at-rest errors.
- [Internetwork privacy](https://docs.aws.amazon.com/efs/latest/ug/internetwork-privacy.html): This topic describes how Amazon EFS secures connections from the service to other locations.

### [Identity and access management](https://docs.aws.amazon.com/efs/latest/ug/security-iam.html)

Use AWS Identity and Access Management (IAM) to control access to resources in Amazon EFS.

- [How Amazon Elastic File System works with IAM](https://docs.aws.amazon.com/efs/latest/ug/security_iam_service-with-iam.html): Learn how Amazon EFS integrates with IAM to control access to your file systems through identity-based and resource-based policies for secure and effective permission management.
- [Identity-based policy examples](https://docs.aws.amazon.com/efs/latest/ug/security_iam_id-based-policy-examples.html): Explore example IAM policies that demonstrate how to control access to Amazon EFS resources.
- [Resource-based policy examples](https://docs.aws.amazon.com/efs/latest/ug/security_iam_resource-based-policy-examples.html): Get example file system policies that grant or deny permissions for various Amazon EFS actions, such as granting read and write access to a specific AWS role and granting read-only access.
- [AWS managed policies](https://docs.aws.amazon.com/efs/latest/ug/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon EFS and recent changes to those policies.
- [Using tags](https://docs.aws.amazon.com/efs/latest/ug/using-tags-efs.html): Create AWS Identity and Access Management (IAM) policies that grant or deny actions on Amazon EFS resources using tags to implement attribute-based access control (ABAC).
- [Using service-linked roles](https://docs.aws.amazon.com/efs/latest/ug/using-service-linked-roles.html): How to use a service-linked role to give Amazon EFS access to resources in your AWS account.
- [Troubleshooting](https://docs.aws.amazon.com/efs/latest/ug/security_iam_troubleshoot.html): Learn how to diagnose and resolve common permission issues when working with Amazon EFS.
- [Controlling file system data access](https://docs.aws.amazon.com/efs/latest/ug/iam-access-control-nfs-efs.html): You can use both IAM identity policies and resource policies to control client access to Amazon EFS resources in a way that is scalable and optimized for cloud environments.
- [Compliance validation](https://docs.aws.amazon.com/efs/latest/ug/EFS-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/efs/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon EFS features for data resiliency.

### [Controlling network access](https://docs.aws.amazon.com/efs/latest/ug/NFS-access-control-efs.html)

Learn how to control NFS client access to EFS file systems using Amazon VPC security groups, network ACLs, and proper security configurations for mount targets.

- [Using VPC security groups](https://docs.aws.amazon.com/efs/latest/ug/network-access.html): Configure Amazon VPC security groups to control network traffic between EC2 instances and EFS mount targets using inbound and outbound rules.
- [Working with VPC endpoints](https://docs.aws.amazon.com/efs/latest/ug/efs-vpc-endpoints.html): Access the Amazon EFS API from your VPC without sending traffic over the internet.

### [NFS-level users, groups, and permissions](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs-nfs-permissions.html)

How to work with network file system (NFS)âlevel permissions and other related considerations for Amazon EFS.

- [File and directory permissions](https://docs.aws.amazon.com/efs/latest/ug/user-and-group-permissions.html): Files and directories in an EFS file system support standard Unix-style read, write, and execute permissions based on the user and group ID asserted by the mounting NFSv4.1 client.

### [Working with access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html)

Learn how Amazon EFS access points provide applications access to shared datasets for EFS file systems.

- [Enforcing a user identity](https://docs.aws.amazon.com/efs/latest/ug/enforce-identity-access-points.html): Enforce user and group information for all file system requests made through the access point.
- [Enforcing a root directory](https://docs.aws.amazon.com/efs/latest/ug/enforce-root-directory-access-point.html): Use an access point to override the root directory for a file system.
- [Using access points in IAM policies](https://docs.aws.amazon.com/efs/latest/ug/access-points-iam-policy.html): Use an IAM policy to enforce that a specific NFS client can only access a specific access point.
- [Blocking public access to file systems](https://docs.aws.amazon.com/efs/latest/ug/access-control-block-public-access.html): Use the Amazon EFS block public access feature to help you manage public access to EFS file systems.
- [Network isolation](https://docs.aws.amazon.com/efs/latest/ug/network-isolation.html): Describes how Amazon EFS isolates service traffic.


## [Quotas](https://docs.aws.amazon.com/efs/latest/ug/limits.html)

- [Troubleshooting file operation errors related to quotas](https://docs.aws.amazon.com/efs/latest/ug/troubleshooting-efs-fileop-errors.html): Certain limits on the files in EFS file systems apply.


## [Amazon EFS API](https://docs.aws.amazon.com/efs/latest/ug/api-reference.html)

### [Actions](https://docs.aws.amazon.com/efs/latest/ug/API_Operations.html)

The following actions are supported:

- [CreateAccessPoint](https://docs.aws.amazon.com/efs/latest/ug/API_CreateAccessPoint.html): Creates an EFS access point.
- [CreateFileSystem](https://docs.aws.amazon.com/efs/latest/ug/API_CreateFileSystem.html): Creates a new, empty file system.
- [CreateMountTarget](https://docs.aws.amazon.com/efs/latest/ug/API_CreateMountTarget.html): Creates a mount target for a file system.
- [CreateReplicationConfiguration](https://docs.aws.amazon.com/efs/latest/ug/API_CreateReplicationConfiguration.html): Creates a replication conï¬guration to either a new or existing EFS file system.
- [CreateTags](https://docs.aws.amazon.com/efs/latest/ug/API_CreateTags.html)
- [DeleteAccessPoint](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteAccessPoint.html): Deletes the specified access point.
- [DeleteFileSystem](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteFileSystem.html): Deletes a file system, permanently severing access to its contents.
- [DeleteFileSystemPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteFileSystemPolicy.html): Deletes the FileSystemPolicy for the specified file system.
- [DeleteMountTarget](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteMountTarget.html): Deletes the specified mount target.
- [DeleteReplicationConfiguration](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteReplicationConfiguration.html): Deletes a replication configuration.
- [DeleteTags](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteTags.html)
- [DescribeAccessPoints](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeAccessPoints.html): Returns the description of a specific Amazon EFS access point if the AccessPointId is provided.
- [DescribeAccountPreferences](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeAccountPreferences.html): Returns the account preferences settings for the AWS account associated with the user making the request, in the current AWS Region.
- [DescribeBackupPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeBackupPolicy.html): Returns the backup policy for the specified EFS file system.
- [DescribeFileSystemPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeFileSystemPolicy.html): Returns the FileSystemPolicy for the specified EFS file system.
- [DescribeFileSystems](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeFileSystems.html): Returns the description of a specific Amazon EFS file system if either the file system CreationToken or the FileSystemId is provided.
- [DescribeLifecycleConfiguration](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeLifecycleConfiguration.html): Returns the current LifecycleConfiguration object for the specified EFS file system.
- [DescribeMountTargets](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeMountTargets.html): Returns the descriptions of all the current mount targets, or a specific mount target, for a file system.
- [DescribeMountTargetSecurityGroups](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeMountTargetSecurityGroups.html): Returns the security groups currently in effect for a mount target.
- [DescribeReplicationConfigurations](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeReplicationConfigurations.html): Retrieves the replication configuration for a specific file system.
- [DescribeTags](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeTags.html)
- [ListTagsForResource](https://docs.aws.amazon.com/efs/latest/ug/API_ListTagsForResource.html): Lists all tags for a top-level EFS resource.
- [ModifyMountTargetSecurityGroups](https://docs.aws.amazon.com/efs/latest/ug/API_ModifyMountTargetSecurityGroups.html): Modifies the set of security groups in effect for a mount target.
- [PutAccountPreferences](https://docs.aws.amazon.com/efs/latest/ug/API_PutAccountPreferences.html): Use this operation to set the account preference in the current AWS Region to use long 17 character (63 bit) or short 8 character (32 bit) resource IDs for new EFS file system and mount target resources.
- [PutBackupPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_PutBackupPolicy.html): Updates the file system's backup policy.
- [PutFileSystemPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_PutFileSystemPolicy.html): Applies an Amazon EFS FileSystemPolicy to an Amazon EFS file system.
- [PutLifecycleConfiguration](https://docs.aws.amazon.com/efs/latest/ug/API_PutLifecycleConfiguration.html): Use this action to manage storage for your file system.
- [TagResource](https://docs.aws.amazon.com/efs/latest/ug/API_TagResource.html): Creates a tag for an EFS resource.
- [UntagResource](https://docs.aws.amazon.com/efs/latest/ug/API_UntagResource.html): Removes tags from an EFS resource.
- [UpdateFileSystem](https://docs.aws.amazon.com/efs/latest/ug/API_UpdateFileSystem.html): Updates the throughput mode or the amount of provisioned throughput of an existing file system.
- [UpdateFileSystemProtection](https://docs.aws.amazon.com/efs/latest/ug/API_UpdateFileSystemProtection.html): Updates protection on the file system.

### [Data Types](https://docs.aws.amazon.com/efs/latest/ug/API_Types.html)

The following data types are supported:

- [AccessPointDescription](https://docs.aws.amazon.com/efs/latest/ug/API_AccessPointDescription.html): Provides a description of an EFS file system access point.
- [BackupPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_BackupPolicy.html): The backup policy for the file system used to create automatic daily backups.
- [CreationInfo](https://docs.aws.amazon.com/efs/latest/ug/API_CreationInfo.html): Required if the RootDirectory > Path specified does not exist.
- [Destination](https://docs.aws.amazon.com/efs/latest/ug/API_Destination.html): Describes the destination file system in the replication configuration.
- [DestinationToCreate](https://docs.aws.amazon.com/efs/latest/ug/API_DestinationToCreate.html): Describes the new or existing destination file system for the replication configuration.
- [FileSystemDescription](https://docs.aws.amazon.com/efs/latest/ug/API_FileSystemDescription.html): A description of the file system.
- [FileSystemProtectionDescription](https://docs.aws.amazon.com/efs/latest/ug/API_FileSystemProtectionDescription.html): Describes the protection on a file system.
- [FileSystemSize](https://docs.aws.amazon.com/efs/latest/ug/API_FileSystemSize.html): The latest known metered size (in bytes) of data stored in the file system, in its Value field, and the time at which that size was determined in its Timestamp field.
- [LifecyclePolicy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html): Describes a policy used by lifecycle management that specifies when to transition files into and out of storage classes.
- [MountTargetDescription](https://docs.aws.amazon.com/efs/latest/ug/API_MountTargetDescription.html): Provides a description of a mount target.
- [PosixUser](https://docs.aws.amazon.com/efs/latest/ug/API_PosixUser.html): The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point.
- [ReplicationConfigurationDescription](https://docs.aws.amazon.com/efs/latest/ug/API_ReplicationConfigurationDescription.html): Describes the replication configuration for a specific file system.
- [ResourceIdPreference](https://docs.aws.amazon.com/efs/latest/ug/API_ResourceIdPreference.html): Describes the resource type and its ID preference for the user's AWS account, in the current AWS Region.
- [RootDirectory](https://docs.aws.amazon.com/efs/latest/ug/API_RootDirectory.html): Specifies the directory on the Amazon EFS file system that the access point provides access to.
- [Tag](https://docs.aws.amazon.com/efs/latest/ug/API_Tag.html): A tag is a key-value pair.
