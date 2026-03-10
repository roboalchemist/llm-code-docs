# Source: https://docs.aws.amazon.com/vpc/latest/tgw/llms.txt

# Amazon VPC AWS Transit Gateway

> A transit gateway is a network transit hub that you can use to interconnect your virtual private clouds and on-premises networks.

- [What is AWS Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
- [How transit gateways work](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html)
- [Design best practices](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-best-design-practices.html)
- [Quotas](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-quotas.html)
- [Document history](https://docs.aws.amazon.com/vpc/latest/tgw/doc-history.html)

## [Get started with transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html)

- [Create a transit gateway using the console](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started-console.html): Learn how to create transit gateways to interconnect your VPCs using the AWS Command Line Interface (AWS CLI)
- [Create a transit gateway using the command line](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started-cli.html): Learn how to create transit gateways to interconnect your VPCs using the AWS Command Line Interface (AWS CLI)


## [Work with transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-transit-gateways.html)

### [Transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html)

Create and manage a transit gateway.

- [Create a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/create-tgw.html): Create a transit gateway using either the console or CLI.
- [View a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/view-tgws.html): View information about your transit gateways using either the AWS console or the CLI.
- [Manage transit gateway tags](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-tagging.html): Add or edit tags associated with a transit gateway.
- [Modify a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-modifying.html): Modify a transit gateway.
- [Accept a resource share](https://docs.aws.amazon.com/vpc/latest/tgw/share-accept-tgw.html): Transit gateway resources can be shared with you from someone else.
- [Accept a shared attachment](https://docs.aws.amazon.com/vpc/latest/tgw/acccept-tgw-attach.html): Accept a cross-account attachment that's shared with you if you didn't enable to auto-accept shared attachments.
- [Delete a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/delete-tgw.html): Delete a transit gateway after first deleting all attachments to that transit gateway.
- [Encryption Support](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-encryption-support.html): Enable and manage Encryption Support for your transit gateway to enforce encryption-in-transit for all traffic.

### [VPC attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html)

Learn about how VPC attachments work in AWS Transit Gateway.

- [Create a VPC attachment](https://docs.aws.amazon.com/vpc/latest/tgw/create-vpc-attachment.html): Create a transit gateway attachment to a VPC.
- [Modify a VPC attachment](https://docs.aws.amazon.com/vpc/latest/tgw/modify-vpc-attachment.html): Create a transit gateway attachment to a VPC.
- [Modify VPC attachment tags](https://docs.aws.amazon.com/vpc/latest/tgw/modify-vpc-attachment-tag.html): Modify tags for a transit gateway VPC attachment using either the Amazon VPC Console or the CLI.
- [View a VPC attachment](https://docs.aws.amazon.com/vpc/latest/tgw/view-vpc-attachment.html): View any of your transit gateway VPC attachments using either the Amazon VPC Console or the CLI.
- [Delete a VPC attachment](https://docs.aws.amazon.com/vpc/latest/tgw/delete-vpc-attachment.html): Delete a transit gateway VPC attachment using either the Amazon VPC Console or the CLI.
- [Update security group inbound rules](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-sg-updates-update.html): Update transit gateway security group rules using the VPC console
- [Identify referenced security groups](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-sg-updates-identify.html): Identify whether your security group is being referenced in transit gateway security rules.
- [Remove stale security group rules](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-sg-updates-stale.html): Remove stale transit gateway security group rules
- [Troubleshoot VPC attachments](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-vpc-attach-troubleshooting.html): Learn about how to troubleshoot issues when you create a transit gateway VPC attachment.

### [Network function attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-nf-fw.html)

This chapter describes how to create and manage network function attachments for your transit gateway.

- [Accept or reject a transit gateway network function attachment](https://docs.aws.amazon.com/vpc/latest/tgw/accept-reject-firewall-attachment.html): You can use either the Amazon VPC console or the AWS Network Firewall CLI or API to accept or reject a transit gateway network function attachment, including Network Firewall attachments.
- [View network function attachments](https://docs.aws.amazon.com/vpc/latest/tgw/view-nf-attachment-nm.html): You can view your network function attachments, including your AWS Network Firewall attachments, using either Amazon VPC Console or the Network Manager console to get a visual representation of your network topology.
- [Route traffic through a transit gateway network function attachment](https://docs.aws.amazon.com/vpc/latest/tgw/route-traffic-nf-attachment.html): After creating a network function attachment, you need to update your transit gateway route tables to send traffic through the firewall for inspection using either the Amazon VPC Console or by using the CLI.

### [VPN attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html)

Work with transit gateway VPN attachments.

- [Create a transit gateway attachment to a VPN](https://docs.aws.amazon.com/vpc/latest/tgw/create-vpn-attachment.html): Use the AWS Transit Gateway console or the CLI to create a transit gateway VPN attachment.
- [View a VPN attachment](https://docs.aws.amazon.com/vpc/latest/tgw/view-vpn-attachment.html): Use the AWS Transit Gateway console or the CLI to view information about a transit gateway VPN attachment.
- [Delete a VPN attachment](https://docs.aws.amazon.com/vpc/latest/tgw/delete-vpn-attachment.html): Use the AWS Transit Gateway or the CLI to delete a transit gateway VPN attachment.

### [VPN Concentrator attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-concentrator-attachments.html)

Connect multiple remote sites cost-effectively using VPN Concentrator attachments.

- [Create a VPN Concentrator attachment](https://docs.aws.amazon.com/vpc/latest/tgw/create-vpn-concentrator-attachment.html): Use the AWS Transit Gateway console or the CLI to create a VPN Concentrator attachment.
- [View a VPN Concentrator attachment](https://docs.aws.amazon.com/vpc/latest/tgw/view-vpn-concentrator-attachment.html): Use the AWS Transit Gateway console or the CLI to view information about a VPN Concentrator attachment.
- [Delete a VPN Concentrator attachment](https://docs.aws.amazon.com/vpc/latest/tgw/delete-vpn-concentrator-attachment.html): Use the AWS Transit Gateway console or the CLI to delete a VPN Concentrator attachment.
- [Transit gateway attachments to a Direct Connect gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-dcg-attachments.html): Work with Direct Connect gateway attachments on a transit gateway.

### [Peering attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html)

Learn about transit gateway peering attachments.

- [Create a peering attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering-create.html): Create a transit gateway peering attachment
- [Accept or reject a peering request](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering-accept-reject.html): Accept or reject a transit gateway attachment peering request.
- [Add a route to a transit gateway route table](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering-add-route.html): Route traffic between two peered transit gateways using a route table.
- [Delete a peering attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering-delete.html): Delete a transit gateway peering attachment.

### [Connect attachments and Connect peers](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html)

Learn about working with Connect attachments and Connect peers in Amazon VPC.

- [Create a Connect attachment](https://docs.aws.amazon.com/vpc/latest/tgw/create-tgw-connect-attachment.html): Create a transit gateway Connect attachment using Amazon VPC.
- [Create a Connect peer](https://docs.aws.amazon.com/vpc/latest/tgw/create-tgw-connect-peer.html): Create a transit gateway Connect peer using Amazon VPC.
- [View Connect attachments and Connect peers](https://docs.aws.amazon.com/vpc/latest/tgw/view-tgw-connect-attachments.html): View your transit gateway Connect attachments and Connect peers in AWS Transit Gateway
- [Modify Connect attachment and Connect peer tags](https://docs.aws.amazon.com/vpc/latest/tgw/modify-connect-attachment-tag.html): Modify Connect attachment and Connect peer tags using Amazon VPC.
- [Delete a Connect peer](https://docs.aws.amazon.com/vpc/latest/tgw/delete-tgw-connect-peer.html): Delete a transit gateway Connect peer using Amazon VPC.
- [Delete a Connect attachment](https://docs.aws.amazon.com/vpc/latest/tgw/delete-tgw-connect-attachment.html): Delete a transit gateway Connect attachment using Amazon VPC.

### [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)

Use transit gateway route tables to route transit gateways in Amazon VPC.

- [Create a transit gateway route table](https://docs.aws.amazon.com/vpc/latest/tgw/create-tgw-route-table.html): Create a transit gateway route table in Amazon VPC.
- [View transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/view-tgw-route-tables.html): View transit gateway route tables in Amazon VPC.
- [Associate a transit gateway route table](https://docs.aws.amazon.com/vpc/latest/tgw/associate-tgw-route-table.html): Associate a transit gateway route table in Amazon VPC.
- [Disassociate a transit gateway route table](https://docs.aws.amazon.com/vpc/latest/tgw/disassociate-tgw-route-table.html): Disassociate a transit gateway route table in Amazon VPC.
- [Enable route propagation](https://docs.aws.amazon.com/vpc/latest/tgw/enable-tgw-route-propagation.html): Enable route propagation to a transit gateway route table in Amazon VPC.
- [Disable route propagation](https://docs.aws.amazon.com/vpc/latest/tgw/disable-tgw-route-propagation.html): Disable route propagation in Amazon VPC.
- [Create a static route](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-create-static-route.html): Create a static route for a VPC, VPN, or transit gateway peering attachment in Amazon VPC.
- [Delete a static route](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-delete-static-route.html): Delete a static route for a VPC, VPN, or transit gateway peering attachment in Amazon VPC.
- [Replace a static route](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-replace-static-route.html): Replace a static route for a VPC, VPN, or transit gateway peering attachment in Amazon VPC.
- [Export route tables to Amazon S3](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-export-route-tables.html): Export route tables to Amazon S3 using Amazon VPC.
- [Delete a transit gateway route table](https://docs.aws.amazon.com/vpc/latest/tgw/delete-tgw-route-table.html): Delete a transit gateway route table in Amazon VPC.
- [Create a prefix list reference](https://docs.aws.amazon.com/vpc/latest/tgw/create-prefix-list-reference.html): Create a transit gateway route table prefix list reference in Amazon VPC.
- [Modify a prefix list reference](https://docs.aws.amazon.com/vpc/latest/tgw/modify-prefix-list-reference.html): Modify a prefix list reference in Amazon VPC.
- [Delete a prefix list reference](https://docs.aws.amazon.com/vpc/latest/tgw/delete-prefix-list-reference.html): Delete a transit gateway route table prefix list reference in Amazon VPC.

### [Transit gateway policy tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-policy-tables.html)

Create and manage a transit gateway policy table.

- [Create a transit gateway policy table](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-policy-tables-create.html): Create a transit gateway policy table.
- [Delete a transit gateway policy table](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-policy-tables-disable.html): Delete a transit gateway policy table.

### [Multicast on transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-multicast-overview.html)

Learn about using multicast on transit gateways.

### [Multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-domains-about.html)

Learn how multicast domains work in Amazon VPC including required permissions and related services.

- [Create an IGMP multicast domain](https://docs.aws.amazon.com/vpc/latest/tgw/create-tgw-igmp-domain.html): Create a transit gateway IGMP multicast domain in Amazon VPC.
- [Create a static source multicast domain](https://docs.aws.amazon.com/vpc/latest/tgw/create-tgw-domain.html): Create a static source multicast domain.
- [Associating VPC attachments and subnets with a multicast domain](https://docs.aws.amazon.com/vpc/latest/tgw/associate-attachment-to-domain.html): Associate VPC attachments and subnets with a multicast domain.
- [Disassociate a subnet from a multicast domain](https://docs.aws.amazon.com/vpc/latest/tgw/remove-subnet-association.html): Disassociate or remove subnet associations from a transit gateway multicast domain in Amazon VPC.
- [View multicast domain associations](https://docs.aws.amazon.com/vpc/latest/tgw/view-tgw-domain-association.html): View your multicast domains to verify that they are available, and that they contain the appropriate subnets and attachments.
- [Add tags to a multicast domain](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-domain-tagging.html): Add tags to a transit gateway multicast domain in Amazon VPC.
- [Delete a multicast domain](https://docs.aws.amazon.com/vpc/latest/tgw/delete-tgw-domain.html): Delete a transit gateway multicast domain in Amazon VPC.

### [Shared multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-share-domain.html)

Learn about working with shared multicast domains in Amazon VPC.

- [Share resources across Availability Zones](https://docs.aws.amazon.com/vpc/latest/tgw/sharing-azs.html): Transit gateway resources in multicast domains shared across Availability Zones are named independently for each account.
- [Share a multicast domain](https://docs.aws.amazon.com/vpc/latest/tgw/sharing-share.html): Share a transit gateway multicast domain in Amazon VPC to allow others to share resources from that transit gateway.
- [Unshare a shared multicast domain](https://docs.aws.amazon.com/vpc/latest/tgw/sharing-unshare.html): Unshare a transit multicast domain and stop sharing those transit gateway resources with other accounts.
- [Identify a shared multicast domain](https://docs.aws.amazon.com/vpc/latest/tgw/sharing-identify.html): Identify shared transit gateway resources in Amazon VPC using either the console or the CLI.
- [Register sources with a multicast group](https://docs.aws.amazon.com/vpc/latest/tgw/add-source-multicast-group.html): Register sources with a transit gateway multicast domain in Amazon VPC.
- [Register members with a multicast group](https://docs.aws.amazon.com/vpc/latest/tgw/add-members-multicast-group.html): Register members with a transit gateway multicast group in Amazon VPC.
- [Deregister sources from a multicast group](https://docs.aws.amazon.com/vpc/latest/tgw/remove-source-multicast-group.html): Deregister or remove sources from a transit gateway multicast group in Amazon VPC.
- [Deregister members from a multicast group](https://docs.aws.amazon.com/vpc/latest/tgw/remove-members-multicast-group.html): Deregister or remove members from a transit gateway multicast group in Amazon VPC.
- [View multicast groups](https://docs.aws.amazon.com/vpc/latest/tgw/view-multicast-group.html): View members of a transit gateway multicast group in Amazon VPC.
- [Set up multicast for Windows Server](https://docs.aws.amazon.com/vpc/latest/tgw/multicastwin.html): Set up Windows Server for using multicast in Amazon VPC.
- [Example: Manage IGMP configurations](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-configurations-igmp.html): Manage IGMP configurations in a multicast domain.
- [Example: Manage static source configurations](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-configurations-no-igmp.html): Statically add multicast source to a group.
- [Example: Manage static group member configurations](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-configurations-no-igmp-source.html): This page provides an example of managing transit gateway static group member configurations in Amazon VPC.

### [Flexible cost allocation](https://docs.aws.amazon.com/vpc/latest/tgw/metering-policy.html)

Configure metering policies to control how data processing and transfer costs are allocated across your organization.

- [Create a metering policy](https://docs.aws.amazon.com/vpc/latest/tgw/metering-policy-create-policy.html): Create a metering policy to establish cost allocation framework and default settings for your transit gateway.

### [Manage metering policies](https://docs.aws.amazon.com/vpc/latest/tgw/metering-policy-manage-policy.html)

View, modify, and delete existing metering policies to adjust cost allocation settings for your transit gateway.

- [Edit a metering policy](https://docs.aws.amazon.com/vpc/latest/tgw/metering-policy-edit.html): Modify existing metering policy settings to adjust cost allocation configuration for your transit gateway.
- [Delete a metering policy](https://docs.aws.amazon.com/vpc/latest/tgw/metering-policy-delete.html): Remove metering policies that are no longer needed to revert to default cost allocation behavior.
- [Create a metering policy entry](https://docs.aws.amazon.com/vpc/latest/tgw/create-metering-policy-entry.html): Create entries to bill specific network flows to different accounts based on traffic flow properties.
- [Delete a metering policy entry](https://docs.aws.amazon.com/vpc/latest/tgw/metering-policy-entry-delete.html): Remove metering policy entries that are no longer needed to simplify cost allocation rules.

### [Manage metering policy middlebox attachments](https://docs.aws.amazon.com/vpc/latest/tgw/metering-policy-middlebox.html)

Configure and manage middlebox attachments to route traffic through network appliances for inspection, filtering, or processing while maintaining precise cost allocation control.

- [Add middlebox attachments](https://docs.aws.amazon.com/vpc/latest/tgw/create-middlebox-attachment.html): Create a middlebox attachments using the console, AWS CLI, or API to route traffic through network appliances for inspection, filtering, or processing.
- [Remove middlebox attachments](https://docs.aws.amazon.com/vpc/latest/tgw/edit-middlebox-attachment.html): Add or remove middlebox attachments from metering policies to control how traffic is metered through intermediate network services.


## [Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)

- [Create or update a Flow Logs IAM role](https://docs.aws.amazon.com/vpc/latest/tgw/create-flow-logs-role.html): Create or update an IAM role for Transit Gateway Flow Logs in Amazon VPC.

### [CloudWatch Logs Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/flow-logs-cwl.html)

Publish flow log data directly to Amazon CloudWatch.

- [Create a Flow Log that publishes to CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/tgw/flow-logs-cwl-create-flow-log.html): Create a Transit Gateways Flow Logs record that publishes to CloudWatch Logs
- [View Flow Logs records](https://docs.aws.amazon.com/vpc/latest/tgw/view-flow-log-records.html): View Transit Gateway Flow Logs records in Amazon CloudWatch.
- [Process Flow Log records](https://docs.aws.amazon.com/vpc/latest/tgw/process-records-cwl.html): Work with AWS Transit Gateway Flow logs as you would with any other log events collected by CloudWatch Logs.

### [Amazon S3 Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/flow-logs-s3.html)

Flow logs can publish flow log data to Amazon S3.

- [Create the source account role](https://docs.aws.amazon.com/vpc/latest/tgw/flowlog-s3-create-source.html): Create the Transit Gateway Flow Logs source account role in AWS Identity and Access Management in order to create flow logs in Amazon S3.
- [Create a Flow Log that publishes to Amazon S3](https://docs.aws.amazon.com/vpc/latest/tgw/flowlog-s3-create.html): Create a Transit Gateway Flow Log record that publishes to S3.
- [View Flow Logs records](https://docs.aws.amazon.com/vpc/latest/tgw/view-flow-log-records-s3.html): View Transit Gateway flow logs records in Amazon S3

### [Amazon Data Firehose Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/flow-logs-kinesis.html)

Create a flow log that publishes to Amazon Data Firehose.

- [Create the source account role](https://docs.aws.amazon.com/vpc/latest/tgw/flowlog-fh-create-source.html): To use Transit Gateway Flow Logs with Amazon Data Firehose, you'll need to create a Firehose source account.
- [Create the destination account role](https://docs.aws.amazon.com/vpc/latest/tgw/flowlog-fh-create-destination.html): To use Transit Gateway Flow Logs with Amazon Data Firehose, you'll need to create a Firehose destination account.
- [Create a Flow Log that publishes to Firehose](https://docs.aws.amazon.com/vpc/latest/tgw/flow-logs-kinesis-create.html): Create a flow log that publishes to Firehose.
- [Create and manage Flow Logs using the APIs or CLI](https://docs.aws.amazon.com/vpc/latest/tgw/flow-logs-api-cli.html): Use either the AWS API or CLI to create, describe, view, or delete a flow log in AWS Transit Gateways Flow Logs.
- [View Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/view-flow-logs.html): View Transit Gateway Flow Logs records through the Amazon VPC console.
- [Manage Flow Logs tags](https://docs.aws.amazon.com/vpc/latest/tgw/modify-tags-flow-logs.html): Add, remove, or edit key value tags for transit gateway flow logs resources.
- [Search Flow Logs records](https://docs.aws.amazon.com/vpc/latest/tgw/search-flow-log-records.html): Search for Transit Gateway Flow Logs records through the Amazon VPC console.
- [Delete a Flow Logs record](https://docs.aws.amazon.com/vpc/latest/tgw/delete-flow-log.html): Delete a Transit Gateway Flow Log in Amazon VPC.


## [Metrics and events](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-monitoring.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-cloudwatch-metrics.html): Learn how to monitor your transit gateways using metrics gathered by CloudWatch.
- [CloudTrail logs](https://docs.aws.amazon.com/vpc/latest/tgw/logging-using-cloudtrail.html): Learn about logging Amazon VPC Transit Gateways with AWS CloudTrail.


## [Identity and access management](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-authentication-access-control.html)

- [Service-linked roles](https://docs.aws.amazon.com/vpc/latest/tgw/service-linked-roles.html): Use service-linked roles to set required permissions for your transit gateways in Amazon VPC.
- [AWS managed policies](https://docs.aws.amazon.com/vpc/latest/tgw/security-iam-awsmanpol.html): Learn about AWS managed policies for transit gateways and recent changes to those policies.
- [Network ACLs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-nacls.html): Learn how transit gateways work with Network ACLs.
