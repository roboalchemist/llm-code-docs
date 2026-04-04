# Source: https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/llms.txt

# FSx for OpenZFS OpenZFS User Guide

> This is the official Amazon Web Services documentation for FSx for OpenZFS. FSx for OpenZFS is an AWS service that makes it easier to launch and run fully-featured OpenZFS file systems in the AWS Cloud. The FSx for OpenZFS User Guide describes key concepts for FSx for OpenZFS and provides instructions for launching and using your file system.

- [What is Amazon FSx for OpenZFS?](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/what-is-fsx.html)
- [Setting up a file system](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/getting-started.html)
- [AWS Regions](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/available-aws-regions.html)
- [Availability and durability](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/availability-durability.html)
- [Tagging your resources](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/tag-resources.html)
- [Troubleshooting](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/troubleshooting.html)
- [Service quotas](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/limits.html)
- [Document history](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/document-history.html)

## [Accessing your data](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/accessing-your-data.html)

- [Accessing data within the AWS Cloud](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-within-aws.html): Learn how to access your data within the AWS Cloud using Amazon VPC
- [Accessing data from on-premises](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-fsxopenzfs-onprem.html): Learn how to access your file systems from on-premises compute instances
- [Mounting volumes](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/mounting-volumes.html): Information about mounting volumes to file systems.

### [Accessing data with S3 access points](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/s3accesspoints-for-FSx.html)

Learn how to use Amazon S3 access points with FSx for OpenZFS to simplify data access, enforce permissions, and perform object operations on files stored in FSx volumes.

- [Naming rules, restrictions, and limitations](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-point-restrictions-limitations-naming-rules.html): Learn about Amazon S3 access points attached to FSx for OpenZFS volumes, including naming rules, restrictions, and limitations for managing data access in the cloud.
- [Referencing access points](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/referencing-access-points.html): Learn how to use Amazon S3 access point ARNs, aliases, and virtual-hostedâstyle URIs to perform operations on FSx for OpenZFS volumes using the Amazon S3 object API.
- [Access point compatibility](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-object-api-support.html): Learn which S3 API object operations you can with S3 access points attached to FSx for OpenZFS volumes for data access.
- [Managing access](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/s3-ap-manage-access-fsx.html): Learn how to configure Amazon S3 access points for Amazon FSx volumes, including permissions, user identity, VPC restrictions, and encryption.

### [Creating an access point](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/fsxz-creating-access-points.html)

Create up to 10,000 access points to simplify managing data access at scale in Amazon S3.

- [Creating access points](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/create-access-points.html): The FSx for OpenZFS volume must already exist in your account when creating an S3 access point for your volume.
- [Creating access points restricted to a VPC](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-vpc.html): Configuring Amazon S3 access points with a virtual private cloud (VPC)

### [Managing access points](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-manage.html)

Managing your Amazon S3 access point attachments

- [Listing S3 access point attachments](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-list.html): This section explains how to list S3 access point using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Viewing access point details](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-details.html): This section explains how to view the details of S3 access points using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Deleting an S3 access point attachment](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/delete-access-point.html): This section explains how to delete S3 access points using the AWS Management Console, AWS Command Line Interface, or REST API.

### [Using access points](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-usage-examples.html)

Access file data with Amazon S3 access point attachments, using a compatible subset of S3 operations and other AWS services, such as AWS CloudTrail.

- [Download a file](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/get-object-ap.html): The following get-object example command shows how you can use the AWS CLI to download a file through an access point.
- [Upload a file](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/put-object-ap.html): The following put-object example command shows how you can use the AWS CLI to upload a file through an access point.
- [List files](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/list-object-ap.html): The following example lists files through the access point alias my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b-ext-s3alias owned by account ID 111122223333 in Region us-east-2.
- [Add a tag-set](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/add-tag-set-ap.html): The following put-object-tagging example command shows how you can use the AWS CLI to add a tag-set through an access point.
- [Delete a file](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/delete-object-ap.html): The following delete-object example command shows how you can use the AWS CLI to delete a file through an access point.
- [Troubleshooting access points](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/troubleshooting-access-points.html): This section describes symptoms, causes, and resolutions for when you encounter issues accessing your FSx data from S3 access points.
- [Accessing data using AWS container services](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/openzfs-integrations.html): Learn about using FSx for OpenZFS with AWS container services.


## [Performance](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html)

- [Working with SSD storage](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance-ssd.html): FSx for OpenZFS file systems that use the SSD (provisioned) storage class consist of a file server that clients communicate with and a set of disks attached to that file server.
- [Working with Intelligent-Tiering](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance-intelligent-tiering.html): The FSx for OpenZFS Intelligent-Tiering storage class offers elastic, low-cost storage for workloads that traditionally run on Network Attached Storage (NAS) file systems.


## [Managing file systems](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-file-systems.html)

- [Creating a file system](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/creating-file-systems.html): How to create an FSx for OpenZFS file system
- [Viewing a file system](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/viewing-file-system.html): Learn how to view your file system details.

### [Updating a file system](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/updating-file-system.html)

How to update a FSx for OpenZFS file system.

- [Modifying SSD storage capacity and IOPS](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-storage-capacity.html): Learn how to increase the storage capacity configured on your Amazon FSx for OpenZFS file system when you need additional storage.
- [Modifying SSD read cache](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-ssd-read-cache.html): Learn how to modify your provisioned SSD read cache.
- [Modifying throughput capacity](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-throughput-capacity.html): Learn how to modify the throughput capacity configured on your FSx for OpenZFS file system when you need additional performance.
- [Modifying network type](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/manage-network-type.html): Describes the two network types of IPv4-only and dual-stack (IPv4 and IPv6) for FSx for OpenZFS file systems and how to manage them.
- [Modifying maintenance windows](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/maintenance-windows.html): Describes the Amazon FSx weekly maintenance window and how to manage it.
- [Deleting a file system](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/delete-file-system.html): Learn how to delete a FSx for OpenZFS file system.


## [Managing volumes](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html)

- [Creating a volume](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/creating-volumes.html): How to create an FSx for OpenZFS volume.
- [Viewing a volume](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/viewing-volumes.html): How to see the FSx for OpenZFS volumes that are currently on your file system.
- [Updating a volume](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/updating-volumes.html): How to update a volume configuration.
- [Deleting a volume](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/deleting-volumes.html): How to delete an FSx for OpenZFS volume.


## [Protecting your data](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/protecting-data.html)

### [Protect data with backups](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-backups.html)

Get more information about using a file system's backups in FSx for OpenZFS.

- [Copying backups](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/copy-backups.html): You can use Amazon FSx to manually copy backups within the same AWS account to another AWS Region (cross-Region copies) or within the same AWS Region (in-Region copies).
- [Restoring backups](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/restoring-backups.html): You can use an available backup to create a new file system, effectively restoring a point-in-time snapshot of another file system.
- [Deleting backups](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/delete-backups.html): Deleting a backup is a permanent, unrecoverable action.

### [Protecting data with snapshots](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/snapshots-openzfs.html)

Learn how to set up and manage OpenZFS snapshots on your file systems.

- [Setting up a custom snapshot schedule](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/custom-snapshot-schedule.html): Learn how to set up an automated custom snapshot schedule for your FSx for OpenZFS volumes using a custom CloudFormation template.

### [Protect data with replication](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/on-demand-replication.html)

Learn how to use on-demand data replication.

- [Setting up ongoing periodic data replication](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/ongoing-periodic-data-replication.html): Learn how to set up ongoing periodic data replication.


## [Monitoring file systems](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/monitoring_overview.html)

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/monitoring-cloudwatch.html)

Learn how to monitor Amazon FSx with Amazon CloudWatch metrics.

- [Using CloudWatch metrics](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/how_to_use_metrics.html): Learn how to use FSx for OpenZFS metrics to monitor your file system.
- [Accessing CloudWatch metrics](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/accessingmetrics.html): Learn how to access Amazon FSx metrics for CloudWatch.
- [Metrics and dimensions](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/fsx-openzfs-metrics.html): Find the metrics published in the AWS/FSx namespace in Amazon CloudWatch for all FSx for OpenZFS file systems.
- [Performance warnings and recommendations](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance-insights-FSxZ.html): Performance warnings that you might see from CloudWatch metrics, and recommendations to resolve them.
- [Creating CloudWatch alarms](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/creating_alarms.html): Learn how to create CloudWatch alarms to monitor Amazon FSx.
- [Logging API calls with AWS CloudTrail](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/logging-using-cloudtrail-win.html): Learn how to log FSx for OpenZFS API calls with AWS CloudTrail.


## [Migrating your existing file storage](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/migrating-fsx-openzfs.html)

- [Migrating files with AWS DataSync](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/migrate-files-to-fsx-datasync.html): Learn how to migrate existing files to FSx for OpenZFS.
- [Migrating files with rsync](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/fsx-migrate-rsync.html): Learn how to migrate existing files to Amazon FSx using rsync.
- [Migrating files with Robocopy](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/fsx-migrate-robocopy.html): How to migrate files to Amazon FSx with robocopy.
- [Cutting over to your file system](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/cutover.html): Learn how to cut over to your FSx for OpenZFS file system.


## [Security](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/security.html)

### [Data encryption](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon FSx.

- [Encryption at rest](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/encryption-rest.html): Learn about encryption of data at rest.
- [Encryption in transit](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/encryption-transit.html): Learn about encryption in transit.
- [Managing file system access](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/limit-access-security-groups.html): Learn about controlling access to your Amazon FSx for OpenZFS file systems and volumes.

### [Identity and access management](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/security-iam.html)

How to authenticate requests and manage access your Amazon FSx resources.

- [How Amazon FSx for OpenZFS works with IAM](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/security_iam_service-with-iam.html): Learn about how Amazon FSx for OpenZFS works with IAM.
- [Identity-based policy examples](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/security_iam_id-based-policy-examples.html): Find examples of identity-based policies.
- [AWS managed policies](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon FSx and recent changes to those policies.
- [Troubleshooting IAM](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/security_iam_troubleshoot.html): Troubleshoot issues with Amazon FSx for OpenZFS identity and access.
- [Using tags to control access to resources](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-tags-fsx.html): Learn how to use tags to control access to Amazon FSx resources and implement attribute-based access control (ABAC).
- [Using service-linked roles](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-service-linked-roles.html): How to use service-linked roles to give Amazon FSx access to resources in your AWS account.
- [Compliance validation](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/fsx-openzfs-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Interface VPC endpoints](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/fsx-vpc-endpoints.html): You can use interface VPC endpoints (AWS PrivateLink) to access the Amazon FSx API from your VPC without sending traffic over the internet.
- [Resilience](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon FSx for OpenZFS features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/infrastructure-security.html): Learn how Amazon FSx for OpenZFS isolates service traffic.
