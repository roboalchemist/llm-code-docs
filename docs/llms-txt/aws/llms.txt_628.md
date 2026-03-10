# Source: https://docs.aws.amazon.com/odb/latest/APIReference/llms.txt

# Oracle Database@AWS API Reference

> Oracle Database@AWS is an offering that enables you to access Oracle Exadata infrastructure managed by Oracle Cloud Infrastructure (OCI) inside AWS data centers. You can migrate your Oracle Exadata workloads, establish low-latency connectivity with applications running on AWS, and integrate with AWS services. For example, you can run application servers in a Virtual Private Cloud (VPC) and access an Oracle Exadata system running in Oracle Database@AWS. You can get started with Oracle Database@AWS by using the familiar AWS Management Console, APIs, or AWS CLI.

- [Welcome](https://docs.aws.amazon.com/odb/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/odb/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/odb/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/odb/latest/APIReference/API_Operations.html)

- [AcceptMarketplaceRegistration](https://docs.aws.amazon.com/odb/latest/APIReference/API_AcceptMarketplaceRegistration.html): Registers the AWS Marketplace token for your AWS account to activate your Oracle Database@AWS subscription.
- [AssociateIamRoleToResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_AssociateIamRoleToResource.html): Associates an AWS Identity and Access Management (IAM) service role with a specified resource to enable AWS service integration.
- [CreateCloudAutonomousVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateCloudAutonomousVmCluster.html): Creates a new Autonomous VM cluster in the specified Exadata infrastructure.
- [CreateCloudExadataInfrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateCloudExadataInfrastructure.html): Creates an Exadata infrastructure.
- [CreateCloudVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateCloudVmCluster.html): Creates a VM cluster on the specified Exadata infrastructure.
- [CreateOdbNetwork](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateOdbNetwork.html): Creates an ODB network.
- [CreateOdbPeeringConnection](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateOdbPeeringConnection.html): Creates a peering connection between an ODB network and a VPC.
- [DeleteCloudAutonomousVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteCloudAutonomousVmCluster.html): Deletes an Autonomous VM cluster.
- [DeleteCloudExadataInfrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteCloudExadataInfrastructure.html): Deletes the specified Exadata infrastructure.
- [DeleteCloudVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteCloudVmCluster.html): Deletes the specified VM cluster.
- [DeleteOdbNetwork](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteOdbNetwork.html): Deletes the specified ODB network.
- [DeleteOdbPeeringConnection](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteOdbPeeringConnection.html): Deletes an ODB peering connection.
- [DisassociateIamRoleFromResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_DisassociateIamRoleFromResource.html): Disassociates an AWS Identity and Access Management (IAM) service role from a specified resource to disable AWS service integration.
- [GetCloudAutonomousVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetCloudAutonomousVmCluster.html): Gets information about a specific Autonomous VM cluster.
- [GetCloudExadataInfrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetCloudExadataInfrastructure.html): Returns information about the specified Exadata infrastructure.
- [GetCloudExadataInfrastructureUnallocatedResources](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetCloudExadataInfrastructureUnallocatedResources.html): Retrieves information about unallocated resources in a specified Cloud Exadata Infrastructure.
- [GetCloudVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetCloudVmCluster.html): Returns information about the specified VM cluster.
- [GetDbNode](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetDbNode.html): Returns information about the specified DB node.
- [GetDbServer](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetDbServer.html): Returns information about the specified database server.
- [GetOciOnboardingStatus](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetOciOnboardingStatus.html): Returns the tenancy activation link and onboarding status for your AWS account.
- [GetOdbNetwork](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetOdbNetwork.html): Returns information about the specified ODB network.
- [GetOdbPeeringConnection](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetOdbPeeringConnection.html): Retrieves information about an ODB peering connection.
- [InitializeService](https://docs.aws.amazon.com/odb/latest/APIReference/API_InitializeService.html): Initializes the ODB service for the first time in an account.
- [ListAutonomousVirtualMachines](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousVirtualMachines.html): Lists all Autonomous VMs in an Autonomous VM cluster.
- [ListCloudAutonomousVmClusters](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListCloudAutonomousVmClusters.html): Lists all Autonomous VM clusters in a specified Cloud Exadata infrastructure.
- [ListCloudExadataInfrastructures](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListCloudExadataInfrastructures.html): Returns information about the Exadata infrastructures owned by your AWS account.
- [ListCloudVmClusters](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListCloudVmClusters.html): Returns information about the VM clusters owned by your AWS account or only the ones on the specified Exadata infrastructure.
- [ListDbNodes](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListDbNodes.html): Returns information about the DB nodes for the specified VM cluster.
- [ListDbServers](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListDbServers.html): Returns information about the database servers that belong to the specified Exadata infrastructure.
- [ListDbSystemShapes](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListDbSystemShapes.html): Returns information about the shapes that are available for an Exadata infrastructure.
- [ListGiVersions](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListGiVersions.html): Returns information about Oracle Grid Infrastructure (GI) software versions that are available for a VM cluster for the specified shape.
- [ListOdbNetworks](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListOdbNetworks.html): Returns information about the ODB networks owned by your AWS account.
- [ListOdbPeeringConnections](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListOdbPeeringConnections.html): Lists all ODB peering connections or those associated with a specific ODB network.
- [ListSystemVersions](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListSystemVersions.html): Returns information about the system versions that are available for a VM cluster for the specified giVersion and shape.
- [ListTagsForResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListTagsForResource.html): Returns information about the tags applied to this resource.
- [RebootDbNode](https://docs.aws.amazon.com/odb/latest/APIReference/API_RebootDbNode.html): Reboots the specified DB node in a VM cluster.
- [StartDbNode](https://docs.aws.amazon.com/odb/latest/APIReference/API_StartDbNode.html): Starts the specified DB node in a VM cluster.
- [StopDbNode](https://docs.aws.amazon.com/odb/latest/APIReference/API_StopDbNode.html): Stops the specified DB node in a VM cluster.
- [TagResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_TagResource.html): Applies tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_UntagResource.html): Removes tags from the specified resource.
- [UpdateCloudExadataInfrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateCloudExadataInfrastructure.html): Updates the properties of an Exadata infrastructure resource.
- [UpdateOdbNetwork](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateOdbNetwork.html): Updates properties of a specified ODB network.
- [UpdateOdbPeeringConnection](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateOdbPeeringConnection.html): Modifies the settings of an Oracle Database@AWS peering connection.


## [Data Types](https://docs.aws.amazon.com/odb/latest/APIReference/API_Types.html)

- [AutonomousVirtualMachineSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousVirtualMachineSummary.html): A summary of an Autonomous Virtual Machine (VM) within an Autonomous VM cluster.
- [CloudAutonomousVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudAutonomousVmCluster.html): Information about an Autonomous VM cluster resource.
- [CloudAutonomousVmClusterResourceDetails](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudAutonomousVmClusterResourceDetails.html): Resource details of an Autonomous VM cluster.
- [CloudAutonomousVmClusterSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudAutonomousVmClusterSummary.html): A summary of an Autonomous VM cluster.
- [CloudExadataInfrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudExadataInfrastructure.html): Information about an Exadata infrastructure.
- [CloudExadataInfrastructureSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudExadataInfrastructureSummary.html): Information about an Exadata infrastructure.
- [CloudExadataInfrastructureUnallocatedResources](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudExadataInfrastructureUnallocatedResources.html): Information about unallocated resources in the Cloud Exadata infrastructure.
- [CloudVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudVmCluster.html): Information about a VM cluster.
- [CloudVmClusterSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudVmClusterSummary.html): Information about a VM cluster.
- [CrossRegionS3RestoreSourcesAccess](https://docs.aws.amazon.com/odb/latest/APIReference/API_CrossRegionS3RestoreSourcesAccess.html): The configuration access for the cross-Region Amazon S3 database restore source for the ODB network.
- [CustomerContact](https://docs.aws.amazon.com/odb/latest/APIReference/API_CustomerContact.html): A contact to receive notification from Oracle about maintenance updates for a specific Exadata infrastructure.
- [DataCollectionOptions](https://docs.aws.amazon.com/odb/latest/APIReference/API_DataCollectionOptions.html): Information about the data collection options enabled for a VM cluster.
- [DayOfWeek](https://docs.aws.amazon.com/odb/latest/APIReference/API_DayOfWeek.html): An enumeration of days of the week used for scheduling maintenance windows.
- [DbIormConfig](https://docs.aws.amazon.com/odb/latest/APIReference/API_DbIormConfig.html): The IORM configuration settings for the database.
- [DbNode](https://docs.aws.amazon.com/odb/latest/APIReference/API_DbNode.html): Information about a DB node.
- [DbNodeSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_DbNodeSummary.html): Information about a DB node.
- [DbServer](https://docs.aws.amazon.com/odb/latest/APIReference/API_DbServer.html): Information about a database server.
- [DbServerPatchingDetails](https://docs.aws.amazon.com/odb/latest/APIReference/API_DbServerPatchingDetails.html): The scheduling details for the quarterly maintenance window.
- [DbServerSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_DbServerSummary.html): Information about a database server.
- [DbSystemShapeSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_DbSystemShapeSummary.html): Information about a hardware system model (shape) that's available for an Exadata infrastructure.
- [ExadataIormConfig](https://docs.aws.amazon.com/odb/latest/APIReference/API_ExadataIormConfig.html): The IORM settings of the Exadata DB system.
- [GiVersionSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_GiVersionSummary.html): Information about a specific version of Oracle Grid Infrastructure (GI) software that can be installed on a VM cluster.
- [IamRole](https://docs.aws.amazon.com/odb/latest/APIReference/API_IamRole.html): Information about an AWS Identity and Access Management (IAM) service role associated with a resource.
- [KmsAccess](https://docs.aws.amazon.com/odb/latest/APIReference/API_KmsAccess.html): Configuration for AWS Key Management Service (KMS) access from the ODB network.
- [MaintenanceWindow](https://docs.aws.amazon.com/odb/latest/APIReference/API_MaintenanceWindow.html): The scheduling details for the maintenance window.
- [ManagedS3BackupAccess](https://docs.aws.amazon.com/odb/latest/APIReference/API_ManagedS3BackupAccess.html): The configuration for managed Amazon S3 backup access from the ODB network.
- [ManagedServices](https://docs.aws.amazon.com/odb/latest/APIReference/API_ManagedServices.html): The managed services configuration for the ODB network.
- [Month](https://docs.aws.amazon.com/odb/latest/APIReference/API_Month.html): An enumeration of months used for scheduling maintenance windows.
- [OciDnsForwardingConfig](https://docs.aws.amazon.com/odb/latest/APIReference/API_OciDnsForwardingConfig.html): DNS configuration to forward DNS resolver endpoints to your OCI Private Zone.
- [OciIdentityDomain](https://docs.aws.amazon.com/odb/latest/APIReference/API_OciIdentityDomain.html): Information about an Oracle Cloud Infrastructure (OCI) identity domain configuration.
- [OdbNetwork](https://docs.aws.amazon.com/odb/latest/APIReference/API_OdbNetwork.html): Information about an ODB network.
- [OdbNetworkSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_OdbNetworkSummary.html): Information about an ODB network.
- [OdbPeeringConnection](https://docs.aws.amazon.com/odb/latest/APIReference/API_OdbPeeringConnection.html): A peering connection between an ODB network and either another ODB network or a customer-owned VPC.
- [OdbPeeringConnectionSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_OdbPeeringConnectionSummary.html): A summary of an ODB peering connection.
- [S3Access](https://docs.aws.amazon.com/odb/latest/APIReference/API_S3Access.html): The configuration for Amazon S3 access from the ODB network.
- [ServiceNetworkEndpoint](https://docs.aws.amazon.com/odb/latest/APIReference/API_ServiceNetworkEndpoint.html): The configuration for a service network endpoint.
- [StsAccess](https://docs.aws.amazon.com/odb/latest/APIReference/API_StsAccess.html): Configuration for AWS Security Token Service (STS) access from the ODB network.
- [SystemVersionSummary](https://docs.aws.amazon.com/odb/latest/APIReference/API_SystemVersionSummary.html): Information about the compatible system versions that can be used with a specific Exadata shape and Grid Infrastructure (GI) version.
- [ValidationExceptionField](https://docs.aws.amazon.com/odb/latest/APIReference/API_ValidationExceptionField.html): The input failed to meet the constraints specified by the service in a specified field.
- [ZeroEtlAccess](https://docs.aws.amazon.com/odb/latest/APIReference/API_ZeroEtlAccess.html): The configuration for Zero-ETL access from the ODB network.
