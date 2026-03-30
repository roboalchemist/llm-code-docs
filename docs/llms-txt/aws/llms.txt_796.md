# Source: https://docs.aws.amazon.com/snowball/latest/api-reference/llms.txt

# AWS Snowball Edge API Reference

> This AWS Snowball Edge API Reference guide describes the APIS and how to use them.

- [Job Management API](https://docs.aws.amazon.com/snowball/latest/api-reference/api-reference.html)
- [Common Parameters](https://docs.aws.amazon.com/snowball/latest/api-reference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/snowball/latest/api-reference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Operations.html)

### [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Operations_Amazon_Import_Export_Snowball.html)

The following actions are supported by AWS Snowball Edge:

- [CancelCluster](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CancelCluster.html)
- [CancelJob](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CancelJob.html)
- [CreateAddress](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateAddress.html)
- [CreateCluster](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateCluster.html)
- [CreateJob](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateJob.html)
- [CreateLongTermPricing](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateLongTermPricing.html)
- [CreateReturnShippingLabel](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateReturnShippingLabel.html)
- [DescribeAddress](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeAddress.html)
- [DescribeAddresses](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeAddresses.html)
- [DescribeCluster](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeCluster.html)
- [DescribeJob](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeJob.html)
- [DescribeReturnShippingLabel](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeReturnShippingLabel.html)
- [GetJobManifest](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetJobManifest.html)
- [GetJobUnlockCode](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetJobUnlockCode.html)
- [GetSnowballUsage](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetSnowballUsage.html)
- [GetSoftwareUpdates](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetSoftwareUpdates.html)
- [ListClusterJobs](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListClusterJobs.html)
- [ListClusters](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListClusters.html)
- [ListCompatibleImages](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListCompatibleImages.html)
- [ListJobs](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListJobs.html)
- [ListLongTermPricing](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListLongTermPricing.html)
- [ListPickupLocations](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListPickupLocations.html)
- [ListServiceVersions](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListServiceVersions.html)
- [UpdateCluster](https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateCluster.html)
- [UpdateJob](https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateJob.html)
- [UpdateJobShipmentState](https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateJobShipmentState.html)
- [UpdateLongTermPricing](https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateLongTermPricing.html)

### [AWS Snowball Edge Device Management](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Operations_AWS_Snow_Device_Management.html)

The following actions are supported by AWS Snowball Edge Device Management:

- [CancelTask](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_CancelTask.html): Sends a cancel request for a specified task.
- [CreateTask](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_CreateTask.html): Instructs one or more devices to start a task, such as unlocking or rebooting.
- [DescribeDevice](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DescribeDevice.html): Checks device-specific information, such as the device type, software version, IP addresses, and lock status.
- [DescribeDeviceEc2Instances](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DescribeDeviceEc2Instances.html): Checks the current state of the Amazon EC2-compatible instances.
- [DescribeExecution](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DescribeExecution.html): Checks the status of a remote task running on one or more target devices.
- [DescribeTask](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DescribeTask.html): Checks the metadata for a given task on a device.
- [ListDeviceResources](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ListDeviceResources.html): Returns a list of the AWS resources available for a device.
- [ListDevices](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ListDevices.html): Returns a list of all devices on your AWS account that have AWS Snow Device Management enabled in the AWS Region where the command is run.
- [ListExecutions](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ListExecutions.html): Returns the status of tasks for one or more target devices.
- [ListTagsForResource](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ListTagsForResource.html): Returns a list of tags for a managed device or task.
- [ListTasks](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ListTasks.html): Returns a list of tasks that can be filtered by state.
- [TagResource](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_TagResource.html): Adds or replaces tags on a device or task.
- [UntagResource](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_UntagResource.html): Removes a tag from a device or task.


## [Data Types](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Types.html)

### [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Types_Amazon_Import_Export_Snowball.html)

The following data types are supported by AWS Snowball Edge:

- [Address](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Address.html)
- [ClusterListEntry](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ClusterListEntry.html)
- [ClusterMetadata](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ClusterMetadata.html)
- [CompatibleImage](https://docs.aws.amazon.com/snowball/latest/api-reference/API_CompatibleImage.html)
- [DataTransfer](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DataTransfer.html)
- [DependentService](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DependentService.html)
- [DeviceConfiguration](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DeviceConfiguration.html): The container for SnowconeDeviceConfiguration.
- [Ec2AmiResource](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Ec2AmiResource.html)
- [EKSOnDeviceServiceConfiguration](https://docs.aws.amazon.com/snowball/latest/api-reference/API_EKSOnDeviceServiceConfiguration.html)
- [EventTriggerDefinition](https://docs.aws.amazon.com/snowball/latest/api-reference/API_EventTriggerDefinition.html)
- [INDTaxDocuments](https://docs.aws.amazon.com/snowball/latest/api-reference/API_INDTaxDocuments.html)
- [JobListEntry](https://docs.aws.amazon.com/snowball/latest/api-reference/API_JobListEntry.html)
- [JobLogs](https://docs.aws.amazon.com/snowball/latest/api-reference/API_JobLogs.html)
- [JobMetadata](https://docs.aws.amazon.com/snowball/latest/api-reference/API_JobMetadata.html)
- [JobResource](https://docs.aws.amazon.com/snowball/latest/api-reference/API_JobResource.html)
- [KeyRange](https://docs.aws.amazon.com/snowball/latest/api-reference/API_KeyRange.html)
- [LambdaResource](https://docs.aws.amazon.com/snowball/latest/api-reference/API_LambdaResource.html)
- [LongTermPricingListEntry](https://docs.aws.amazon.com/snowball/latest/api-reference/API_LongTermPricingListEntry.html)
- [NFSOnDeviceServiceConfiguration](https://docs.aws.amazon.com/snowball/latest/api-reference/API_NFSOnDeviceServiceConfiguration.html)
- [Notification](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Notification.html)
- [OnDeviceServiceConfiguration](https://docs.aws.amazon.com/snowball/latest/api-reference/API_OnDeviceServiceConfiguration.html)
- [PickupDetails](https://docs.aws.amazon.com/snowball/latest/api-reference/API_PickupDetails.html)
- [S3OnDeviceServiceConfiguration](https://docs.aws.amazon.com/snowball/latest/api-reference/API_S3OnDeviceServiceConfiguration.html)
- [S3Resource](https://docs.aws.amazon.com/snowball/latest/api-reference/API_S3Resource.html)
- [ServiceVersion](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ServiceVersion.html)
- [Shipment](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Shipment.html)
- [ShippingDetails](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ShippingDetails.html)
- [SnowconeDeviceConfiguration](https://docs.aws.amazon.com/snowball/latest/api-reference/API_SnowconeDeviceConfiguration.html)
- [TargetOnDeviceService](https://docs.aws.amazon.com/snowball/latest/api-reference/API_TargetOnDeviceService.html)
- [TaxDocuments](https://docs.aws.amazon.com/snowball/latest/api-reference/API_TaxDocuments.html)
- [TGWOnDeviceServiceConfiguration](https://docs.aws.amazon.com/snowball/latest/api-reference/API_TGWOnDeviceServiceConfiguration.html)
- [WirelessConnection](https://docs.aws.amazon.com/snowball/latest/api-reference/API_WirelessConnection.html)

### [AWS Snowball Edge Device Management](https://docs.aws.amazon.com/snowball/latest/api-reference/API_Types_AWS_Snow_Device_Management.html)

The following data types are supported by AWS Snowball Edge Device Management:

- [Capacity](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_Capacity.html): The physical capacity of the AWS Snow Family device.
- [Command](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_Command.html): The command given to the device to execute.
- [CpuOptions](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_CpuOptions.html): The options for how a device's CPU is configured.
- [DeviceSummary](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DeviceSummary.html): Identifying information about the device.
- [EbsInstanceBlockDevice](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_EbsInstanceBlockDevice.html): Describes a parameter used to set up an Amazon Elastic Block Store (Amazon EBS) volume in a block device mapping.
- [ExecutionSummary](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ExecutionSummary.html): The summary of a task execution on a specified device.
- [Instance](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_Instance.html): The description of an instance.
- [InstanceBlockDeviceMapping](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_InstanceBlockDeviceMapping.html): The description of a block device mapping.
- [InstanceState](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_InstanceState.html): The description of the current state of an instance.
- [InstanceSummary](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_InstanceSummary.html): The details about the instance.
- [PhysicalNetworkInterface](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_PhysicalNetworkInterface.html): The details about the physical network interface for the device.
- [Reboot](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_Reboot.html): A structure used to reboot the device.
- [ResourceSummary](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ResourceSummary.html): A summary of a resource available on the device.
- [SecurityGroupIdentifier](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_SecurityGroupIdentifier.html): Information about the device's security group.
- [SoftwareInformation](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_SoftwareInformation.html): Information about the software on the device.
- [TaskSummary](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_TaskSummary.html): Information about the task assigned to one or many devices.
- [Unlock](https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_Unlock.html): A structure used to unlock a device.
