# Source: https://docs.aws.amazon.com/directconnect/latest/APIReference/llms.txt

# Direct Connect API Reference

> Direct Connect links your internal network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an Direct Connect router. With this connection in place, you can create virtual interfaces directly to the AWS Cloud (for example, to Amazon EC2 and Amazon S3) and to Amazon VPC, bypassing Internet service providers in your network path. A connection provides access to all AWS Regions except the China (Beijing) and (China) Ningxia Regions. AWS resources in the China Regions can only be accessed through locations associated with those Regions.

- [Welcome](https://docs.aws.amazon.com/directconnect/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/directconnect/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/directconnect/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Operations.html)

- [AcceptDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AcceptDirectConnectGatewayAssociationProposal.html): Accepts a proposal request to attach a virtual private gateway or transit gateway to a Direct Connect gateway.
- [AllocateConnectionOnInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateConnectionOnInterconnect.html)
- [AllocateHostedConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateHostedConnection.html): Creates a hosted connection on the specified interconnect or a link aggregation group (LAG) of interconnects.
- [AllocatePrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocatePrivateVirtualInterface.html): Provisions a private virtual interface to be owned by the specified AWS account.
- [AllocatePublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocatePublicVirtualInterface.html): Provisions a public virtual interface to be owned by the specified AWS account.
- [AllocateTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateTransitVirtualInterface.html): Provisions a transit virtual interface to be owned by the specified AWS account.
- [AssociateConnectionWithLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateConnectionWithLag.html): Associates an existing connection with a link aggregation group (LAG).
- [AssociateHostedConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateHostedConnection.html): Associates a hosted connection and its virtual interfaces with a link aggregation group (LAG) or interconnect.
- [AssociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateMacSecKey.html): Associates a MAC Security (MACsec) Connection Key Name (CKN)/ Connectivity Association Key (CAK) pair with a Direct Connect connection.
- [AssociateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateVirtualInterface.html): Associates a virtual interface with a specified link aggregation group (LAG) or connection.
- [ConfirmConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmConnection.html): Confirms the creation of the specified hosted connection on an interconnect.
- [ConfirmCustomerAgreement](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmCustomerAgreement.html): The confirmation of the terms of agreement when creating the connection/link aggregation group (LAG).
- [ConfirmPrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmPrivateVirtualInterface.html): Accepts ownership of a private virtual interface created by another AWS account.
- [ConfirmPublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmPublicVirtualInterface.html): Accepts ownership of a public virtual interface created by another AWS account.
- [ConfirmTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmTransitVirtualInterface.html): Accepts ownership of a transit virtual interface created by another AWS account.
- [CreateBGPPeer](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateBGPPeer.html): Creates a BGP peer on the specified virtual interface.
- [CreateConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateConnection.html): Creates a connection between a customer network and a specific Direct Connect location.
- [CreateDirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGateway.html): Creates a Direct Connect gateway, which is an intermediate object that enables you to connect a set of virtual interfaces and virtual private gateways.
- [CreateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociation.html): Creates an association between a Direct Connect gateway and a virtual private gateway.
- [CreateDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociationProposal.html): Creates a proposal to associate the specified virtual private gateway or transit gateway with the specified Direct Connect gateway.
- [CreateInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateInterconnect.html): Creates an interconnect between an Direct Connect Partner's network and a specific Direct Connect location.
- [CreateLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateLag.html): Creates a link aggregation group (LAG) with the specified number of bundled physical dedicated connections between the customer network and a specific Direct Connect location.
- [CreatePrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreatePrivateVirtualInterface.html): Creates a private virtual interface.
- [CreatePublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreatePublicVirtualInterface.html): Creates a public virtual interface.
- [CreateTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateTransitVirtualInterface.html): Creates a transit virtual interface.
- [DeleteBGPPeer](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteBGPPeer.html): Deletes the specified BGP peer on the specified virtual interface with the specified customer address and ASN.
- [DeleteConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteConnection.html): Deletes the specified connection.
- [DeleteDirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGateway.html): Deletes the specified Direct Connect gateway.
- [DeleteDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociation.html): Deletes the association between the specified Direct Connect gateway and virtual private gateway.
- [DeleteDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociationProposal.html): Deletes the association proposal request between the specified Direct Connect gateway and virtual private gateway or transit gateway.
- [DeleteInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteInterconnect.html): Deletes the specified interconnect.
- [DeleteLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteLag.html): Deletes the specified link aggregation group (LAG).
- [DeleteVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteVirtualInterface.html): Deletes a virtual interface.
- [DescribeConnectionLoa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnectionLoa.html)
- [DescribeConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnections.html): Displays the specified connection or all connections in this Region.
- [DescribeConnectionsOnInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnectionsOnInterconnect.html)
- [DescribeCustomerMetadata](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeCustomerMetadata.html): Get and view a list of customer agreements, along with their signed status and whether the customer is an NNIPartner, NNIPartnerV2, or a nonPartner.
- [DescribeDirectConnectGatewayAssociationProposals](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociationProposals.html): Describes one or more association proposals for connection between a virtual private gateway or transit gateway and a Direct Connect gateway.
- [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html): Lists the associations between your Direct Connect gateways and virtual private gateways and transit gateways.
- [DescribeDirectConnectGatewayAttachments](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAttachments.html): Lists the attachments between your Direct Connect gateways and virtual interfaces.
- [DescribeDirectConnectGateways](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGateways.html): Lists all your Direct Connect gateways or only the specified Direct Connect gateway.
- [DescribeHostedConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeHostedConnections.html): Lists the hosted connections that have been provisioned on the specified interconnect or link aggregation group (LAG).
- [DescribeInterconnectLoa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeInterconnectLoa.html)
- [DescribeInterconnects](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeInterconnects.html): Lists the interconnects owned by the AWS account or only the specified interconnect.
- [DescribeLags](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLags.html): Describes all your link aggregation groups (LAG) or the specified LAG.
- [DescribeLoa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLoa.html): Gets the LOA-CFA for a connection, interconnect, or link aggregation group (LAG).
- [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html): Lists the Direct Connect locations in the current AWS Region.
- [DescribeRouterConfiguration](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeRouterConfiguration.html): Details about the router.
- [DescribeTags](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeTags.html): Describes the tags associated with the specified Direct Connect resources.
- [DescribeVirtualGateways](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualGateways.html)
- [DescribeVirtualInterfaces](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualInterfaces.html): Displays all virtual interfaces for an AWS account.
- [DisassociateConnectionFromLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DisassociateConnectionFromLag.html): Disassociates a connection from a link aggregation group (LAG).
- [DisassociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DisassociateMacSecKey.html): Removes the association between a MAC Security (MACsec) security key and a Direct Connect connection.
- [ListVirtualInterfaceTestHistory](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceTestHistory.html): Lists the virtual interface failover test history.
- [StartBgpFailoverTest](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StartBgpFailoverTest.html): Starts the virtual interface failover test that verifies your configuration meets your resiliency requirements by placing the BGP peering session in the DOWN state.
- [StopBgpFailoverTest](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StopBgpFailoverTest.html): Stops the virtual interface failover test.
- [TagResource](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_TagResource.html): Adds the specified tags to the specified Direct Connect resource.
- [UntagResource](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UntagResource.html): Removes one or more tags from the specified Direct Connect resource.
- [UpdateConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateConnection.html): Updates the Direct Connect connection configuration.
- [UpdateDirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateDirectConnectGateway.html): Updates the name of a current Direct Connect gateway.
- [UpdateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateDirectConnectGatewayAssociation.html): Updates the specified attributes of the Direct Connect gateway association.
- [UpdateLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateLag.html): Updates the attributes of the specified link aggregation group (LAG).
- [UpdateVirtualInterfaceAttributes](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateVirtualInterfaceAttributes.html): Updates the specified attributes of the specified virtual private interface.


## [Data Types](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Types.html)

- [AssociatedCoreNetwork](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociatedCoreNetwork.html): The AWS Cloud WAN core network that the Direct Connect gateway is associated to.
- [AssociatedGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociatedGateway.html): Information about the associated gateway.
- [BGPPeer](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_BGPPeer.html): Information about a BGP peer.
- [Connection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Connection.html): Information about an Direct Connect connection.
- [CustomerAgreement](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CustomerAgreement.html): The name and status of a customer agreement.
- [DirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGateway.html): Information about a Direct Connect gateway, which enables you to connect virtual interfaces and virtual private gateway or transit gateways.
- [DirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGatewayAssociation.html): Information about an association between a Direct Connect gateway and a virtual private gateway or transit gateway.
- [DirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGatewayAssociationProposal.html): Information about the proposal request to attach a virtual private gateway to a Direct Connect gateway.
- [DirectConnectGatewayAttachment](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGatewayAttachment.html): Information about an attachment between a Direct Connect gateway and a virtual interface.
- [Interconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Interconnect.html): Information about an interconnect.
- [Lag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Lag.html): Information about a link aggregation group (LAG).
- [Loa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Loa.html): Information about a Letter of Authorization - Connecting Facility Assignment (LOA-CFA) for a connection.
- [Location](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Location.html): Information about an Direct Connect location.
- [MacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_MacSecKey.html): Information about the MAC Security (MACsec) secret key.
- [NewBGPPeer](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_NewBGPPeer.html): Information about a new BGP peer.
- [NewPrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_NewPrivateVirtualInterface.html): Information about a private virtual interface.
- [NewPrivateVirtualInterfaceAllocation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_NewPrivateVirtualInterfaceAllocation.html): Information about a private virtual interface to be provisioned on a connection.
- [NewPublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_NewPublicVirtualInterface.html): Information about a public virtual interface.
- [NewPublicVirtualInterfaceAllocation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_NewPublicVirtualInterfaceAllocation.html): Information about a public virtual interface to be provisioned on a connection.
- [NewTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_NewTransitVirtualInterface.html): Information about a transit virtual interface.
- [NewTransitVirtualInterfaceAllocation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_NewTransitVirtualInterfaceAllocation.html): Information about a transit virtual interface to be provisioned on a connection.
- [ResourceTag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ResourceTag.html): Information about a tag associated with an Direct Connect resource.
- [RouteFilterPrefix](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_RouteFilterPrefix.html): Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.
- [RouterType](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_RouterType.html): Information about the virtual router.
- [Tag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Tag.html): Information about a tag.
- [VirtualGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_VirtualGateway.html): Information about a virtual private gateway for a private virtual interface.
- [VirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_VirtualInterface.html): Information about a virtual interface.
- [VirtualInterfaceTestHistory](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_VirtualInterfaceTestHistory.html): Information about the virtual interface failover test.
