# Source: https://docs.aws.amazon.com/filegateway/latest/files3/llms.txt

# AWS Storage Gateway Amazon S3 File Gateway User Guide

> Storage Gateway is a hybrid storage service that seamlessly connects your on-premises applications to Amazon Web Services cloud storage. You can use the service for backup and archiving, disaster recovery, cloud bursting, storage tiering, and migration. Storage Gateway is a hybrid storage service that seamlessly connects your on-premises applications to Amazon Web Services cloud storage. You can use the service for backup and archiving, disaster recovery, cloud bursting, storage tiering, and migration. This guide explains how to create and manage a Storage Gateway.

- [Best practices](https://docs.aws.amazon.com/filegateway/latest/files3/best-practices.html)
- [API Reference](https://docs.aws.amazon.com/filegateway/latest/files3/AWSStorageGatewayAPI.html)
- [Document history](https://docs.aws.amazon.com/filegateway/latest/files3/DocumentHistory.html)
- [AL2 to AL2023 Migration](https://docs.aws.amazon.com/filegateway/latest/files3/al2-to-al2023-migration.html)
- [Release notes](https://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)

## [What is Amazon S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html)

- [How S3 File Gateway works](https://docs.aws.amazon.com/filegateway/latest/files3/file-gateway-concepts.html): Learn about how Amazon S3 File Gateway works, including details about the solution architecture, basic configuration, operational capabilities, and use cases.


## [Getting Started with AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/setting-up.html)

- [Sign up for Amazon Web Services](https://docs.aws.amazon.com/filegateway/latest/files3/setting-up-aws-sign-up.html): Learn how to sign up for AWS and create an AWS account.
- [Create an IAM user with administrator privileges](https://docs.aws.amazon.com/filegateway/latest/files3/setting-up-create-iam-user.html): Learn how to create an IAM user with administrative privileges for your AWS account.
- [Accessing AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/WhatIsAPIIntro.html): Learn how to access AWS Storage Gateway through the Storage Gateway console or programmatically using the AWS SDKs.
- [AWS Regions that support Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/available-regions-intro.html): Learn which AWS Regions you can use to store your data when you activate your gateway in Storage Gateway.


## [File Gateway setup requirements](https://docs.aws.amazon.com/filegateway/latest/files3/Requirements.html)

### [Managing local disks](https://docs.aws.amazon.com/filegateway/latest/files3/ManagingLocalStorage-common.html)

Topics describing how to manage local storage for your gateway.

- [Deciding the amount of local disk storage](https://docs.aws.amazon.com/filegateway/latest/files3/decide-local-disks-and-sizes.html): Learn about local disk storage requirements for your File Gateway
- [Add cache storage](https://docs.aws.amazon.com/filegateway/latest/files3/ConfiguringLocalDiskStorage.html): Configure additional cache storage space to accommodate increased File Gateway workloads.
- [Using ephemeral storage with EC2 gateways](https://docs.aws.amazon.com/filegateway/latest/files3/ephemeral-disk-cache.html): Learn how to prevent data loss when using ephemeral disk storage with File Gateway.


## [Using the hardware appliance](https://docs.aws.amazon.com/filegateway/latest/files3/hardware-appliance.html)

- [Setting up your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/files3/appliance-quick-start.html): Set up and configure your Storage Gateway Hardware Appliance.
- [Physically installing your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/files3/appliance-rack-mount.html): Learn how to physically mount and connect your hardware appliance
- [Accessing the hardware appliance console](https://docs.aws.amazon.com/filegateway/latest/files3/access-hardware-appliance-console.html): Learn how to access the hardware appliance console.
- [Configuring hardware appliance network parameters](https://docs.aws.amazon.com/filegateway/latest/files3/appliance-configure-network.html): Configure network parameters for your Storage Gateway Hardware Appliance.
- [Activating your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/files3/appliance-activation.html): Activate your hardware appliance as a Storage Gateway.
- [Creating a gateway on your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/files3/appliance-launch-gateway.html): Create a Storage Gateway on the AWS Storage Gateway Hardware Appliance.
- [Configuring a gateway IP address on the hardware appliance](https://docs.aws.amazon.com/filegateway/latest/files3/appliance-configure-ip.html): Configure the gateway IP address on the hardware appliance to work with applications.
- [Removing gateway software from your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/files3/appliance-remove-gateway.html): Remove gateway software from your Storage Gateway Hardware Appliance.
- [Deleting your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/files3/delete-appliance.html): Delete your Storage Gateway Hardware Appliance from your AWS account.


## [Creating your gateway](https://docs.aws.amazon.com/filegateway/latest/files3/create-file-gateway.html)

- [Create an S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/create-gateway-file.html): Create, deploy, and activate a File Gateway in AWS Storage Gateway.

### [Activating a gateway in a VPC](https://docs.aws.amazon.com/filegateway/latest/files3/gateway-private-link.html)

Learn how to activate your AWS Storage Gateway in a VPC, including how to create a VPC endpoint and configure your gateway to send data through the VPC.

- [Create a VPC endpoint for Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/create-vpc-endpoint.html): Create a VPC endpoint.


## [Creating a file share](https://docs.aws.amazon.com/filegateway/latest/files3/GettingStartedCreateFileShare.html)

- [Avoid unanticipated costs](https://docs.aws.amazon.com/filegateway/latest/files3/avoid-unanticipated-costs.html): When a file is written to the File Gateway by an NFS client, the File Gateway uploads the file's data to Amazon S3 followed by its metadata.
- [Encrypt objects stored by File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/encrypt-objects-stored-by-file-gateway-in-amazon-s3.html): S3 File Gateway supports the following methods of server-side encryption for the data that it stores in Amazon S3:

### [Create an NFS file share](https://docs.aws.amazon.com/filegateway/latest/files3/create-nfs-file-share.html)

Creating an NFS File Share.

- [Create NFS file share with default configuration](https://docs.aws.amazon.com/filegateway/latest/files3/nfs-fileshare-quickstart-settings.html): Create a Network File System (NFS) file share with default settings.
- [Create NFS file share with custom configuration](https://docs.aws.amazon.com/filegateway/latest/files3/CreatingAnNFSFileShare.html): Use this procedure to create an NFS file share with customized settings.

### [Create an SMB file share](https://docs.aws.amazon.com/filegateway/latest/files3/create-smb-file-share.html)

Topics describing various methods for creating an SMB file share.

- [Create SMB file share with default configuration](https://docs.aws.amazon.com/filegateway/latest/files3/smb-fileshare-quickstart-settings.html): Create an SMB file share with default settings
- [Create SMB file share with custom configuration](https://docs.aws.amazon.com/filegateway/latest/files3/CreatingAnSMBFileShare.html): Use this procedure to create an SMB file share with customized settings.


## [Mounting and using your file share](https://docs.aws.amazon.com/filegateway/latest/files3/getting-started-use-fileshare.html)

- [Mount your NFS file share on your client](https://docs.aws.amazon.com/filegateway/latest/files3/GettingStartedAccessFileShare.html): Learn about how to mount your NFS file share, including command prompt commands for mounting the file share on your Linux, MacOS, or Microsoft Windows client.
- [Mount your SMB file share on your client](https://docs.aws.amazon.com/filegateway/latest/files3/using-smb-fileshare.html): Learn how to mount your SMB file share, including command prompt commands for mounting the file share for all authorized AD users, specific users, or guests.
- [Using file shares on buckets with pre-existing objects](https://docs.aws.amazon.com/filegateway/latest/files3/FileSharePrexistingObjects.html): Learn tips and best practices for working with file shares on a bucket with pre-exisiting objects
- [Test your S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/GettingStartedTestFileShare.html): Test your gateway by copying files and verifying that they appear in your Amazon S3 bucket.


## [Managing your Amazon S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/managing-gateway-file.html)

- [Edit basic gateway information](https://docs.aws.amazon.com/filegateway/latest/files3/edit-gateway-information.html): Edit basic information for an existing Storage Gateway

### [Granting access and permissions](https://docs.aws.amazon.com/filegateway/latest/files3/add-file-share.html)

Topics describing how to grant appropriate access and permissions for file shares and Amazon S3 buckets.

- [Granting access to an S3 bucket](https://docs.aws.amazon.com/filegateway/latest/files3/grant-access-s3.html): Grant access for your gateway to upload files to an Amazon S3 bucket using IAM roles and access policies.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/filegateway/latest/files3/cross-service-confused-deputy-prevention.html): Learn about the cross-service confused deputy problem and how to prevent it.
- [Using a file share for cross-account access](https://docs.aws.amazon.com/filegateway/latest/files3/cross-account-access.html): Use a file share for cross-account access.
- [Delete a file share](https://docs.aws.amazon.com/filegateway/latest/files3/remove-file-share.html): Learn how to delete a file share using the Storage Gateway console, including how to forcibly delete the file share without waiting for data to upload first.

### [Editing gateway SMB settings](https://docs.aws.amazon.com/filegateway/latest/files3/edit-smb-access-settings.html)

Topics describing how to edit gateway-level SMB settings.

- [Set gateway security level](https://docs.aws.amazon.com/filegateway/latest/files3/security-strategy.html): Set a security level to specify whether your gateway should require SMB encryption.
- [Configure Active Directory authentication](https://docs.aws.amazon.com/filegateway/latest/files3/enable-ad-settings.html): Use your corporate Active Directory for user authenticated access to your SMB file share
- [Provide guest access](https://docs.aws.amazon.com/filegateway/latest/files3/guest-access.html): Provide guest access to allow anyone with the guest user credentials to use your file share.
- [Configure local groups](https://docs.aws.amazon.com/filegateway/latest/files3/local-group-settings.html): Configure local groups to grant Active Directory users special file share permissions.
- [Set file share visibility](https://docs.aws.amazon.com/filegateway/latest/files3/file-share-visibility.html): Set file share visibility to control which shares are presented to users.
- [Edit SMB file share settings](https://docs.aws.amazon.com/filegateway/latest/files3/edit-smbfileshare-settings.html): Learn how to edit settings for an existing SMB file share.
- [Limit SMB file share access](https://docs.aws.amazon.com/filegateway/latest/files3/edit-file-share-access-smb.html): Learn how to add allowed or denied users or groups for your SMB file share to limit access to authenticated users in your Active Directory environment.
- [Change file share encryption method](https://docs.aws.amazon.com/filegateway/latest/files3/edit-file-share-encryption.html): Learn how to change the method that your NFS or SMB file share uses to encrypt data at rest in Amazon S3.
- [Edit NFS file share settings](https://docs.aws.amazon.com/filegateway/latest/files3/edit-storage-class.html): Edit NSF file share settings such as storage class, name, metadata, squash level, and cache refresh.
- [Edit NFS file share metadata defaults](https://docs.aws.amazon.com/filegateway/latest/files3/edit-metadata-defaults.html): Specify the default metadata values that your gateway sets for Amazon S3 bucket objects that do not already have their own.
- [Limit NFS file share access](https://docs.aws.amazon.com/filegateway/latest/files3/edit-nfs-client.html): Edit access settings to allow only clients from specific IP addresses or IP ranges for your NFS fileshare.
- [Refreshing Amazon S3 bucket object cache](https://docs.aws.amazon.com/filegateway/latest/files3/refresh-cache.html): Topics describing how to refresh the S3 bucket object cache for a file share and configure a schedule to refresh the cache automatically.
- [Using S3 Object Lock](https://docs.aws.amazon.com/filegateway/latest/files3/s3-object-lock.html): How to use S3 Object Lock with an Amazon S3 File Gateway
- [File share status](https://docs.aws.amazon.com/filegateway/latest/files3/understand-file-share.html): Learn about the various status indicators that can be for file shares in the Storage Gateway console.
- [Gateway status](https://docs.aws.amazon.com/filegateway/latest/files3/understand-gateway-status.html): Learn how to interpret gateway status indicators displayed by the Storage Gateway console
- [Managing bandwidth](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceUpdateBandwidth-common.html): Topics describing how to manage the bandwidth-rate limits for your Amazon S3 File Gateway.


## [Monitoring Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/Main_monitoring-gateways-common.html)

- [Understanding CloudWatch alarms](https://docs.aws.amazon.com/filegateway/latest/files3/cloudwatch-alarms.html): Learn about CloudWatch alarms and how to use them to monitor your File Gateway.
- [Create recommended CloudWatch alarms](https://docs.aws.amazon.com/filegateway/latest/files3/cloudwatch-alarms-create-recommended.html): Create the recommended CloudWatch alarms to monitor your File Gateway resources.
- [Create a custom CloudWatch alarm](https://docs.aws.amazon.com/filegateway/latest/files3/cloudwatch-alarms-create-alarm.html): Create custom gateway alarms to be notified of specific gateway issues or behavior.
- [Monitoring your S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html): Topics describing how to measure metrics and audit logs for S3 File Gateway.
- [Create a cache report](https://docs.aws.amazon.com/filegateway/latest/files3/create-cache-report.html): Generate a report of the file metadata currently cached by an S3 File Gateway.
- [Manage cache reports](https://docs.aws.amazon.com/filegateway/latest/files3/manage-cache-reports.html): View, check status, or delete cache reports for a specific file share associated with your S3 File Gateway.
- [Understanding cache reports](https://docs.aws.amazon.com/filegateway/latest/files3/understand-cache-reports.html): Learn how to interpret the information provided in cache reports for the file shares associated with your S3 File Gateway.


## [Maintaining your gateway](https://docs.aws.amazon.com/filegateway/latest/files3/maintaining-gateway.html)

### [Managing gateway updates](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceManagingUpdate-common.html)

Use the Storage Gateway console to turn gateway maintenance updates updates on or off, or configure an update schedule.

- [Turn maintenance updates on or off](https://docs.aws.amazon.com/filegateway/latest/files3/maintenance-updates-on-off.html): Use the Storage Gateway console to turn maintenance updates on or off for a specific gateway.
- [Modify the gateway maintenance window schedule](https://docs.aws.amazon.com/filegateway/latest/files3/configure-maintenance-window-schedule.html): Use the Storage Gateway console to configure the maintenance window schedule for a specific gateway.
- [Apply an update manually](https://docs.aws.amazon.com/filegateway/latest/files3/apply-update-manually.html): Learn how to manually apply a gateway appliance software update using the Storage Gateway console.

### [Performing maintenance tasks using the local console](https://docs.aws.amazon.com/filegateway/latest/files3/manage-on-premises.html)

Topics describing how to perform maintenance tasks using the gateway local console.

- [Accessing the gateway local console](https://docs.aws.amazon.com/filegateway/latest/files3/accessing-local-console.html): Topics describing how to access the gateway local console, where you can perform various maintenance tasks for your gateway.

### [Performing tasks on the virtual machine local console](https://docs.aws.amazon.com/filegateway/latest/files3/manage-on-premises-fgw.html)

Topics describing how to perform maintenance tasks on the VM local console for your File Gateway.

- [Logging in to the File Gateway local console](https://docs.aws.amazon.com/filegateway/latest/files3/LocalConsole-login-fgw.html): How to log in to the File Gateway local console or Storage Gateway console and change your local console password.
- [Configuring an HTTP proxy](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceRoutingProxy-fgw.html): Use the gateway local console to configure an HTTP proxy server if necessary for your gateway to communicate over the internet.
- [Configuring your gateway network settings](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceConfiguringStaticIP-fgw.html): Use the gateway local console to configure network settings, including setting a static IP address for your gateway.
- [Testing your gateway's network connectivity](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceTestGatewayConnectivity-fgw.html): Use the gateway local console to test your gateway's network connectivity.
- [Viewing your gateway system resource status](https://docs.aws.amazon.com/filegateway/latest/files3/system-resource-check-fgw.html): Use the gateway local console to view the virtual machine system resources allocated to your gateway.
- [Configuring your NTP server](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceTimeSync-fgw.html): Manage your system time configuration, including NTP, and synchronize the VM time on your gateway with your hypervisor host to avoid time drift.
- [Running Storage Gateway commands on the local console](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceGatewayConsole-fgw.html): Run commands from the storage gateway console terminal to perform maintenance tasks and collect gateway information.

### [Performing tasks on the EC2 local console](https://docs.aws.amazon.com/filegateway/latest/files3/ec2-local-console-fgw.html)

Topics describing how to perform maintenance tasks for a File Gateway deployed on an Amazon EC2 instance using the local console.

- [Logging in to your EC2 gateway local console](https://docs.aws.amazon.com/filegateway/latest/files3/EC2_MaintenanceConsoleWindow-fgw.html): Log in to your gateway local console and change your password if necessary.
- [Configuring an HTTP proxy](https://docs.aws.amazon.com/filegateway/latest/files3/EC2_MaintenanceRoutingProxy-fgw.html): Configure an HTTP proxy for your gateway to route HTTPS traffic through a local HTTP proxy server.
- [Testing your your gateway's network connectivity](https://docs.aws.amazon.com/filegateway/latest/files3/EC2_MaintenanceTestGatewayConnectivity-fgw.html): Test your gateway's network connectivity using your gateway's local console.
- [Viewing your gateway system resource status](https://docs.aws.amazon.com/filegateway/latest/files3/EC2_system-resource-check-fgw.html): Use the gateway local console to view the system resources allocated to your Amazon EC2 gateway.
- [Running Storage Gateway commands on the local console for an Amazon EC2 gateway](https://docs.aws.amazon.com/filegateway/latest/files3/EC2_MaintenanceGatewayConsole-fgw.html): Run commands from the storage gateway console terminal to perform maintenance tasks and collect information about an Amazon EC2 gateway.
- [Configuring your gateway network settings](https://docs.aws.amazon.com/filegateway/latest/files3/EC2-MaintenanceConfiguringStaticIP-fgw.html): Use the local console to change the virtual network adapter type for your Amazon EC2 gateway, or configure it to be accessed by more than one IP address.
- [Shutting down your gateway VM](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceShutDown-common.html): Learn about what to do if you need to shutdown or reboot your gateway virtual machine for maintenance, such as when applying a patch to your hypervisor.
- [Replacing your existing S3 File Gateway with a new instance](https://docs.aws.amazon.com/filegateway/latest/files3/migrate-data.html): Replace your S3 File Gateway with a new instance when you want to improve performance or to respond to a notification to migrate the gateway.
- [Deleting your gateway and removing resources](https://docs.aws.amazon.com/filegateway/latest/files3/deleting-gateway-common.html): Delete your gateway using the AWS Storage Gateway console and clean up associated resources to avoid being charged for their continued use.


## [Performance and optimization](https://docs.aws.amazon.com/filegateway/latest/files3/Performance.html)

- [Maximizing S3 File Gateway throughput](https://docs.aws.amazon.com/filegateway/latest/files3/Performance-Throughput.html): Topics describing guidance and best practices for maximizing throughput of your Amazon S3 File Gateway.
- [Optimizing S3 File Gateway for SQL Server database backups](https://docs.aws.amazon.com/filegateway/latest/files3/SQL-Backup-Best-Practices.html): Learn best practices for maximizing throughput when storing Microsoft SQL Server database backups in Amazon S3 using Amazon S3 File Gateway.


## [Security](https://docs.aws.amazon.com/filegateway/latest/files3/security.html)

### [Data protection](https://docs.aws.amazon.com/filegateway/latest/files3/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Storage Gateway.

- [Data encryption](https://docs.aws.amazon.com/filegateway/latest/files3/encryption.html): Encrypt your data using AWS Key Management Service.

### [Identity and access management](https://docs.aws.amazon.com/filegateway/latest/files3/security-iam.html)

Topics describing how to authenticate requests and manage access your AWS SGW resources with AWS Identity and Access Management.

- [How AWS Storage Gateway works with IAM](https://docs.aws.amazon.com/filegateway/latest/files3/security_iam_service-with-iam.html): Before using IAM to manage access to AWS Storage Gateway, learn which IAM features are supported by the Storage Gateway service.
- [Identity-based policy examples](https://docs.aws.amazon.com/filegateway/latest/files3/security_iam_id-based-policy-examples.html): Topics providing examples and describing best practices for using identity-based IAM policies with Storage Gateway.
- [Troubleshooting](https://docs.aws.amazon.com/filegateway/latest/files3/security_iam_troubleshoot.html): Topics describing how to troubleshoot common issues you might encounter when working with IAM and Storage Gateway.
- [Using tags to control access to resources](https://docs.aws.amazon.com/filegateway/latest/files3/restrict-fgw-access.html): Topics describing how to use IAM policies to control access to Storage Gateway resources based on their tags.
- [Using ACLs for SMB file share access](https://docs.aws.amazon.com/filegateway/latest/files3/smb-acl.html): Topics describing how to control access to Server Message Block (SMB) file shares using Windows Access Control Lists (ACLs).
- [Compliance validation](https://docs.aws.amazon.com/filegateway/latest/files3/storagegateway-compliance.html): Learn which AWS services are in scope for specific compliance programs.
- [Resilience](https://docs.aws.amazon.com/filegateway/latest/files3/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Storage Gateway features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/filegateway/latest/files3/infrastructure-security.html): Learn how AWS Storage Gateway isolates service traffic.
- [AWS Security Best Practices](https://docs.aws.amazon.com/filegateway/latest/files3/security-best-practice.html): Learn where to find more information about security best practices for AWS, including features you might consider as you develop your own security policies.
- [Logging and monitoring](https://docs.aws.amazon.com/filegateway/latest/files3/logging-using-cloudtrail.html): Topics describing how to use AWS CloudTrail with Storage Gateway.


## [Troubleshooting](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-gateway-issues.html)

- [Troubleshooting: gateway offline issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-gateway-offline.html): Learn what to do if the status of your gateway shows offline in the Storage Gateway console.
- [Troubleshooting: Active Directory issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-active-directory.html): Learn what to do if you encounter errors when attempting to join File Gateway to a Microsoft Active Directory domain.
- [Troubleshooting: gateway activation issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-gateway-activation.html): Learn what to do if you receive an internal error message when activating your AWS Storage Gateway.
- [Troubleshooting: on-premises gateway issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-on-premises-gateway-issues.html): Learn how to avoid or remediate issues that can occur with on-premises Storage Gateway appliances.
- [Troubleshooting: Microsoft Hyper-V setup issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-hyperv-setup.html): Learn how to avoid or remediate issues that can occur with Storage Gateway appliances on the Microsoft Hyper-V host platform.
- [Troubleshooting: Amazon EC2 gateway issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-EC2-gateway-issues.html): Topics describing how to avoid or remediate issues that can occur with Storage Gateway appliances on Amazon EC2 instances.
- [Troubleshooting: hardware appliance issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-hardware-appliance-issues.html): Topics describing how to avoid or remediate issues that can occur with Storage Gateway on the AWS Storage Gateway Hardware Appliance.
- [Troubleshooting: File Gateway issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-file-gateway-issues.html): Topics describing how to avoid or remediate errors and notifications that appear in CloudWatch logs for your File Gateway.
- [Troubleshooting: file share issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-file-share-issues.html): Topics describing troubleshooting and best practices information to avoid or resolve file share issues for File Gateway.
- [Troubleshooting: high availability issues](https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-ha-issues.html): Topics describing troubleshooting and best practices information to avoid or resolve high availability issues for File Gateway.


## [Additional resources](https://docs.aws.amazon.com/filegateway/latest/files3/Resources.html)

### [Host setup](https://docs.aws.amazon.com/filegateway/latest/files3/resource-vm-setup.html)

Topics describing how to set up and configure the virtual host platform for your File Gateway.

- [Deploy a default Amazon EC2 host for File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/ec2-quicklaunch-settings.html): Learn how to deploy an Amazon EC2 instance to host your .
- [Deploy a customized Amazon EC2 host for File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/ec2-gateway-file.html): Learn how to deploy an Amazon EC2 instance to host your Amazon S3 File Gateway.
- [Modify Amazon EC2 instance metadata options](https://docs.aws.amazon.com/filegateway/latest/files3/modify-ec2-instance-metadata.html): Learn how to modify an existing Amazon EC2 instance so that it requires Instance Metadata Service Version 2 for all metadata requests.
- [Synchronize VM time with Hyper-V or Linux KVM host time](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceTimeSync-hyperv.html): Learn how to synchronize the time on the virtual machine hosting your File Gateway with the time registered by your hypervisor host to avoid time drift.
- [Synchronize VM time with VMware host time](https://docs.aws.amazon.com/filegateway/latest/files3/GettingStartedSyncVMTime-common.html): Learn how synchronize the time registered on the VMware virtual machine that hosts your gateway with the time on the host system that runs your hypervisor software.
- [Configuring network adapters for your gateway](https://docs.aws.amazon.com/filegateway/latest/files3/configure-multi-nic.html): Topics describing how to configure multiple network adapters for gateways running on various hypervisors.
- [Using Storage Gateway with VMware HA](https://docs.aws.amazon.com/filegateway/latest/files3/vmware-ha.html): Topics describing how to set up Storage Gateway to work with VMware vSphere high availability features.
- [Getting activation key](https://docs.aws.amazon.com/filegateway/latest/files3/get-activation-key.html): Topics describing how to obtain the activation key for your gateway in Storage Gateway.
- [File attribute support](https://docs.aws.amazon.com/filegateway/latest/files3/s3-dos-attribute-support.html): Learn about Amazon S3 File Gateway support for DOS or Windows file attributes.
- [Using Direct Connect](https://docs.aws.amazon.com/filegateway/latest/files3/using-dx.html): Learn how to use Direct Connect with Storage Gateway.
- [Active Directory permissions](https://docs.aws.amazon.com/filegateway/latest/files3/ad-serviceaccount-permissions.html): Learn about the minimum permissions required for the service account that your gateway uses to join your Microsoft Active Directory domain.
- [Getting the gateway IP address](https://docs.aws.amazon.com/filegateway/latest/files3/getting-ip-address.html): Learn how to connect to the local console for your File Gateway and obtain its IP address.
- [IPv6 support](https://docs.aws.amazon.com/filegateway/latest/files3/ipv6-support.html): IPv6 considerations for file gateways
- [Understanding resources and resource IDs](https://docs.aws.amazon.com/filegateway/latest/files3/storage-gateway-resource-id.html): Learn about Storage Gateway resources and resource IDs.
- [Tagging your resources](https://docs.aws.amazon.com/filegateway/latest/files3/tagging-resources-common.html): Learn about resource tags and how to use them to manage your Storage Gateway resources.
- [Open-source components](https://docs.aws.amazon.com/filegateway/latest/files3/AboutAWSStorageGatewaySoftware.html): Topics describing the open-source software components utilized by AWS Storage Gateway.
- [Quotas](https://docs.aws.amazon.com/filegateway/latest/files3/fgw-quotas.html): Learn about limits and quotas for Amazon S3 File Gateway, including the minimum and maximum limitations for file shares and local cache disks.
- [Using storage classes](https://docs.aws.amazon.com/filegateway/latest/files3/storage-classes.html): Topics describing the Amazon S3 storage classes supported by Storage Gateway and how to use them.

### [Using Kubernetes CSI drivers](https://docs.aws.amazon.com/filegateway/latest/files3/using-csi-drivers.html)

Topics describing how to install and configure CSI drivers to allow a Kubernetes cluster to use an existing S3 File Gateway as storage.

- [Working with SMB CSI drivers](https://docs.aws.amazon.com/filegateway/latest/files3/use-smb-csi.html): Learn how to install, configure, or delete the CSI drivers required to use an SMB file share on an S3 File Gateway for storage in your Kubernetes cluster.
- [Working with NFS CSI drivers](https://docs.aws.amazon.com/filegateway/latest/files3/use-nfs-csi.html): Learn how to install, configure, or delete the CSI drivers required to use an NFS file share on an S3 File Gateway for storage in your Kubernetes cluster.
- [Terraform module](https://docs.aws.amazon.com/filegateway/latest/files3/sgw-terraform.html): Learn about HashiCorp Terraform and how you can use it to deploy File Gateway.
