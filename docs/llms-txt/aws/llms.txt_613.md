# Source: https://docs.aws.amazon.com/network-manager/latest/cloudwan/llms.txt

# AWS Network Manager AWS Cloud WAN User Guide

> Forthcoming.

- [What is AWS Cloud WAN?](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html)
- [Quick start: Create a global and core network](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-getting-started.html)
- [Quotas](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-quotas.html)
- [Document history](https://docs.aws.amazon.com/network-manager/latest/cloudwan/doc-history.html)

## [Modify AWS Cloud WAN networks](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-working-with.html)

### [Global and core networks](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-networks-working-with.html)

View details about, edit, or delete a Cloud WAN global or core network.

- [View global network information](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-global-view.html): View details about a Cloud WAN global network.
- [Delete a global network](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-global-network-delete.html): Delete a Cloud WAN global network
- [View core network information](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-core-network-view.html): View information about a core network within a Cloud WAN global network.
- [Delete a core network](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-core-network-delete.html): Delete a Cloud WAN core network if it's no longer needed.

### [Attachment tags](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tags.html)

Tag your Cloud WAN network resources to help identify them on your network.

- [Add or update a resource attachment tag](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tag-proposed.html): Add key-value tags to your Cloud WAN core network attachments to further help identify them.
- [Remove a resource attachment tag](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tag-remove.html): Remove key-value tags from your Cloud WAN core network attachment.

### [Attachments](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-attachment.html)

Add a Connect, Connect peer, transit gateway route table, VPC, or Site-to-Site VPN attachments to your Cloud WAN core network.

### [Connect attachments and Connect peers](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-connect-attachment.html)

Learn how Connect attachments and Connect peers operate in a Cloud WAN core network.

- [Create a Connect attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-connect-attachment-add.html): Create a Connect attachment for your Cloud WAN core network.
- [View or edit a Connect attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-viewing-editing-connect.html): View and edit a Cloud WAN core network Connect attachment.
- [Add a Connect peer](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-connect-peer-attachment.html): Create a Connect peer for an existing Connect attachment in a Cloud WAN core network.

### [Direct Connect gateway attachments](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-dxattach-about.html)

Direct Connect gateways you've created through the Direct Connect console can be registered in your Cloud WAN global network as a Direct Connect gateway attachment.

- [Create a Direct Connect gateway attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-dxattachment-add.html): Create a Direct Connect gateway attachment for your Cloud WAN core network.
- [View or edit a Direct Connect gateway attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-dxattachment-update.html): Update a Direct Connect gateway attachment in your Cloud WAN core network.

### [VPC attachments](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-vpc-attachment.html)

This describes what you need to know about VPC attachments in your Cloud WAN core network.

- [Create a VPC attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-vpc-attachment-add.html): This topic includes information about Connect attachment in a Cloud WAN core network, as well as Connect peers
- [View or edit a VPC attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-viewing-editing-vpc.html): View and edit a Cloud WAN core VP attachment.

### [Site-to-Site VPN attachments in Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-s2s-vpn-attachment.html)

This describes what you need to know about VPC attachments in your Cloud WAN core network.

- [Create a Site-to-Site VPN attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-vpn-attachment-add.html): Create a Site-to-Site VPN attachment for your Cloud WAN core network.
- [View or edit a Site-to-Site VPN attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-viewing-editing-vpn.html): View and edit a Cloud WAN core Site-to-Site VPN table attachment.

### [Transit gateway route table attachments](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tgw-attachment.html)

This describes what you need to know about transit gateway route talbe attachments in your Cloud WAN core network.

- [Create a transit gateway route table attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tgw-attachment-add.html): Add a transit gateway route table attachment to your Cloud WAN core network.
- [View or edit a transit gateway route table attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-viewing-editing-rtb.html): View and edit a Cloud WAN core network transit gateway route table attachment.
- [Accept or reject a core network attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-acceptance.html): Accept or reject a Cloud WAN core network attachment for segments requiring acceptance.
- [Delete an attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-deleting.html): Delete an existing Cloud WAN core network attachment.

### [Core network policy versions](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-policy-version.html)

Create a Cloud WAN core network policy version based on current LIVE version.

- [Service insertion](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-service-insertion.html): Cloud WAN service insertion allows you to send your network traffic to security appliances for added security .
- [Routing policies](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-routing-policies.html): Routing policies on Cloud WAN provide fine-grained routing controls to optimize route management, customize network behavior, and improve route scaling for global networks.

### [Create a policy version using the console](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-policy-console.html)

Create a Cloud WAN core network policy version using the Network Manager console to deploy as your new LIVE policy.

- [Configure the core network settings](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-core-network-config.html): Configure the network for a Cloud WAN core network policy version, including assigning ASNs, CIDR blocks, and edge locations.
- [Add a segment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-segments.html): Create a segment to divide your Cloud WAN global network into separate isolated networks, and then define the how it communicates with other segments.
- [Create a network function group](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-network-function-groups.html): Create a Cloud WAN network functions group to route traffic to security appliances.
- [Add a segment action](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-network-actions-routes.html): Segment actions allow you to optionally share your Cloud WAN segments or create routes.
- [Create a core network attachment policy](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-attachments.html): Attachment policies control how your Cloud WAN attachments map to your segments.
- [Create a route policy and rule](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-route-policy.html): Create routing policies and routing policy rules within your Cloud WAN policy document to control traffic flow, filter routes, and optimize network performance across segments and attachments.
- [Create an attachment routing policy](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-attachment-routing.html): Create attachment routing policies to determine which routing policies are associated with core network attachments.

### [Create a policy version using JSON](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-policy-json.html)

Create a AWS Cloud WAN core network policy version based on your existing LIVE version.

- [Core network policy version parameters](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policies-json.html): Create a Cloud WAN policy version using a JSON file, composed of these required and optional parameters.

### [Core network policy examples](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples.html)

Examples of Cloud WAN core network JSON policies.

- [Example: One segment, one AWS Region](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-one-segment-region.html): Example Cloud WAN policy that sets up one network in one AWS Region.
- [Example: Two segments, multiple Regions](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-two-segments-regions.html): Example Cloud WAN policy that sets up two networks across multiple AWS Regions.
- [Example: Edge consolidation](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-edge-consolidation.html): Example AWS Cloud WAN core network policy that creates two segments, development and hybrid.
- [Example: Development environment with tags and shared services](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-three-stage.html): This Cloud WAN core network policy creates a common software development lifecycle policy.
- [Example: Distributed WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-distributed-wan.html): Example Cloud WAN core network policy that creates a network across four Regions for a global wide-area network (WAN).
- [Example: Insert firewalls](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-firewalls.html): Example AWS Cloud WAN core network policy that sends all traffic from on-premises to AWS through a firewall.
- [Example: Service insertion](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-service-insertion.html): This AWS Cloud WAN policy example uses service insertion to send traffic first through an Inspection VPC.
- [Example: Routing Policies](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-examples-routing-policies.html): Example Cloud WAN policy that sets up multiple routing policies.
- [View a core network policy change set](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-version-view.html): View a Cloud WAN core network policy change set before deploying the policy.
- [Compare policy change set versions](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-version-compare.html): Compare two Cloud WAN core network policies to see changes between those two versions.
- [Deploy a core network policy version](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-version-deploy.html): Deploy a Cloud WAN core network policy to become the new live policy for your core network.
- [Delete a policy version](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-version-delete.html): Delete a Cloud WAN policy version.
- [Download a core network policy](https://docs.aws.amazon.com/network-manager/latest/cloudwan/ccloudwan-policy-version-download.html): Download any version of your Cloud WAN core network policy.
- [Restore an out-of-date core network policy version](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-version-restore.html): Restore an out-of-date Cloud WAN core network policy as the new live version.

### [Devices](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices.html)

Add a device to your Cloud WAN core network.

- [Add a device](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-add.html): Add a device to you Cloud WAN global network.
- [Delete a device](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-delete.html): Delete a device from your Cloud WAN core network.
- [Edit a device](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-device-edit.html): Edit a device in your Cloud WAN global network.

### [View device details](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-working.html)

View, update, or delete devices in your Cloud WAN core network.

- [Associate or disassociate a device](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-device-link-associate.html): Associate a link with a device in your Cloud WAN global network.
- [Associate or disassociate an on-premises link](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-on-premises.html): Associate or disassociate an on-premises device link association in your Cloud WAN global network.
- [Associate or disassociate a Connect peer link](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-connect-peer.html): Associate or disassociate a Connect peer device link association in your Cloud WAN global network.
- [Create or delete a device connection](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-connections.html): Create or delete a connection between two devices in your Cloud WAN global network.
- [View VPNs](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-vpns.html): View the VPNs associated with a device in your Cloud WAN global network.
- [Monitor devices](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-monitoring.html): Use CloudWatch metrics to monitor device events in your Cloud WAN global network.

### [Peerings](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-peerings.html)

Learn about transit gateway route evaluation and peerings in Cloud WAN.

- [Create a peering](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-peerings-create.html): Create a peering between transit gateways in Cloud WAN.
- [View peering details](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-peerings-view.html): View peering details between transit gateways in Cloud WAN.
- [Delete a peering](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-peerings-delete.html): Delete a peering between transit gateways in Cloud WAN.
- [Edit peering tags](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-peerings-edit.html): Edit the tags that are associated with transit gateway peering in Cloud WAN.

### [Prefix list associations](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-prefix-lists.html)

Prefix list associations for Cloud WAN core networks.

- [Create a prefix list association](https://docs.aws.amazon.com/network-manager/latest/cloudwan/create-prefix-list-association.html): Associate a prefix list with your Cloud WAN network resources to centrally manage IP address ranges.
- [Delete a prefix list association](https://docs.aws.amazon.com/network-manager/latest/cloudwan/delete-prefix-list-association.html): Remove a prefix list association from your Cloud WAN network resources when no longer needed.

### [Shared attachments](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-shared-attachments.html)

View your shared Cloud WAN transit gateway attachments and peerings.

- [Create a shared VPC attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-vpc-share-create.html): Create a shared VPC attachment in Cloud WAN.
- [Create a shared transit gateway route table attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tgw-share.html): Create a shared transit gateway route table attachment in your Cloud WAN core network.
- [Create a shared Direct Connect gateway attachment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-dx-share.html): Create a shared Direct Connect gate table attachment in your Cloud WAN core network.
- [View shared attachments](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-shared-view.html): View your shared Cloud WAN VPC and transit gateway attachments.

### [Shared core network](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-share-network.html)

Share a Cloud WAN core network across AWS accounts or across your organizations.

- [Share a core network](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-share-network-steps.html): Share a Cloud WAN core network across AWS accounts or across your organizations.
- [Stop sharing a core network](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-share-network-stop.html): Stop sharing a Cloud WAN core network with other AWS accounts or from across your organizations.

### [Shared peerings](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-shared-peerings.html)

View your shared Cloud WAN transit gateway attachments and peerings.

- [Create a shared peering](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-peerings-share-create.html): View your shared AWS Cloud WAN global network transit gateway peerings
- [Delete a shared peering](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-peerings-share-delete.html): Delete a shared transit gateway peering.
- [Edit tags for a shared peering](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-peerings-share-tags.html): Edit the key-value tags for a shared peering in your Cloud WAN global network.

### [Sites and links](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-sites-links.html)

Create a site in AWS Cloud WAN.

- [Create a site](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-sites-add.html): Create a site in AWS Cloud WAN.
- [View site details](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-sites-view.html): View the details of a Cloud WAN site, which is a representation of the physical location of your network.
- [Update a site](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-sites-update.html): Create a site in AWS Cloud WAN.
- [Delete a site](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-site-delete.html): Delete a site from your Cloud WAN global network.
- [Create a link](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-site-link-add.html): Create a link in your Cloud WAN global network.
- [Edit a device link](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-link-update.html): Edit the link between two devices in your Cloud WAN global network.
- [Delete a link](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-link-delete.html): Links represent connections between devices in your Cloud WAN global network.

### [Transit gateways](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tgws-about.html)

Transit gateways you've created in Amazon VPC can be registered in your Cloud WAN global network, allowing you to view and monitor those transit gateway resources.

- [Register a transit gateway](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-register-tgw.html): Create transit gateways in Amazon VPC, and then register those transit gateways in your Cloud WAN global network.


## [Global and core network dashboards](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-visualize-networks.html)

- [Access global network dashboards](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-visualize-networks-global.html): Visualize and monitor your global networks in the Network Manager console through a graphical representation of your global network topology.
- [Access core network dashboards](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-visualize-networks-core.html): Visualize and monitor your core networks through the Network Manager console through a graphical representation of your core network topology.


## [Transit gateway network and transit gateway dashboards](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-visualize-tgw.html)

- [Access transit gateway network dashboards](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tgw-networks.html): View Cloud WAN dashboard information about registered transit gateways in your core network.
- [Access transit gateway dashboards](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tgw-dashboard.html): Access and view dashboard information about transit gateways registered in your Cloud WAN global network.


## [Authentication and access control](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-security.html)

- [AWS managed policies](https://docs.aws.amazon.com/network-manager/latest/cloudwan/security-iam-awsmanpol.html): Learn about AWS managed policies for transit gateways and AWS Cloud WAN and recent changes to those policies.
- [Service-linked roles](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cwan-using-service-linked-roles.html): How service-linked roles are used by Cloud WAN


## [Events and metrics](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-events-metrics.html)

- [CloudWatch metrics](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-metrics.html): Learn about the features that you can use to monitor your Cloud WAN network.
- [Onboard CloudWatch Logs Insights](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-onboard-events.html): Onboard events with CloudWatch Logs Insights to view Cloud WAN events.
- [Monitor with Amazon CloudWatch Events](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-cloudwatch-events.html): Monitor Cloud WAN global and core networks using Amazon CloudWatch Events.
- [Monitor Cloud WAN with CloudWatch metrics](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-cloudwatch-metrics.html): This section describes how to use CloudWatch metrics for your AWS Cloud WAN global and core networks.
