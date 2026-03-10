# Source: https://docs.aws.amazon.com/network-manager/latest/tgwnm/llms.txt

# AWS Network Manager AWS Global Networks for Transit Gateways User Guide

> A transit gateway is a network transit hub that you can use to interconnect your virtual private clouds and on-premises networks.

- [What is AWS Global Networks for Transit Gateways?](https://docs.aws.amazon.com/network-manager/latest/tgwnm/what-are-global-networks.html)
- [How global networks work](https://docs.aws.amazon.com/network-manager/latest/tgwnm/how-gnw-works.html)
- [Get started](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gnw-getting-started.html)
- [Scenarios](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gnw-scenarios.html)
- [Quotas](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-quotas.html)
- [Document history](https://docs.aws.amazon.com/network-manager/latest/tgwnm/doc-history.html)

## [Modify a global network](https://docs.aws.amazon.com/network-manager/latest/tgwnm/working-with-gnws.html)

### [Multi-account](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-multi-account.html)

Use the AWS Network Manager console to set up multi-account support for your AWS global network.

- [Enable trusted access](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-enable-trusted.html): Use the AWS Global Networks for Transit Gateways console to enable multi-account access, allowing other accounts in your AWS organization to access your global network resources.
- [Disabled trusted access](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-multi-disable.html): Disable trusted access for an organization.
- [Register a delegated administrator](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-delegate-admin.html): Register a delegated administrator, who can then access transit gateway resources in your AWS global network.
- [Deregister a delegated administrator](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-deregister-admin.html): Deregister delegated administrators after trusted access is enabled.
- [Manage IAM role deployments](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-multi-manage-iam.html): Manage IAM deployments for multi-account access in your AWS global network.
- [Troubleshoot self-managed roles](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-multi-account-troubleshooting.html): A multi-account role can be either AWS CloudFormation StackSets-managed or self-managed.

### [Global networks](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks.html)

An AWS global network is a container for your network objects, such as transit gateways, devices, or sites.

- [Create a global network](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks-creating.html): Create the framework for an AWS global network using the Network Manager console or using the CLI.
- [View a global network](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks-viewing.html): View the framework for your AWS global network using the Network Manager console or using the CLI.
- [Update a global network](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks-updating.html): Update the framework for your AWS global network using the Network Manager console or using the CLI.
- [Delete a global network](https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks-deleting.html): Delete the framework for your AWS global network using the Network Manager console or using the CLI.

### [Transit gateway registrations](https://docs.aws.amazon.com/network-manager/latest/tgwnm/tgw-registrations.html)

Register transit gateways that you've created in Amazon Virtual Private Cloud within your global network.

- [Register a transit gateway](https://docs.aws.amazon.com/network-manager/latest/tgwnm/register-tgw.html): Register a transit gateway created using Amazon Virtual Private Cloud with your AWS global network using either the Network Manager console or using the CLI.
- [View registered transit gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/view-registered-tgws.html): View a transit gateway registered with an AWS global network using either the Network Manager console or using the CLI.
- [Deregister a transit gateway](https://docs.aws.amazon.com/network-manager/latest/tgwnm/deregister-tgw.html): Deregister a transit gateway registered from your AWS global network.

### [Sites and links](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html)

Create a site in your AWS global network.

- [Create a site](https://docs.aws.amazon.com/network-manager/latest/tgwnm/creating-a-site.html): Create a site in your AWS global network.
- [View site details](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites-view.html): View the details of an AWS global network site, which is a representation of the physical location of your network.
- [Update a site](https://docs.aws.amazon.com/network-manager/latest/tgwnm/updating-a-site.html): Update all details of a previously created site in your AWS global network.
- [Delete a site](https://docs.aws.amazon.com/network-manager/latest/tgwnm/deleting-a-site.html): Delete a site from your AWS global network if the site is no longer valid or you no longer want to display the site on your dashboards.
- [Add a link](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-site-link-add.html): Add a link to your AWS global network.
- [Edit a link](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-link-update.html): Edit the link between two devices in your AWS global network.
- [Delete a link](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-link-delete.html): Links represent connections between devices in your AWS global network.

### [Devices](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices.html)

Add a device to your Cloud WAN core network.

- [Add a device](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices-add.html): Create a device to represent a physical or virtual appliance in your AWS global network.
- [Delete a device](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices-delete.html): Delete a device from your AWS global network.
- [Edit a device](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices-update.html): Edit a device in your Cloud WAN global network.

### [View device details](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices-working-with.html)

View, update, or delete devices in your AWS global network.

- [Associate or disassociate a device link](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-device-link-associate.html): Associate a link with a device in your AWS global network.
- [Associate or disassociae an on-premises link](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices-onprem.html): Associate or disassociate an on-premises device link association in your AWS global network.
- [Associate or disassociate a Connect peer](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices-connect-peer.html): Associate or disassociate a Connect peer device link association in your AWS global network.
- [View VPNs](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices-vpns.html): View the VPNs associated with a device in your AWS global network.
- [Monitor devices](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-devices-monitoring.html): Use CloudWatch metrics to monitor device events in your AWS global network.

### [Connections](https://docs.aws.amazon.com/network-manager/latest/tgwnm/device-connections.html)

Create a connection between two devices in your AWS global network.

- [Create a connection](https://docs.aws.amazon.com/network-manager/latest/tgwnm/creating-a-connection.html): Create a connection between two devices in your AWS global network.
- [Update a connection](https://docs.aws.amazon.com/network-manager/latest/tgwnm/updating-a-connection.html): Update a connection between two devices in your AWS global network.
- [Delete a connection](https://docs.aws.amazon.com/network-manager/latest/tgwnm/deleting-a-connection.html): Delete a connection between two devices in your AWS global network.

### [Gateway associations](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gw-association.html)

Create a customer gateway association with either a device or with a transit gateway Connect peer in your AWS global network.

- [Associate a customer gateway with a device](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-cgw-associate.html): Associate a customer gateway with a device in your AWS global network using AWS Network Manager.
- [Disassociate a customer gateway association from a device](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-cgw-diasssociate.html): Disassociate a customer gateway association from a device or link from your AWS global network.
- [Add a Connect peer association](https://docs.aws.amazon.com/network-manager/latest/tgwnm/connect-peer-association.html): Create a transit gateway Connect peer association in your AWS global network.
- [Disassociate a Connect peer from a device](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-cgw-connect-disassociate.html): Disassociate a Connect peer from a device in your AWS global network.
- [Resource tags](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gnw-tagging.html): Tag your global networks transit gateway resources.


## [Transit gateway network and transit gateway dashboards](https://docs.aws.amazon.com/network-manager/latest/tgwnm/tgw-visualize-networks.html)

- [Access transit gateway network dashboards](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-monitoring-console.html): Visualize and monitor your transit gateway networks using the AWS Global Networks for Transit Gateways console.
- [Access transit gateway dashboards](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-visualize-tgw.html): Visualize and monitor your transit gateways using transit gateway dashboards in the AWS Global Networks for Transit Gateways console.


## [Route Analyzer](https://docs.aws.amazon.com/network-manager/latest/tgwnm/route-analyzer.html)

- [Perform a route analysis](https://docs.aws.amazon.com/network-manager/latest/tgwnm/working-with-route-analyzer.html): Perform a route analysis of your AWS global network..
- [Example: Route analysis for peered transit gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/example-route-analyzer.html): This page shows an example of route analysis for a peer transit gateway in an AWS global network.
- [Example: Route analysis with a middlebox configuration](https://docs.aws.amazon.com/network-manager/latest/tgwnm/example-route-analyzer-middlebox.html): This page shows an example of route analysis for a middlebox configuration in an AWS global network.


## [Metrics and events](https://docs.aws.amazon.com/network-manager/latest/tgwnm/monitoring-overview.html)

### [Monitor with CloudWatch metrics](https://docs.aws.amazon.com/network-manager/latest/tgwnm/monitoring-cloudwatch-metrics.html)

Monitor your AWS global network using Amazon CloudWatch metrics

- [View CloudWatch metrics for on-premises resources](https://docs.aws.amazon.com/network-manager/latest/tgwnm/cw-metrics-on-premises.html): AWS Global Networks for Transit Gateways publishes data points for your on-premises resources, including devices and links.
- [View global network CloudWatch metrics](https://docs.aws.amazon.com/network-manager/latest/tgwnm/viewing-metrics.html): View metrics for your AWS global network.
- [Monitor with EventBridge](https://docs.aws.amazon.com/network-manager/latest/tgwnm/monitoring-events.html): Monitor events for your AWS global network using EventBridge.
- [Log API calls using CloudTrail](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-logging-using-cloudtrail.html): Learn about logging AWS Global Networks for Transit Gateways with AWS CloudTrail.


## [Identity and access management](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-security-iam.html)

- [Service-linked role](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-service-linked-roles.html): Amazon CloudWatch uses service-linked roles to call other AWS services on your behalf in your AWS global network.
- [AWS managed policies](https://docs.aws.amazon.com/network-manager/latest/tgwnm/security-iam-awsmanpol.html): Learn about AWS managed policies for transit gateways and AWS Global Networks for Transit Gateways and recent changes to those policies.
- [Multi-account access roles](https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-custom-multi-role.html): AWS Global Networks for Transit Gateways uses CloudFormation StackSets and two custom IAM roles in member accounts for multi-account access.
