# Source: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/llms.txt

# Amazon FSx for Windows File Server Windows User Guide

> This is the official Amazon Web Services documentation for Amazon FSx for Windows File Server. Amazon FSx is an AWS service that makes it easier to launch and run shared file storage for Microsoft Windows workloads in the AWS Cloud. These workloads can include your business applications, home directories, web serving environments, and software build setups.

- [What is FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)
- [FSx for Windows best practices](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/windows-best-practices.html)
- [Getting started](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html)
- [Availability and durability](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html)
- [Using FSx for Windows File Server with Microsoft SQL Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/sql-server.html)
- [Quotas](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limits.html)
- [Document history](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/doc-history.html)

## [Accessing your data](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/supported-fsx-clients.html)

### [Accessing data using DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/dns-aliases.html)

Learn how you can use DNS aliases with your Amazon FSx for Windows File Server file systems so that you can continue using the existing DNS names to access data on Amazon FSx when you migrate your file storage to Amazon FSx.

- [Associate DNS aliases with your file system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/step1-assign-dns-alias.html): Learn how to associate DNS aliases with your FSx for Windows File Server file system so that you can access your file shares using DNS names other than the default DNS name that Amazon FSx creates.
- [Configure service principal names (SPNs) for Kerberos](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/step2-configure-spn-kerberos.html): Learn how to configure service principal names required for Kerberos authentication and encryption in transit when using DNS aliases with the Amazon FSx for Windows File Server file systems.
- [Update or create a DNS CNAME record](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/step4-configure-dns-cname.html): When configuring your FSx for Windows File Server environment to use DNS aliases along with Kerberos authentication and encryption, learn how to replace existing DNS records that resolved to the original file system with a DNS record that resolves to the default DNS name of the Amazon FSx file system.
- [Enforcing Kerberos authentication using Group Policy Objects (GPOs)](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/enforce-kerberos.html): Learn how use Group Policy Objects to enforce the use of Kerberos authentication and encryption in transit with clients accessing your Amazon FSx for Windows File Server file systems when you are using DNS aliases instead of the default DNS names.

### [Accessing data using file shares](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-file-shares.html)

Learn how to connect Windows, Linux, and Mac clients to the file shares that you've created on your Amazon FSx for Windows File Server file systems to access your file data.

- [Mapping a file share on an Amazon EC2 Windows instance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/map-share-windows.html): Learn how to map file shares on your Amazon FSx for Windows File Server file systems on an Amazon Elastic Compute Cloud (EC2) instance running Windows using the Windows File Explorer GUI and the command shell.
- [Mounting a file share on an Amazon EC2 Mac instance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/map-share-mac.html): Learn how to map file shares on your Amazon FSx for Windows File Server file systems to an Amazon Elastic Compute Cloud (EC2) Mac instance using the mac Finder GUI and the command shell.
- [Mounting a file share on an Amazon EC2 Linux instance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/map-shares-linux.html): Learn how to mount file shares on your Amazon FSx for Windows File Server file systems to an Amazon Elastic Compute Cloud (EC2) Linux instance that is joined to an Active Directory, and to a Linux instance that is not joined to an Active Directory.
- [Automatically mount file shares on an Amazon EC2 Linux instance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/automount-fsxw-ec2-linux.html): Learn how to mount a FSx for Windows File Server file share on an Amazon Elastic Compute Cloud Linux instance using /etc/fstab so that the share is automatically mounted if the EC2 instance is rebooted.

### [Managing file shares](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-file-shares.html)

Learn how to create, edit, and delete file shares on your Amazon FSx for Windows File Server file systems using the Amazon FSx CLI for PowerShell and the Windows Shared Folders GUI.

- [New-FSxSmbShare command fails with a one-way trust](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/new-smbshare-fails.html): Amazon FSx does not support executing the New-FSxSmbShare PowerShell command in cases where you have a one-way trust.


## [Working with Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/aws-ad-integration-fsxW.html)

### [Using AWS Managed Microsoft AD](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsx-aws-managed-ad.html)

Learn about how FSx for Windows File Server integrates with a Microsoft Active Directory using AWS Directory Service for Microsoft Active Directory and a AWS Managed Microsoft Active Directory.

- [Using AWS Managed Microsoft AD in different VPC or account](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/shared-mad.html): Learn how to join your FSx for Windows File Server file system to an AWS Managed Microsoft AD in a different VPC or account using VPC peering or directory sharing.
- [Validating connectivity to your Active Directory domain controllers](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/validate-ad-domain-controllers.html): Learn how to validate connectivity to your Active Directory domain controllers before creating an FSx for Windows File Server file system.

### [Using a self-managed Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html)

Integrate Amazon FSx directly with Microsoft Active Directory systems, enabling direct access to and from on-premises file systems.

- [Delegating privileges to Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/assign-permissions-to-service-account.html): Learn how to use either the Delegate Control or Advanced Features in the Active Directory User and Computers MMC snap-in to delegate just the privileges necessary to join Amazon FSx file systems to your self-managed Active Directory domain.
- [Validating your Active Directory configuration](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/validate-ad-config.html): Learn how to use the FSx Active Directory Validation tool to validate that your Microsoft Windows Active Directory is configured correctly so that you can join your FSx for Windows File Server file system to it successfully.
- [Join FSx to a self-managed Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/creating-joined-ad-file-systems.html): Learn how to create an FSx for Windows File Server file system that is joined to your on-premises Microsoft Active Directory domain using the AWS Management Console and AWS CLI.
- [Getting IP addresses for manual DNS entries](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/file-system-ip-addresses-for-dns.html): Learn how to find the correct file system IP addresses to use in manual DNS entries for your file system if you are using a third-party (non-Microsoft) DNS service for your default DNS service.
- [Update self-managed Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/update-self-ad-config.html): Learn how to use the AWS Management Console, Amazon FSx API, or AWS CLI to update the service account username and password and the DNS server IP addresses of a file system's self-managed Active Directory configuration.
- [Changing the Amazon FSx service account](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/changing-ad-service-account.html): Learn about what's required to ensure that Amazon FSx can fully manage the file systems and their associated objects in your self-managed Active Directory when you change the Amazon FSx service account.
- [Monitoring self-managed Active Directory updates](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitor-self-ad-update.html): Learn how to monitor the progress of a self-managed Active Directory configuration update on your FSx for Windows File Server file system using the AWS Management Console, the API, or the AWS CLI.


## [Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)

- [Troubleshooting performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance-troubleshooting.html): Learn about issues related to FSx for Windows File Server file system performance, and the steps you can take diagnose and resolve them.


## [Administering file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/administering-file-systems.html)

- [Starting an Amazon FSx remote PowerShell session](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/start-remote-powershell-session.html): This topic provides instructions for starting a long-lived remote PowerShell session on your FSx for Windows File Server file server.
- [One-time file system setup tasks](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/one-time-admin-tasks.html): Learn about simple one-time tasks to set up your Amazon FSx for Windows File Server file system following best practices, using the Amazon FSx CLI for Remote Management on Powershell.
- [Troubleshooting access to the Amazon FSx CLI on PowerShell](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/cant-access-rps.html): Learn how to troubleshoot issues related to accessing the Amazon FSx CLI for remote management on PowerShell when trying to perform file system administrative tasks for FSx for Windows file systems.
- [Changing the weekly maintenance window](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/update-maintenance-window.html): Learn how to set when the weekly maintenance window for your Amazon FSx for Windows File Server file system occurs using the AWS Management Console, AWS CLI and API.

### [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html)

Learn how associate and disassociate DNS aliases with your Amazon FSx for Windows File Server file systems so that you can access your file systems using familiar names instead of the default DNS name that Amazon FSx provides.

- [Viewing existing DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/view-aliases.html): Learn how to view the DNS aliases currently associated with your Amazon FSx for Windows File Server file systems and backups using the Amazon FSx console, the AWS CLI, and API.
- [Associating DNS aliases with file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/add-alias-new-filesystem.html): Learn how to associate DNS aliases when creating a new FSx for Windows File Server file system from scratch, or when creating a file system from a backup, using the AWS Management Console, AWS CLI, and API.
- [Managing DNS aliases on existing file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/manage-aliases-existing-fs.html): Learn how to use the AWS Management Console and AWS CLI to add and remove DNS aliases on existing Amazon FSx for Windows File Server file systems.
- [User sessions and open files](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/manage-sessions-and-files.html): Learn how to monitor connected user sessions and open files on your FSx for Windows File Server file system using the Shared Folders tool.

### [File Server Resource Manager](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-files-fsrm.html)

Learn how to use File Server Resource Manager (FSRM) to manage, classify, and control data on your Amazon FSx for Windows File Server file system through automated policy enforcement, storage quotas, file screening, and compliance reporting.

- [How to Get Started](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/enabling-fsrm.html): Learn how to enable and configure File Server Resource Manager (FSRM) on Amazon FSx for Windows File Server file systems, including requirements, setup procedures, and management options.
- [Quota Management](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-quota-management.html): Learn how to use File Server Resource Manager (FSRM) quota management to control storage space consumption on your FSx for Windows File Server file system.
- [File Groups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-file-groups.html): File groups define logical collections of file name patterns that you must use when configuring file screens, and that you can optionally use when generating storage reports.
- [File Screening](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-file-screening.html): File screening controls which types of files users can save to folders on your file system.
- [File Classification](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-file-classification.html): File classification automatically assigns metadata properties to files based on their content, location, or other attributes.
- [Storage Reports](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-storage-reports.html): Learn how to use File Server Resource Manager (FSRM) storage reports to analyze file system usage, identify files for archiving or deletion, and monitor compliance with file management policies on Amazon FSx for Windows File Server.
- [File Management Tasks](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-file-management.html): Learn about FSRM file management task limitations in Amazon FSx for Windows File Server and how to use PowerShell scripts from client machines to achieve common file management use cases like data archiving and retention policies.
- [FSRM Settings](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-settings.html): Configure system-wide FSRM settings to customize behavior and streamline feature management.
- [Event Logs](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-event-logs.html): Monitor FSRM operations through event logs sent to CloudWatch Logs or Kinesis Data Firehose.
- [Common Use Cases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-common-use-cases.html): Step-by-step examples for common File Server Resource Manager tasks, including setting quotas, restricting file types, classifying data, creating retention policies, and generating storage reports.

### [Managing storage](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-configuration.html)

Learn how to manage your FSx for Windows file system's storage configuration, including storage-related performance and throughput, the storage capacity, the storage type, data deduplication, and more.

- [Managing storage quotas](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-user-quotas.html): Learn about user storage quotas and how to use them to limit how much data storage that users can consume on your Amazon FSx for Windows File Server file systems.
- [Increasing storage capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/increase-storage-capacity.html): Learn how to increase an FSx for Windows file system's storage capacity using the AWS Management Console and AWS CLI.
- [Monitoring storage increases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-storage-capacity-increase.html): Learn how to monitor an in-progress storage capacity increase on your FSx for Windows file system.
- [Increasing storage capacity dynamically](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/automate-storage-capacity-increase.html): Learn how to build a solution that dynamically increases the storage capacity of an FSx for Windows file system when the amount of available storage capacity falls below a settable threshold amount.
- [Updating storage type](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/updating-storage-type.html): Learn about changing the storage type used by your FSx for Windows file system from HDD to SSD.
- [Monitoring storage type updates](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-storage-type-updates.html): Learn how to monitor the progress of a storage type update on an FSx for Windows file system using the AWS Management Console and AWS CLI.
- [Updating the SSD IOPS](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/how-to-provision-ssd-iops.html): Learn how to change the amount of provisioned SSD IOPS for an FSx for Windows file system using the AWS Management Console and AWS CLI.
- [Monitoring provisioned SSD IOPS updates](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-provisioned-ssd-iops.html): Learn how to monitor the status and progress when you make a change to your Amazon FSx for Windows File Server file system's provisioned SSD IOPS.
- [Managing data deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-data-dedup.html): Learn how to manage Data Deduplication settings to minimize or eliminate redundant data and reduce your data storage costs on your FSx for Windows File Server file system using the Amazon FSx CLI for remote management on PowerShell.
- [Troubleshooting data deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/data-dedup-ts.html): Learn to identify and resolve issues that arise when using data deduplication on your FSx for Windows File Server file systems.

### [Using DFS Namespaces](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-dfs-namespaces.html)

Learn how you can use Microsoft's Distributed File System Namespaces service to create solutions that make it easier to access data and increase performance by grouping file systems.

- [Group file systems into one namespace](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/group-fsx-namespace.html): Learn how to set up DFS Namespaces so that you can group multiple FSx for Windows File Server file systems under a single namespace.
- [Sharding data using DFS Namespaces for scale-out performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/scaleout-performance.html): Learn how you can use Microsoft's DFS Namespaces to shard the data on multiple FSx for Windows File Server file systems to get scale-out performance improvements.

### [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html)

Learn how to manage your FSx for Windows File Server file system's performance by modifying the amount of throughput capacity.

- [Modifying throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/increase-throughput-capacity.html): Learn how to scale your FSx for Windows File Server file system's throughput capacity using the AWS Management Console and AWS CLI.
- [Monitoring throughput capacity updates](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-throughput-capacity-changes.html): Learn how to monitor the status and progress of a throughput capacity update on your Amazon FSx for Windows File Server file system using the AWS Management Console and AWS CLI.
- [Managing network type](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/manage-network-type.html): Describes the two network types of IPv4-only and dual-stack (IPv4 and IPv6) for FSx for Windows file systems and how to manage them.
- [Tagging resources](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/tag-resources.html): Learn how to use tags to assign your own metadata to your Amazon FSx resources which can help you categorize and identify them to meet your needs.
- [Update a file system using the AWS CLI](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/walkthrough03-update-file-system.html): Learn how to make changes to an existing FSx for Windows File Server file system configuration using the AWS CLI.


## [Protecting your data](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/data-protection.html)

### [Protecting your data with backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html)

Learn how to use Amazon FSx native backups and AWS Backup to take automatic and user-initiated backups that protect the data on your FSx for Windows File Server file systems.

- [Creating user-initiated backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/creating-backups.html): Learn how to create a user-initiated backup of your FSx for Windows File Server file system using the AWS Management Console.
- [Deleting backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/delete-backups.html): Learn how to delete backups of your FSx for Windows File Server file systems.
- [Copying backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/copying-backups.html): Learn how to copy backups of your FSx for Windows File Server file system.
- [Restoring a backup](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/how-to-restore-backups.html): Learn how to restore an FSx for Windows File Server file system backup to a new file system

### [Protecting data with shadow copies](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/shadow-copies-fsxW.html)

Learn how to configure shadow copies on your FSx for Windows File Server file systems to protect so that users can view and restore previous versions of individual files.

- [Configure shadow copies to use default settings](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/setting-up-fsx-shadow-copies.html): Learn how to set up automated shadow copies on your Amazon FSx file system that use the default storage and schedule configuration.
- [Setting the maximum amount of shadow copy storage](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/shadow-copy-storage.html): Learn how to define the maximum amount of storage that shadow copies can consume on your FSx for Windows File Server file system to help manage file system storage capacity.
- [Viewing shadow copy storage](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/get-fsxshadowstorage.html): Learn how to see the shadow copy storage configuration on your FSx for Windows File Server file system using PowerShell.
- [Creating a custom shadow copy schedule](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/shadow-schedules.html): Learn how to create a customized shadow copy schedule on your FSx for Windows File Server file system to meet your organizations storage retention goals.
- [Viewing the shadow copy schedule](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/get-fsxshadowcopy-sched.html): Learn how to see the current shadow copy schedule on your Amazon FSx for Windows File Server file system.
- [Creating a shadow copy](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/new-fsxshadow-copy.html): Learn how to manually create a shadow on your FSx for Windows File Server file system when one is needed out cycle with the shadow copy schedule.
- [Viewing existing shadow copies](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/get-fsxshadow-copies.html): Learn how to see the set of existing shadow copies on your FSx for Windows File Server file system as part of storage management activities.
- [Deleting shadow copies](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/remove-fsxshadow-copies.html): Learn how to delete exising shadow copies from your FSx for Windows File Server file system as part of storage management activities.
- [Deleting a shadow copy schedule](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/remove-fsxshadowcopy-sched.html): Learn how to delete the shadow copy configuration on your FSx for Windows File Server file system, including all existing shadow copies and the shadow copy schedule.
- [Deleting a shadow copy configuration](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/remove-fsxshadowstorage.html): Learn how to delete the shadow copy configuration on your FSx for Windows File Server file system, including all existing shadow copies and the shadow copy schedule.
- [Troubleshooting shadow copies](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/shadow-copy-ts.html): Learn how to address problems and situations that arise when you are using shadow copies on your Amazon FSx for Windows File Server file systems.


## [Migrating to Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-to-fsx.html)

### [Migrating files to FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-fsx.html)

Learn how to migrate the file data stored in your on-premises Microsoft Windows File Server file systems to an FSx for Windows File Server file system using the AWS DataSync data transfer service

- [Migrating files using AWS DataSync](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-to-fsx-datasync.html): Learn how to migrate your file storage, NTFS ACLs and SACLs from your on-premises servers to your FSx for Windows File Server file system using AWS DataSync.
- [Migrating files using Robocopy](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-to-fsx.html): Use robocopy to migrate your on-premises file data to your Amazon FSx for Windows File Server file system as part of the process for migrating to FSx for Windows File Server.
- [Migrating file share configurations](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-file-share-config-to-fsx.html): Learn how to migrate your on-premises Microsoft Windows File Server file share configuration to FSx for Windows File Server as part of the overall migration process.
- [Migrating your on-premises DNS configuration to FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-dns-config.html): Learn how to migrate your on-premises DNS configuration to your FSx for Windows File Server file system so that you can use the familiar DNS names as aliases to access your FSx for Windows File Server file system shares.
- [Cutting over to FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/cutover-to-fsx.html): Learn how to cut over your workloads and users to your Amazon FSx for Windows File Server file systems after completing the migration of your on-premises file storage, file share configuration, and DNS configuration.


## [Monitoring file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring_overview.html)

### [Monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-cloudwatch.html)

Learn how to use Amazon CloudWatch metrics and alarms to monitor the performance and health of your Amazon FSx for Windows File Server file system.

- [Accessing file system metrics](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/accessingmetrics.html): Learn how access and view your FSx for Windows File Server file system metrics using the AWS Management Console, AWS CLI, and API.
- [Creating CloudWatch alarms](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/creating_alarms.html): Learn how to create CloudWatch alarms to help you monitor your FSx for Windows File Server file systems for specific conditions using the AWS Management Console and AWS CLI.
- [CloudTrail logs](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/logging-using-cloudtrail.html): Learn how Amazon FSx for Windows File Server logs all actions by users, roles, and other AWS services with AWS CloudTrail as events.


## [Security](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/security.html)

### [Data protection](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/data-protection-encryption.html)

Learn how the AWS shared responsibility model applies to data protection in FSx for Windows File Server.

- [Encryption at rest](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption-at-rest.html): Learn how Amazon FSx uses AWS KMS for encryption at rest, including AWS KMS key types, key policies, and permissions.
- [Encryption in transit](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption-in-transit.html): Learn how to manage encryption in transit for FSx for Windows File Server file systems using SMB encryption.
- [Windows ACLs](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-file-folder.html): Learn how to control file- and folder-level access in FSx for Windows File Server using Windows ACLs.
- [File system access control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html): Learn how to control access to your Amazon FSx file system using Amazon VPC security groups and network ACLs.

### [Logging end user access](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/file-access-auditing.html)

Learn how to audit end-user access to files, folders, and file shares in FSx for Windows File Server.

- [Setting file and folder auditing controls](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/faa-audit-controls.html): Learn how to set file and folder auditing controls using Windows File Explorer GUI or PowerShell commands to monitor user access attempts on your file system.
- [Managing file access auditing](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/manage-faa.html): Learn how to enable and manage file access auditing on FSx for Windows File Server file systems.

### [Identity and access management](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/security-iam.html)

Learn how IAM controls access to Amazon FSx for Windows File Server resources.

- [How Amazon FSx for Windows File Server works with IAM](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/security_iam_service-with-iam.html): Learn how FSx for Windows File Server works with IAM to manage access.
- [Identity-based policy examples](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/security_iam_id-based-policy-examples.html): Learn how to create identity-based policies for FSx for Windows File Server to grant permissions for creating, accessing, and deleting resources.
- [AWS managed policies](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon FSx and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/security_iam_troubleshoot.html): Learn how to troubleshoot common identity and access issues in FSx for Windows File Server, including unauthorized actions, IAM role permissions, and cross-account access to resources.
- [Using tags with Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-tags-fsx.html): Learn how to use tags with Amazon FSx to control access to resources and implement attribute-based access control (ABAC).
- [Using service-linked roles](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-service-linked-roles.html): How to use service-linked roles to give FSx for Windows File Server access to resources in your AWS account.
- [Compliance Validation](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsx-compliance.html): Learn about compliance validation for Amazon FSx for Windows File Server.
- [Interface VPC endpoints](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsx-vpc-endpoints.html): You can use interface VPC endpoints (AWS PrivateLink) to access the Amazon FSx API from your VPC without sending traffic over the internet.


## [Working with other services](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/walkthroughs.html)

- [Using Amazon FSx with Amazon WorkSpaces Applications](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/walkthrough04-fsx-with-appstream2.html): Learn how to use Amazon FSx with Amazon WorkSpaces Applications Amazon AppStream 2.0 to provide personal persistent storage for each user and create shared folders for multiple users to access common files.
- [Using FSx for Windows File Server with Amazon Kendra](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/kendra-integration.html): Learn about using Amazon Kendra with your Amazon FSx for Windows File Server file systems to index your data and provide your user with intelligent search capabilities.


## [Troubleshooting](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/troubleshooting.html)

- [You can't access your file system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/unable-to-access.html): Learn how to troubleshoot problems related to accessing your FSx for Windows File Server file systems.
- [Creating file system fails](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/unable-to-create-fs.html): Learn about troubleshooting issues related to unsuccessful attempts to create an FSx for Windows File Server file system.
- [File system is in a misconfigured state](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/misconfigured-ad-config.html): Learn how to diagnose and resolve issue that cause an FSx for Windows File Server file system to enter a misconfigured state.
- [You can't configure DFS-R on a Multi-AZ or Single-AZ 2 file system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/dfs-r.html): Learn why Microsoft Distributed File System Replication (DFS-R) is not supported on Multi-AZ and Single-AZ file systems in Amazon FSx, and how to achieve high availability natively.
- [Storage or throughput capacity updates fail](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/admin-actions-ts.html): Learn how to troubleshoot and resolve common issues when updating storage or throughput capacity for Amazon FSx file systems, including KMS key access, Active Directory configuration, and capacity constraints.
