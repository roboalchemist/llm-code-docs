# Source: https://docs.aws.amazon.com/global-accelerator/latest/api/llms.txt

# AWS Global Accelerator API Reference

> This is the AWS Global Accelerator API Reference. This guide is for developers who need detailed information about AWS Global Accelerator API actions, data types, and errors. For more information about Global Accelerator features, see the AWS Global Accelerator Developer Guide.

- [Welcome](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/global-accelerator/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/global-accelerator/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Operations.html)

- [AddCustomRoutingEndpoints](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AddCustomRoutingEndpoints.html): Associate a virtual private cloud (VPC) subnet endpoint with your custom routing accelerator.
- [AddEndpoints](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AddEndpoints.html): Add endpoints to an endpoint group.
- [AdvertiseByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AdvertiseByoipCidr.html): Advertises an IPv4 address range that is provisioned for use with your AWS resources through bring your own IP addresses (BYOIP).
- [AllowCustomRoutingTraffic](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html): Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC subnet endpoint that can receive traffic for a custom routing accelerator.
- [CreateAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateAccelerator.html): Create an accelerator.
- [CreateCrossAccountAttachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCrossAccountAttachment.html): Create a cross-account attachment in AWS Global Accelerator.
- [CreateCustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingAccelerator.html): Create a custom routing accelerator.
- [CreateCustomRoutingEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingEndpointGroup.html): Create an endpoint group for the specified listener for a custom routing accelerator.
- [CreateCustomRoutingListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingListener.html): Create a listener to process inbound connections from clients to a custom routing accelerator.
- [CreateEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateEndpointGroup.html): Create an endpoint group for the specified listener.
- [CreateListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateListener.html): Create a listener to process inbound connections from clients to an accelerator.
- [DeleteAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteAccelerator.html): Delete an accelerator.
- [DeleteCrossAccountAttachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCrossAccountAttachment.html): Delete a cross-account attachment.
- [DeleteCustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCustomRoutingAccelerator.html): Delete a custom routing accelerator.
- [DeleteCustomRoutingEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCustomRoutingEndpointGroup.html): Delete an endpoint group from a listener for a custom routing accelerator.
- [DeleteCustomRoutingListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCustomRoutingListener.html): Delete a listener for a custom routing accelerator.
- [DeleteEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteEndpointGroup.html): Delete an endpoint group from a listener.
- [DeleteListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteListener.html): Delete a listener from an accelerator.
- [DenyCustomRoutingTraffic](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DenyCustomRoutingTraffic.html): Specify the Amazon EC2 instance (destination) IP addresses and ports for a VPC subnet endpoint that cannot receive traffic for a custom routing accelerator.
- [DeprovisionByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeprovisionByoipCidr.html): Releases the specified address range that you provisioned to use with your AWS resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool.
- [DescribeAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAccelerator.html): Describe an accelerator.
- [DescribeAcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAcceleratorAttributes.html): Describe the attributes of an accelerator.
- [DescribeCrossAccountAttachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCrossAccountAttachment.html): Gets configuration information about a cross-account attachment.
- [DescribeCustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCustomRoutingAccelerator.html): Describe a custom routing accelerator.
- [DescribeCustomRoutingAcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCustomRoutingAcceleratorAttributes.html): Describe the attributes of a custom routing accelerator.
- [DescribeCustomRoutingEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCustomRoutingEndpointGroup.html): Describe an endpoint group for a custom routing accelerator.
- [DescribeCustomRoutingListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCustomRoutingListener.html): The description of a listener for a custom routing accelerator.
- [DescribeEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeEndpointGroup.html): Describe an endpoint group.
- [DescribeListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeListener.html): Describe a listener.
- [ListAccelerators](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListAccelerators.html): List the accelerators for an AWS account.
- [ListByoipCidrs](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListByoipCidrs.html): Lists the IP address ranges that were specified in calls to ProvisionByoipCidr, including the current state and a history of state changes.
- [ListCrossAccountAttachments](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCrossAccountAttachments.html): List the cross-account attachments that have been created in AWS Global Accelerator.
- [ListCrossAccountResourceAccounts](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCrossAccountResourceAccounts.html): List the accounts that have cross-account resources.
- [ListCrossAccountResources](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCrossAccountResources.html): List the cross-account resources available to work with.
- [ListCustomRoutingAccelerators](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingAccelerators.html): List the custom routing accelerators for an AWS account.
- [ListCustomRoutingEndpointGroups](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingEndpointGroups.html): List the endpoint groups that are associated with a listener for a custom routing accelerator.
- [ListCustomRoutingListeners](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingListeners.html): List the listeners for a custom routing accelerator.
- [ListCustomRoutingPortMappings](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingPortMappings.html): Provides a complete mapping from the public accelerator IP address and port to destination EC2 instance IP addresses and ports in the virtual public cloud (VPC) subnet endpoint for a custom routing accelerator.
- [ListCustomRoutingPortMappingsByDestination](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingPortMappingsByDestination.html): List the port mappings for a specific EC2 instance (destination) in a VPC subnet endpoint.
- [ListEndpointGroups](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListEndpointGroups.html): List the endpoint groups that are associated with a listener.
- [ListListeners](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListListeners.html): List the listeners for an accelerator.
- [ListTagsForResource](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListTagsForResource.html): List all tags for an accelerator.
- [ProvisionByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ProvisionByoipCidr.html): Provisions an IP address range to use with your AWS resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool.
- [RemoveCustomRoutingEndpoints](https://docs.aws.amazon.com/global-accelerator/latest/api/API_RemoveCustomRoutingEndpoints.html): Remove endpoints from a custom routing accelerator.
- [RemoveEndpoints](https://docs.aws.amazon.com/global-accelerator/latest/api/API_RemoveEndpoints.html): Remove endpoints from an endpoint group.
- [TagResource](https://docs.aws.amazon.com/global-accelerator/latest/api/API_TagResource.html): Add tags to an accelerator resource.
- [UntagResource](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UntagResource.html): Remove tags from a Global Accelerator resource.
- [UpdateAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateAccelerator.html): Update an accelerator to make changes, such as the following:
- [UpdateAcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateAcceleratorAttributes.html): Update the attributes for an accelerator.
- [UpdateCrossAccountAttachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCrossAccountAttachment.html): Update a cross-account attachment to add or remove principals or resources.
- [UpdateCustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCustomRoutingAccelerator.html): Update a custom routing accelerator.
- [UpdateCustomRoutingAcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCustomRoutingAcceleratorAttributes.html): Update the attributes for a custom routing accelerator.
- [UpdateCustomRoutingListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCustomRoutingListener.html): Update a listener for a custom routing accelerator.
- [UpdateEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateEndpointGroup.html): Update an endpoint group.
- [UpdateListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateListener.html): Update a listener.
- [WithdrawByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_WithdrawByoipCidr.html): Stops advertising an address range that is provisioned as an address pool.


## [Data Types](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Types.html)

- [Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Accelerator.html): An accelerator is a complex type that includes one or more listeners that process inbound connections and then direct traffic to one or more endpoint groups, each of which includes endpoints, such as load balancers.
- [AcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AcceleratorAttributes.html): Attributes of an accelerator.
- [AcceleratorEvent](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AcceleratorEvent.html): A complex type that contains a Timestamp value and Message for changes that you make to an accelerator in Global Accelerator.
- [Attachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Attachment.html): A cross-account attachment in AWS Global Accelerator.
- [ByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ByoipCidr.html): Information about an IP address range that is provisioned for use with your AWS resources through bring your own IP address (BYOIP).
- [ByoipCidrEvent](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ByoipCidrEvent.html): A complex type that contains a Message and a Timestamp value for changes that you make in the status of an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).
- [CidrAuthorizationContext](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CidrAuthorizationContext.html): Provides authorization for Amazon to bring a specific IP address range to a specific AWS account using bring your own IP addresses (BYOIP).
- [CrossAccountResource](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CrossAccountResource.html): An endpoint (AWS resource) or an IP address range, in CIDR format, that is listed in a cross-account attachment.
- [CustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingAccelerator.html): Attributes of a custom routing accelerator.
- [CustomRoutingAcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingAcceleratorAttributes.html): Attributes of a custom routing accelerator.
- [CustomRoutingDestinationConfiguration](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingDestinationConfiguration.html): For a custom routing accelerator, sets the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.
- [CustomRoutingDestinationDescription](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingDestinationDescription.html): For a custom routing accelerator, describes the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.
- [CustomRoutingEndpointConfiguration](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingEndpointConfiguration.html): The list of endpoint objects.
- [CustomRoutingEndpointDescription](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingEndpointDescription.html): A complex type for an endpoint for a custom routing accelerator.
- [CustomRoutingEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingEndpointGroup.html): A complex type for the endpoint group for a custom routing accelerator.
- [CustomRoutingListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingListener.html): A complex type for a listener for a custom routing accelerator.
- [DestinationPortMapping](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DestinationPortMapping.html): The port mappings for a specified endpoint IP address (destination).
- [EndpointConfiguration](https://docs.aws.amazon.com/global-accelerator/latest/api/API_EndpointConfiguration.html): A complex type for endpoints.
- [EndpointDescription](https://docs.aws.amazon.com/global-accelerator/latest/api/API_EndpointDescription.html): A complex type for an endpoint.
- [EndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_EndpointGroup.html): A complex type for the endpoint group.
- [EndpointIdentifier](https://docs.aws.amazon.com/global-accelerator/latest/api/API_EndpointIdentifier.html): A complex type for an endpoint.
- [IpSet](https://docs.aws.amazon.com/global-accelerator/latest/api/API_IpSet.html): A complex type for the set of IP addresses for an accelerator.
- [Listener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Listener.html): A complex type for a listener.
- [PortMapping](https://docs.aws.amazon.com/global-accelerator/latest/api/API_PortMapping.html): Returns the ports and associated IP addresses and ports of Amazon EC2 instances in your virtual private cloud (VPC) subnets.
- [PortOverride](https://docs.aws.amazon.com/global-accelerator/latest/api/API_PortOverride.html): Override specific listener ports used to route traffic to endpoints that are part of an endpoint group.
- [PortRange](https://docs.aws.amazon.com/global-accelerator/latest/api/API_PortRange.html): A complex type for a range of ports for a listener.
- [Resource](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Resource.html): A resource is one of the following: the ARN for an AWS resource that is supported by AWS Global Accelerator to be added as an endpoint, or a CIDR range that specifies a bring your own IP (BYOIP) address pool.
- [SocketAddress](https://docs.aws.amazon.com/global-accelerator/latest/api/API_SocketAddress.html): An IP address/port combination.
- [Tag](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Tag.html): A complex type that contains a Tag key and Tag value.
