# Source: https://docs.aws.amazon.com/panorama/latest/api/llms.txt

# AWS Panorama API Reference

> Overview

- [Welcome](https://docs.aws.amazon.com/panorama/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/panorama/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/panorama/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/panorama/latest/api/API_Operations.html)

- [CreateApplicationInstance](https://docs.aws.amazon.com/panorama/latest/api/API_CreateApplicationInstance.html)
- [CreateJobForDevices](https://docs.aws.amazon.com/panorama/latest/api/API_CreateJobForDevices.html)
- [CreateNodeFromTemplateJob](https://docs.aws.amazon.com/panorama/latest/api/API_CreateNodeFromTemplateJob.html)
- [CreatePackage](https://docs.aws.amazon.com/panorama/latest/api/API_CreatePackage.html)
- [CreatePackageImportJob](https://docs.aws.amazon.com/panorama/latest/api/API_CreatePackageImportJob.html)
- [DeleteDevice](https://docs.aws.amazon.com/panorama/latest/api/API_DeleteDevice.html)
- [DeletePackage](https://docs.aws.amazon.com/panorama/latest/api/API_DeletePackage.html)
- [DeregisterPackageVersion](https://docs.aws.amazon.com/panorama/latest/api/API_DeregisterPackageVersion.html)
- [DescribeApplicationInstance](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeApplicationInstance.html)
- [DescribeApplicationInstanceDetails](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeApplicationInstanceDetails.html)
- [DescribeDevice](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeDevice.html)
- [DescribeDeviceJob](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeDeviceJob.html)
- [DescribeNode](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeNode.html)
- [DescribeNodeFromTemplateJob](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeNodeFromTemplateJob.html)
- [DescribePackage](https://docs.aws.amazon.com/panorama/latest/api/API_DescribePackage.html)
- [DescribePackageImportJob](https://docs.aws.amazon.com/panorama/latest/api/API_DescribePackageImportJob.html)
- [DescribePackageVersion](https://docs.aws.amazon.com/panorama/latest/api/API_DescribePackageVersion.html)
- [ListApplicationInstanceDependencies](https://docs.aws.amazon.com/panorama/latest/api/API_ListApplicationInstanceDependencies.html)
- [ListApplicationInstanceNodeInstances](https://docs.aws.amazon.com/panorama/latest/api/API_ListApplicationInstanceNodeInstances.html)
- [ListApplicationInstances](https://docs.aws.amazon.com/panorama/latest/api/API_ListApplicationInstances.html)
- [ListDevices](https://docs.aws.amazon.com/panorama/latest/api/API_ListDevices.html)
- [ListDevicesJobs](https://docs.aws.amazon.com/panorama/latest/api/API_ListDevicesJobs.html)
- [ListNodeFromTemplateJobs](https://docs.aws.amazon.com/panorama/latest/api/API_ListNodeFromTemplateJobs.html)
- [ListNodes](https://docs.aws.amazon.com/panorama/latest/api/API_ListNodes.html)
- [ListPackageImportJobs](https://docs.aws.amazon.com/panorama/latest/api/API_ListPackageImportJobs.html)
- [ListPackages](https://docs.aws.amazon.com/panorama/latest/api/API_ListPackages.html)
- [ListTagsForResource](https://docs.aws.amazon.com/panorama/latest/api/API_ListTagsForResource.html)
- [ProvisionDevice](https://docs.aws.amazon.com/panorama/latest/api/API_ProvisionDevice.html)
- [RegisterPackageVersion](https://docs.aws.amazon.com/panorama/latest/api/API_RegisterPackageVersion.html)
- [RemoveApplicationInstance](https://docs.aws.amazon.com/panorama/latest/api/API_RemoveApplicationInstance.html)
- [SignalApplicationInstanceNodeInstances](https://docs.aws.amazon.com/panorama/latest/api/API_SignalApplicationInstanceNodeInstances.html)
- [TagResource](https://docs.aws.amazon.com/panorama/latest/api/API_TagResource.html)
- [UntagResource](https://docs.aws.amazon.com/panorama/latest/api/API_UntagResource.html)
- [UpdateDeviceMetadata](https://docs.aws.amazon.com/panorama/latest/api/API_UpdateDeviceMetadata.html)


## [Data Types](https://docs.aws.amazon.com/panorama/latest/api/API_Types.html)

- [AlternateSoftwareMetadata](https://docs.aws.amazon.com/panorama/latest/api/API_AlternateSoftwareMetadata.html): Details about a beta appliance software update.
- [ApplicationInstance](https://docs.aws.amazon.com/panorama/latest/api/API_ApplicationInstance.html): An application instance on a device.
- [ConflictExceptionErrorArgument](https://docs.aws.amazon.com/panorama/latest/api/API_ConflictExceptionErrorArgument.html): A conflict exception error argument.
- [Device](https://docs.aws.amazon.com/panorama/latest/api/API_Device.html): A device.
- [DeviceJob](https://docs.aws.amazon.com/panorama/latest/api/API_DeviceJob.html): A job that runs on a device.
- [DeviceJobConfig](https://docs.aws.amazon.com/panorama/latest/api/API_DeviceJobConfig.html): A job's configuration.
- [EthernetPayload](https://docs.aws.amazon.com/panorama/latest/api/API_EthernetPayload.html): A device's network configuration.
- [EthernetStatus](https://docs.aws.amazon.com/panorama/latest/api/API_EthernetStatus.html): A device's Ethernet status.
- [Job](https://docs.aws.amazon.com/panorama/latest/api/API_Job.html): A job for a device.
- [JobResourceTags](https://docs.aws.amazon.com/panorama/latest/api/API_JobResourceTags.html): Tags for a job.
- [LatestDeviceJob](https://docs.aws.amazon.com/panorama/latest/api/API_LatestDeviceJob.html): Returns information about the latest device job.
- [ManifestOverridesPayload](https://docs.aws.amazon.com/panorama/latest/api/API_ManifestOverridesPayload.html): Parameter overrides for an application instance.
- [ManifestPayload](https://docs.aws.amazon.com/panorama/latest/api/API_ManifestPayload.html): A application verion's manifest file.
- [NetworkPayload](https://docs.aws.amazon.com/panorama/latest/api/API_NetworkPayload.html): The network configuration for a device.
- [NetworkStatus](https://docs.aws.amazon.com/panorama/latest/api/API_NetworkStatus.html): The network status of a device.
- [Node](https://docs.aws.amazon.com/panorama/latest/api/API_Node.html): An application node that represents a camera stream, a model, code, or output.
- [NodeFromTemplateJob](https://docs.aws.amazon.com/panorama/latest/api/API_NodeFromTemplateJob.html): A job to create a camera stream node.
- [NodeInputPort](https://docs.aws.amazon.com/panorama/latest/api/API_NodeInputPort.html): A node input port.
- [NodeInstance](https://docs.aws.amazon.com/panorama/latest/api/API_NodeInstance.html): A node instance.
- [NodeInterface](https://docs.aws.amazon.com/panorama/latest/api/API_NodeInterface.html): A node interface.
- [NodeOutputPort](https://docs.aws.amazon.com/panorama/latest/api/API_NodeOutputPort.html): A node output port.
- [NodeSignal](https://docs.aws.amazon.com/panorama/latest/api/API_NodeSignal.html): A signal to a camera node to start or stop processing video.
- [NtpPayload](https://docs.aws.amazon.com/panorama/latest/api/API_NtpPayload.html): Network time protocol (NTP) server settings.
- [NtpStatus](https://docs.aws.amazon.com/panorama/latest/api/API_NtpStatus.html): Details about an NTP server connection.
- [OTAJobConfig](https://docs.aws.amazon.com/panorama/latest/api/API_OTAJobConfig.html): An over-the-air update (OTA) job configuration.
- [OutPutS3Location](https://docs.aws.amazon.com/panorama/latest/api/API_OutPutS3Location.html): The location of an output object in Amazon S3.
- [PackageImportJob](https://docs.aws.amazon.com/panorama/latest/api/API_PackageImportJob.html): A job to import a package version.
- [PackageImportJobInputConfig](https://docs.aws.amazon.com/panorama/latest/api/API_PackageImportJobInputConfig.html): A configuration for a package import job.
- [PackageImportJobOutput](https://docs.aws.amazon.com/panorama/latest/api/API_PackageImportJobOutput.html): Results of a package import job.
- [PackageImportJobOutputConfig](https://docs.aws.amazon.com/panorama/latest/api/API_PackageImportJobOutputConfig.html): An output configuration for a package import job.
- [PackageListItem](https://docs.aws.amazon.com/panorama/latest/api/API_PackageListItem.html): A package summary.
- [PackageObject](https://docs.aws.amazon.com/panorama/latest/api/API_PackageObject.html): A package object.
- [PackageVersionInputConfig](https://docs.aws.amazon.com/panorama/latest/api/API_PackageVersionInputConfig.html): A package version input configuration.
- [PackageVersionOutputConfig](https://docs.aws.amazon.com/panorama/latest/api/API_PackageVersionOutputConfig.html): A package version output configuration.
- [ReportedRuntimeContextState](https://docs.aws.amazon.com/panorama/latest/api/API_ReportedRuntimeContextState.html): An application instance's state.
- [S3Location](https://docs.aws.amazon.com/panorama/latest/api/API_S3Location.html): A location in Amazon S3.
- [StaticIpConnectionInfo](https://docs.aws.amazon.com/panorama/latest/api/API_StaticIpConnectionInfo.html): A static IP configuration.
- [StorageLocation](https://docs.aws.amazon.com/panorama/latest/api/API_StorageLocation.html): A storage location.
- [ValidationExceptionErrorArgument](https://docs.aws.amazon.com/panorama/latest/api/API_ValidationExceptionErrorArgument.html): A validation exception error argument.
- [ValidationExceptionField](https://docs.aws.amazon.com/panorama/latest/api/API_ValidationExceptionField.html): A validation exception field.
