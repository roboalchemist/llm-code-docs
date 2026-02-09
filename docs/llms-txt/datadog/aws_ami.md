# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_ami.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_ami{% #aws_ami %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `architecture`{% #architecture %}

**Type**: `STRING`**Provider name**: `Architecture`**Description**: The architecture of the image.

## `arn`{% #arn %}

**Type**: `STRING`

## `block_device_mappings`{% #block_device_mappings %}

**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `BlockDeviceMappings`**Description**: Any block device mapping entries.

- `device_name`**Type**: `STRING`**Provider name**: `DeviceName`**Description**: The device name (for example, `/dev/sdh` or `xvdh`).
- `ebs`**Type**: `STRUCT`**Provider name**: `Ebs`**Description**: Parameters used to automatically set up EBS volumes when the instance is launched.
  - `availability_zone`**Type**: `STRING`**Provider name**: `AvailabilityZone`**Description**: The Availability Zone where the EBS volume will be created (for example, `us-east-1a`). Either `AvailabilityZone` or `AvailabilityZoneId` can be specified, but not both. If neither is specified, Amazon EC2 automatically selects an Availability Zone within the Region. This parameter is not supported when using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html).
  - `availability_zone_id`**Type**: `STRING`**Provider name**: `AvailabilityZoneId`**Description**: The ID of the Availability Zone where the EBS volume will be created (for example, `use1-az1`). Either `AvailabilityZone` or `AvailabilityZoneId` can be specified, but not both. If neither is specified, Amazon EC2 automatically selects an Availability Zone within the Region. This parameter is not supported when using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html).
  - `delete_on_termination`**Type**: `BOOLEAN`**Provider name**: `DeleteOnTermination`**Description**: Indicates whether the EBS volume is deleted on instance termination. For more information, see [Preserving Amazon EBS volumes on instance termination](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#preserving-volumes-on-termination) in the Amazon EC2 User Guide.
  - `encrypted`**Type**: `BOOLEAN`**Provider name**: `Encrypted`**Description**: Indicates whether the encryption state of an EBS volume is changed while being restored from a backing snapshot. The effect of setting the encryption state to `true` depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html#encryption-parameters) in the Amazon EBS User Guide. In no case can you remove encryption from an encrypted volume. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. For more information, see [Supported instance types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html#ebs-encryption_supported_instances). This parameter is not returned by DescribeImageAttribute. For CreateImage and RegisterImage, whether you can include this parameter, and the allowed values differ depending on the type of block device mapping you are creating.
    - If you are creating a block device mapping for a new (empty) volume, you can include this parameter, and specify either `true` for an encrypted volume, or `false` for an unencrypted volume. If you omit this parameter, it defaults to `false` (unencrypted).
    - If you are creating a block device mapping from an existing encrypted or unencrypted snapshot, you must omit this parameter. If you include this parameter, the request will fail, regardless of the value that you specify.
    - If you are creating a block device mapping from an existing unencrypted volume, you can include this parameter, but you must specify `false`. If you specify `true`, the request will fail. In this case, we recommend that you omit the parameter.
    - If you are creating a block device mapping from an existing encrypted volume, you can include this parameter, and specify either `true` or `false`. However, if you specify `false`, the parameter is ignored and the block device mapping is always encrypted. In this case, we recommend that you omit the parameter.
  - `iops`**Type**: `INT32`**Provider name**: `Iops`**Description**: The number of I/O operations per second (IOPS). For `gp3`, `io1`, and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. The following are the supported values for each volume type:
    - `gp3`: 3,000 - 16,000 IOPS
    - `io1`: 100 - 64,000 IOPS
    - `io2`: 100 - 256,000 IOPS
For `io2` volumes, you can achieve up to 256,000 IOPS on [instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances). On other instances, you can achieve performance up to 32,000 IOPS. This parameter is required for `io1` and `io2` volumes. The default for `gp3` volumes is 3,000 IOPS.
  - `kms_key_id`**Type**: `STRING`**Provider name**: `KmsKeyId`**Description**: Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption. This parameter is only supported on `BlockDeviceMapping` objects called by [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html), [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html), and [RequestSpotInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html).
  - `outpost_arn`**Type**: `STRING`**Provider name**: `OutpostArn`**Description**: The ARN of the Outpost on which the snapshot is stored. This parameter is not supported when using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html).
  - `snapshot_id`**Type**: `STRING`**Provider name**: `SnapshotId`**Description**: The ID of the snapshot.
  - `throughput`**Type**: `INT32`**Provider name**: `Throughput`**Description**: The throughput that the volume supports, in MiB/s. This parameter is valid only for `gp3` volumes. Valid Range: Minimum value of 125. Maximum value of 1000.
  - `volume_initialization_rate`**Type**: `INT32`**Provider name**: `VolumeInitializationRate`**Description**: Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the volume. This is also known as volume initialization. Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation. This parameter is supported only for volumes created from snapshots. Omit this parameter if:
    - You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.
    - You want to create a volume that is initialized at the default rate.
For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the Amazon EC2 User Guide. This parameter is not supported when using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html). Valid range: 100 - 300 MiB/s
  - `volume_size`**Type**: `INT32`**Provider name**: `VolumeSize`**Description**: The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to or larger than the snapshot size. The following are the supported sizes for each volume type:
    - `gp2` and `gp3`: 1 - 16,384 GiB
    - `io1`: 4 - 16,384 GiB
    - `io2`: 4 - 65,536 GiB
    - `st1` and `sc1`: 125 - 16,384 GiB
    - `standard`: 1 - 1024 GiB
  - `volume_type`**Type**: `STRING`**Provider name**: `VolumeType`**Description**: The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the Amazon EBS User Guide.
- `no_device`**Type**: `STRING`**Provider name**: `NoDevice`**Description**: To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.
- `virtual_name`**Type**: `STRING`**Provider name**: `VirtualName`**Description**: The virtual device name (`ephemeral`N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1`. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume. NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect. Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.

## `boot_mode`{% #boot_mode %}

**Type**: `STRING`**Provider name**: `BootMode`**Description**: The boot mode of the image. For more information, see [Instance launch behavior with Amazon EC2 boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the Amazon EC2 User Guide.

## `creation_date`{% #creation_date %}

**Type**: `STRING`**Provider name**: `CreationDate`**Description**: The date and time the image was created.

## `deprecation_time`{% #deprecation_time %}

**Type**: `STRING`**Provider name**: `DeprecationTime`**Description**: The date and time to deprecate the AMI, in UTC, in the following format: YYYY-MM-DDTHH:MM:SSZ. If you specified a value for seconds, Amazon EC2 rounds the seconds to the nearest minute.

## `deregistration_protection`{% #deregistration_protection %}

**Type**: `STRING`**Provider name**: `DeregistrationProtection`**Description**: Indicates whether deregistration protection is enabled for the AMI.

## `description`{% #description %}

**Type**: `STRING`**Provider name**: `Description`**Description**: The description of the AMI that was provided during image creation.

## `ena_support`{% #ena_support %}

**Type**: `BOOLEAN`**Provider name**: `EnaSupport`**Description**: Specifies whether enhanced networking with ENA is enabled.

## `hypervisor`{% #hypervisor %}

**Type**: `STRING`**Provider name**: `Hypervisor`**Description**: The hypervisor type of the image. Only `xen` is supported. `ovm` is not supported.

## `image_allowed`{% #image_allowed %}

**Type**: `BOOLEAN`**Provider name**: `ImageAllowed`**Description**: If `true`, the AMI satisfies the criteria for Allowed AMIs and can be discovered and used in the account. If `false` and Allowed AMIs is set to `enabled`, the AMI can't be discovered or used in the account. If `false` and Allowed AMIs is set to `audit-mode`, the AMI can be discovered and used in the account. For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) in Amazon EC2 User Guide.

## `image_id`{% #image_id %}

**Type**: `STRING`**Provider name**: `ImageId`**Description**: The ID of the AMI.

## `image_location`{% #image_location %}

**Type**: `STRING`**Provider name**: `ImageLocation`**Description**: The location of the AMI.

## `image_owner_alias`{% #image_owner_alias %}

**Type**: `STRING`**Provider name**: `ImageOwnerAlias`**Description**: The owner alias (`amazon` | `aws-backup-vault` | `aws-marketplace`).

## `image_type`{% #image_type %}

**Type**: `STRING`**Provider name**: `ImageType`**Description**: The type of image.

## `imds_support`{% #imds_support %}

**Type**: `STRING`**Provider name**: `ImdsSupport`**Description**: If `v2.0`, it indicates that IMDSv2 is specified in the AMI. Instances launched from this AMI will have `HttpTokens` automatically set to `required` so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, `HttpPutResponseHopLimit` is set to `2`. For more information, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the Amazon EC2 User Guide.

## `kernel_id`{% #kernel_id %}

**Type**: `STRING`**Provider name**: `KernelId`**Description**: The kernel associated with the image, if any. Only applicable for machine images.

## `last_launched_time`{% #last_launched_time %}

**Type**: `STRING`**Provider name**: `LastLaunchedTime`**Description**: The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the AMI was last used to launch an EC2 instance. When the AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.`lastLaunchedTime` data is available starting April 2017.

## `launch_permissions`{% #launch_permissions %}

**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `LaunchPermissions`**Description**: The launch permissions.

- `group`**Type**: `STRING`**Provider name**: `Group`**Description**: The name of the group.
- `organization_arn`**Type**: `STRING`**Provider name**: `OrganizationArn`**Description**: The Amazon Resource Name (ARN) of an organization.
- `organizational_unit_arn`**Type**: `STRING`**Provider name**: `OrganizationalUnitArn`**Description**: The Amazon Resource Name (ARN) of an organizational unit (OU).
- `user_id`**Type**: `STRING`**Provider name**: `UserId`**Description**: The Amazon Web Services account ID. Constraints: Up to 10 000 account IDs can be specified in a single request.

## `name`{% #name %}

**Type**: `STRING`**Provider name**: `Name`**Description**: The name of the AMI that was provided during image creation.

## `owner_id`{% #owner_id %}

**Type**: `STRING`**Provider name**: `OwnerId`**Description**: The ID of the Amazon Web Services account that owns the image.

## `platform`{% #platform %}

**Type**: `STRING`**Provider name**: `Platform`**Description**: This value is set to `windows` for Windows AMIs; otherwise, it is blank.

## `platform_details`{% #platform_details %}

**Type**: `STRING`**Provider name**: `PlatformDetails`**Description**: The platform details associated with the billing code of the AMI. For more information, see [Understand AMI billing information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html) in the Amazon EC2 User Guide.

## `product_codes`{% #product_codes %}

**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `ProductCodes`**Description**: The product codes.

- `product_code_id`**Type**: `STRING`**Provider name**: `ProductCodeId`**Description**: The product code.
- `product_code_type`**Type**: `STRING`**Provider name**: `ProductCodeType`**Description**: The type of product code.

## `public`{% #public %}

**Type**: `BOOLEAN`**Provider name**: `Public`**Description**: Indicates whether the image has public launch permissions. The value is `true` if this image has public launch permissions or `false` if it has only implicit and explicit launch permissions.

## `ramdisk_id`{% #ramdisk_id %}

**Type**: `STRING`**Provider name**: `RamdiskId`**Description**: The RAM disk associated with the image, if any. Only applicable for machine images.

## `root_device_name`{% #root_device_name %}

**Type**: `STRING`**Provider name**: `RootDeviceName`**Description**: The device name of the root device volume (for example, `/dev/sda1`).

## `root_device_type`{% #root_device_type %}

**Type**: `STRING`**Provider name**: `RootDeviceType`**Description**: The type of root device used by the AMI. The AMI can use an Amazon EBS volume or an instance store volume.

## `source_image_id`{% #source_image_id %}

**Type**: `STRING`**Provider name**: `SourceImageId`**Description**: The ID of the source AMI from which the AMI was created. The ID only appears if the AMI was created using CreateImage, CopyImage, or CreateRestoreImageTask. The ID does not appear if the AMI was created using any other API. For some older AMIs, the ID might not be available. For more information, see [Identify the source AMI used to create a new Amazon EC2 AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify-source-ami-used-to-create-new-ami.html) in the Amazon EC2 User Guide.

## `source_image_region`{% #source_image_region %}

**Type**: `STRING`**Provider name**: `SourceImageRegion`**Description**: The Region of the source AMI. The Region only appears if the AMI was created using CreateImage, CopyImage, or CreateRestoreImageTask. The Region does not appear if the AMI was created using any other API. For some older AMIs, the Region might not be available. For more information, see [Identify the source AMI used to create a new Amazon EC2 AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify-source-ami-used-to-create-new-ami.html) in the Amazon EC2 User Guide.

## `source_instance_id`{% #source_instance_id %}

**Type**: `STRING`**Provider name**: `SourceInstanceId`**Description**: The ID of the instance that the AMI was created from if the AMI was created using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html). This field only appears if the AMI was created using CreateImage.

## `sriov_net_support`{% #sriov_net_support %}

**Type**: `STRING`**Provider name**: `SriovNetSupport`**Description**: Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.

## `state`{% #state %}

**Type**: `STRING`**Provider name**: `State`**Description**: The current state of the AMI. If the state is `available`, the image is successfully registered and can be used to launch an instance.

## `state_reason`{% #state_reason %}

**Type**: `STRUCT`**Provider name**: `StateReason`**Description**: The reason for the state change.

- `code`**Type**: `STRING`**Provider name**: `Code`**Description**: The reason code for the state change.
- `message`**Type**: `STRING`**Provider name**: `Message`**Description**: The message for the state change.
  - `Server.InsufficientInstanceCapacity`: There was insufficient capacity available to satisfy the launch request.
  - `Server.InternalError`: An internal error caused the instance to terminate during launch.
  - `Server.ScheduledStop`: The instance was stopped due to a scheduled retirement.
  - `Server.SpotInstanceShutdown`: The instance was stopped because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
  - `Server.SpotInstanceTermination`: The instance was terminated because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
  - `Client.InstanceInitiatedShutdown`: The instance was shut down from the operating system of the instance.
  - `Client.InstanceTerminated`: The instance was terminated or rebooted during AMI creation.
  - `Client.InternalError`: A client error caused the instance to terminate during launch.
  - `Client.InvalidSnapshot.NotFound`: The specified snapshot was not found.
  - `Client.UserInitiatedHibernate`: Hibernation was initiated on the instance.
  - `Client.UserInitiatedShutdown`: The instance was shut down using the Amazon EC2 API.
  - `Client.VolumeLimitExceeded`: The limit on the number of EBS volumes or total storage was exceeded. Decrease usage or request an increase in your account limits.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `tpm_support`{% #tpm_support %}

**Type**: `STRING`**Provider name**: `TpmSupport`**Description**: If the image is configured for NitroTPM support, the value is `v2.0`. For more information, see [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the Amazon EC2 User Guide.

## `uefi_data`{% #uefi_data %}

**Type**: `STRUCT`**Provider name**: `UefiData`**Description**: Base64 representation of the non-volatile UEFI variable store. To retrieve the UEFI data, use the [GetInstanceUefiData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceUefiData) command. You can inspect and modify the UEFI data by using the [python-uefivars tool](https://github.com/awslabs/python-uefivars) on GitHub. For more information, see [UEFI Secure Boot for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html) in the Amazon EC2 User Guide.

- `value`**Type**: `STRING`**Provider name**: `Value`**Description**: The attribute value. The value is case-sensitive.

## `usage_operation`{% #usage_operation %}

**Type**: `STRING`**Provider name**: `UsageOperation`**Description**: The operation of the Amazon EC2 instance and the billing code that is associated with the AMI. `usageOperation` corresponds to the [lineitem/Operation](https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html#Lineitem-details-O-Operation) column on your Amazon Web Services Cost and Usage Report and in the [Amazon Web Services Price List API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html). You can view these fields on the Instances or AMIs pages in the Amazon EC2 console, or in the responses that are returned by the [DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) command in the Amazon EC2 API, or the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command in the CLI.

## `virtualization_type`{% #virtualization_type %}

**Type**: `STRING`**Provider name**: `VirtualizationType`**Description**: The type of virtualization of the AMI.
