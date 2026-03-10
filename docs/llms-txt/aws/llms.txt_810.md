# Source: https://docs.aws.amazon.com/storagegateway/latest/tgw/llms.txt

# AWS Storage Gateway Tape Gateway User Guide

> Storage Gateway is a hybrid storage service that allows your on-premises applications to seamlessly use Amazon Web Services cloud storage. You can use the service for backup and archiving, disaster recovery, cloud bursting, storage tiering, and migration. Storage Gateway is a hybrid storage service that allows your on-premises applications to seamlessly use Amazon Web Services cloud storage. You can use the service for backup and archiving, disaster recovery, cloud bursting, storage tiering, and migration. This guide explains how to create and manage a Storage Gateway.

- [Tape Gateway setup requirements](https://docs.aws.amazon.com/storagegateway/latest/tgw/Requirements.html)
- [Performance and optimization for Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/Performance.html)
- [Best practices](https://docs.aws.amazon.com/storagegateway/latest/tgw/best-practices.html)
- [API Reference](https://docs.aws.amazon.com/storagegateway/latest/tgw/AWSStorageGatewayAPI.html)
- [Document history](https://docs.aws.amazon.com/storagegateway/latest/tgw/DocumentHistory.html)
- [AL2 to AL2023 Migration](https://docs.aws.amazon.com/storagegateway/latest/tgw/al2-to-al2023-migration.html)
- [Release notes](https://docs.aws.amazon.com/storagegateway/latest/tgw/release-notes.html)

## [What is Tape Gateway?](https://docs.aws.amazon.com/storagegateway/latest/tgw/WhatIsStorageGateway.html)

- [How Tape Gateway works](https://docs.aws.amazon.com/storagegateway/latest/tgw/StorageGatewayConcepts.html): Find an architectural overview of the Tape Gateway solution.


## [Getting started with AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStarted.html)

- [Sign Up for AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStartedSignUpStep1-common.html): Sign up for an Amazon Web Services account to get access to all AWS resources, forums, support, and usage reports to use with Storage Gateway.
- [Create an IAM user with administrator privileges](https://docs.aws.amazon.com/storagegateway/latest/tgw/setting-up-create-iam-user.html): Learn how to create an IAM user with administrative privileges for your AWS account.
- [Accessing AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/WhatIsAPIIntro.html): Access Storage Gateway through the console or programmatically using the AWS SDKs.
- [AWS Regions that support Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/available-regions-intro.html): Find the AWS Regions that you can select for storing your data when you activate your gateway.


## [Using the hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/tgw/hardware-appliance.html)

- [Setting up your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/tgw/appliance-quick-start.html): Set up and configure your Storage Gateway Hardware Appliance.
- [Physically installing your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/tgw/appliance-rack-mount.html): Learn how to physically mount and connect your hardware appliance
- [Accessing the hardware appliance console](https://docs.aws.amazon.com/storagegateway/latest/tgw/access-hardware-appliance-console.html): Learn how to access the hardware appliance console.
- [Configuring hardware appliance network parameters](https://docs.aws.amazon.com/storagegateway/latest/tgw/appliance-configure-network.html): Configure network parameters for your Storage Gateway Hardware Appliance.
- [Activating your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/tgw/appliance-activation.html): Activate your hardware appliance as a Storage Gateway.
- [Creating a gateway on your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/tgw/appliance-launch-gateway.html): Create a Storage Gateway on the Storage Gateway Hardware Appliance.
- [Configuring a gateway IP address on the hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/tgw/appliance-configure-ip.html): Configure the gateway IP address on the hardware appliance to work with applications.
- [Removing gateway software from your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/tgw/appliance-remove-gateway.html): Remove gateway software from your Storage Gateway Hardware Appliance.
- [Deleting your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/tgw/delete-appliance.html): Delete your Storage Gateway Hardware Appliance from your AWS account.


## [Creating your gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/creating-your-gateway.html)

- [Create and activate a Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/create-gateway-vtl.html): Learn how to set up and use a fully functioning Tape Gateway.

### [Creating Tapes](https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStartedCreateTapes.html)

Create virtual tapes using the AWS Storage Gateway console.

- [Creating Tapes Manually](https://docs.aws.amazon.com/storagegateway/latest/tgw/CreateTapesManually.html): Create virtual tapes manually using the AWS Storage Gateway console or the Storage Gateway API.
- [Allowing Automatic Tape Creation](https://docs.aws.amazon.com/storagegateway/latest/tgw/CreateTapesAutomatically.html): Allow automatic tape creation using the AWS Storage Gateway console.
- [Creating Custom Tape Pools](https://docs.aws.amazon.com/storagegateway/latest/tgw/CreatingCustomTapePool.html): Create a custom tape pool using the AWS Storage Gateway console.
- [Connecting Your VTL Devices](https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStartedAccessTapesVTL.html): Learn how to connect your gateway VTL devices to your client.

### [Testing Your Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStartedTestGatewayVTL.html)

Back up your data to virtual tape with Storage Gateway.

- [Arcserve Backup](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-arcserve.html): Learn how to test your Storage Gateway setup using Arcserve Backup.
- [Bacula Enterprise](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-bacula.html): Learn how to test your Storage Gateway setup using Bacula Enterprise.
- [Commvault](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-commvault.html): Learn how to test your Storage Gateway setup using Commvault.
- [Dell EMC NetWorker](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-emc.html): Learn how to test your Storage Gateway setup using Dell EMC NetWorker.
- [IBM Data Protect](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-tsm.html): Learn how to use IBM Data Protect with AWS Storage Gateway.
- [OpenText Data Protector](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-hpdataprotector.html): Use OpenText Data Protector with Storage Gateway.
- [Microsoft System Center DPM](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-DPM.html): Use Microsoft System Center Data Protection Manager with Storage Gateway.
- [NovaStor DataCenter/Network](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-novastor.html): Use NovaStor DataCenter/Network with AWS Storage Gateway.
- [Quest NetVault Backup](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-netvault.html): Learn how to test your Storage Gateway setup using Quest NetVault Backup.
- [Veeam Backup & Replication](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-Veeam.html): Learn how to test your Storage Gateway using Veeam Backup and Replication.
- [Veritas Backup Exec](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup-BackupExec.html): Learn how to test your Storage Gateway setup using Veritas Backup Exec.
- [Veritas NetBackup](https://docs.aws.amazon.com/storagegateway/latest/tgw/backup_netbackup-vtl.html): Storage Gateway supports backing up data to virtual tapes and archiving the tapes by using Veritas NetBackup.
- [Where do I go from here?](https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStartedWhatsNextStep3-vtl.html): Find more information about setting up, managing, and troubleshooting your Tape Gateway.
- [Activating your gateway in a virtual private cloud](https://docs.aws.amazon.com/storagegateway/latest/tgw/gateway-private-link.html): Additional information on activating a gateway in a VPC.


## [Managing your Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/managing-gateway-common.html)

- [Editing Gateway Information](https://docs.aws.amazon.com/storagegateway/latest/tgw/edit-gateway-information.html): Edit basic information for an existing Storage Gateway
- [Managing Automatic Tape Creation](https://docs.aws.amazon.com/storagegateway/latest/tgw/managing-automatic-tape-creation.html): Learn how to manage, change, or delete an automatic tape creation configuration.
- [Archiving Tapes](https://docs.aws.amazon.com/storagegateway/latest/tgw/archiving-tapes-vtl.html): Archive tapes to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive.
- [Moving tapes to S3 Glacier Deep Archive](https://docs.aws.amazon.com/storagegateway/latest/tgw/moving-tapes-vtl.html): Move virtual tapes from S3 Glacier Flexible Retrieval to S3 Glacier Deep Archive.
- [Retrieving Archived Tapes](https://docs.aws.amazon.com/storagegateway/latest/tgw/retrieving-archived-tapes-vtl.html): To access tape data, retrieve tapes from your virtual tape shelf to your Tape Gateway.
- [Viewing tape usage statistics](https://docs.aws.amazon.com/storagegateway/latest/tgw/tape-usage.html): Learn how to view usage statistics for the tapes in your tape library.
- [Deleting Tapes](https://docs.aws.amazon.com/storagegateway/latest/tgw/deleting-tapes-vtl.html): Delete virtual tapes from your Tape Gateway when you no longer need them.
- [Deleting Custom Tape Pools](https://docs.aws.amazon.com/storagegateway/latest/tgw/deleting-tape-pools-vtl.html): Delete custom tape pools in Storage Gateway when you no longer need them.
- [Deactivating Your Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/disabling-gateway-vtl.html): Deactivate your Tape Gateway to lock down virtual tapes.
- [Understanding Tape Status](https://docs.aws.amazon.com/storagegateway/latest/tgw/understand-tapes-status.html): Use virtual tape status in Storage Gateway to assess tape health, ranging from normal functioning to problems where action is needed.
- [Moving your data to a new gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/migrate-data.html): Move data between gateways in Storage Gateway when you want to improve performance or to respond to a notification to migrate the gateway.


## [Monitoring Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/Main_monitoring-gateways-common.html)

- [Understanding gateway metrics](https://docs.aws.amazon.com/storagegateway/latest/tgw/MonitoringGateways-common.html): Learn about the metrics that help you monitor your Storage Gateway appliance.
- [Monitoring the upload buffer](https://docs.aws.amazon.com/storagegateway/latest/tgw/PerfUploadBuffer-common.html): Learn how to monitor the gateway upload buffer and create an alarm for when the buffer exceeds a specified threshold.
- [Monitoring cache storage](https://docs.aws.amazon.com/storagegateway/latest/tgw/PerfCache-common.html): Learn how to monitor the cache storage of a gateway in a cached volumes setup.
- [Understanding CloudWatch alarms](https://docs.aws.amazon.com/storagegateway/latest/tgw/cloudwatch-alarms.html): Learn about CloudWatch alarms, which monitor information about your gateway based on metrics and expressions.
- [Creating recommended CloudWatch alarms](https://docs.aws.amazon.com/storagegateway/latest/tgw/cloudwatch-alarms-create-recommended.html): Create recommended CloudWatch alarms for your gateway.
- [Creating a custom CloudWatch alarm](https://docs.aws.amazon.com/storagegateway/latest/tgw/cloudwatch-alarms-create-alarm.html): Learn how to create CloudWatch alarms that send you notifications when a metric changes state.

### [Monitoring Your Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/GatewayMetrics-vtl-common.html)

Monitor your Tape Gateway in Storage Gateway, including its virtual tapes, cache storage, and upload buffer.

- [Getting Tape Gateway Health Logs](https://docs.aws.amazon.com/storagegateway/latest/tgw/cw-log-groups-tape.html): Learn how to use Amazon CloudWatch Logs to get information about the health of your Tape Gateway and related resources.
- [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/storagegateway/latest/tgw/UsingCloudWatchConsole-vtl-common.html): Get monitoring data for your Tape Gateway using either the AWS Management Console or the CloudWatch API.
- [Understanding virtual tape metrics](https://docs.aws.amazon.com/storagegateway/latest/tgw/monitoring-tape.html): Learn about the Storage Gateway metrics that cover the virtual associated with your gateways.
- [Measuring Performance Between Your Tape Gateway and AWS](https://docs.aws.amazon.com/storagegateway/latest/tgw/PerfGatewayAWS-vtl-common.html): Measure performance of data throughput, data latency, and operations per second between your Tape Gateway and AWS.


## [Maintaining Your Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/maintaining-gateway.html)

### [Managing local disks](https://docs.aws.amazon.com/storagegateway/latest/tgw/ManagingLocalStorage-common.html)

Learn how to manage and allocate the local disks that your gateway virtual machine uses for buffering and storage.

- [Deciding the amount of local disk storage](https://docs.aws.amazon.com/storagegateway/latest/tgw/decide-local-disks-and-sizes.html): Learn how to properly size the local disks that your gateway uses for cache and upload buffer.
- [Add upload buffer or cache storage](https://docs.aws.amazon.com/storagegateway/latest/tgw/ConfiguringLocalDiskStorage.html): Configure additional upload buffer and cache storage space for your Tape Gateway.
- [Managing Bandwidth](https://docs.aws.amazon.com/storagegateway/latest/tgw/MaintenanceUpdateBandwidth-common.html): Update the bandwidth-rate limits for your gateway.

### [Managing gateway updates](https://docs.aws.amazon.com/storagegateway/latest/tgw/MaintenanceManagingUpdate-common.html)

Use the Storage Gateway console to turn gateway maintenance updates updates on or off, or configure an update schedule.

- [Turn maintenance updates on or off](https://docs.aws.amazon.com/storagegateway/latest/tgw/maintenance-updates-on-off.html): Use the Storage Gateway console to turn maintenance updates on or off for a specific gateway.
- [Modify the gateway maintenance window schedule](https://docs.aws.amazon.com/storagegateway/latest/tgw/configure-maintenance-window-schedule.html): Use the Storage Gateway console to configure the maintenance window schedule for a specific gateway.
- [Apply an update manually](https://docs.aws.amazon.com/storagegateway/latest/tgw/apply-update-manually.html): Learn how to manually apply a gateway appliance software update using the Storage Gateway console.
- [Shutting Down Your Gateway VM](https://docs.aws.amazon.com/storagegateway/latest/tgw/MaintenanceShutDown-common.html): Learn how to shutdown or reboot your gateway virtual machine for maintenance, such as when applying a patch to your hypervisor.
- [Deleting your gateway and removing resources](https://docs.aws.amazon.com/storagegateway/latest/tgw/deleting-gateway-common.html): Delete your gateway using the AWS Storage Gateway console and clean up associated resources.


## [Performing maintenance tasks using the local console](https://docs.aws.amazon.com/storagegateway/latest/tgw/manage-on-premises.html)

- [Accessing the Gateway Local Console](https://docs.aws.amazon.com/storagegateway/latest/tgw/accessing-local-console.html): Learn how to access the local console on your gateway virtual machine host.

### [Performing Tasks on the VM Local Console](https://docs.aws.amazon.com/storagegateway/latest/tgw/manage-on-premises-common.html)

Learn how to perform maintenance tasks using the gateway local console.

- [Logging in to the Tape Gateway local console](https://docs.aws.amazon.com/storagegateway/latest/tgw/LocalConsole-login-common.html): Learn how to log into the gateway local console and change the default password.
- [Configuring a SOCKS5 proxy for your on-premises gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/MaintenanceRoutingProxy-common.html): Learn how to route your gateway through a SOCKS proxy server.
- [Configuring Your Gateway Network](https://docs.aws.amazon.com/storagegateway/latest/tgw/MaintenanceConfiguringStaticIP-common.html): Configure your gateway to use a static IP address.
- [Testing your gateway connectivity to the internet](https://docs.aws.amazon.com/storagegateway/latest/tgw/MaintenanceTestGatewayConnectivity-common.html): Test the connection from your gateway to the internet using the gateway local console.
- [Running storage gateway commands in the local console for an on-premises gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/MaintenanceGatewayConsole-common.html): Learn how to run commands in the local console for an on-premises gateway to perform maintenance tasks such as saving routing tables or connecting to Support.
- [Viewing your gateway system resource status](https://docs.aws.amazon.com/storagegateway/latest/tgw/system-resource-check-common.html): Learn how to check the virtual CPU cores, root volume size, and RAM available to your gateway.

### [Performing Tasks on the EC2 Local Console](https://docs.aws.amazon.com/storagegateway/latest/tgw/ec2-local-console-common.html)

Perform maintenance tasks for a gateway deployed on an Amazon EC2 instance by using the local EC2 console.

- [Logging In to Your EC2 Gateway Local Console](https://docs.aws.amazon.com/storagegateway/latest/tgw/EC2_MaintenanceConsoleWindow-common.html): Log in to your gateway local console so that you can perform maintenance tasks on your Amazon EC2 gateway.
- [Configuring an HTTP proxy](https://docs.aws.amazon.com/storagegateway/latest/tgw/EC2_MaintenanceRoutingProxy-common.html): Configure an HTTP proxy for your gateway to route HTTPS traffic through a local HTTP proxy server.
- [Testing gateway network connectivity](https://docs.aws.amazon.com/storagegateway/latest/tgw/EC2_MaintenanceTestGatewayConnectivity-common.html): Learn how to test gateway network connectivity using the gateway local console.
- [Viewing your gateway system resource status](https://docs.aws.amazon.com/storagegateway/latest/tgw/EC2_system-resource-check-common.html): Learn how to check the virtual CPU cores, root volume size, and RAM for a gateway.
- [Running Storage Gateway commands on the local console](https://docs.aws.amazon.com/storagegateway/latest/tgw/EC2_MaintenanceGatewayConsole-common.html): Learn how to run commands in the gateway local console to perform maintenance tasks such as saving routing tables or connecting to Support.


## [Security](https://docs.aws.amazon.com/storagegateway/latest/tgw/security.html)

### [Data protection](https://docs.aws.amazon.com/storagegateway/latest/tgw/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Storage Gateway.

- [Data encryption](https://docs.aws.amazon.com/storagegateway/latest/tgw/encryption.html): Encrypt your data using AWS Key Management Service.

### [Identity and Access Management](https://docs.aws.amazon.com/storagegateway/latest/tgw/security-iam.html)

How to authenticate requests and manage access to your AWS SGW resources.

- [How AWS Storage Gateway works with IAM](https://docs.aws.amazon.com/storagegateway/latest/tgw/security_iam_service-with-iam.html): Learn about how AWS Storage Gateway works with IAM to secure access to your resources and data.
- [Identity-based policy examples](https://docs.aws.amazon.com/storagegateway/latest/tgw/security_iam_id-based-policy-examples.html): Learn how to grant users permission to perform actions on the resources that they need by creating IAM policies.
- [Troubleshooting](https://docs.aws.amazon.com/storagegateway/latest/tgw/security_iam_troubleshoot.html): Learn how to diagnose and fix common issues that you might encounter when working with AWS Storage Gateway and IAM.
- [Compliance validation](https://docs.aws.amazon.com/storagegateway/latest/tgw/storagegateway-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/storagegateway/latest/tgw/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Storage Gateway features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/storagegateway/latest/tgw/infrastructure-security.html): Learn how AWS Storage Gateway isolates service traffic.
- [AWS Security Best Practices](https://docs.aws.amazon.com/storagegateway/latest/tgw/security-best-practice.html): Learn about security features to consider as you develop and implement your own Storage Gateway security policies.
- [Logging and Monitoring](https://docs.aws.amazon.com/storagegateway/latest/tgw/logging-using-cloudtrail.html): Learn about logging Storage Gateway with AWS CloudTrail.


## [Troubleshooting gateway issues](https://docs.aws.amazon.com/storagegateway/latest/tgw/troubleshooting-gateway-issues.html)

- [Troubleshooting: gateway offline issues](https://docs.aws.amazon.com/storagegateway/latest/tgw/troubleshooting-gateway-offline.html): Learn what to do if the status of your gateway shows offline in the Storage Gateway console.
- [Troubleshooting: gateway activation issues](https://docs.aws.amazon.com/storagegateway/latest/tgw/troubleshooting-gateway-activation.html): Learn what to do if you receive an internal error message when activating your AWS Storage Gateway.
- [Troubleshooting on-premises gateway issues](https://docs.aws.amazon.com/storagegateway/latest/tgw/troubleshooting-on-premises-gateway-issues.html): Learn how to diagnose and fix common problems you might encounter with gateways deployed on-premises.
- [Troubleshooting Microsoft Hyper-V setup issues](https://docs.aws.amazon.com/storagegateway/latest/tgw/troubleshooting-hyperv-setup.html): The following table lists typical issues that you might encounter when deploying Storage Gateway on the Microsoft Hyper-V platform.
- [Troubleshooting Amazon EC2 gateway issues](https://docs.aws.amazon.com/storagegateway/latest/tgw/troubleshooting-EC2-gateway-issues.html): Learn how to diagnose and fix common problems you might encounter with gateways deployed on Amazon EC2 instances.
- [Troubleshooting hardware appliance issues](https://docs.aws.amazon.com/storagegateway/latest/tgw/troubleshooting-hardware-appliance-issues.html): Learn now to diagnose and fix common problems that you might encounter with the Storage Gateway Hardware Appliance.
- [Troubleshooting virtual tape issues](https://docs.aws.amazon.com/storagegateway/latest/tgw/Main_TapesIssues-vtl.html): Learn how to diagnose and resolve issues with virtual tapes.
- [Troubleshooting high availability issues](https://docs.aws.amazon.com/storagegateway/latest/tgw/troubleshooting-ha-issues.html): Troubleshoot Storage Gateway high availability issues using Amazon CloudWatch health notifications and metrics.


## [Additional Resources](https://docs.aws.amazon.com/storagegateway/latest/tgw/Resources.html)

### [Host setup](https://docs.aws.amazon.com/storagegateway/latest/tgw/resource-vm-setup.html)

Learn about how to set up and configure virtual host platforms for Storage Gateway.

- [Deploy a default Amazon EC2 host for Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/ec2-quicklaunch-settings.html): Deploy an Amazon EC2 instance to host your Tape Gateway.
- [Deploy a customized Amazon EC2 instance for Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/ec2-gateway-common.html): Deploy an Amazon EC2 instance to host your Tape Gateway.
- [Modify Amazon EC2 instance metadata options](https://docs.aws.amazon.com/storagegateway/latest/tgw/modify-ec2-instance-metadata.html): Learn how to modify an existing Amazon EC2 instance so that it requires Instance Metadata Service Version 2 for all metadata requests.
- [Synchronize VM time with Hyper-V or Linux KVM host time](https://docs.aws.amazon.com/storagegateway/latest/tgw/MaintenanceTimeSync-hyperv.html): Learn how to synchronize the time on the virtual machine hosting your Tape Gateway with the time registered by your hypervisor host to avoid time drift.
- [Synchronize VM time with VMware host time](https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStartedSyncVMTime-common.html): Learn how synchronize VMware virtual machine time with the time on the host system that runs your hypervisor software.
- [Configure paravirtualized disk controllers](https://docs.aws.amazon.com/storagegateway/latest/tgw/SetParaVirtualization-common.html): Learn how to configure the VMware host platform for your gateway to use paravirtual iSCSI controllers.
- [Configuring network adapters for your gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/NICConfiguring-common.html): Learn how to configure your gateway to use the E1000 network adapter, or use multiple network adapters.
- [Using VMware High Availability with Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/vmware-ha.html): Find information about Storage Gateway high availability for VMware environments.

### [Working with Tape Gateway storage resources](https://docs.aws.amazon.com/storagegateway/latest/tgw/resource-tapegateway.html)

Learn how to manage the physical and virtual storage resources associated with your Tape Gateway.

- [Removing Disks from Your Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/add-remove-disks.html): Learn how to remove local disks from your gateway, for example if you have a failed disk.
- [EBS Volumes for EC2 Gateways](https://docs.aws.amazon.com/storagegateway/latest/tgw/GatewayInstanceStorage-common.html): Add and remove EBS volumes for your gateway running as an Amazon EC2 instance.
- [Working with VTL Devices](https://docs.aws.amazon.com/storagegateway/latest/tgw/resource_vtl-devices.html): Use Tape Gateway devices to activate your gateway.
- [Working with Tapes](https://docs.aws.amazon.com/storagegateway/latest/tgw/managing-virtual-tapes-vtl.html): Manage virtual tapes in your Tape Gateway, including creating and deleting virtual tapes.
- [Getting Activation Key](https://docs.aws.amazon.com/storagegateway/latest/tgw/get-activation-key.html): Getting an activation key for your gateway in Storage Gateway.

### [Connecting iSCSI Initiators](https://docs.aws.amazon.com/storagegateway/latest/tgw/initiator-connection-common.html)

Learn how to work with volumes or virtual tape library devices that are exposed as Internet Small Computer System Interface targets.

- [Connecting VTL devices to a Windows client](https://docs.aws.amazon.com/storagegateway/latest/tgw/ConfiguringiSCSIClient-vtl.html): Connect your VTL devices, such as tape drives and a media changer, to an iSCSI target for your Tape Gateway.
- [Connecting VTL devices to a Linux client](https://docs.aws.amazon.com/storagegateway/latest/tgw/ConfiguringiSCSIClientInitiatorRedHatClient.html): Learn how to connect your gateway VTL devices from a Red Hat Linux client with the iscsi-initiator-utils RPM package.
- [Customizing iSCSI Settings](https://docs.aws.amazon.com/storagegateway/latest/tgw/recommendediSCSISettings.html): Use recommended iSCSI settings for Storage Gateway.
- [Configuring CHAP Authentication](https://docs.aws.amazon.com/storagegateway/latest/tgw/ConfiguringiSCSIClientInitiatorCHAP.html): Configure CHAP authentication for your gateway volumes to provide protection against playback attacks.
- [Using Direct Connect with Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/using-dx.html): Learn how to use Direct Connect to link your internal network to the Amazon Web Services Cloud for high-throughput workload needs.
- [Getting the gateway IP address](https://docs.aws.amazon.com/storagegateway/latest/tgw/getting-ip-address.html): Learn how to connect and activate your gateway after choosing a host and deploying your gateway virtual machine.
- [IPv6 support](https://docs.aws.amazon.com/storagegateway/latest/tgw/ipv6-support.html): IPv6 considerations for tape and volume gateways.
- [Understanding Resources and Resource IDs](https://docs.aws.amazon.com/storagegateway/latest/tgw/storage-gateway-resource-id.html): Learn about Storage Gateway resources and resource IDs.
- [Tagging Your Resources](https://docs.aws.amazon.com/storagegateway/latest/tgw/tagging-resources-common.html): Learn about tagging your Storage Gateway resources.
- [Open-Source Components](https://docs.aws.amazon.com/storagegateway/latest/tgw/AboutAWSStorageGatewaySoftware.html): Lists open-source software components available for Storage Gateway.
- [Quotas](https://docs.aws.amazon.com/storagegateway/latest/tgw/resource-gateway-limits.html): Lists the quotas for volumes, virtual tapes, and upload and download rates in Storage Gateway.
