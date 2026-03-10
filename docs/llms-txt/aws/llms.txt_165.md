# Source: https://docs.aws.amazon.com/bgw/v20210101/APIReference/llms.txt

# AWS Backup Backup gateway

> AWS Backup gateway connects AWS Backup to your hypervisor, so you can create, store, and restore backups of your virtual machines (VMs) anywhere, whether on-premises or in the VMware Cloud (VMC) on AWS.

- [Welcome](https://docs.aws.amazon.com/bgw/v20210101/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/bgw/v20210101/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/bgw/v20210101/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_Operations.html)

- [AssociateGatewayToServer](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_AssociateGatewayToServer.html): Associates a backup gateway with your server.
- [CreateGateway](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_CreateGateway.html): Creates a backup gateway.
- [DeleteGateway](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_DeleteGateway.html): Deletes a backup gateway.
- [DeleteHypervisor](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_DeleteHypervisor.html): Deletes a hypervisor.
- [DisassociateGatewayFromServer](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_DisassociateGatewayFromServer.html): Disassociates a backup gateway from the specified server.
- [GetBandwidthRateLimitSchedule](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_GetBandwidthRateLimitSchedule.html): Retrieves the bandwidth rate limit schedule for a specified gateway.
- [GetGateway](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_GetGateway.html): By providing the ARN (Amazon Resource Name), this API returns the gateway.
- [GetHypervisor](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_GetHypervisor.html): This action requests information about the specified hypervisor to which the gateway will connect.
- [GetHypervisorPropertyMappings](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_GetHypervisorPropertyMappings.html): This action retrieves the property mappings for the specified hypervisor.
- [GetVirtualMachine](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_GetVirtualMachine.html): By providing the ARN (Amazon Resource Name), this API returns the virtual machine.
- [ImportHypervisorConfiguration](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_ImportHypervisorConfiguration.html): Connect to a hypervisor by importing its configuration.
- [ListGateways](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_ListGateways.html): Lists backup gateways owned by an AWS account in an AWS Region.
- [ListHypervisors](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_ListHypervisors.html): Lists your hypervisors.
- [ListTagsForResource](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_ListTagsForResource.html): Lists the tags applied to the resource identified by its Amazon Resource Name (ARN).
- [ListVirtualMachines](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_ListVirtualMachines.html): Lists your virtual machines.
- [PutBandwidthRateLimitSchedule](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_PutBandwidthRateLimitSchedule.html): This action sets the bandwidth rate limit schedule for a specified gateway.
- [PutHypervisorPropertyMappings](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_PutHypervisorPropertyMappings.html): This action sets the property mappings for the specified hypervisor.
- [PutMaintenanceStartTime](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_PutMaintenanceStartTime.html): Set the maintenance start time for a gateway.
- [StartVirtualMachinesMetadataSync](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_StartVirtualMachinesMetadataSync.html): This action sends a request to sync metadata across the specified virtual machines.
- [TagResource](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_TagResource.html): Tag the resource.
- [TestHypervisorConfiguration](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_TestHypervisorConfiguration.html): Tests your hypervisor configuration to validate that backup gateway can connect with the hypervisor and its resources.
- [UntagResource](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_UntagResource.html): Removes tags from the resource.
- [UpdateGatewayInformation](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_UpdateGatewayInformation.html): Updates a gateway's name.
- [UpdateGatewaySoftwareNow](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_UpdateGatewaySoftwareNow.html): Updates the gateway virtual machine (VM) software.
- [UpdateHypervisor](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_UpdateHypervisor.html): Updates a hypervisor metadata, including its host, username, and password.


## [Data Types](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_Types.html)

- [BandwidthRateLimitInterval](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_BandwidthRateLimitInterval.html): Describes a bandwidth rate limit interval for a gateway.
- [Gateway](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_Gateway.html): A gateway is an AWS Backup Gateway appliance that runs on the customer's network to provide seamless connectivity to backup storage in the AWS Cloud.
- [GatewayDetails](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_GatewayDetails.html): The details of gateway.
- [Hypervisor](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_Hypervisor.html): Represents the hypervisor's permissions to which the gateway will connect.
- [HypervisorDetails](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_HypervisorDetails.html): These are the details of the specified hypervisor.
- [MaintenanceStartTime](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_MaintenanceStartTime.html): This is your gateway's weekly maintenance start time including the day and time of the week.
- [Tag](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_Tag.html): A key-value pair you can use to manage, filter, and search for your resources.
- [VirtualMachine](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_VirtualMachine.html): A virtual machine that is on a hypervisor.
- [VirtualMachineDetails](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_VirtualMachineDetails.html): Your VirtualMachine objects, ordered by their Amazon Resource Names (ARNs).
- [VmwareTag](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_VmwareTag.html): A VMware tag is a tag attached to a specific virtual machine.
- [VmwareToAwsTagMapping](https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_VmwareToAwsTagMapping.html): This displays the mapping of VMware tags to the corresponding AWS tags.
