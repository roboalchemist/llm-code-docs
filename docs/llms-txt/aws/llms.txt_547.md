# Source: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/llms.txt

# Amazon Managed Blockchain API Reference

- [Welcome](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Operations.html)

- [CreateAccessor](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateAccessor.html): Creates a new accessor for use with Amazon Managed Blockchain service that supports token based access.
- [CreateMember](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateMember.html): Creates a member within a Managed Blockchain network.
- [CreateNetwork](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateNetwork.html): Creates a new blockchain network using Amazon Managed Blockchain.
- [CreateNode](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateNode.html): Creates a node on the specified blockchain network.
- [CreateProposal](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateProposal.html): Creates a proposal for a change to the network that other members of the network can vote on, for example, a proposal to add a new member to the network.
- [DeleteAccessor](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_DeleteAccessor.html): Deletes an accessor that your AWS account owns.
- [DeleteMember](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_DeleteMember.html): Deletes a member.
- [DeleteNode](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_DeleteNode.html): Deletes a node that your AWS account owns.
- [GetAccessor](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetAccessor.html): Returns detailed information about an accessor.
- [GetMember](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetMember.html): Returns detailed information about a member.
- [GetNetwork](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetNetwork.html): Returns detailed information about a network.
- [GetNode](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetNode.html): Returns detailed information about a node.
- [GetProposal](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetProposal.html): Returns detailed information about a proposal.
- [ListAccessors](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListAccessors.html): Returns a list of the accessors and their properties.
- [ListInvitations](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListInvitations.html): Returns a list of all invitations for the current AWS account.
- [ListMembers](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListMembers.html): Returns a list of the members in a network and properties of their configurations.
- [ListNetworks](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListNetworks.html): Returns information about the networks in which the current AWS account participates.
- [ListNodes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListNodes.html): Returns information about the nodes within a network.
- [ListProposals](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListProposals.html): Returns a list of proposals for the network.
- [ListProposalVotes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListProposalVotes.html): Returns the list of votes for a specified proposal, including the value of each vote and the unique identifier of the member that cast the vote.
- [ListTagsForResource](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListTagsForResource.html): Returns a list of tags for the specified resource.
- [RejectInvitation](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_RejectInvitation.html): Rejects an invitation to join a network.
- [TagResource](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_TagResource.html): Adds or overwrites the specified tags for the specified Amazon Managed Blockchain resource.
- [UntagResource](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_UntagResource.html): Removes the specified tags from the Amazon Managed Blockchain resource.
- [UpdateMember](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_UpdateMember.html): Updates a member configuration with new parameters.
- [UpdateNode](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_UpdateNode.html): Updates a node configuration with new parameters.
- [VoteOnProposal](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_VoteOnProposal.html): Casts a vote for a specified ProposalId on behalf of a member.


## [Data Types](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Types.html)

- [Accessor](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Accessor.html): The properties of the Accessor.
- [AccessorSummary](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_AccessorSummary.html): A summary of accessor properties.
- [ApprovalThresholdPolicy](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ApprovalThresholdPolicy.html): A policy type that defines the voting rules for the network.
- [Invitation](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Invitation.html): An invitation to an AWS account to create a member and join the network.
- [InviteAction](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_InviteAction.html): An action to invite a specific AWS account to create a member and join the network.
- [LogConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_LogConfiguration.html): A configuration for logging events.
- [LogConfigurations](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_LogConfigurations.html): A collection of log configurations.
- [Member](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Member.html): Member configuration properties.
- [MemberConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberConfiguration.html): Configuration properties of the member.
- [MemberFabricAttributes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberFabricAttributes.html): Attributes of Hyperledger Fabric for a member in a Managed Blockchain network using the Hyperledger Fabric framework.
- [MemberFabricConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberFabricConfiguration.html): Configuration properties for Hyperledger Fabric for a member in a Managed Blockchain network that is using the Hyperledger Fabric framework.
- [MemberFabricLogPublishingConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberFabricLogPublishingConfiguration.html): Configuration properties for logging events associated with a member of a Managed Blockchain network using the Hyperledger Fabric framework.
- [MemberFrameworkAttributes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberFrameworkAttributes.html): Attributes relevant to a member for the blockchain framework that the Managed Blockchain network uses.
- [MemberFrameworkConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberFrameworkConfiguration.html): Configuration properties relevant to a member for the blockchain framework that the Managed Blockchain network uses.
- [MemberLogPublishingConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberLogPublishingConfiguration.html): Configuration properties for logging events associated with a member of a Managed Blockchain network.
- [MemberSummary](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_MemberSummary.html): A summary of configuration properties for a member.
- [Network](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Network.html): Network configuration properties.
- [NetworkEthereumAttributes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NetworkEthereumAttributes.html): Attributes of Ethereum for a network.
- [NetworkFabricAttributes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NetworkFabricAttributes.html): Attributes of Hyperledger Fabric for a network.
- [NetworkFabricConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NetworkFabricConfiguration.html): Hyperledger Fabric configuration properties for the network.
- [NetworkFrameworkAttributes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NetworkFrameworkAttributes.html): Attributes relevant to the network for the blockchain framework that the network uses.
- [NetworkFrameworkConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NetworkFrameworkConfiguration.html): Configuration properties relevant to the network for the blockchain framework that the network uses.
- [NetworkSummary](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NetworkSummary.html): A summary of network configuration properties.
- [Node](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Node.html): Configuration properties of a node.
- [NodeConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeConfiguration.html): Configuration properties of a node.
- [NodeEthereumAttributes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeEthereumAttributes.html): Attributes of an Ethereum node.
- [NodeFabricAttributes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeFabricAttributes.html): Attributes of Hyperledger Fabric for a peer node on a Hyperledger Fabric network on Managed Blockchain.
- [NodeFabricLogPublishingConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeFabricLogPublishingConfiguration.html): Configuration properties for logging events associated with a peer node owned by a member in a Managed Blockchain network.
- [NodeFrameworkAttributes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeFrameworkAttributes.html): Attributes relevant to a node on a Managed Blockchain network for the blockchain framework that the network uses.
- [NodeLogPublishingConfiguration](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeLogPublishingConfiguration.html): Configuration properties for logging events associated with a peer node on a Hyperledger Fabric network on Managed Blockchain.
- [NodeSummary](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_NodeSummary.html): A summary of configuration properties for a node.
- [Proposal](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_Proposal.html): Properties of a proposal on a Managed Blockchain network.
- [ProposalActions](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ProposalActions.html): The actions to carry out if a proposal is APPROVED.
- [ProposalSummary](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ProposalSummary.html): Properties of a proposal.
- [RemoveAction](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_RemoveAction.html): An action to remove a member from a Managed Blockchain network as the result of a removal proposal that is APPROVED.
- [VoteSummary](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_VoteSummary.html): Properties of an individual vote that a member cast for a proposal.
- [VotingPolicy](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_VotingPolicy.html): The voting rules for the network to decide if a proposal is accepted
