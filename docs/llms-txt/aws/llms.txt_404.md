# Source: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/llms.txt

# FSx for ONTAP ONTAP User Guide

> This is the official Amazon Web Services documentation for Amazon FSx for NetApp ONTAP. Amazon FSx for NetApp ONTAP is an AWS service that makes it easier to launch and run fully-featured NetApp ONTAP file systems in the AWS Cloud. The Amazon FSx for NetApp ONTAP User Guide describes key concepts for FSx for ONTAP and provides instructions for launching and using your file system.

- [What is Amazon FSx for NetApp ONTAP?](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)
- [How it works](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap.html)
- [Getting started](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/getting-started.html)
- [AWS Regions](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/available-aws-regions.html)
- [Availability, durability, and deployment options](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html)
- [Performance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/performance.html)
- [Billing and usage reporting](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/FSxONTAP-Billing.html)
- [Quotas](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/limits.html)
- [Document history](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/document-history.html)

## [Accessing your data](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/supported-fsx-clients.html)

- [Configure routing to access Multi-AZ file systems from outside your VPC](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/configuring-routing-using-AWSTG.html): Configure routing with AWS Transit Gateway to access FSx for ONTAP file systems from peered or on-premises networks when the endpoint IP address range is outside your VPC's CIDR range.
- [Configure routing to access Multi-AZ file systems from on-premises](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/configure-routing-maz-on-prem.html): Configure AWS Transit Gateway to access Multi-AZ FSx for ONTAP file systems from on-premises networks when the endpoint IP address range is outside your VPC's CIDR range.
- [Mounting on Linux clients](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/attach-linux-client.html): Learn how to mount an FSx for ONTAP volume on a Linux client, including steps for automatic mounting on instance reboot and configuring access from peered networks.
- [Mounting on Windows clients](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/attach-windows-client.html): Learn how to access FSx for ONTAP file systems using Windows clients.
- [Mounting on macOS clients](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/attach-mac-client.html): Learn how to access data in FSx for ONTAP file systems using macOS clients.
- [Provisioning iSCSI for Linux](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/mount-iscsi-luns-linux.html): Learn how to configure the Internet Small Computer Systems Interface (iSCSI) storage area network (SAN) on Linux hosts and create iSCSI LUNs on FSx for ONTAP file systems for shared block storage.
- [Provisioning iSCSI for Windows](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/mount-iscsi-windows.html): Learn how to provision the Internet Small Computer Interface (iSCI) protocol on a Windows client and create an iSCSI LUN your FSx for ONTAP file system to use transport data using the iSCSI block data protocol.
- [Provisioning NVMe/TCP for Linux](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/provision-nvme-linux.html): Learn how to configure the Non-Volatile Memory Express (NVMe) block storage protocol over TCP on a Linux host and your Amazon FSx for NetApp ONTAP file system to use NVMe/TCP shared block storage.

### [Accessing data via S3 access points](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/accessing-data-via-s3-access-points.html)

Learn how to use Amazon S3 access points with FSx for ONTAP to simplify data access, enforce permissions, and perform object operations on files stored in FSx volumes.

- [Naming rules, restrictions, and limitations](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/access-point-for-fsxn-restrictions-limitations-naming-rules.html): Learn about Amazon S3 access points attached to FSx for ONTAP volumes, including naming rules, restrictions, and limitations for managing data access in the cloud.
- [Referencing access points](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/referencing-access-points-for-fsxn.html): Learn how to use Amazon S3 access point ARNs, aliases, and virtual-hostedâstyle URIs to perform operations on FSx for ONTAP volumes using the Amazon S3 object API.
- [Access point compatibility](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/access-points-for-fsxn-object-api-support.html): Learn which S3 API object operations you can with S3 access points attached to FSx for ONTAP volumes for data access.
- [Managing access](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/s3-ap-manage-access-fsxn.html): Learn how to configure Amazon S3 access points for Amazon FSx volumes, including permissions, user identity, VPC restrictions, and encryption.

### [Creating an access point](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/fsxn-creating-access-points.html)

Create up to 10,000 access points to simplify managing data access at scale in Amazon S3.

- [Creating access points](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/create-access-points.html)
- [Creating access points restricted to a VPC](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/access-points-for-fsxn-vpc.html): Configuring Amazon S3 access points with a virtual private cloud (VPC)

### [Managing access points](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/access-points-for-fsxn-manage.html)

Managing your Amazon S3 access point attachments

- [Listing S3 access point attachments](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/access-points-list.html): This section explains how to list S3 access point using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Viewing access point details](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/access-points-details.html): This section explains how to view the details of S3 access points using the AWS Management Console, AWS Command Line Interface, or REST API.
- [Deleting an S3 access point attachment](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/delete-access-point.html): This section explains how to delete S3 access points using the AWS Management Console, AWS Command Line Interface, or REST API.

### [Using access points](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/access-points-for-fsxn-usage-examples.html)

Access file data with Amazon S3 access point attachments, using a compatible subset of S3 operations and other AWS services, such as AWS CloudTrail.

- [Download a file](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/get-object-ap.html): The following get-object example command shows how you can use the AWS CLI to download a file through an access point.
- [Upload a file](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/put-object-ap.html): The following put-object example command shows how you can use the AWS CLI to upload a file through an access point.
- [List files](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/list-object-ap.html): The following example lists files through the access point alias my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b-ext-s3alias owned by account ID 111122223333 in Region us-east-2.
- [Add a tag-set](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/add-tag-set-ap.html): The following put-object-tagging example command shows how you can use the AWS CLI to add a tag-set through an access point.
- [Delete a file](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/delete-object-ap.html): The following delete-object example command shows how you can use the AWS CLI to delete a file through an access point.
- [Troubleshooting access points](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/troubleshooting-access-points-for-fsxn.html): This section describes symptoms, causes, and resolutions for when you encounter issues accessing your FSx data from S3 access points.

### [Accessing data from other AWS services](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-fsx-with-other-AWS-services.html)

Discover which AWS services you can use to access your data.

- [Using Amazon WorkSpaces](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-workspaces.html): Learn how to manage Amazon WorkSpaces connections to FSx for ONTAP.
- [Using Amazon ECS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/mount-ontap-ecs-containers.html): Learn how to access Amazon FSx for NetApp ONTAP file systems from Amazon ECS Docker containers on EC2 Linux and Windows instances, including mounting volumes and configuring task definitions.
- [Using Amazon EVS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/evs-ontap.html): Learn how to use FSx for ONTAP as an external datastore for Amazon EVS on AWS SDDCs and access configuration guides for deployment.
- [Using VMware Cloud](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/vmware-cloud-ontap.html): Learn how to use FSx for ONTAP as an external datastore for VMware Cloud on AWS SDDCs and access configuration guides for deployment.


## [Administering resources](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/administering-file-systems.html)

### [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-storage-capacity.html)

Monitor and manage the storage capacity of your FSx for ONTAP file system by using volume data tiering policies, and scaling storage capacity and IOPS.

### [File system storage capacity and IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html)

Learn how to manage and update SSD capacity and IOPS for Amazon FSx for NetApp ONTAP file systems, including considerations, monitoring, and best practices.

- [Creating a storage capacity utilization alarm](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/alarm-low-primary-storage.html): Learn how to create a CloudWatch alarm to monitor and alert when your FSx for ONTAP file system's SSD storage utilization approaches 80%.
- [Updating storage capacity and IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/increase-storage-capacity.html): Learn how to modify SSD storage capacity and provisioned IOPS for an FSx for ONTAP file system using the Amazon FSx console, the CLI;, or the API.
- [Updating storage capacity dynamically](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/automate-storage-capacity-increase.html): Learn how to automatically increase the SSD storage capacity of an FSx for ONTAP file system using CloudFormation.
- [Monitoring SSD storage utilization](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitor-fs-storage-console.html): Monitor SSD storage capacity utilization for FSx for ONTAP file systems using AWS tools and set alerts for optimal performance.
- [Monitoring storage efficiency savings](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/view-storage-efficiency.html): Learn how to view storage efficiency savings for FSx for ONTAP file systems using the AWS Management Console, CloudWatch, and ONTAP CLI.
- [Monitoring storage capacity and IOPS updates](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitoring-storage-capacity-increase.html): Learn how to monitor the progress of storage capacity and IOPS update requests for FSx for ONTAP file systems.

### [Volume storage capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-storage-capacity.html)

Learn how to manage and monitor storage capacity for FSx for ONTAP volumes, including data tiering, snapshots, and file capacity.

- [Managing storage efficiencies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/manage-vol-SE.html): Discover ways to manage storage efficiencies on your FSx for ONTAP volumes.
- [Enabling autosizing](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/enable-volume-autosizing.html): Learn how to enable the autosizing feature on FSx for ONTAP volumes.
- [Enabling cloud write mode](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/cloud-write-mode.html): Learn how to enable or disable cloud write mode for existing FSx for ONTAP volumes using the ONTAP CLI.
- [Updating storage capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/manage-volume-capacity.html): Learn how to change the amount of storage capacity for an FSx for ONTAP volume.
- [Updating a tiering policy](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/modify-volume-tiering-policy.html): Learn how set the tiering policy of an FSx for ONTAP volume.
- [Updating cooling days](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/set-cooling-days.html): Set minimum cooling days for a volume to determine warm and cold data thresholds using the AWS CLI, API, or ONTAP CLI.
- [Updating cloud retrieval policy](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/set-cloud-retrieval.html): Learn how to set the cloud retrieval policy for an existing FSx for ONTAP volume using the ONTAP CLI.
- [Updating the maximum number of files](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/increase-volume-max-files.html): Learn how to increase the number of files that an FSx for ONTAP volume can contain.
- [Monitoring storage capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitor-volume-storage-console.html): Learn how to monitor and manage storage capacity for FSx for ONTAP volumes using the AWS Management Console, AWS CLI, and ONTAP CLI.
- [Monitoring file capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/view-volume-file-capacity.html): Learn how to monitor file usage on FSx for ONTAP volumes using CloudWatch metrics or Amazon FSx console.

### [Managing file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-file-systems.html)

Learn about the various tasks available for managing FSx for ONTAP file systems, including the updates you can make to existing file systems.

- [Creating file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-file-systems.html): Explains how to create FSx for ONTAP file systems using the AWS Management Console and AWS CLI.
- [Updating file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/updating-file-system.html): Learn how to update properties of an existing FSx for ONTAP file system, including backups, maintenance windows, administrative passwords, and VPC route tables.

### [Managing HA pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/HA-pairs.html)

Learn about high-availability (HA) pairs in FSx for ONTAP file systems, including their configuration, performance capabilities, and how to choose the right number of HA pairs for your workload.

- [Adding HA pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/adding-HA-pairs.html): Learn how to add high-availability pairs to your second-generation file system.
- [Balancing HA pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitor-workload-balance.html): Describes how to monitor the workload balance of an FSx for ONTAP file system.
- [Managing the NVMe cache](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/nvme-cache.html): Learn how to enable, disable, and validate your file system's NVMe cache.
- [Managing network type](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/manage-network-type.html): Describes the two network types of IPv4-only and dual-stack (IPv4 and IPv6) for FSx for ONTAP file systems and how to manage them.
- [Monitoring file system details](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/viewing-file-system.html): Learn how to view and understand detailed configuration information for your FSx for ONTAP file system using the Amazon FSx console, AWS CLI, and API.
- [Deleting file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/delete-file-system.html): Learn how to delete an FSx for ONTAP file system using the Amazon FSx console, AWS CLI, or API, including steps to clean up resources and remove volumes and SVMs.

### [Managing SVMs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html)

Learn how to manage your FSx for ONTAP SVMs using the AWS Management Console, AWS CLI, and API.

- [Creating SVMs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-svms.html): Learn how to create an FSx for ONTAP SVM using the AWS Management Console, AWS CLI, and API.
- [Updating SVMs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/updating-svms.html): Learn how to make configuration updates to an FSx for ONTAP storage virtual machine using the AWS Management Console, AWS CLI, and API.
- [Managing SVM Microsoft Active Directory configurations](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/manage-svm-ad-config-secrets-manager.html): Learn how to manage Microsoft Active Directory configurations for your FSx for ONTAP SVMs using Secrets Manager for secure credential management.
- [Auditing file access](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/file-access-auditing.html): Describes how to set up and use the file access auditing feature.

### [Setting up workgroups](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/smb-server-workgroup-setup.html)

Learn how to configure an SMB server on a storage virtual machine (SVM) in a workgroup for FSx for ONTAP.

- [Creating an SMB server in a workgroup](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/create-smb-server-workgroup.html): Learn how to create an SMB server on an SVM in FSx for ONTAP using the ONTAP CLI vserver cifs create command, specifying the workgroup it belongs to.
- [Creating a local user account on the SMB server](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/smb-workgroup-create-local-accounts.html): Learn how to create and manage local user accounts for SMB authentication on FSx for ONTAP storage virtual machines (SVMs) using ONTAP CLI commands.
- [Creating local groups on the SMB server](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/smb-workgroup-create-local-groups.html): Learn how to create local groups on the SMB server for authorizing access to data on the SVM over SMB connections and assigning user rights and capabilities.
- [Adding local users to the local group](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/smb-workgroup-add-users-to-group.html): Learn how to manage local group membership in FSx for ONTAP by adding or removing local users, domain users, and domain groups using ONTAP CLI commands.
- [Monitoring SVM details](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/viewing-svms.html): Learn how to view FSx for ONTAP SVM configuration details using the AWS Management Console, AWS CLI, and API.
- [Deleting SVMs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/deleting-svms.html): Learn how to delete an FSx for ONTAP SVM using the AWS Management Console, AWS CLI, and API.

### [Managing volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html)

Learn how to manage FSx for ONTAP volumes using the AWS Management Console, AWS CLI, and API.

- [Creating volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-volumes.html): Learn how to create an FSx for ONTAP volume using the AWS Management Console, AWS CLI, and API.

### [Updating volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/updating-volumes.html)

Learn how to update the configuration of an FSx for ONTAP volume using the AWS Management Console, AWS CLI, and API.

- [Expanding FlexGroup volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/expanding-fg-volumes.html): Learn how to expand a FlexGroup FSx for ONTAP volume using the ONTAP CLI.
- [Moving volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/moving-fg-volumes.html): Learn how to move an FSx for ONTAP volume between aggregates using the ONTAP CLI.

### [Monitoring volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/viewing-volumes.html)

Learn how to view configuration details of an FSx for ONTAP volume using the AWS Management Console, AWS CLI, and API.

- [Viewing offline volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/offline-volumes.html): Learn how to manage volume backups and bring offline volumes online using ONTAP CLI commands in FSx for ONTAP file systems.

### [Deleting volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/deleting-volumes.html)

Learn how to delete an FSx for ONTAP volume using the AWS Management Console, AWS CLI, and API.

- [Deleting SnapLock volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-delete-volume.html): Explains how to delete a SnapLock volume.
- [Creating an iSCSI LUN](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/create-iscsi-lun.html): Learn how to create an iSCSI LUN on an FSx for ONTAP file system using the NetApp ONTAP CLI.
- [Updating maintenance windows](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/maintenance-windows.html): Describes the Amazon FSx weekly maintenance window and how to manage it.

### [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-throughput-capacity.html)

Learn how to modify the throughput capacity that's configured on your FSx for ONTAP file system when you need additional performance.

- [Updating throughput capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/increase-throughput-capacity.html): Learn how to update throughput capacity.
- [Monitoring throughput capacity changes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitoring-throughput-capacity-changes.html): Learn how to monitor throughput capacity changes.
- [Managing SMB shares](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/create-smb-shares.html): Learn how to manage SMB file shares on FSx for ONTAP using the Microsoft Windows Shared Folders GUI.
- [Managing with NetApp applications](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-resources-ontap-apps.html): Learn how access and manage Amazon FSx for NetApp ONTAP resources using the NetApp management applications.
- [Tagging resources](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/tag-resources.html): Learn about applying tags to Amazon FSx resources.


## [Protecting your data](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/protecting-data.html)

### [Backing up volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-backups.html)

Learn how to backup and restore volumes on your FSx for ONTAP file system to protect your data.

- [Creating user-initiated backups](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-backups.html): Create a user-initiated backup of an FSx for ONTAP volume using the AWS Management Console.
- [Restoring backups](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/to-restore-backups.html): Learn how to restore an FSx for ONTAP backup to a new volume using the AWS Management Console and AWS CLI, including step-by-step instructions and monitoring options.
- [Restoring a subset of data](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/data-subset-restore.html): Learn how to restore a subset of your data from an FSx for ONTAP volume backup so that you can resume operations faster in the event of accidental deletion, modification, or corruption of data.
- [Monitoring volume restore progress](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitor-backup-restore.html): Learn how to monitor the progress of restoring a volume backup to an FSx for ONTAP file system using the AWS Management Console, AWS CLI, and API.
- [Deleting backups](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-to-delete-backups.html): Learn how to delete backups.

### [Using volume snapshots](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html)

Learn how to set up and manage volume snapshots on your FSx for ONTAP file systems.

- [Restoring files from snapshots](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/user-restore-all-clients.html): Learn how to restore previous versions of files and folders using snapshots on FSx for ONTAP file systems for both Linux, macOS, and Windows clients.
- [Viewing the common snapshot](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/common-snapshot.html): Learn how to view the common snapshot on your volume.
- [Updating snapshot reserve space](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/modify-snapshot-reserve.html): Learn how to modify the snapshot reserve on an FSx for ONTAP volume using the ONTAP CLI.
- [Disabling automatic snapshots](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/disable-snapshots.html): Learn how to disable automatic snapshots for volumes in your FSx for ONTAP file system using the AWS Management Console, AWS CLI, or ONTAP CLI.

### [Deleting snapshots](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/manually-delete-snapshots.html)

Learn how to manually delete volume snapshots using the ONTAP CLI command in FSx for ONTAP, including important considerations for FSx for ONTAP backups.

- [Creating a Snapshot autodelete policy](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshot-autodelete-policy.html): Learn how to create an autodelete policy for volume snapshots in ONTAP using the volume snapshot autodelete modify CLI command to manage storage space efficiently.

### [Protecting data with Autonomous Ransomware Protection](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/ARP.html)

Learn about Autonomous Ransomware Protection (ARP) for FSx for ONTAP.

- [Enabling ARP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/enable-ARP.html): Learn how to enable and verify Autonomous Ransomware Protection (ARP) on FSx for ONTAP volumes using the ONTAP CLI.
- [Responding to ARP alerts](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/respond-ARP.html): Learn how to use the ONTAP CLI to view Autonomous Ransomware Protection (ARP) alerts, generate attack reports, and take action on potential ransomware threats in your FSx for ONTAP file systems.
- [Understanding EMS alerts for ARP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/EMS-ARP.html): Monitor FSx for ONTAP Events Management System (EMS) alerts related to Autonomous Ransomware Protection (ARP).

### [Protecting data with SnapLock](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock.html)

Introduces the SnapLock feature.

- [How SnapLock works](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html): Explains central concepts of the SnapLock feature including retention modes, the SnapLock administrator, the audit log volume, and which protocols you can use to access your data.
- [Understanding SnapLock Compliance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-compliance.html): Explains the SnapLock Compliance retention mode and how to set it up for a volume.
- [Understanding SnapLock Enterprise](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html): Explains the SnapLock Enterprise retention mode and how to set it up for a volume.
- [Understanding the SnapLock retention period](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-retention.html): Introduces the retention period concept and explains how to set it.
- [Committing files to WORM](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html): Introduces write once, read many (WORM) and explains how to commit files to it.

### [Replicating your data with FlexCache](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-flexcache.html)

Learn about using FlexCache on your FSx for ONTAP file system to bring your datasets closer to clients requiring access in a space efficient, cost efficient, and performant manner.

- [Creating a FlexCache](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/create-flexcache.html): Learn how to create a FlexCache with Amazon FSx for NetApp ONTAP.
- [Using SnapMirror for scheduled replication](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/scheduled-replication.html): Learn how to use NetApp SnapMirror for periodic replication of FSx for ONTAP file systems, including in-Region and cross-Region deployments, and explore configuration options using various AWS and NetApp tools.


## [Monitoring file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitoring_overview.html)

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitoring-cloudwatch.html)

How to use Amazon CloudWatch to monitor your Amazon FSx for NetApp ONTAP file system.

- [Accessing CloudWatch metrics](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/accessingmetrics.html): How to view Amazon CloudWatch metrics for Amazon FSx.

### [Monitoring in the Amazon FSx console](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitor-throughput-cloudwatch.html)

Learn how to monitor FSx for ONTAP file systems and volumes using CloudWatch metrics.

- [Performance warnings and recommendations](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/performance-insights-FSxN.html): Explains warnings that you might see from CloudWatch metrics and recommendations to resolve them.
- [Creating alarms](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating_alarms.html): How to create Amazon CloudWatch alarms to monitor Amazon FSx file systems.
- [File system metrics](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/file-system-metrics.html): Detailed information about Amazon CloudWatch file system metrics for Amazon FSx for NetApp ONTAP.
- [Second-generation file system metrics](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/so-file-system-metrics.html): Learn about the available CloudWatch metrics for FSx for ONTAP second-generation file systems, including network I/O, file server, disk I/O, and detailed file system metrics.
- [Volume metrics](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-metrics.html): Detailed information about Amazon CloudWatch volume metrics for Amazon FSx for NetApp ONTAP.
- [Monitoring EMS events](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/ems-events.html): Lists the supported NetApp ONTAP EMS events and how to view them.
- [Monitoring with Data Infrastructure Insights](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitoring-cloud-insights.html): How to use NetApp Data Infrastructure Insights to monitor your Amazon FSx for NetApp ONTAP file system.
- [Monitoring with Harvest and Grafana](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/monitoring-harvest-grafana.html): Learn how to set up and configure NetApp Harvest and Grafana to monitor performance and capacity metrics for your FSx for ONTAP file systems using an CloudFormation template.
- [Monitoring with AWS CloudTrail](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/logging-using-cloudtrail-win.html): Learn how FSx for ONTAP integrates with AWS CloudTrail to log and monitor API activity, enabling you to track requests, analyze events, and maintain security compliance for your file systems.


## [Working with Active Directory](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/ad-integration-ontap.html)

- [Self-managed Active Directory prerequisites](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/self-manage-prereqs.html): Learn about the network and Active Directory service account requirements for joining an FSx for ONTAP storage virtual machine (SVM) to your Active Directory.
- [Self-managed Active Directory best practices](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/self-managed-AD-best-practices.html): Learn best practices to follow when joining your FSx for ONTAP SVMs to an on-premises or other self-managed Microsoft Active Directory domain.
- [How joining SVMs to Active Directory works](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/self-managed-AD-join.html): Learn how to join your FSx for ONTAP storage virtual machines (SVMs) to a self-managed Microsoft Active Directory.

### [Managing SVM Active Directory configurations](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/manage-svm-ad-config.html)

Learn how to manage Active Directory configurations for FSx for ONTAP SVMs using the AWS Management Console, AWS CLI, and API.

- [Joining SVMs to Active Directory](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/join-svm-to-ad.html): Create and manage storage virtual machines (SVMs) in FSx for ONTAP using the AWS CLI.
- [Updating Active Directory configurations](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/update-svm-ad-config.html): Learn how to update the Active Directory configuration for an existing FSx for ONTAP storage virtual machine (SVM) using the AWS Management Console or AWS CLI.
- [Updating Active Directory configurations with the NetApp CLI](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/manage-svm-ad-config-ontap-cli.html): Learn how to join, modify, and unjoin SVMs to Active Directory using the NetApp ONTAP CLI for FSx for ONTAP file systems.


## [Migrating to Amazon FSx](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/migrating-fsx-ontap.html)

- [Migrating using SnapMirror](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/migrating-fsx-ontap-snapmirror.html): Learn how to migrate NetApp ONTAP file systems to FSx for ONTAP using NetApp SnapMirror.
- [Migrating files with AWS DataSync](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/migrate-files-to-fsx-datasync.html): Learn how to use AWS DataSync to transfer data between FSx for ONTAP and other storage systems, including prerequisites and basic steps for migrating files efficiently and securely.


## [Security](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security.html)

### [Data protection](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon FSx.

- [Encryption at rest](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/encryption-at-rest.html): Discover how encryption of data at rest works for Amazon FSx for NetApp ONTAP.

### [Encrypting data in transit](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/encryption-in-transit.html)

Learn about the options available for encrypting data in-transit between an FSx for ONTAP file system and connected clients.

- [Enabling SMB encryption of data in transit](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/enable-smb-encryption.html): Learn how to enable and manage SMB encryption for secure data transfers on FSx for ONTAP file systems using the ONTAP CLI.
- [Configuring IPsec using PSK authentication](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/config-ipsec-psk-auth.html): Learn how to configure IPsec encryption for FSx for ONTAP using pre-shared key (PSK) authentication, including steps for file system setup, client configuration, and multi-client access.
- [Configuring IPsec using certificate authentication](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/config-ipsec-ca-auth.html): Learn how to configure IPsec encryption using certificate authentication on FSx for ONTAP file systems and connected clients.

### [Identity and access management](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html)

How to authenticate requests and manage access your Amazon FSx resources.

- [FSx for ONTAP and IAM](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security_iam_service-with-iam.html): Learn about IAM features available for Amazon FSx, including identity-based policies, policy actions, resources, and condition keys.
- [Identity-based policy examples](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security_iam_id-based-policy-examples.html): Learn how to manage permissions for Amazon FSx resources using IAM policies.
- [Troubleshooting IAM](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security_iam_troubleshoot.html): Learn how to troubleshoot common authorization issues when using Amazon FSx with IAM, including unauthorized actions, iam:PassRole errors, and granting access to external users.
- [Using service-linked roles](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-service-linked-roles.html): How to use service-linked roles to give Amazon FSx access to resources in your AWS account.
- [Using tags with Amazon FSx](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-tags-fsx.html): Create AWS Identity and Access Management (IAM) policies to allow users to tag Amazon FSx resources on creation.
- [AWS managed policies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon FSx and recent changes to those policies.
- [File System Access Control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/limit-access-security-groups.html): Learn how to configure network access and security for FSx for ONTAP file systems using VPC security groups and inbound/outbound rules.
- [Compliance Validation](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/fsx-ontap-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Interface VPC endpoints](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/fsx-vpc-endpoints.html): You can use interface VPC endpoints (AWS PrivateLink) to access the Amazon FSx API from your VPC without sending traffic over the internet.
- [Resilience](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon FSx for NetApp ONTAP features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/infrastructure-security.html): Learn how Amazon FSx for NetApp ONTAP isolates service traffic.
- [Using antivirus software](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-vscan.html): Learn about using antivirus solutions with your FSx for ONTAP file systems.

### [ONTAP roles and users](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/roles-and-users.html)

Learn about ONTAP role-based access control (RBAC) in FSx for ONTAP, including file system and SVM administrator roles, creating users and custom roles, and configuring Active Directory authentication.

- [Creating ONTAP users](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/create-new-ontap-users.html): Learn how to create file system and SVM administrative users for your FSx for ONTAP file system.
- [Creating SVM roles](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-new-svm-roles.html): Learn how to create SVM roles so that you can customize the amount of administrative access for SVM users with FSx for ONTAP file systems.
- [Configuring Active Directory authentication for ONTAP users](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/set-up-ad-auth.html): Learn how to configure and use Active Directory authentication for the administrative users on your FSx for ONTAP file system.
- [Configuring public key authentication](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/public-key-auth.html): Learn how to configure and use SSH public key authentication for the administrative users on your FSx for ONTAP file system.
- [Updating password requirements](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/update-password-requirements.html): Learn how to change the password requirements for FSx for ONTAP file system and SVM administrator roles to meet your security requirements.
- [Updating the fsxadmin account password fails](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/updating-admin-password.html): Learn how to view password requirements for the fsxadmin user in FSx for ONTAP using the ONTAP CLI.


## [Troubleshooting](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/troubleshooting.html)

- [Misconfigured file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/file-system-in-misconfigured-state.html): Learn how to troubleshoot and resolve MISCONFIGURED states in FSx for ONTAP file systems, including issues with Multi-AZ VPC sharing and SSD storage tier capacity.
- [You can't access your file system](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/unable-to-access.html): There are a number of potential causes for a file system to become inaccessible, each with their own resolution, as follows.
- [Misconfigured SVM](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/misconfigured-svm.html): Learn how to troubleshoot a misconfigured FSx for ONTAP storage virtual machine (SVM).
- [Troubleshooting SSD decrease issues](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/ssd-decrease-troubleshooting.html): Learn how to troubleshoot issues that might occur during SSD capacity decrease operations.
- [Can't join SVM to Active Directory](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/cannot-join-svm-to-ad.html): Tips to help resolve issues that arise when trying to join a storage virtual machine (SVM) to an Active Directory.
- [Can't delete SVM or volume](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/cannot-delete-svm.html): Fix a problem where you can't delete a storage virtual machine (SVM) or a volume.
- [Misconfigured volume](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/misconfigured-volume.html): Learn how to troubleshoot FSx for ONTAP volumes that are in a misconfigured state.
- [Volume has insufficient storage](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/low-volume-capacity.html): Fix the problem where an ONTAP volume has run out of storage capacity.
- [Failed volume backups](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/backups-failing.html): Troubleshoot and resolve automatic daily backup failures for FSx for ONTAP volumes due to insufficient storage capacity, and learn mitigation strategies.
- [Recovering deleted volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/recovering-deleted-volumes.html): Learn about the ONTAP recovery queue.
- [Troubleshooting network issues](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/network-issues.html): Diagnose and fix networking problems.
- [I/O errors and NFS lock reclaim failures](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/nfs-failover-issues.html): Resolve I/O errors and NFS lock reclaim failures during FSx for ONTAP failover events.
