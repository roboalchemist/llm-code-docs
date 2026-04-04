# Source: https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/llms.txt

# Amazon Managed Blockchain (AMB) Hyperledger Fabric Developer Guide

> Learn how to create and configure an Amazon Managed Blockchain (AMB) network for Hyperledger Fabric and Ethereum blockchains.

- [What Is Amazon Managed Blockchain (AMB) Hyperledger Fabric](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/what-is-managed-blockchain.html)
- [Key Concepts](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/network-components.html)
- [Create a Network](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/create-network.html)
- [Delete a Network](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/delete-network.html)
- [Invite or Remove Members](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-members.html)
- [Create an Interface VPC Endpoint](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-endpoints.html)
- [API Reference](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/api-ref-link.html)
- [Tagging resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging.html)
- [Monitoring](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/monitoring-cloudwatch-logs.html)
- [CloudTrail logs](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/logging-using-cloudtrail.html)
- [Document History](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-management-guide-doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/glossary.html)

## [Getting Started](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-get-started-tutorial.html)

- [Prerequisites and Considerations](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/get-started-prerequisites.html): To complete this tutorial, you must have the resources listed in this section.
- [Step 1: Create the Network and First Member](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/get-started-create-network.html): When you create the network, you specify the following parameters along with basic information such as names and descriptions:
- [Step 2: Create an Endpoint](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/get-started-create-endpoint.html): Now that the network is up and running in your VPC, you set up an interface VPC endpoint (AWS PrivateLink) for your member.
- [Step 3: Create a Peer Node](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/get-started-create-peer-node.html): Now that your network and the first member are up and running, you can use the AMB Access console or the AWS CLI to create a peer node.
- [Step 4: Set Up a Client](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/get-started-create-client.html): To complete this step, you launch an Amazon EC2 instance using the Amazon Linux AMI.
- [Step 5: Enroll the Member Admin](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/get-started-enroll-admin.html): In this step, you use a pre-configured certificate to enroll a user with administrative permissions to your member's certificate authority (CA).
- [Step 6: Create a Channel](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/get-started-create-channel.html): In Hyperledger Fabric, a ledger exists in the scope of a channel.
- [Step 7: Run Chaincode](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/get-started-chaincode.html): In this section, you create and install a package for golang sample chaincode on your peer node.
- [Step 8: Invite a Member and Create a Multi-Member Channel](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/get-started-joint-channel.html): Now that you have a Hyperledger Fabric network set up using Amazon Managed Blockchain (AMB), with an initial member in your AWS account and a VPC endpoint with a service name, you are ready to invite additional members.


## [Accept an Invitation and Create a Member](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-hyperledger-member.html)

- [Work with Invitations](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/accept-invitation.html): If you are invited to join a Hyperledger Fabric network on Amazon Managed Blockchain (AMB), you can accept the invitation by creating a member using the invitation ID.
- [Create a Member](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-hyperledger-create-member.html): You can use the AMB Access console, the AWS CLI, or the AMB Access SDK CreateMember action to create a member in a network that your account is invited to.


## [Work with Peer Nodes](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-hyperledger-peer-nodes.html)

- [Create a Peer Node](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-create-peer-node.html): You can create a Hyperledger Fabric peer node in a member that is in your AWS account using the AWS Management Console, the AWS CLI, or the AMB Access SDK CreateNode action.
- [View Peer Node Properties](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-view-peer-node.html): You can view information about each Hyperledger Fabric peer node that belong to your member using the AWS Management Console, the AWS CLI or the AMB Access API GetNode command.
- [Use Peer Node Metrics](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-peer-node-metrics.html): You can use peer node metrics to track the activity and health of Hyperledger Fabric peer nodes on Amazon Managed Blockchain (AMB) that belong to your member.


## [Work with Proposals](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-proposals.html)

- [Automating with CloudWatch Events](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/automating-proposals-with-cloudwatch-events.html): Automate AMB Access Proposal Notifications with CloudWatch Events.


## [Work with Hyperledger Fabric](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/framework-client.html)

- [Create an Admin](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-hyperledger-create-admin.html): Only identities who are admins within a Hyperledger Fabric member can install and query chaincode.
- [Work with Channels](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/hyperledger-work-with-channels.html): A channel is a private communication pathway between two or more members of a Hyperledger Fabric network on Amazon Managed Blockchain (AMB).
- [Add an Anchor Peer to a Channel](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/hyperledger-anchor-peers.html): Anchor peers within an organization enable cross-organization communication among peer nodes using the Hyperledger Fabric gossip protocol.

### [Develop Chaincode](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-hyperledger-develop-chaincode.html)

Smart contracts in Hyperledger Fabric are known as chaincode.

- [Private Data Collections](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-hyperledger-create-pdc.html): Network members that participate on a Hyperledger Fabric channel on AMB Access may want to keep some data private from other members on the same channel.
- [Develop Java Chaincode](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/java-chaincode.html): Hyperledger Fabric 2.2 networks on Amazon Managed Blockchain (AMB) are based on the following components:


## [Security](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-security.html)

### [Data Protection](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Managed Blockchain (AMB) Hyperledger Fabric.

- [Encryption at Rest](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-at-rest.html): Learn how Amazon Managed Blockchain (AMB) Hyperledger Fabric helps protect your data by default using the fully managed encryption at rest functionality.
- [Encryption in Transit](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-in-transit.html): Learn how Amazon Managed Blockchain (AMB) Hyperledger Fabric helps protect your data in transit by default using Transport Layer Security (TLS).

### [Authentication and Access Control](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-auth-and-access-control.html)

AWS Identity and Access Management (IAM) permissions policies, VPC endpoint services powered by AWS PrivateLink, and Amazon EC2 security groups provide the primary means for you to control access to Amazon Managed Blockchain (AMB).

### [Identity and Access Management](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/security-iam.html)

How to authenticate requests and manage access to your AMB Access Hyperledger Fabric resources.

- [How Amazon Managed Blockchain (AMB) Hyperledger Fabric works with IAM](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/security_iam_service-with-iam.html): Before you use IAM to manage access to AMB Access Hyperledger Fabric, learn what IAM features are available to use with AMB Access Hyperledger Fabric.
- [Troubleshooting](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AMB Access Hyperledger Fabric and IAM.
- [Identity-Based Policy Examples](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify AMB Access Hyperledger Fabric resources.
- [Hyperledger Fabric Client IAM Permissions](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/security_iam_hyperledger_ec2_client.html): When you administer, develop, and deploy chaincode using an EC2 instance as a Hyperledger Fabric client, the permissions policies attached to the AWS Identity and Access Management instance profile and instance role associated with the instance determine its permissions to interact with other AWS resources, including AMB Access.
- [Using Service-Linked Roles](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/using-service-linked-roles.html): How to use service-linked roles to give AMB Access access to resources in your AWS account.
- [Configuring Security Groups](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-security-sgs.html): Security groups act as virtual firewalls.
