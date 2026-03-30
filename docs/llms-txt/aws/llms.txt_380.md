# Source: https://docs.aws.amazon.com/evs/latest/APIReference/llms.txt

# Amazon Elastic VMware Service Welcome

> Amazon Elastic VMware Service (Amazon EVS) is a service that you can use to deploy a VMware Cloud Foundation (VCF) software environment directly on EC2 bare metal instances within an Amazon Virtual Private Cloud (VPC).

- [Welcome](https://docs.aws.amazon.com/evs/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/evs/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/evs/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/evs/latest/APIReference/API_Operations.html)

- [AssociateEipToVlan](https://docs.aws.amazon.com/evs/latest/APIReference/API_AssociateEipToVlan.html): Associates an Elastic IP address with a public HCX VLAN.
- [CreateEnvironment](https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEnvironment.html): Creates an Amazon EVS environment that runs VCF software, such as SDDC Manager, NSX Manager, and vCenter Server.
- [CreateEnvironmentHost](https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEnvironmentHost.html): Creates an ESX host and adds it to an Amazon EVS environment.
- [DeleteEnvironment](https://docs.aws.amazon.com/evs/latest/APIReference/API_DeleteEnvironment.html): Deletes an Amazon EVS environment.
- [DeleteEnvironmentHost](https://docs.aws.amazon.com/evs/latest/APIReference/API_DeleteEnvironmentHost.html): Deletes a host from an Amazon EVS environment.
- [DisassociateEipFromVlan](https://docs.aws.amazon.com/evs/latest/APIReference/API_DisassociateEipFromVlan.html): Disassociates an Elastic IP address from a public HCX VLAN.
- [GetEnvironment](https://docs.aws.amazon.com/evs/latest/APIReference/API_GetEnvironment.html): Returns a description of the specified environment.
- [GetVersions](https://docs.aws.amazon.com/evs/latest/APIReference/API_GetVersions.html): Returns information about VCF versions, ESX versions and EC2 instance types provided by Amazon EVS.
- [ListEnvironmentHosts](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironmentHosts.html): List the hosts within an environment.
- [ListEnvironments](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironments.html): Lists the Amazon EVS environments in your AWS account in the specified AWS Region.
- [ListEnvironmentVlans](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironmentVlans.html): Lists environment VLANs that are associated with the specified environment.
- [ListTagsForResource](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListTagsForResource.html): Lists the tags for an Amazon EVS resource.
- [TagResource](https://docs.aws.amazon.com/evs/latest/APIReference/API_TagResource.html): Associates the specified tags to an Amazon EVS resource with the specified resourceArn.
- [UntagResource](https://docs.aws.amazon.com/evs/latest/APIReference/API_UntagResource.html): Deletes specified tags from an Amazon EVS resource.


## [Data Types](https://docs.aws.amazon.com/evs/latest/APIReference/API_Types.html)

- [Check](https://docs.aws.amazon.com/evs/latest/APIReference/API_Check.html): A check on the environment to identify environment health and validate VMware VCF licensing compliance.
- [ConnectivityInfo](https://docs.aws.amazon.com/evs/latest/APIReference/API_ConnectivityInfo.html): The connectivity configuration for the environment.
- [EipAssociation](https://docs.aws.amazon.com/evs/latest/APIReference/API_EipAssociation.html): An Elastic IP address association with the elastic network interface in the VLAN subnet.
- [Environment](https://docs.aws.amazon.com/evs/latest/APIReference/API_Environment.html): An object that represents an Amazon EVS environment.
- [EnvironmentSummary](https://docs.aws.amazon.com/evs/latest/APIReference/API_EnvironmentSummary.html): A list of environments with summarized environment details.
- [Host](https://docs.aws.amazon.com/evs/latest/APIReference/API_Host.html): An ESX host that runs on an Amazon EC2 bare metal instance.
- [HostInfoForCreate](https://docs.aws.amazon.com/evs/latest/APIReference/API_HostInfoForCreate.html): An object that represents a host.
- [InitialVlanInfo](https://docs.aws.amazon.com/evs/latest/APIReference/API_InitialVlanInfo.html): An object that represents an initial VLAN subnet for the Amazon EVS environment.
- [InitialVlans](https://docs.aws.amazon.com/evs/latest/APIReference/API_InitialVlans.html): The initial VLAN subnets for the environment.
- [InstanceTypeEsxVersionsInfo](https://docs.aws.amazon.com/evs/latest/APIReference/API_InstanceTypeEsxVersionsInfo.html): Information about ESX versions offered for each EC2 instance type.
- [LicenseInfo](https://docs.aws.amazon.com/evs/latest/APIReference/API_LicenseInfo.html): The license information that Amazon EVS requires to create an environment.
- [NetworkInterface](https://docs.aws.amazon.com/evs/latest/APIReference/API_NetworkInterface.html): An elastic network interface (ENI) that connects hosts to the VLAN subnets.
- [Secret](https://docs.aws.amazon.com/evs/latest/APIReference/API_Secret.html): A managed secret that contains the credentials for installing vCenter Server, NSX, and SDDC Manager.
- [ServiceAccessSecurityGroups](https://docs.aws.amazon.com/evs/latest/APIReference/API_ServiceAccessSecurityGroups.html): The security groups that allow traffic between the Amazon EVS control plane and your VPC for Amazon EVS service access.
- [ValidationExceptionField](https://docs.aws.amazon.com/evs/latest/APIReference/API_ValidationExceptionField.html): Stores information about a field passed inside a request that resulted in an exception.
- [VcfHostnames](https://docs.aws.amazon.com/evs/latest/APIReference/API_VcfHostnames.html): The DNS hostnames that Amazon EVS uses to install VMware vCenter Server, NSX, SDDC Manager, and Cloud Builder.
- [VcfVersionInfo](https://docs.aws.amazon.com/evs/latest/APIReference/API_VcfVersionInfo.html): Information about a VCF versions provided by Amazon EVS, including its status, default ESX version, and EC2 instance types.
- [Vlan](https://docs.aws.amazon.com/evs/latest/APIReference/API_Vlan.html): The VLANs that Amazon EVS creates during environment creation.


## [Service-specific Errors](https://docs.aws.amazon.com/evs/latest/APIReference/API_Errors.html)

- [InternalServerException](https://docs.aws.amazon.com/evs/latest/APIReference/API_InternalServerException.html): An internal server error occurred.
- [ResourceNotFoundException](https://docs.aws.amazon.com/evs/latest/APIReference/API_ResourceNotFoundException.html): A service resource associated with the request could not be found.
- [ServiceQuotaExceededException](https://docs.aws.amazon.com/evs/latest/APIReference/API_ServiceQuotaExceededException.html): The number of one or more Amazon EVS resources exceeds the maximum allowed.
- [TagPolicyException](https://docs.aws.amazon.com/evs/latest/APIReference/API_TagPolicyException.html)
- [ThrottlingException](https://docs.aws.amazon.com/evs/latest/APIReference/API_ThrottlingException.html): The operation could not be performed because the service is throttling requests.
- [TooManyTagsException](https://docs.aws.amazon.com/evs/latest/APIReference/API_TooManyTagsException.html)
- [ValidationException](https://docs.aws.amazon.com/evs/latest/APIReference/API_ValidationException.html): The input fails to satisfy the specified constraints.
