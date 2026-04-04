# Source: https://docs.aws.amazon.com/storagegateway/latest/vgw/llms.txt

# AWS Storage Gateway Volume Gateway User Guide

> Storage Gateway is a hybrid storage service that allows your on-premises applications to seamlessly use Amazon Web Services cloud storage. You can use the service for backup and archiving, disaster recovery, cloud bursting, storage tiering, and migration. Storage Gateway is a hybrid storage service that allows your on-premises applications to seamlessly use Amazon Web Services cloud storage. You can use the service for backup and archiving, disaster recovery, cloud bursting, storage tiering, and migration. This guide explains how to create and manage a Storage Gateway.

- [Volume Gateway setup requirements](https://docs.aws.amazon.com/storagegateway/latest/vgw/Requirements.html)
- [Performance and optimization for Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/Performance.html)
- [Best practices](https://docs.aws.amazon.com/storagegateway/latest/vgw/best-practices.html)
- [API Reference](https://docs.aws.amazon.com/storagegateway/latest/vgw/AWSStorageGatewayAPI.html)
- [Document history](https://docs.aws.amazon.com/storagegateway/latest/vgw/DocumentHistory.html)
- [AL2 to AL2023 Migration](https://docs.aws.amazon.com/storagegateway/latest/vgw/al2-to-al2023-migration.html)
- [Release notes](https://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)

## [What is Volume Gateway?](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html)

- [How Volume Gateway works](https://docs.aws.amazon.com/storagegateway/latest/vgw/StorageGatewayConcepts.html): Find an architectural overview of the Volume Gateway solution.


## [Getting started with AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStarted.html)

- [Sign Up for AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedSignUpStep1-common.html): Sign up for an Amazon Web Services account to get access to all AWS resources, forums, support, and usage reports to use with Storage Gateway.
- [Create an IAM user with administrator privileges](https://docs.aws.amazon.com/storagegateway/latest/vgw/setting-up-create-iam-user.html): Learn how to create an IAM user with administrative privileges for your AWS account.
- [Accessing AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsAPIIntro.html): Access Storage Gateway through the console or programmatically using the AWS SDKs.
- [AWS Regions that support Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/available-regions-intro.html): Find the AWS Regions that you can select for storing your data when you activate your gateway.


## [Using the hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/vgw/hardware-appliance.html)

- [Setting up your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/vgw/appliance-quick-start.html): Set up and configure your Storage Gateway Hardware Appliance.
- [Physically installing your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/vgw/appliance-rack-mount.html): Learn how to physically mount and connect your hardware appliance
- [Accessing the hardware appliance console](https://docs.aws.amazon.com/storagegateway/latest/vgw/access-hardware-appliance-console.html): Learn how to access the hardware appliance console.
- [Configuring hardware appliance network parameters](https://docs.aws.amazon.com/storagegateway/latest/vgw/appliance-configure-network.html): Configure network parameters for your Storage Gateway Hardware Appliance.
- [Activating your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/vgw/appliance-activation.html): Activate your hardware appliance as a Storage Gateway.
- [Creating a gateway on your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/vgw/appliance-launch-gateway.html): Create a Storage Gateway on the Storage Gateway Hardware Appliance.
- [Configuring a gateway IP address on the hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/vgw/appliance-configure-ip.html): Configure the gateway IP address on the hardware appliance to work with applications.
- [Removing gateway software from your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/vgw/appliance-remove-gateway.html): Remove gateway software from your Storage Gateway Hardware Appliance.
- [Deleting your hardware appliance](https://docs.aws.amazon.com/storagegateway/latest/vgw/delete-appliance.html): Delete your Storage Gateway Hardware Appliance from your AWS account.


## [Creating your gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/creating-your-gateway.html)

- [Creating a Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/create-volume-gateway.html): Find instructions on how to download, deploy, and activate a Volume Gateway.
- [Creating a volume](https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedCreateVolumes.html): Create volumes to store your data, now that you have activated your gateway.
- [Connecting your volumes to your client](https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedAccessVolumes.html): Learn how to connect your gateway volumes to your client.
- [Initializing and formatting your volume](https://docs.aws.amazon.com/storagegateway/latest/vgw/format-volume.html): After you use the iSCSI initiator in your client to connect to your volumes, you initialize and format your volume.
- [Testing your gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedTestGatewayMain.html): Test your setup on Microsoft Windows by writing data to the volume, taking a snapshot, and restoring the snapshot to another volume.
- [Backing up your volumes](https://docs.aws.amazon.com/storagegateway/latest/vgw/backing-up-volumes.html): Learn how to back up your Storage Gateway volumes.
- [Where do I go from here?](https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedWhatsNextStep3.html): Find additional resources to learn more about Storage Gateway.
- [Activating your gateway in a virtual private cloud](https://docs.aws.amazon.com/storagegateway/latest/vgw/gateway-private-link.html): Additional information on activating a gateway in a VPC.


## [Managing Your Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/managing-gateway-common.html)

- [Editing Gateway Information](https://docs.aws.amazon.com/storagegateway/latest/vgw/edit-gateway-information.html): Edit basic information for an existing Storage Gateway
- [Adding and expanding volumes](https://docs.aws.amazon.com/storagegateway/latest/vgw/volume-size-increase.html): Learn how to add more volumes or expand the size of existing volumes as your application needs grow.
- [Cloning a volume](https://docs.aws.amazon.com/storagegateway/latest/vgw/clone-volume.html): Learn how to create a new volume from the most recent recovery point of an existing volume.
- [Viewing volume usage](https://docs.aws.amazon.com/storagegateway/latest/vgw/volume-usage.html): Learn how to view the amount of data stored on a volume using the Storage Gateway console.
- [Deleting storage volumes](https://docs.aws.amazon.com/storagegateway/latest/vgw/ApplicationStorageVolumesCached-Removing.html): Remove Storage Gateway cached volumes as application needs change.
- [Moving Your Volumes to a Different Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/attach-detach-volume.html): Attach and detach a volume from a gateway in Storage Gateway to move it or to refresh your underlying hardware.
- [Creating a recovery snapshot](https://docs.aws.amazon.com/storagegateway/latest/vgw/snapshot.html): Learn about how to create a recovery snapshot from a volume recovery point.
- [Editing a snapshot schedule](https://docs.aws.amazon.com/storagegateway/latest/vgw/SchedulingSnapshot.html): Learn how to change a snapshot schedule by specifying either the time the snapshot occurs each day or the frequency or both.
- [Deleting Snapshots](https://docs.aws.amazon.com/storagegateway/latest/vgw/DeletingASnapshot.html): Learn how to delete a snapshot of your storage volume.
- [Understanding Volume Status and Transitions](https://docs.aws.amazon.com/storagegateway/latest/vgw/StorageVolumeStatuses.html): Understand the possible status values for your volume and transitions between statuses as shown in the Storage Gateway console.
- [Moving your data to a new gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/migrate-data.html): Move data between gateways in Storage Gateway when you want to improve performance or to respond to a notification to migrate the gateway.


## [Monitoring Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/Main_monitoring-gateways-common.html)

- [Understanding gateway metrics](https://docs.aws.amazon.com/storagegateway/latest/vgw/MonitoringGateways-common.html): Learn about the metrics that help you monitor your Storage Gateway appliance.
- [Monitoring the upload buffer](https://docs.aws.amazon.com/storagegateway/latest/vgw/PerfUploadBuffer-common.html): Learn how to monitor the gateway upload buffer and create an alarm for when the buffer exceeds a specified threshold.
- [Monitoring cache storage](https://docs.aws.amazon.com/storagegateway/latest/vgw/PerfCache-common.html): Learn how to monitor the cache storage of a gateway in a cached volumes setup.
- [Understanding CloudWatch alarms](https://docs.aws.amazon.com/storagegateway/latest/vgw/cloudwatch-alarms.html): Learn about CloudWatch alarms, which monitor information about your gateway based on metrics and expressions.
- [Creating recommended CloudWatch alarms](https://docs.aws.amazon.com/storagegateway/latest/vgw/cloudwatch-alarms-create-recommended.html): Create recommended CloudWatch alarms for your gateway.
- [Creating a custom CloudWatch alarm](https://docs.aws.amazon.com/storagegateway/latest/vgw/cloudwatch-alarms-create-alarm.html): Learn how to create CloudWatch alarms that send you notifications when a metric changes state.

### [Monitoring your Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/monitoring-volume-gateway.html)

Monitor your gateway, volumes associated with the gateway, and the upload buffer.

- [Getting Volume Gateway health logs](https://docs.aws.amazon.com/storagegateway/latest/vgw/cw-log-groups-volume.html): Learn to use Amazon CloudWatch Logs to get information about your Volume Gateway and related resources.
- [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/storagegateway/latest/vgw/UsingCloudWatchConsole-common.html): Get monitoring data for your gateway using either the AWS Management Console or the CloudWatch API.
- [Measuring Performance Between Your Application and Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/PerfAppGateway-common.html): Measure performance of data throughput, data latency, and operations per second between your application and your gateway.
- [Measuring Performance Between Your Gateway and AWS](https://docs.aws.amazon.com/storagegateway/latest/vgw/PerfGatewayAWS-common.html): Measure performance of data throughput, data latency, and operations per second between your gateway and AWS.
- [Understanding volume metrics](https://docs.aws.amazon.com/storagegateway/latest/vgw/MonitoringVolumes-common.html): Learn about the Storage Gateway metrics that cover the volumes associated with your gateways.


## [Maintaining Your Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/maintaining-gateway.html)

### [Managing local disks](https://docs.aws.amazon.com/storagegateway/latest/vgw/ManagingLocalStorage-common.html)

Learn how to manage and allocate the local disks that your gateway virtual machine uses for buffering and storage.

- [Deciding the amount of local disk storage](https://docs.aws.amazon.com/storagegateway/latest/vgw/decide-local-disks-and-sizes.html): Learn how to properly size the local disks that your gateway uses for cache and upload buffer.
- [Add upload buffer or cache storage](https://docs.aws.amazon.com/storagegateway/latest/vgw/ConfiguringLocalDiskStorage.html): Configure additional upload buffer and cache storage space for your Volume Gateway.
- [Managing Bandwidth](https://docs.aws.amazon.com/storagegateway/latest/vgw/MaintenanceUpdateBandwidth-common.html): Update the bandwidth-rate limits for your gateway.

### [Managing gateway updates](https://docs.aws.amazon.com/storagegateway/latest/vgw/MaintenanceManagingUpdate-common.html)

Use the Storage Gateway console to turn gateway maintenance updates updates on or off, or configure an update schedule.

- [Turn maintenance updates on or off](https://docs.aws.amazon.com/storagegateway/latest/vgw/maintenance-updates-on-off.html): Use the Storage Gateway console to turn maintenance updates on or off for a specific gateway.
- [Modify the gateway maintenance window schedule](https://docs.aws.amazon.com/storagegateway/latest/vgw/configure-maintenance-window-schedule.html): Use the Storage Gateway console to configure the maintenance window schedule for a specific gateway.
- [Apply an update manually](https://docs.aws.amazon.com/storagegateway/latest/vgw/apply-update-manually.html): Learn how to manually apply a gateway appliance software update using the Storage Gateway console.
- [Shutting Down Your Gateway VM](https://docs.aws.amazon.com/storagegateway/latest/vgw/MaintenanceShutDown-common.html): Learn how to shutdown or reboot your gateway virtual machine for maintenance, such as when applying a patch to your hypervisor.
- [Deleting your gateway and removing resources](https://docs.aws.amazon.com/storagegateway/latest/vgw/deleting-gateway-common.html): Delete your gateway using the AWS Storage Gateway console and clean up associated resources.


## [Performing maintenance tasks using the local console](https://docs.aws.amazon.com/storagegateway/latest/vgw/manage-on-premises.html)

- [Accessing the Gateway Local Console](https://docs.aws.amazon.com/storagegateway/latest/vgw/accessing-local-console.html): Learn how to access the local console on your gateway virtual machine host.

### [Performing Tasks on the VM Local Console](https://docs.aws.amazon.com/storagegateway/latest/vgw/manage-on-premises-common.html)

Learn how to perform maintenance tasks using the gateway local console.

- [Logging in to the Volume Gateway local console](https://docs.aws.amazon.com/storagegateway/latest/vgw/LocalConsole-login-common.html): Learn how to log into the gateway local console and change the default password.
- [Configuring a SOCKS5 proxy for your on-premises gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/MaintenanceRoutingProxy-common.html): Learn how to route your gateway through a SOCKS proxy server.
- [Configuring Your Gateway Network](https://docs.aws.amazon.com/storagegateway/latest/vgw/MaintenanceConfiguringStaticIP-common.html): Configure your gateway to use a static IP address.
- [Testing your gateway connectivity to the internet](https://docs.aws.amazon.com/storagegateway/latest/vgw/MaintenanceTestGatewayConnectivity-common.html): Test the connection from your gateway to the internet using the gateway local console.
- [Running storage gateway commands in the local console for an on-premises gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/MaintenanceGatewayConsole-common.html): Learn how to run commands in the local console for an on-premises gateway to perform maintenance tasks such as saving routing tables or connecting to Support.
- [Viewing your gateway system resource status](https://docs.aws.amazon.com/storagegateway/latest/vgw/system-resource-check-common.html): Learn how to check the virtual CPU cores, root volume size, and RAM available to your gateway.

### [Performing Tasks on the EC2 Local Console](https://docs.aws.amazon.com/storagegateway/latest/vgw/ec2-local-console-common.html)

Perform maintenance tasks for a gateway deployed on an Amazon EC2 instance by using the local EC2 console.

- [Logging In to Your EC2 Gateway Local Console](https://docs.aws.amazon.com/storagegateway/latest/vgw/EC2_MaintenanceConsoleWindow-common.html): Log in to your gateway local console so that you can perform maintenance tasks on your Amazon EC2 gateway.
- [Configuring an HTTP proxy](https://docs.aws.amazon.com/storagegateway/latest/vgw/EC2_MaintenanceRoutingProxy-common.html): Configure an HTTP proxy for your gateway to route HTTPS traffic through a local HTTP proxy server.
- [Testing gateway network connectivity](https://docs.aws.amazon.com/storagegateway/latest/vgw/EC2_MaintenanceTestGatewayConnectivity-common.html): Learn how to test gateway network connectivity using the gateway local console.
- [Viewing your gateway system resource status](https://docs.aws.amazon.com/storagegateway/latest/vgw/EC2_system-resource-check-common.html): Learn how to check the virtual CPU cores, root volume size, and RAM for a gateway.
- [Running Storage Gateway commands on the local console](https://docs.aws.amazon.com/storagegateway/latest/vgw/EC2_MaintenanceGatewayConsole-common.html): Learn how to run commands in the gateway local console to perform maintenance tasks such as saving routing tables or connecting to Support.


## [Security](https://docs.aws.amazon.com/storagegateway/latest/vgw/security.html)

### [Data protection](https://docs.aws.amazon.com/storagegateway/latest/vgw/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Storage Gateway.

- [Data encryption](https://docs.aws.amazon.com/storagegateway/latest/vgw/encryption.html): Encrypt your data using AWS Key Management Service.
- [Configuring CHAP authentication](https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedConfigureChap.html): Learn how to configure CHAP to authenticate iSCSI and initiator connections.

### [Identity and Access Management](https://docs.aws.amazon.com/storagegateway/latest/vgw/security-iam.html)

How to authenticate requests and manage access to your AWS SGW resources.

- [How AWS Storage Gateway works with IAM](https://docs.aws.amazon.com/storagegateway/latest/vgw/security_iam_service-with-iam.html): Learn about how AWS Storage Gateway works with IAM to secure access to your resources and data.
- [Identity-based policy examples](https://docs.aws.amazon.com/storagegateway/latest/vgw/security_iam_id-based-policy-examples.html): Learn how to grant users permission to perform actions on the resources that they need by creating IAM policies.
- [Troubleshooting](https://docs.aws.amazon.com/storagegateway/latest/vgw/security_iam_troubleshoot.html): Learn how to diagnose and fix common issues that you might encounter when working with AWS Storage Gateway and IAM.
- [Compliance validation](https://docs.aws.amazon.com/storagegateway/latest/vgw/storagegateway-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/storagegateway/latest/vgw/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Storage Gateway features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/storagegateway/latest/vgw/infrastructure-security.html): Learn how AWS Storage Gateway isolates service traffic.
- [AWS Security Best Practices](https://docs.aws.amazon.com/storagegateway/latest/vgw/security-best-practice.html): Learn about security features to consider as you develop and implement your own Storage Gateway security policies.
- [Logging and Monitoring](https://docs.aws.amazon.com/storagegateway/latest/vgw/logging-using-cloudtrail.html): Learn about logging Storage Gateway with AWS CloudTrail.


## [Troubleshooting gateway issues](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshooting-gateway-issues.html)

- [Troubleshooting: gateway offline issues](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshooting-gateway-offline.html): Learn what to do if the status of your gateway shows offline in the Storage Gateway console.
- [Troubleshooting: gateway activation issues](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshooting-gateway-activation.html): Learn what to do if you receive an internal error message when activating your AWS Storage Gateway.
- [Troubleshooting on-premises gateway issues](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshooting-on-premises-gateway-issues.html): Learn how to diagnose and fix common problems you might encounter with gateways deployed on-premises.
- [Troubleshooting Microsoft Hyper-V setup issues](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshooting-hyperv-setup.html): The following table lists typical issues that you might encounter when deploying Storage Gateway on the Microsoft Hyper-V platform.
- [Troubleshooting Amazon EC2 gateway issues](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshooting-EC2-gateway-issues.html): Learn how to diagnose and fix common problems you might encounter with gateways deployed on Amazon EC2 instances.
- [Troubleshooting hardware appliance issues](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshooting-hardware-appliance-issues.html): Learn now to diagnose and fix common problems that you might encounter with the Storage Gateway Hardware Appliance.
- [Troubleshooting volume issues](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshoot-volume-issues.html): Learn about the most typical issues you might encounter when working with volumes, and actions you can take to fix them.
- [Troubleshooting high availability issues](https://docs.aws.amazon.com/storagegateway/latest/vgw/troubleshooting-ha-issues.html): Troubleshoot Storage Gateway high availability issues using Amazon CloudWatch health notifications and metrics.


## [Additional Resources](https://docs.aws.amazon.com/storagegateway/latest/vgw/Resources.html)

### [Host setup](https://docs.aws.amazon.com/storagegateway/latest/vgw/resource-vm-setup.html)

Learn about how to set up and configure virtual host platforms for Storage Gateway.

- [Deploy a default Amazon EC2 host for Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/ec2-quicklaunch-settings.html): Deploy an Amazon EC2 instance to host your Volume Gateway using default specifications.
- [Deploy a customized Amazon EC2 instance for Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/ec2-gateway-common.html): Deploy an Amazon EC2 instance to host your Volume Gateway.
- [Modify Amazon EC2 instance metadata options](https://docs.aws.amazon.com/storagegateway/latest/vgw/modify-ec2-instance-metadata.html): Learn how to modify an existing Amazon EC2 instance so that it requires Instance Metadata Service Version 2 for all metadata requests.
- [Synchronize VM time with Hyper-V or Linux KVM host time](https://docs.aws.amazon.com/storagegateway/latest/vgw/MaintenanceTimeSync-hyperv.html): Learn how to synchronize the time on the virtual machine hosting your Volume Gateway with the time registered by your hypervisor host to avoid time drift.
- [Synchronize VM time with VMware host time](https://docs.aws.amazon.com/storagegateway/latest/vgw/GettingStartedSyncVMTime-common.html): Learn how synchronize VMware virtual machine time with the time on the host system that runs your hypervisor software.
- [Configure paravirtualized disk controllers](https://docs.aws.amazon.com/storagegateway/latest/vgw/SetParaVirtualization-common.html): Learn how to configure the VMware host platform for your gateway to use paravirtual iSCSI controllers.
- [Configuring network adapters for your gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/NICConfiguring-common.html): Learn how to configure your gateway to use the E1000 network adapter, or use multiple network adapters.
- [Using VMware High Availability with Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/vmware-ha.html): Find information about Storage Gateway high availability for VMware environments.

### [Working with Volume Gateway storage resources](https://docs.aws.amazon.com/storagegateway/latest/vgw/resource-volume-gateway.html)

Learn how to manage the storage resources associated with your Volume Gateway appliance and its virtual host platform.

- [Removing Disks from Your Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/add-remove-disks.html): Learn how to remove local disks from your gateway, for example if you have a failed disk.
- [EBS Volumes for EC2 Gateways](https://docs.aws.amazon.com/storagegateway/latest/vgw/GatewayInstanceStorage-common.html): Add and remove EBS volumes for your gateway running as an Amazon EC2 instance.
- [Getting Activation Key](https://docs.aws.amazon.com/storagegateway/latest/vgw/get-activation-key.html): Getting an activation key for your gateway in Storage Gateway.

### [Connecting iSCSI Initiators](https://docs.aws.amazon.com/storagegateway/latest/vgw/initiator-connection-common.html)

Learn how to work with volumes or virtual tape library devices that are exposed as Internet Small Computer System Interface targets.

- [Connecting to your volumes from a Windows client](https://docs.aws.amazon.com/storagegateway/latest/vgw/ConfiguringiSCSIClient.html): Learn how to connect your gateway volumes from a Windows client.
- [Connecting volumes to a Linux client](https://docs.aws.amazon.com/storagegateway/latest/vgw/ConfiguringiSCSIClientInitiatorRedHatClient.html): Learn how to connect your gateway volumes from a Red Hat Linux client with the iscsi-initiator-utils RPM package.
- [Customizing iSCSI Settings](https://docs.aws.amazon.com/storagegateway/latest/vgw/recommendediSCSISettings.html): Use recommended iSCSI settings for Storage Gateway.
- [Configuring CHAP Authentication](https://docs.aws.amazon.com/storagegateway/latest/vgw/ConfiguringiSCSIClientInitiatorCHAP.html): Configure CHAP authentication for your gateway volumes to provide protection against playback attacks.
- [Using Direct Connect with Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/using-dx.html): Learn how to use Direct Connect to link your internal network to the Amazon Web Services Cloud for high-throughput workload needs.
- [Getting the gateway IP address](https://docs.aws.amazon.com/storagegateway/latest/vgw/getting-ip-address.html): Learn how to connect and activate your gateway after choosing a host and deploying your gateway virtual machine.
- [IPv6 support](https://docs.aws.amazon.com/storagegateway/latest/vgw/ipv6-support.html): IPv6 considerations for tape and volume gateways.
- [Understanding Resources and Resource IDs](https://docs.aws.amazon.com/storagegateway/latest/vgw/storage-gateway-resource-id.html): Learn about Storage Gateway resources and resource IDs.
- [Tagging Your Resources](https://docs.aws.amazon.com/storagegateway/latest/vgw/tagging-resources-common.html): Learn about tagging your Storage Gateway resources.
- [Open-Source Components](https://docs.aws.amazon.com/storagegateway/latest/vgw/AboutAWSStorageGatewaySoftware.html): Lists open-source software components available for Storage Gateway.
- [Quotas](https://docs.aws.amazon.com/storagegateway/latest/vgw/resource-gateway-limits.html): Lists the quotas for volumes, virtual tapes, and upload and download rates in Storage Gateway.
