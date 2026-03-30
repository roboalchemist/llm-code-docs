# Source: https://docs.aws.amazon.com/filegateway/latest/filefsxw/llms.txt

# AWS Storage Gateway Amazon FSx File Gateway User Guide

> Storage Gateway is a hybrid storage service that seamlessly connects your on-premises applications to Amazon Web Services cloud storage. You can use the service for backup and archiving, disaster recovery, cloud bursting, storage tiering, and migration. Storage Gateway is a hybrid storage service that seamlessly connects your on-premises applications to Amazon Web Services cloud storage. You can use the service for backup and archiving, disaster recovery, cloud bursting, storage tiering, and migration. This guide explains how to create and manage a Storage Gateway.

- [What is Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html)
- [Configure Microsoft Active Directory domain access settings](https://docs.aws.amazon.com/filegateway/latest/filefsxw/join-domain-fsx.html)
- [Attach an Amazon FSx file system](https://docs.aws.amazon.com/filegateway/latest/filefsxw/attach-fsxw-filesystem.html)
- [Mount and use your Amazon FSx file share](https://docs.aws.amazon.com/filegateway/latest/filefsxw/use-fsxw-gateway.html)
- [Managing your Amazon FSx File Gateway resources](https://docs.aws.amazon.com/filegateway/latest/filefsxw/managing-gateway-file-fsx.html)
- [Best practices](https://docs.aws.amazon.com/filegateway/latest/filefsxw/best-practices.html)
- [API Reference](https://docs.aws.amazon.com/filegateway/latest/filefsxw/AWSStorageGatewayAPI.html)
- [Document history](https://docs.aws.amazon.com/filegateway/latest/filefsxw/DocumentHistory.html)

## [Getting Started with AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/setting-up.html)

- [Sign up for Amazon Web Services](https://docs.aws.amazon.com/filegateway/latest/filefsxw/setting-up-aws-sign-up.html): Learn how to sign up for AWS and create an AWS account.
- [Create an IAM user with administrator privileges](https://docs.aws.amazon.com/filegateway/latest/filefsxw/setting-up-create-iam-user.html): Learn how to create an IAM user with administrative privileges for your AWS account.
- [Accessing AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/WhatIsAPIIntro.html): Learn how to access AWS Storage Gateway through the Storage Gateway console or programmatically using the AWS SDKs.
- [AWS Regions that support Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/available-regions-intro.html): Learn which AWS Regions you can use to store your data when you activate your gateway in Storage Gateway.


## [File Gateway setup requirements](https://docs.aws.amazon.com/filegateway/latest/filefsxw/Requirements.html)

### [Managing local disks](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ManagingLocalStorage-common.html)

Topics describing how to manage local storage for your gateway.

- [Deciding the amount of local disk storage](https://docs.aws.amazon.com/filegateway/latest/filefsxw/decide-local-disks-and-sizes.html): Learn about local disk storage requirements for your File Gateway
- [Add cache storage](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ConfiguringLocalDiskStorage.html): Configure additional cache storage space to accommodate increased File Gateway workloads.
- [Using ephemeral storage with EC2 gateways](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ephemeral-disk-cache.html): Learn how to prevent data loss when using ephemeral disk storage with File Gateway.


## [Using the hardware appliance](https://docs.aws.amazon.com/filegateway/latest/filefsxw/hardware-appliance.html)

- [Setting up your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/filefsxw/appliance-quick-start.html): Set up and configure your Storage Gateway Hardware Appliance.
- [Physically installing your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/filefsxw/appliance-rack-mount.html): Learn how to physically mount and connect your hardware appliance
- [Accessing the hardware appliance console](https://docs.aws.amazon.com/filegateway/latest/filefsxw/access-hardware-appliance-console.html): Learn how to access the hardware appliance console.
- [Configuring hardware appliance network parameters](https://docs.aws.amazon.com/filegateway/latest/filefsxw/appliance-configure-network.html): Configure network parameters for your Storage Gateway Hardware Appliance.
- [Activating your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/filefsxw/appliance-activation.html): Activate your hardware appliance as a Storage Gateway.
- [Creating a gateway on your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/filefsxw/appliance-launch-gateway.html): Create a Storage Gateway on the AWS Storage Gateway Hardware Appliance.
- [Configuring a gateway IP address on the hardware appliance](https://docs.aws.amazon.com/filegateway/latest/filefsxw/appliance-configure-ip.html): Configure the gateway IP address on the hardware appliance to work with applications.
- [Removing gateway software from your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/filefsxw/appliance-remove-gateway.html): Remove gateway software from your Storage Gateway Hardware Appliance.
- [Deleting your hardware appliance](https://docs.aws.amazon.com/filegateway/latest/filefsxw/delete-appliance.html): Delete your Storage Gateway Hardware Appliance from your AWS account.


## [Creating your gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/create-file-gateway.html)

- [Create an Amazon FSx for Windows File Server file system](https://docs.aws.amazon.com/filegateway/latest/filefsxw/create-file-system.html): Create a file system for an Amazon FSx File Gateway in AWS Storage Gateway.
- [Create and activate an Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/create-gateway-file.html): Create, deploy, and activate a File Gateway in AWS Storage Gateway.

### [Activating a gateway in a VPC](https://docs.aws.amazon.com/filegateway/latest/filefsxw/gateway-private-link.html)

Learn how to activate your AWS Storage Gateway in a VPC, including how to create a VPC endpoint and configure your gateway to send data through the VPC.

- [Create a VPC endpoint for Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/create-vpc-endpoint.html): Create a VPC endpoint.


## [Monitoring Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/Main_monitoring-gateways-common.html)

- [Understanding CloudWatch alarms](https://docs.aws.amazon.com/filegateway/latest/filefsxw/cloudwatch-alarms.html): Learn about CloudWatch alarms and how to use them to monitor your File Gateway.
- [Create recommended CloudWatch alarms](https://docs.aws.amazon.com/filegateway/latest/filefsxw/cloudwatch-alarms-create-recommended.html): Create the recommended CloudWatch alarms to monitor your File Gateway resources.
- [Create a custom CloudWatch alarm](https://docs.aws.amazon.com/filegateway/latest/filefsxw/cloudwatch-alarms-create-alarm.html): Create custom gateway alarms to be notified of specific gateway issues or behavior.
- [Monitoring your FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/monitoring-file-gateway.html): Topics describing how to measure metrics and audit logs for FSx File Gateway.


## [Maintaining your gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/maintaining-gateway.html)

### [Managing gateway updates](https://docs.aws.amazon.com/filegateway/latest/filefsxw/MaintenanceManagingUpdate-common.html)

Use the Storage Gateway console to turn gateway maintenance updates updates on or off, or configure an update schedule.

- [Turn maintenance updates on or off](https://docs.aws.amazon.com/filegateway/latest/filefsxw/maintenance-updates-on-off.html): Use the Storage Gateway console to turn maintenance updates on or off for a specific gateway.
- [Modify the gateway maintenance window schedule](https://docs.aws.amazon.com/filegateway/latest/filefsxw/configure-maintenance-window-schedule.html): Use the Storage Gateway console to configure the maintenance window schedule for a specific gateway.
- [Apply an update manually](https://docs.aws.amazon.com/filegateway/latest/filefsxw/apply-update-manually.html): Learn how to manually apply a gateway appliance software update using the Storage Gateway console.

### [Performing maintenance tasks using the local console](https://docs.aws.amazon.com/filegateway/latest/filefsxw/manage-on-premises.html)

Topics describing how to perform maintenance tasks using the gateway local console.

- [Accessing the gateway local console](https://docs.aws.amazon.com/filegateway/latest/filefsxw/accessing-local-console.html): Topics describing how to access the gateway local console, where you can perform various maintenance tasks for your gateway.

### [Performing tasks on the virtual machine local console](https://docs.aws.amazon.com/filegateway/latest/filefsxw/manage-on-premises-fgw.html)

Topics describing how to perform maintenance tasks on the VM local console for your File Gateway.

- [Logging in to the File Gateway local console](https://docs.aws.amazon.com/filegateway/latest/filefsxw/LocalConsole-login-fgw.html): How to log in to the File Gateway local console or Storage Gateway console and change your local console password.
- [Configuring an HTTP proxy](https://docs.aws.amazon.com/filegateway/latest/filefsxw/MaintenanceRoutingProxy-fgw.html): Use the gateway local console to configure an HTTP proxy server if necessary for your gateway to communicate over the internet.
- [Configuring your gateway network settings](https://docs.aws.amazon.com/filegateway/latest/filefsxw/MaintenanceConfiguringStaticIP-fgw.html): Use the gateway local console to configure network settings, including setting a static IP address for your gateway.
- [Testing your gateway's network connectivity](https://docs.aws.amazon.com/filegateway/latest/filefsxw/MaintenanceTestGatewayConnectivity-fgw.html): Use the gateway local console to test your gateway's network connectivity.
- [Viewing your gateway system resource status](https://docs.aws.amazon.com/filegateway/latest/filefsxw/system-resource-check-fgw.html): Use the gateway local console to view the virtual machine system resources allocated to your gateway.
- [Configuring your NTP server](https://docs.aws.amazon.com/filegateway/latest/filefsxw/MaintenanceTimeSync-fgw.html): Manage your system time configuration, including NTP, and synchronize the VM time on your gateway with your hypervisor host to avoid time drift.
- [Running Storage Gateway commands on the local console](https://docs.aws.amazon.com/filegateway/latest/filefsxw/MaintenanceGatewayConsole-fgw.html): Run commands from the storage gateway console terminal to perform maintenance tasks and collect gateway information.

### [Performing tasks on the EC2 local console](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ec2-local-console-fgw.html)

Topics describing how to perform maintenance tasks for a File Gateway deployed on an Amazon EC2 instance using the local console.

- [Logging in to your EC2 gateway local console](https://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2_MaintenanceConsoleWindow-fgw.html): Log in to your gateway local console and change your password if necessary.
- [Configuring an HTTP proxy](https://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2_MaintenanceRoutingProxy-fgw.html): Configure an HTTP proxy for your gateway to route HTTPS traffic through a local HTTP proxy server.
- [Testing your your gateway's network connectivity](https://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2_MaintenanceTestGatewayConnectivity-fgw.html): Test your gateway's network connectivity using your gateway's local console.
- [Viewing your gateway system resource status](https://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2_system-resource-check-fgw.html): Use the gateway local console to view the system resources allocated to your Amazon EC2 gateway.
- [Running Storage Gateway commands on the local console for an Amazon EC2 gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2_MaintenanceGatewayConsole-fgw.html): Run commands from the storage gateway console terminal to perform maintenance tasks and collect information about an Amazon EC2 gateway.
- [Configuring your gateway network settings](https://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2-MaintenanceConfiguringStaticIP-fgw.html): Use the local console to change the virtual network adapter type for your Amazon EC2 gateway, or configure it to be accessed by more than one IP address.
- [Shutting down your gateway VM](https://docs.aws.amazon.com/filegateway/latest/filefsxw/MaintenanceShutDown-common.html): Learn about what to do if you need to shutdown or reboot your gateway virtual machine for maintenance, such as when applying a patch to your hypervisor.
- [Replacing your existing FSx File Gateway with a new instance](https://docs.aws.amazon.com/filegateway/latest/filefsxw/migrate-data.html): Replace your FSx File Gateway with a new instance when you want to improve performance or to respond to a notification to migrate the gateway.
- [Deleting your gateway and removing resources](https://docs.aws.amazon.com/filegateway/latest/filefsxw/deleting-gateway-common.html): Delete your gateway using the AWS Storage Gateway console and clean up associated resources to avoid being charged for their continued use.


## [Performance and optimization](https://docs.aws.amazon.com/filegateway/latest/filefsxw/Performance.html)

- [Maximizing S3 File Gateway throughput](https://docs.aws.amazon.com/filegateway/latest/filefsxw/Performance-Throughput.html): Topics describing guidance and best practices for maximizing throughput of your Amazon S3 File Gateway.
- [Optimizing S3 File Gateway for SQL Server database backups](https://docs.aws.amazon.com/filegateway/latest/filefsxw/SQL-Backup-Best-Practices.html): Learn best practices for maximizing throughput when storing Microsoft SQL Server database backups in Amazon S3 using Amazon S3 File Gateway.


## [Security](https://docs.aws.amazon.com/filegateway/latest/filefsxw/security.html)

### [Data protection](https://docs.aws.amazon.com/filegateway/latest/filefsxw/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Storage Gateway.

- [Data encryption](https://docs.aws.amazon.com/filegateway/latest/filefsxw/encryption.html): Encrypt your data using AWS Key Management Service.

### [Identity and access management](https://docs.aws.amazon.com/filegateway/latest/filefsxw/security-iam.html)

Topics describing how to authenticate requests and manage access your AWS SGW resources with AWS Identity and Access Management.

- [How AWS Storage Gateway works with IAM](https://docs.aws.amazon.com/filegateway/latest/filefsxw/security_iam_service-with-iam.html): Before using IAM to manage access to AWS Storage Gateway, learn which IAM features are supported by the Storage Gateway service.
- [Identity-based policy examples](https://docs.aws.amazon.com/filegateway/latest/filefsxw/security_iam_id-based-policy-examples.html): Topics providing examples and describing best practices for using identity-based IAM policies with Storage Gateway.
- [Troubleshooting](https://docs.aws.amazon.com/filegateway/latest/filefsxw/security_iam_troubleshoot.html): Topics describing how to troubleshoot common issues you might encounter when working with IAM and Storage Gateway.
- [Using tags to control access to resources](https://docs.aws.amazon.com/filegateway/latest/filefsxw/restrict-fgw-access.html): Topics describing how to use IAM policies to control access to Storage Gateway resources based on their tags.
- [Compliance validation](https://docs.aws.amazon.com/filegateway/latest/filefsxw/storagegateway-compliance.html): Learn which AWS services are in scope for specific compliance programs.
- [Resilience](https://docs.aws.amazon.com/filegateway/latest/filefsxw/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Storage Gateway features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/filegateway/latest/filefsxw/infrastructure-security.html): Learn how AWS Storage Gateway isolates service traffic.
- [AWS Security Best Practices](https://docs.aws.amazon.com/filegateway/latest/filefsxw/security-best-practice.html): Learn where to find more information about security best practices for AWS, including features you might consider as you develop your own security policies.
- [Logging and monitoring](https://docs.aws.amazon.com/filegateway/latest/filefsxw/logging-using-cloudtrail.html): Topics describing how to use AWS CloudTrail with Storage Gateway.


## [Troubleshooting](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-gateway-issues.html)

- [Troubleshooting: gateway offline issues](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-gateway-offline.html): Learn what to do if the status of your gateway shows offline in the Storage Gateway console.
- [Troubleshooting: Active Directory issues](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-active-directory.html): Learn what to do if you encounter errors when attempting to join File Gateway to a Microsoft Active Directory domain.
- [Troubleshooting: gateway activation issues](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-gateway-activation.html): Learn what to do if you receive an internal error message when activating your AWS Storage Gateway.
- [Troubleshooting: on-premises gateway issues](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-on-premises-gateway-issues.html): Learn how to avoid or remediate issues that can occur with on-premises Storage Gateway appliances.
- [Troubleshooting: Microsoft Hyper-V setup issues](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-hyperv-setup.html): Learn how to avoid or remediate issues that can occur with Storage Gateway appliances on the Microsoft Hyper-V host platform.
- [Troubleshooting: Amazon EC2 gateway issues](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-EC2-gateway-issues.html): Topics describing how to avoid or remediate issues that can occur with Storage Gateway appliances on Amazon EC2 instances.
- [Troubleshooting: hardware appliance issues](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-hardware-appliance-issues.html): Topics describing how to avoid or remediate issues that can occur with Storage Gateway on the AWS Storage Gateway Hardware Appliance.
- [Troubleshooting: File Gateway issues](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-file-gateway-issues.html): Topics describing how to avoid or remediate errors and notifications that appear in CloudWatch logs for your File Gateway.
- [Troubleshooting: high availability issues](https://docs.aws.amazon.com/filegateway/latest/filefsxw/troubleshooting-ha-issues.html): Topics describing troubleshooting and best practices information to avoid or resolve high availability issues for File Gateway.


## [Additional resources](https://docs.aws.amazon.com/filegateway/latest/filefsxw/Resources.html)

### [Host setup](https://docs.aws.amazon.com/filegateway/latest/filefsxw/resource-vm-setup.html)

Topics describing how to set up and configure the virtual host platform for your File Gateway.

- [Deploy a default Amazon EC2 host for File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ec2-quicklaunch-settings.html): Learn how to deploy an Amazon EC2 instance to host your Amazon S3 File GatewayAmazon FSx File Gateway using Use default settings specifications.
- [Deploy a customized Amazon EC2 host for File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ec2-gateway-file.html): Learn how to deploy an Amazon EC2 instance to host your .
- [Modify Amazon EC2 instance metadata options](https://docs.aws.amazon.com/filegateway/latest/filefsxw/modify-ec2-instance-metadata.html): Learn how to modify an existing Amazon EC2 instance so that it requires Instance Metadata Service Version 2 for all metadata requests.
- [Synchronize VM time with Hyper-V or Linux KVM host time](https://docs.aws.amazon.com/filegateway/latest/filefsxw/MaintenanceTimeSync-hyperv.html): Learn how to synchronize the time on the virtual machine hosting your File Gateway with the time registered by your hypervisor host to avoid time drift.
- [Synchronize VM time with VMware host time](https://docs.aws.amazon.com/filegateway/latest/filefsxw/GettingStartedSyncVMTime-common.html): Learn how synchronize the time registered on the VMware virtual machine that hosts your gateway with the time on the host system that runs your hypervisor software.
- [Configuring network adapters for your gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/configure-multi-nic.html): Topics describing how to configure multiple network adapters for gateways running on various hypervisors.
- [Using Storage Gateway with VMware HA](https://docs.aws.amazon.com/filegateway/latest/filefsxw/vmware-ha.html): Topics describing how to set up Storage Gateway to work with VMware vSphere high availability features.
- [Getting activation key](https://docs.aws.amazon.com/filegateway/latest/filefsxw/get-activation-key.html): Topics describing how to obtain the activation key for your gateway in Storage Gateway.
- [Using Direct Connect](https://docs.aws.amazon.com/filegateway/latest/filefsxw/using-dx.html): Learn how to use Direct Connect with Storage Gateway.
- [Active Directory permissions](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ad-serviceaccount-permissions.html): Learn about the minimum permissions required for the service account that your gateway uses to join your Microsoft Active Directory domain.
- [Getting the gateway IP address](https://docs.aws.amazon.com/filegateway/latest/filefsxw/getting-ip-address.html): Learn how to connect to the local console for your File Gateway and obtain its IP address.
- [Understanding resources and resource IDs](https://docs.aws.amazon.com/filegateway/latest/filefsxw/storage-gateway-resource-id.html): Learn about Storage Gateway resources and resource IDs.
- [Tagging your resources](https://docs.aws.amazon.com/filegateway/latest/filefsxw/tagging-resources-common.html): Learn about resource tags and how to use them to manage your Storage Gateway resources.
- [Open-source components](https://docs.aws.amazon.com/filegateway/latest/filefsxw/AboutAWSStorageGatewaySoftware.html): Topics describing the open-source software components utilized by AWS Storage Gateway.
- [Quotas](https://docs.aws.amazon.com/filegateway/latest/filefsxw/fgw-quotas.html): Learn about limits and quotas for Amazon FSx File Gateway, including the minimum and maximum limitations for file systems and local cache disks.
