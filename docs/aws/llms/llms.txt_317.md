# Source: https://docs.aws.amazon.com/ebs/latest/userguide/llms.txt

# Amazon EBS User Guide

- [What is Amazon EBS?](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)
- [Set up for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/setting-up.html)
- [Quotas](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-resource-quotas.html)
- [Document history](https://docs.aws.amazon.com/ebs/latest/userguide/doc-history.html)

## [EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html)

- [Features and benefits](https://docs.aws.amazon.com/ebs/latest/userguide/EBSFeatures.html): Understand the benefits and features of Amazon EBS volumes.

### [EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

Learn about the different volume types offered by Amazon EBS.

- [General Purpose SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html): Learn about the performance characteristics of Amazon EBS General Purpose SSD (gp2 and gp3) volumes.
- [Provisioned IOPS SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html): Learn about the performance characteristics of Amazon EBS Provisioned IOPS SSD (io1 and io2) volumes.
- [Throughput Optimized HDD and Cold HDD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/hdd-vols.html): Learn about the performance characteristics of Amazon EBS Throughput Optimized HDD (st1) and Cold HDD (sc1) volumes.
- [EBS volume constraints](https://docs.aws.amazon.com/ebs/latest/userguide/volume_constraints.html): Learn about the Amazon EBS volume configuration constraints and service limitations.

### [EBS volumes and NVMe](https://docs.aws.amazon.com/ebs/latest/userguide/nvme-ebs-volumes.html)

Learn how to install and use the NVMe drivers with Amazon EBS volumes.

- [Map volumes to device names](https://docs.aws.amazon.com/ebs/latest/userguide/identify-nvme-ebs-device.html): Map Amazon EBS volumes to the NVMe device names assigned by the operating system.
- [I/O operation timeout](https://docs.aws.amazon.com/ebs/latest/userguide/timeout-nvme-ebs-volumes.html): Modify the timeout period for I/O operations submitted to NVMe devices.
- [Abort command](https://docs.aws.amazon.com/ebs/latest/userguide/abort-command.html): Learn how Amazon EBS volumes support the NVMe Abort command.

### [Volume lifecycle](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-lifecycle.html)

Understand how Amazon EBS volumes can be used throughout their lifecycle.

- [Create a volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html): Create an Amazon EBS volume that you can then attach to any Amazon EC2 instance within the same Availability Zone.
- [Copy a volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copying-volume.html): Create an instant point-in-time copy of an Amazon EBS volume within the same Availability Zone.
- [Attach a volume to an instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-attaching-volume.html): Attach an Amazon EBS volume that you have created to an Amazon EC2 instance in the same Availability Zone.

### [Attach a volume to multiple instances](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html)

Attach an Amazon EBS volume to multiple Amazon EC2 instances in the same Availability Zone using EBS Multi-Attach.

- [Performance for Multi-Attach volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-multi-attach-perf.html): Understand the performance characteristics and limitations of Multi-Attach enabled Amazon EBS volumes.
- [Enable Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/working-with-multi-attach.html): Enable Multi-Attach for an Amazon EBS Provisioned IOPS SSD volume.
- [Disable Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/disable-multi-attach.html): Disable Multi-Attach for an Amazon EBS Provisioned IOPS SSD volume.
- [NVMe reservations](https://docs.aws.amazon.com/ebs/latest/userguide/nvme-reservations.html): Use NVMe reservations to create and manage reservations that coordinate access from multiple Amazon EC2 instances to a shared Amazon EBS volume.
- [Make a volume available for use](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-using-volumes.html): Make an Amazon EBS volume available for use with an Amazon EC2 instance.
- [View volume details](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-describing-volumes.html): View the information about an Amazon EBS volume, including its free space, status, and Amazon EC2 instance attachment details.

### [Modify a volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modify-volume.html)

Learn how to modify the size, IOPS performance, or volume type of an Amazon EBS volume.

- [Requirements](https://docs.aws.amazon.com/ebs/latest/userguide/modify-volume-requirements.html): Understand the requirements and limitations when modifying Amazon EBS volumes.
- [Request volume modifications](https://docs.aws.amazon.com/ebs/latest/userguide/requesting-ebs-volume-modifications.html): Modify the size, performance, and type of an Amazon EBS volume.
- [Monitor modifications](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-modifications.html): Learn about the methods available to monitor the progress of Amazon EBS volume modifications.
- [Extend the file system](https://docs.aws.amazon.com/ebs/latest/userguide/recognize-expanded-volume-linux.html): Learn how to extend the partition and file system to fill available space on expanded Amazon EBS volumes.
- [Detach a volume from an instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-detaching-volume.html): Detach an Amazon EBS volume from an Amazon EC2 instance explicitly or by terminating the instance.
- [Delete a volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-volume.html): Delete an Amazon EBS volume that you no longer need.
- [Replace a volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-restoring-volume.html): Replace an Amazon EBS volume with data from a previously created Amazon EBS snapshot.

### [Status checks](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-checks.html)

Learn about the Amazon EBS volume status checks.

- [Volume events](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-vol-events.html): Understand the events that are generated when an Amazon EBS volume fails a status check.
- [Work with an impaired volume](https://docs.aws.amazon.com/ebs/latest/userguide/work_volumes_impaired.html): Understand what to do when an Amazon EBS volume is impaired because of potentially inconsistent data.
- [Auto-enable I/O](https://docs.aws.amazon.com/ebs/latest/userguide/volumeIO.html): Use Auto-Enabled IO to automatically re-enable I/O for impaired Amazon EBS volumes.

### [Fault testing](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fis.html)

Use AWS FIS to temporarily stop I/O between an Amazon EBS volume and its attached Amazon EC2 instances to test how your workloads handle I/O interruptions.

- [Pause I/O fault injection](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fis-pause-io.html): Learn how to temporarily pause I/O between an Amazon EBS volume and the instances to which it is attached to test your workloads.
- [Latency injection](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fis-latency-injection.html): Learn how to temporarily inject latency into your volumes to test how your workload responds to storage latency.


## [EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)

- [How snapshots work](https://docs.aws.amazon.com/ebs/latest/userguide/how_snapshots_work.html): Understand how Amazon EBS snapshots back up the data on Amazon EBS volumes.

### [Snapshot lifecycle](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lifecycle.html)

Understand how Amazon EBS snapshots can be used throughout their lifecycle.

### [Create snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-snapshot.html)

Create Amazon EBS snapshots to create point-in-time backups of your EBS volumes and Amazon EC2 instances.

- [Create snapshot of a volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-create-snapshot.html): Create an Amazon EBS snapshot from an individual EBS volume.
- [Create multi-volume snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-create-snapshots.html): Create multi-volume Amazon EBS snapshots from the volumes attached to an Amazon EC2 instance.
- [View snapshot information](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-describing-snapshots.html): View detailed information about Amazon EBS snapshots.

### [Copy a snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html)

Copy snapshots across AWS Regions for geographical expansion, data center migration, and disaster recovery.

- [Time-based copies](https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html): Time-based copies can help you meet compliance or business requirements for data replication by ensuring that your EBS snapshots and EBS-backed AMIs are copied, within and across AWS Regions, in a specified timeframe.

### [Share a snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modifying-snapshot-permissions.html)

Share your Amazon EBS snapshots privately with specific AWS accounts or, publicly with all AWS accounts.

- [Share a KMS key](https://docs.aws.amazon.com/ebs/latest/userguide/share-kms-key.html): Share the AWS KMS customer managed key used to encrypt a shared Amazon EBS snapshot.
- [Use shared snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/view-shared-snapshot.html): Find and use Amazon EBS snapshots that are shared with your AWS account.

### [Archive snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive.html)

Amazon EBS Snapshots Archive is a storage tier that you can use for low-cost, long-term storage of your rarely-accessed snapshots that do not need frequent or fast retrieval.

- [Considerations and limitations](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive-considerations.html): Understand the considerations and limitations for archiving Amazon EBS snapshots.
- [Pricing and billing](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive-pricing.html): Understand how Amazon EBS snapshots are billed when they are archived, and when they are retrieved from the archive storage tier.
- [Guidelines and best practices](https://docs.aws.amazon.com/ebs/latest/userguide/archiving-guidelines.html): Understand the guidelines and best practices for archiving Amazon EBS snapshots.
- [Required permissions](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archiving-iam.html): Learn about the IAM permissions required for Amazon EBS snapshot archiving.
- [Archive a snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/archive-snapshot.html): Archive an Amazon EBS snapshot that you own.
- [Restore an archived snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/restore-archived-snapshot.html): Restore an archived Amazon EBS snapshot temporarily or permanently so that it can be used.
- [Modify the restore period](https://docs.aws.amazon.com/ebs/latest/userguide/modify-temp-restore-period.html): Modify the period for which a temporarily restored Amazon EBS snapshot remains in the standard storage tier.
- [View archived snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/view-archived-snapshot.html): View storage tier information for Amazon EBS snapshots.
- [Monitor snapshot archiving](https://docs.aws.amazon.com/ebs/latest/userguide/monitor-snapshot-archiving.html): Monitor events related to Amazon EBS snapshot archiving using Amazon CloudWatch Events.
- [Delete a snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-snapshot.html): Delete an Amazon EBS snapshot when it is no longer needed.

### [Fast snapshot restore](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fast-snapshot-restore.html)

Amazon EBS fast snapshot restore (FSR) enables you to create a Amazon EBS volume from an EBS snapshot that is fully initialized after creation.

- [Volume creation credits](https://docs.aws.amazon.com/ebs/latest/userguide/volume-creation-credits.html): Understand how Amazon EBS fast snapshot restore volume creation credits are earned and used.
- [Configure fast snapshot restore](https://docs.aws.amazon.com/ebs/latest/userguide/manage-fsr-enable.html): Enable or disable fast snapshot restore for Amazon EBS snapshots that you own and for snapshots that are shared with you.
- [Check fast snapshot restore state](https://docs.aws.amazon.com/ebs/latest/userguide/view-fsr-enabled-snapshots.html): Check whether fast snapshot restore is enabled or disabled for an Amazon EBS snapshot.
- [View volumes restored using fast snapshot restore](https://docs.aws.amazon.com/ebs/latest/userguide/view-fast-restored-volumes.html): Find Amazon EBS volumes that were created from Amazon EBS snapshots that were enabled for fast snapshot restore.

### [Snapshot lock](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lock.html)

Use Amazon EBS snapshot lock to protect your snapshots against accidental or malicious deletions.

- [Concepts](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lock-concepts.html): Understand the key concepts related to Amazon EBS snapshot locks.
- [Considerations](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lock-considerations.html): Understand the key considerations for using Amazon EBS snapshot lock.
- [Control access](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lock-iam.html): Understand the IAM permissions that are required to work with Amazon EBS snapshot lock.
- [Lock a snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/lock-snapshot.html): Lock an Amazon EBS snapshot to prevent it from being deleted.
- [Unlock a snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/unlock-snapshot.html): Unlock an Amazon EBS snapshot so that it can be deleted.
- [Update snapshot lock settings](https://docs.aws.amazon.com/ebs/latest/userguide/update-snapshot-lock.html): Change the lock settings for a locked Amazon EBS snapshot.
- [Monitor snapshot lock](https://docs.aws.amazon.com/ebs/latest/userguide/monitor-snapshot-lock.html): Monitor actions related to Amazon EBS snapshot lock using AWS CloudTrail and Amazon EventBridge.

### [Block public access for snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots.html)

Block public access for snapshots prevents users from publicly sharing your Amazon EBS snapshots.

- [IAM permissions](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-perms.html): Understand the IAM permissions required to work with block public access for Amazon EBS snapshots.
- [Configure block public access](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-enable.html): Enable block public access for Amazon EBS snapshots to prevent public sharing.
- [View block public access setting](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-view.html): Check whether block public access for Amazon EBS snapshots is enabled for an AWS account and Region.
- [Disable block public access](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-disable.html): Disable block public access for Amazon EBS snapshots to allow public sharing.
- [Monitor block public access](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-events.html): Monitor actions related to block public access for Amazon EBS snapshots using Amazon EventBridge events.
- [Local snapshots on Outposts](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html): Create and work with Amazon EBS snapshots locally on AWS Outposts.
- [Local snapshots in Local Zones](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-localzones.html): Create and work with Amazon EBS snapshots locally in AWS Local Zones.


## [EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html)

- [How EBS encryption works](https://docs.aws.amazon.com/ebs/latest/userguide/how-ebs-encryption-works.html): Understand how Amazon EBS works to encrypt EBS volumes and snapshots.
- [Requirements](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html): Understand the requirements for Amazon EBS encryption.
- [Enable encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html): Enable or disable Amazon EBS encryption by default for EBS resources in a specific Region.
- [Rotate KMS keys](https://docs.aws.amazon.com/ebs/latest/userguide/kms-key-rotation.html): Understand the best practices for rotating the AWS KMS keys used for Amazon EBS encryption.
- [Examples](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-examples.html): Learn about the possible encryption outcome for Amazon EBS resource creation and copy operations.


## [EBS performance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-performance.html)

- [EBS optimization](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-optimization.html): Use Amazon EBS-optimized Amazon EC2 instance types to get the best performance from your Amazon EBS volumes.

### [Initialize volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html)

When you create an Amazon EBS volume, either from an EBS snapshot or from another EBS volume (volume copy), the data blocks must be written to the volume before you can access them.

- [Monitor volume initialization](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-initialize-monitor.html): When you create a volume, either from a snapshot or from another volume (volume copy), you can monitor the status of the volume initialization to determine whether the initialization process is complete.
- [Configurable instance bandwidth weighting](https://docs.aws.amazon.com/ebs/latest/userguide/instance-bandwidth-configuration.html): Instance bandwidth configuration (IBC) is a feature that enables you to adjust the allocation of network bandwidth between Amazon EBS and VPC networking for an Amazon EC2 instance.
- [I/O characteristics and monitoring](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-io-characteristics.html): Understand how to optimize I/O operations to improve Amazon EBS volume performance.
- [RAID configuration](https://docs.aws.amazon.com/ebs/latest/userguide/raid-config.html): Use RAID 0 arrays to achieve a higher level of performance than you can provision on a single Amazon EBS volume.
- [Benchmark EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/benchmark_procedures.html): Test the performance of Amazon EBS volumes by simulating workloads with benchmark testing.


## [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)

- [How it works](https://docs.aws.amazon.com/ebs/latest/userguide/dlm-elements.html): Understand the key elements of Amazon Data Lifecycle Manager.
- [Default vs custom policies](https://docs.aws.amazon.com/ebs/latest/userguide/policy-differences.html): Understand the differences between Amazon Data Lifecycle Manager default and custom policies.

### [Create default policies](https://docs.aws.amazon.com/ebs/latest/userguide/default-policies.html)

Create Amazon Data Lifecycle Manager default policies to create periodic backups of your Amazon EC2 instances and Amazon EBS volumes.

- [Enable default policies across accounts and Regions](https://docs.aws.amazon.com/ebs/latest/userguide/dlm-stacksets.html): Enable Amazon Data Lifecycle Manager default policies across accounts and Regions using CloudFormation StackSets.

### [Create custom policy for snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-ami-policy.html)

Create an Amazon Data Lifecycle Manager custom policy for Amazon EBS snapshots to automate Amazon EBS snapshot lifecycles.

- [Automate application-consistent snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/automate-app-consistent-backups.html): Use Amazon Data Lifecycle Manager pre and post scripts to automate the creation of application-consistent Amazon EBS snapshots.
- [Other use cases for pre and post scripts](https://docs.aws.amazon.com/ebs/latest/userguide/script-other-use-cases.html): Understand the other use cases for Amazon Data Lifecycle Manager pre and post scripts.
- [How pre and post scripts work](https://docs.aws.amazon.com/ebs/latest/userguide/script-flow.html): Understand how Amazon Data Lifecycle Manager pre and post scripts work.
- [Identify snapshots created with pre and post scripts](https://docs.aws.amazon.com/ebs/latest/userguide/dlm-script-tags.html): Understand how to identify snapshots created with Amazon Data Lifecycle Manager pre and post scripts.
- [Monitor pre and post scripts](https://docs.aws.amazon.com/ebs/latest/userguide/dlm-script-monitoring.html): Monitor Amazon Data Lifecycle Manager pre and post script execution using Amazon CloudWatch metrics and Amazon EventBridge events.
- [Create custom policy for AMIs](https://docs.aws.amazon.com/ebs/latest/userguide/ami-policy.html): Create an Amazon Data Lifecycle Manager custom policy for EBS-backed AMIs to automate EBS-backed AMI lifecycles.
- [Automate cross-account snapshot copies](https://docs.aws.amazon.com/ebs/latest/userguide/event-policy.html): Create an Amazon Data Lifecycle Manager cross-account copy event policy to automatically copy snapshots that are shared with your account.
- [Modify policies](https://docs.aws.amazon.com/ebs/latest/userguide/modify.html): Modify an Amazon Data Lifecycle Manager custom or default policy.
- [Delete policies](https://docs.aws.amazon.com/ebs/latest/userguide/delete.html): Delete an Amazon Data Lifecycle Manager custom or default policy.

### [Control access](https://docs.aws.amazon.com/ebs/latest/userguide/dlm-prerequisites.html)

Control access to Amazon Data Lifecycle Manager resources using IAM.

- [AWS managed policies](https://docs.aws.amazon.com/ebs/latest/userguide/managed-policies.html): Learn about the AWS managed policies for Amazon Data Lifecycle Manager, and about changes to those policies.
- [IAM service roles](https://docs.aws.amazon.com/ebs/latest/userguide/service-role.html): Learn how to grant Amazon Data Lifecycle Manager access to resources in your account using IAM service roles.

### [Monitor policies](https://docs.aws.amazon.com/ebs/latest/userguide/dlm-monitor-lifecycle.html)

Monitor Amazon Data Lifecycle Manager policies to maintain reliability, availability, and performance.

- [Monitor policies using EventBridge](https://docs.aws.amazon.com/ebs/latest/userguide/monitor-cloudwatch-events.html): Monitor Amazon Data Lifecycle Manager policies using Amazon EventBridge events.
- [Monitor policies using CloudWatch](https://docs.aws.amazon.com/ebs/latest/userguide/monitor-dlm-cw-metrics.html): Learn about the metrics that Amazon Data Lifecycle Manager sends to Amazon CloudWatch.
- [Service endpoints](https://docs.aws.amazon.com/ebs/latest/userguide/dlm-service-endpoints.html): Understand how to use the IPv4, dual-stack, and FIPS service endpoints supported by Amazon Data Lifecycle Manager.
- [Interface VPC endpoints](https://docs.aws.amazon.com/ebs/latest/userguide/dlm-vpc-endpoints.html): Use AWS PrivateLink to create a private connection between your VPC and Amazon EBS.
- [Troubleshoot](https://docs.aws.amazon.com/ebs/latest/userguide/dlm-troubleshooting.html): Troubleshoot common issues with Amazon Data Lifecycle Manager policies.


## [Amazon EBS direct APIs](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-accessing-snapshot.html)

- [Pricing](https://docs.aws.amazon.com/ebs/latest/userguide/ebsapi-pricing.html): Understand how billing and pricing works for EBS direct APIs.
- [Concepts](https://docs.aws.amazon.com/ebs/latest/userguide/ebsapi-elements.html): Understand the key concepts for using EBS direct APIs.
- [Control access](https://docs.aws.amazon.com/ebs/latest/userguide/ebsapi-permissions.html): Control access to EBS direct APIs using IAM policies and permissions.
- [Read snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/readsnapshots.html): List Amazon EBS snapshot blocks and read snapshot block data using the EBS direct APIs.
- [Write snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/writesnapshots.html): Write data to a new Amazon EBS snapshot using EBS direct APIs.
- [Encryption outcomes](https://docs.aws.amazon.com/ebs/latest/userguide/ebsapis-using-encryption.html): Understand how Amazon EBS snapshots are encrypted when using EBS direct APIs.
- [Validate snapshot data](https://docs.aws.amazon.com/ebs/latest/userguide/ebsapis-using-checksums.html): Learn how to use checksums with EBS direct APIs to validate the integrity of snapshot data.
- [Ensure idempotency](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-direct-api-idempotency.html): Learn how to use idempotency to ensure that StartSnapshot API requests complete only once.
- [Error retries](https://docs.aws.amazon.com/ebs/latest/userguide/error-retries.html): Understand how to handle error retries for EBS direct APIs.
- [Optimize performance](https://docs.aws.amazon.com/ebs/latest/userguide/ebsapi-performance.html): Understand how to optimize performance when using EBS direct APIs.
- [Service endpoints](https://docs.aws.amazon.com/ebs/latest/userguide/using-endpoints.html): Understand how to use the IPv4, dual-stack, and FIPS service endpoints supported by EBS direct APIs.
- [SDK code examples](https://docs.aws.amazon.com/ebs/latest/userguide/sdk.html): Learn how to work with EBS direct APIs using the AWS SDKs.
- [Interface VPC endpoints](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-apis-vpc-endpoints.html): Use AWS PrivateLink to create a private connection between your VPC and EBS direct APIs.
- [CloudTrail logs](https://docs.aws.amazon.com/ebs/latest/userguide/logging-ebs-apis-using-cloudtrail.html): Capture detailed information about the API calls made to EBS direct APIs using AWS CloudTrail.
- [FAQs](https://docs.aws.amazon.com/ebs/latest/userguide/ebsapi-faq.html): View some frequently asked questions about EBS direct APIs.


## [Recycle Bin](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin.html)

- [How does it work?](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-concepts.html): To enable and use Recycle Bin, you must create retention rules in the AWS Regions in which you want to protect your resources.
- [Considerations](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-factors.html): Learn how to effectively use Recycle Bin to protect your snapshots and EBS-backed AMIs against accidental deletions.
- [Control access](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-perms.html): Control access to Recycle Bin using AWS Identity and Access Management.
- [Create retention rule](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-create-rule.html): Create a Recycle Bin retention rule to protect resources.
- [Update retention rule](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-update-rule.html): Update an existing Recycle Bin retention rule.
- [Lock retention rule](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-lock.html): Lock a Recycle Bin retention rule to protect it against malicious or unintentional updates and deletions.
- [Unlock retention rule](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-unlock.html): Unlock a Recycle Bin retention rule to allow it to be updated or deleted.
- [Tag retention rules](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-tag-resource.html): Assign custom tags to Recycle Bin retention rules to help categorize and identify them.
- [Delete retention rules](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-delete-rule.html): Delete a Recycle Bin retention rule to stop it from retaining deleted EBS volumes, EBS snapshots, and EBS-backed AMIs.
- [Recover deleted snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-working-with-snaps.html): Recover accidentally deleted snapshots from the Recycle Bin.
- [Recover deleted volumes](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-working-with-volumes.html): Recover accidentally deleted volumes from the Recycle Bin.
- [Recover deleted AMIs](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-working-with-amis.html): Recover accidentally deleted AMIs from the Recycle Bin.
- [Monitor using EventBridge](https://docs.aws.amazon.com/ebs/latest/userguide/rbin-eventbridge.html): Monitor Recycle Bin with Amazon EventBridge to maintain reliability, availability, and performance.
- [Monitor using CloudTrail](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-ct.html): Monitor Recycle Bin using AWS CloudTrail to maintain reliability, availability, and performance.
- [Service endpoints](https://docs.aws.amazon.com/ebs/latest/userguide/rbin-service-endpoints.html): Understand how to use the IPv4, dual-stack, and FIPS service endpoints supported by EBS direct APIs.
- [Use interface VPC endpoints](https://docs.aws.amazon.com/ebs/latest/userguide/rbin-vpcendpoints.html): Establish a private connection between your VPC and Recycle Bin using AWS PrivateLink.


## [Security](https://docs.aws.amazon.com/ebs/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/ebs/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon EBS.

### [Identity and access management](https://docs.aws.amazon.com/ebs/latest/userguide/security-iam.html)

Learn how to control access to Amazon EBS resources using IAM.

- [How EBS works with IAM](https://docs.aws.amazon.com/ebs/latest/userguide/security_iam_service-with-iam.html): Learn about the IAM features that Amazon EBS supports.
- [Example IAM policies](https://docs.aws.amazon.com/ebs/latest/userguide/security_iam_id-based-policy-examples.html): Learn how to use IAM identity-based policies to grant users and roles access to Amazon EBS.
- [Troubleshoot](https://docs.aws.amazon.com/ebs/latest/userguide/security_iam_troubleshoot.html): Troubleshoot common authorization issues with IAM in Amazon EBS.
- [Compliance validation](https://docs.aws.amazon.com/ebs/latest/userguide/compliance-validation.html): Learn about the security and compliance programs of Amazon EBS.
- [Data resiliency](https://docs.aws.amazon.com/ebs/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and about specific Amazon EBS features for data resiliency.


## [Monitoring](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-overview.html)

- [Amazon CloudWatch](https://docs.aws.amazon.com/ebs/latest/userguide/using_cloudwatch_ebs.html): Learn about the metrics that Amazon EBS sends to Amazon CloudWatch.

### [Amazon EventBridge](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-cloud-watch-events.html)

Use EventBridge events to track changes to your Amazon EBS resources and to trigger programmatic actions in response to those events.

- [Using AWS Lambda to handle EventBridge events](https://docs.aws.amazon.com/ebs/latest/userguide/using_lambda.html): You can use Amazon EBS and Amazon EventBridge to automate your data-backup workflow.
- [EBS detailed performance statistics](https://docs.aws.amazon.com/ebs/latest/userguide/nvme-detailed-performance-stats.html): EBS detailed performance statistics provide real-time, high-resolution I/O performance statistics for Amazon EBS volumes attached to Nitro-based Amazon EC2 instances.
- [Amazon GuardDuty](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-guardduty.html): Learn how Amazon GuardDuty can be used to protect the Amazon EBS volumes attached to your Amazon EC2 instances against malware.
- [Billing and usage reports](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-billing-usage-reports.html): Learn about activity related to Amazon EBS in the AWS billing and usage reports.
- [Inventory your EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-data-inventory.html): Learn how to identify key characteristics of your Amazon EBS volumes so that you can create functionally equivalent volumes.
