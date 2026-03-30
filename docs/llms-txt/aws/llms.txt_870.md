# Source: https://docs.aws.amazon.com/workspaces-instances/latest/api/llms.txt

# WorkSpaces Instances API Reference

> Amazon WorkSpaces Instances provides an API framework for managing virtual workspace environments across multiple AWS regions, enabling programmatic creation and configuration of desktop infrastructure.

- [Welcome](https://docs.aws.amazon.com/workspaces-instances/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/workspaces-instances/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/workspaces-instances/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_Operations.html)

- [AssociateVolume](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_AssociateVolume.html): Attaches a volume to a WorkSpace Instance.
- [CreateVolume](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CreateVolume.html): Creates a new volume for WorkSpace Instances.
- [CreateWorkspaceInstance](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CreateWorkspaceInstance.html): Launches a new WorkSpace Instance with specified configuration parameters, enabling programmatic workspace deployment.
- [DeleteVolume](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_DeleteVolume.html): Deletes a specified volume.
- [DeleteWorkspaceInstance](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_DeleteWorkspaceInstance.html): Deletes the specified WorkSpace
- [DisassociateVolume](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_DisassociateVolume.html): Detaches a volume from a WorkSpace Instance.
- [GetWorkspaceInstance](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_GetWorkspaceInstance.html): Retrieves detailed information about a specific WorkSpace Instance.
- [ListInstanceTypes](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ListInstanceTypes.html): Retrieves a list of instance types supported by Amazon WorkSpaces Instances, enabling precise workspace infrastructure configuration.
- [ListRegions](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ListRegions.html): Retrieves a list of AWS regions supported by Amazon WorkSpaces Instances, enabling region discovery for workspace deployments.
- [ListTagsForResource](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ListTagsForResource.html): Retrieves tags for a WorkSpace Instance.
- [ListWorkspaceInstances](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ListWorkspaceInstances.html): Retrieves a collection of WorkSpaces Instances based on specified filters.
- [TagResource](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_TagResource.html): Adds tags to a WorkSpace Instance.
- [UntagResource](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_UntagResource.html): Removes tags from a WorkSpace Instance.


## [Data Types](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_Types.html)

- [BillingConfiguration](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_BillingConfiguration.html): Defines billing configuration settings for WorkSpace Instances, containing the billing mode selection.
- [BlockDeviceMappingRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_BlockDeviceMappingRequest.html): Defines device mapping for WorkSpace Instance storage.
- [CapacityReservationSpecification](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CapacityReservationSpecification.html): Specifies capacity reservation preferences.
- [CapacityReservationTarget](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CapacityReservationTarget.html): Identifies a specific capacity reservation.
- [ConnectionTrackingSpecificationRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ConnectionTrackingSpecificationRequest.html): Defines connection tracking parameters for network interfaces.
- [CpuOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CpuOptionsRequest.html): Configures CPU-specific settings for WorkSpace Instance.
- [CreditSpecificationRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CreditSpecificationRequest.html): Defines CPU credit configuration for burstable instances.
- [EbsBlockDevice](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_EbsBlockDevice.html): Defines configuration for an Elastic Block Store volume.
- [EC2InstanceError](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_EC2InstanceError.html): Captures detailed error information for EC2 instance operations.
- [EC2ManagedInstance](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_EC2ManagedInstance.html): Represents an EC2 instance managed by WorkSpaces.
- [EnaSrdSpecificationRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_EnaSrdSpecificationRequest.html): Defines Elastic Network Adapter (ENA) Scalable Reliable Datagram (SRD) configuration.
- [EnaSrdUdpSpecificationRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_EnaSrdUdpSpecificationRequest.html): Specifies UDP configuration for ENA SRD.
- [EnclaveOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_EnclaveOptionsRequest.html): Configures AWS Nitro Enclave options for the WorkSpace Instance.
- [HibernationOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_HibernationOptionsRequest.html): Defines hibernation configuration for the WorkSpace Instance.
- [IamInstanceProfileSpecification](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_IamInstanceProfileSpecification.html): Defines IAM instance profile configuration for WorkSpace Instance.
- [InstanceConfigurationFilter](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceConfigurationFilter.html): Defines filtering criteria for WorkSpace Instance type searches.
- [InstanceIpv6Address](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceIpv6Address.html): Represents an IPv6 address configuration for a WorkSpace Instance.
- [InstanceMaintenanceOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceMaintenanceOptionsRequest.html): Configures automatic maintenance settings for WorkSpace Instance.
- [InstanceMarketOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceMarketOptionsRequest.html): Configures marketplace-specific instance deployment options.
- [InstanceMetadataOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceMetadataOptionsRequest.html): Defines instance metadata service configuration.
- [InstanceNetworkInterfaceSpecification](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceNetworkInterfaceSpecification.html): Defines network interface configuration for WorkSpace Instance.
- [InstanceNetworkPerformanceOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceNetworkPerformanceOptionsRequest.html): Configures network performance settings for WorkSpace Instance.
- [InstanceTypeInfo](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceTypeInfo.html): Provides details about a specific WorkSpace Instance type.
- [Ipv4PrefixSpecificationRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_Ipv4PrefixSpecificationRequest.html): Specifies IPv4 prefix configuration for network interfaces.
- [Ipv6PrefixSpecificationRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_Ipv6PrefixSpecificationRequest.html): Specifies IPv6 prefix configuration for network interfaces.
- [LicenseConfigurationRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_LicenseConfigurationRequest.html): Specifies license configuration for WorkSpace Instance.
- [ManagedInstanceRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ManagedInstanceRequest.html): Defines comprehensive configuration for a managed WorkSpace Instance.
- [Placement](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_Placement.html): Defines instance placement configuration for WorkSpace Instance.
- [PrivateDnsNameOptionsRequest](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_PrivateDnsNameOptionsRequest.html): Configures private DNS name settings for WorkSpace Instance.
- [PrivateIpAddressSpecification](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_PrivateIpAddressSpecification.html): Defines private IP address configuration for network interface.
- [Region](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_Region.html): Represents an AWS region supported by WorkSpaces Instances.
- [RunInstancesMonitoringEnabled](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_RunInstancesMonitoringEnabled.html): Configures detailed monitoring for WorkSpace Instance.
- [SpotMarketOptions](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_SpotMarketOptions.html): Defines configuration for spot instance deployment.
- [SupportedInstanceConfiguration](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_SupportedInstanceConfiguration.html): Represents a single valid configuration combination that an instance type supports, combining tenancy, platform type, and billing mode into one complete configuration specification.
- [Tag](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_Tag.html): Represents a key-value metadata tag.
- [TagSpecification](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_TagSpecification.html): Defines tagging configuration for a resource.
- [ValidationExceptionField](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ValidationExceptionField.html): Represents a validation error field in an API request.
- [WorkspaceInstance](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_WorkspaceInstance.html): Represents a single WorkSpace Instance.
- [WorkspaceInstanceError](https://docs.aws.amazon.com/workspaces-instances/latest/api/API_WorkspaceInstanceError.html): Captures errors specific to WorkSpace Instance operations.
