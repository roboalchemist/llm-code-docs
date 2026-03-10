# Source: https://docs.aws.amazon.com/mediaconnect/latest/ug/llms.txt

# AWS Elemental MediaConnect User Guide

> Describes the components and features that provides and how to use them. Describes the components and features that provides and how to use them.

- [Getting started](https://docs.aws.amazon.com/mediaconnect/latest/ug/getting-started.html)
- [Quotas](https://docs.aws.amazon.com/mediaconnect/latest/ug/quotas.html)
- [Reference: Supported media standards](https://docs.aws.amazon.com/mediaconnect/latest/ug/reference-media-standards.html)
- [Document history](https://docs.aws.amazon.com/mediaconnect/latest/ug/doc-history.html)

## [What is MediaConnect?](https://docs.aws.amazon.com/mediaconnect/latest/ug/what-is.html)

- [Concepts and terminology](https://docs.aws.amazon.com/mediaconnect/latest/ug/what-is-concepts.html): To help you get started with AWS Elemental MediaConnect, and to understand how it works, refer to the follow key concepts and terminology
- [Accessing MediaConnect](https://docs.aws.amazon.com/mediaconnect/latest/ug/what-is-accessing.html): You can access AWS Elemental MediaConnect using any of the following methods:
- [Pricing](https://docs.aws.amazon.com/mediaconnect/latest/ug/what-is-pricing.html): As with other AWS products, there are no contracts or minimum commitments for using MediaConnect.
- [Regions and endpoints](https://docs.aws.amazon.com/mediaconnect/latest/ug/what-is-regions.html): To reduce data latency in your applications, AWS Elemental MediaConnect offers a regional endpoint to make your requests:
- [Open-source attributions](https://docs.aws.amazon.com/mediaconnect/latest/ug/mediaconnect-os-attributions.html): Learn more about AWS and how to use AWS Elemental MediaConnect to ingest manage video assets.


## [Use cases](https://docs.aws.amazon.com/mediaconnect/latest/ug/use-cases.html)

### [Distribution](https://docs.aws.amazon.com/mediaconnect/latest/ug/distribute-content.html)

You can use AWS Elemental MediaConnect to distribute content to different geographical locations.

- [Distributing content across Regions](https://docs.aws.amazon.com/mediaconnect/latest/ug/distribution-across-regions.html): Set up two AWS Elemental MediaConnect flows to distribute content from one AWS Region to another.
- [Distributing content to MediaLive](https://docs.aws.amazon.com/mediaconnect/latest/ug/distribution-to-medialive.html): Set up your AWS Elemental MediaConnect flows to be used as inputs to your AWS Elemental MediaLive channel.
- [Distributing content from a MediaLive multiplex](https://docs.aws.amazon.com/mediaconnect/latest/ug/distribution-from-medialive.html): When you create a multiplex in AWS Elemental MediaLive, the service creates an entitlement in MediaConnect for your own account.
- [Entitlements](https://docs.aws.amazon.com/mediaconnect/latest/ug/use-cases-entitlements.html): To share your content with another AWS account, add an entitlement to your flow.
- [Contribution for transport stream flows](https://docs.aws.amazon.com/mediaconnect/latest/ug/use-cases-contribution.html): You can use AWS Elemental MediaConnect to ingest your content from an on-premises contribution encoder into the AWS Cloud.
- [Contribution for CDI flows](https://docs.aws.amazon.com/mediaconnect/latest/ug/use-cases-cdi.html): Ingest your JPEG XS video into the AWS Cloud via the SMPTE 2110, part 22 transport standard.
- [CDI replication and monitoring](https://docs.aws.amazon.com/mediaconnect/latest/ug/use-cases-cdi-replication-monitoring.html): You can use AWS Elemental MediaConnect CDI workflows to replicate and distribute video to multiple destinations.
- [Receiving SRT content from MediaLive](https://docs.aws.amazon.com/mediaconnect/latest/ug/receiving_srt_output_from_medialive.html): This guide details the process of setting up MediaConnect to receive SRT output from a MediaLive channel.


## [Setting up](https://docs.aws.amazon.com/mediaconnect/latest/ug/setting-up.html)

- [Create non-admin roles](https://docs.aws.amazon.com/mediaconnect/latest/ug/setting-up-create-nonadmin-roles.html): Create a role and allow a user to assume that role with secure and temporary credentials that are limited to AWS Elemental MediaConnect.
- [(Optional) Set up encryption](https://docs.aws.amazon.com/mediaconnect/latest/ug/setting-up-encryption.html): Use encryption to protect your content from unauthorized use.


## [Using the router](https://docs.aws.amazon.com/mediaconnect/latest/ug/using-mediaconnect-router.html)

### [Managing network interfaces](https://docs.aws.amazon.com/mediaconnect/latest/ug/managing-router-network-interfaces.html)

Learn how to create and manage router network interfaces in MediaConnect.

- [Creating network interfaces](https://docs.aws.amazon.com/mediaconnect/latest/ug/creating-router-network-interfaces.html): Learn how to create router network interfaces in MediaConnect.
- [Viewing network interfaces](https://docs.aws.amazon.com/mediaconnect/latest/ug/viewing-router-network-interfaces.html): View details about your router network interfaces in MediaConnect, including their status and configuration information.
- [Updating network interfaces](https://docs.aws.amazon.com/mediaconnect/latest/ug/editing-router-network-interface.html): Learn how to update router network interface configurations to meet your changing network requirements.
- [Deleting network interfaces](https://docs.aws.amazon.com/mediaconnect/latest/ug/deleting-router-network-interface.html): Learn how to permanently remove router network interfaces that you no longer need.

### [Managing router I/Os](https://docs.aws.amazon.com/mediaconnect/latest/ug/managing-router-io.html)

Learn how to create and manage router I/Os in MediaConnect.

- [Creating router I/Os](https://docs.aws.amazon.com/mediaconnect/latest/ug/creating-router-io.html): Learn how to create router I/Os in MediaConnect.
- [Viewing router I/Os](https://docs.aws.amazon.com/mediaconnect/latest/ug/viewing-router-io.html): View details about your router inputs and outputs in MediaConnect, including their status and connection information.
- [Updating router I/Os](https://docs.aws.amazon.com/mediaconnect/latest/ug/editing-router-io.html): Learn how to update router I/O configurations in MediaConnect.
- [Starting router I/Os](https://docs.aws.amazon.com/mediaconnect/latest/ug/starting-router-io.html): Start a router input or output in MediaConnect and set the maximum bitrate so that your content can flow through the router.
- [Stopping router I/Os](https://docs.aws.amazon.com/mediaconnect/latest/ug/stopping-router-io.html): Learn how to stop router I/Os when you need to pause their operation and stop incurring charges.
- [Restarting router I/Os](https://docs.aws.amazon.com/mediaconnect/latest/ug/restarting-router-io.html): Restart a router input or output in MediaConnect to manually initiate maintenance or system updates.
- [Deleting router I/Os](https://docs.aws.amazon.com/mediaconnect/latest/ug/deleting-router-io.html): Learn how to permanently remove router I/Os that you no longer need.
- [Understanding I/O states](https://docs.aws.amazon.com/mediaconnect/latest/ug/io-state-changes.html): Learn about the I/O lifecycle and the transitions between I/O states.
- [Integrating flows](https://docs.aws.amazon.com/mediaconnect/latest/ug/integrate-flow-with-router.html): Learn about how to connect your flows to your router I/Os.
- [Integrating MediaLive inputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/integrate-eml-with-router.html): Learn about how to connect your MediaLive inputs to your router outputs.
- [Source failover](https://docs.aws.amazon.com/mediaconnect/latest/ug/router-input-failover.html): Learn how you can set up two redundant sources for a router input, to prevent any disruption to the video stream.

### [Managing routes](https://docs.aws.amazon.com/mediaconnect/latest/ug/assigning-route.html)

Learn how to control the flow of content through the MediaConnect router.

- [Control panel view](https://docs.aws.amazon.com/mediaconnect/latest/ug/using-router-control-panel.html): Learn how to use the router control panel in MediaConnect to manage your video routing operations in real-time.
- [Matrix view](https://docs.aws.amazon.com/mediaconnect/latest/ug/using-router-matrix-editor.html): Learn how to manage multiple MediaConnect routes at once and save routing configurations for quick access.


## [Using flows](https://docs.aws.amazon.com/mediaconnect/latest/ug/using-mediaconnect-flows.html)

### [Managing flows](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows.html)

Create a flow to establish a transport between a source and one or more outputs.

### [Creating a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-create.html)

When you set up a new flow, you specify settings such as a name for the flow and the Availability Zone.

- [Transport stream flow, standard source](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-create-standard-source.html): When you set up a new flow, you specify settings such as a name for the flow and the Availability Zone.
- [Transport stream flow, entitled source](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-create-entitled-source.html): When you set up a new flow, you specify settings such as a name for the flow and the Availability Zone.
- [Transport stream flow, VPC source](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-create-vpc-source.html): When you create a flow that uses a source from your virtual private cloud (VPC), your content does not go over the public internet.
- [CDI source](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-create-cdi.html): Learn how to set up a CDI flow to ingest uncompressed JPEG XS video into the AWS Cloud via the SMPTE 2110, part 22 transport standard.
- [NDI source](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-create-ndi.html): Learn how use MediaConnect to create flows that ingest content from NDIÂ® discovery servers within your VPC
- [Viewing a list of flows](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-view-list.html): View a list of your AWS Elemental MediaConnect flows in a specific AWS Region.
- [Viewing the details of a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-view-details.html): View the details of a flow in AWS Elemental MediaConnect using the console or the AWS CLI.
- [Starting a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-start.html): After you create a flow, you must start the flow.
- [Stopping a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-stop.html): When you stop an active flow, it immediately becomes unavailable to customers who are accessing the output directly from your AWS Elemental MediaConnect flow or through an entitlement.

### [Updating a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-update.html)

You can change a flow's size, source, entitlements, outputs and several other settings.

- [Updating the flow size](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-update-size.html): Updating the flow size allows you to modify the processing capacity and feature set that's available for your MediaConnect flow.
- [Updating NDI configuration](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-update-ndi-configuration.html): Updating the flow NDIÂ® configuration allows you to determine how this flow communicates with the rest of your NDI environment.

### [Managing tags on a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-manage-tags.html)

Use tags to help you track the billing and organization for your AWS Elemental MediaConnect flows, sources, outputs, and entitlements.

- [Adding tags on a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-manage-tags-add.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect flows.
- [Editing tags on a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-manage-tags-edit.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect flows.
- [Removing tags from a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-manage-tags-remove.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect flows.
- [Deleting a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-delete.html): When you delete an active flow, it immediately becomes unavailable to customers who are accessing the output directly from your AWS Elemental MediaConnect flow or through an entitlement.
- [Flow sizes and capabilities](https://docs.aws.amazon.com/mediaconnect/latest/ug/flow-sizes-capabilities.html): A flow size determines how much video throughput your flow can handle and which source and output types it supports.

### [Managing sources](https://docs.aws.amazon.com/mediaconnect/latest/ug/sources.html)

Each AWS Elemental MediaConnect flow has at least one source and as many as two sources.

- [NDI sources](https://docs.aws.amazon.com/mediaconnect/latest/ug/sources-using-ndi.html): AWS Elemental MediaConnect can ingest Network Device Interface (NDIÂ®), a protocol for high-quality, low-latency video and audio over IP networks, and convert it into MPEG transport streams.

### [Adding a second source to a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/source-adding.html)

If your flow has only one source, you can add a second source later.

- [Standard source](https://docs.aws.amazon.com/mediaconnect/latest/ug/source-adding-standard.html): If your flow has only one source, you can add a second source later.
- [VPC source](https://docs.aws.amazon.com/mediaconnect/latest/ug/source-adding-vpc.html): If your flow has only one source, you can add a second source later.
- [Updating a source](https://docs.aws.amazon.com/mediaconnect/latest/ug/source-update.html): You can update the source of an existing flow, even when the flow is currently running.
- [Source failover](https://docs.aws.amazon.com/mediaconnect/latest/ug/source-failover.html): Learn how you can set up two redundant sources for a flow, to prevent any disruption to the video stream.

### [Managing tags on a source](https://docs.aws.amazon.com/mediaconnect/latest/ug/sources-manage-tags.html)

Use tags to help you track the billing and organization for your AWS Elemental MediaConnect sources.

- [Adding tags on a source](https://docs.aws.amazon.com/mediaconnect/latest/ug/sources-manage-tags-add.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect sources.
- [Editing tags on a source](https://docs.aws.amazon.com/mediaconnect/latest/ug/sources-manage-tags-edit.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect sources.
- [Removing tags from a source](https://docs.aws.amazon.com/mediaconnect/latest/ug/sources-manage-tags-remove.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect sources.
- [Removing a source from a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/source-remove.html): If a flow has more than one source, you can remove one of the sources even when the flow is currently running.
- [Source ports](https://docs.aws.amazon.com/mediaconnect/latest/ug/source-ports.html): Each source on an AWS Elemental MediaConnect flow must come in from a different port.
- [Determining a source's peer IP address](https://docs.aws.amazon.com/mediaconnect/latest/ug/source-ip-address.html): Learn how to identify the peer IP address for a flow source so that you can monitor connected devices and troubleshoot connecitvity issues.

### [Managing outputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs.html)

Add outputs to define the destinations where you want to send the content of your flow.

- [NDI outputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-using-ndi.html): AWS Elemental MediaConnect can convert MPEG transport streams into Network Device Interface (NDIÂ®), a protocol for high-quality, low-latency video and audio over IP networks.

### [Adding outputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-add.html)

Add outputs to define the different destinations where you want MediaConnect to send the content of your flow.

- [Adding standard outputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-add-standard.html): You can add up to 50 outputs for each flow in AWS Elemental MediaConnect.
- [Adding VPC outputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-add-vpc.html): Add VPC outputs to direct AWS Elemental MediaConnect to send content to a virtual private cloud (VPC) that you created using Amazon Virtual Private Cloud.
- [Adding NDI outputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-add-ndi.html): This procedure walks you through the process of setting up an NDIÂ® output and configuring how your NDI video streams appear to other devices in your VPC network.
- [Viewing outputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-view-list.html): In AWS Elemental MediaConnect, you can view a list of a flow's outputs, along with the setup that is associated with each output.
- [Updating outputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-update.html): You can update outputs on an existing flow using the AWS Elemental MediaConnect console or AWS CLI.

### [Managing tags on an output](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-manage-tags.html)

Use tags to help you track the billing and organization for your AWS Elemental MediaConnect outputs.

- [Adding tags on an output](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-manage-tags-add.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect outputs.
- [Editing tags on an output](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-manage-tags-edit.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect outputs.
- [Removing tags from an output](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-manage-tags-remove.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect flows, sources, outputs, and entitlements.
- [Disabling or removing outputs](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-remove.html): You can disable or remove outputs that you added to the flow.
- [Output destinations](https://docs.aws.amazon.com/mediaconnect/latest/ug/destinations.html): Each output on an AWS Elemental MediaConnect flow must be sent to a different destination.
- [Determining an output's IP address](https://docs.aws.amazon.com/mediaconnect/latest/ug/output-ip-address.html): For flows that use listener protocols (such as Zixi pull or SRT listener), the receiver requires the IP address of the output to establish a connection with the flow.

### [Managing entitlements](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements.html)

Grant entitlements on your flow to share content with other AWS accounts (subscriber accounts).

### [Sharing content with other AWS accounts](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-originator.html)

Share your content with other AWS accounts by granting entitlements on your AWS Elemental MediaConnect flows.

- [Granting an entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-grant.html): Grant an entitlement to another AWS account (subscriber account) to share your flow.
- [Updating an entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-update.html): After an entitlement has been created, you can still update the description, status, and subscribers.

### [Managing tags on an entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-manage-tags.html)

Use tags to help you track the billing and organization for your AWS Elemental MediaConnect flows, sources, outputs, and entitlements.

- [Adding tags on a entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-manage-tags-add.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect entitlements.
- [Editing tags on a entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-manage-tags-edit.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect entitlements.
- [Removing tags from a entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-manage-tags-remove.html): Use tags to help you track the billing and organization for your AWS Elemental MediaConnect entitlement.
- [Revoking an entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-revoke.html): Revoke an entitlement to stop allowing a particular subscriber account to access your content.
- [Disabling an entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-disable.html): Disable an entitlement to stop streaming content to the subscriberâs flow on a temporary basis.
- [Enabling an entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-enable.html): If an entitlement has been disabled, you can enable it to reinstate full access for the subscriber account.
- [Subscribing to content provided by another AWS account](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-subscriber.html): When another AWS account (originator account) grants an entitlement to your AWS account (subscriber account), you can create an AWS Elemental MediaConnect flow that uses the originator's content as your source.

### [VPC interfaces](https://docs.aws.amazon.com/mediaconnect/latest/ug/vpc-interfaces.html)

A virtual private cloud (VPC) based on the Amazon Virtual Private Cloud service is your private, logically isolated network in the AWS Cloud.

- [Adding a VPC interface](https://docs.aws.amazon.com/mediaconnect/latest/ug/vpc-interface-add.html): To avoid streaming your content over the public internet, you can add a VPC interface to your MediaConnect flow.
- [Removing a VPC interface](https://docs.aws.amazon.com/mediaconnect/latest/ug/vpc-interface-remove.html): You can remove a VPC interface from your flow if it isn't used as a source for the flow.
- [Security group considerations](https://docs.aws.amazon.com/mediaconnect/latest/ug/vpc-interface-security-groups.html): When you set up a virtual private cloud (VPC) in Amazon Virtual Private Cloud, you create security groups that control inbound and outbound traffic.

### [Protocols](https://docs.aws.amazon.com/mediaconnect/latest/ug/protocols.html)

AWS Elemental MediaConnect supports multiple protocols for incoming (source) and outgoing (output) live video streams: Zixi, SRT, RIST, RTP-FEC, RTP, ST 2110 JPEG XS, and CDI.

- [Color support for CDI protocols](https://docs.aws.amazon.com/mediaconnect/latest/ug/protocol-color.html): MediaConnect CDI flows support multiple configurations of color space, bit depth, and chroma sampling for each protocol.

### [Media streams](https://docs.aws.amazon.com/mediaconnect/latest/ug/media-streams.html)

Learn how to use media streams in a MediaConnect flow.

- [Adding a media stream to a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/media-stream-add.html): Learn how to add a media stream to a MediaConnect flow.
- [Updating a media stream](https://docs.aws.amazon.com/mediaconnect/latest/ug/media-stream-update.html): Learn how to update a media stream on a MediaConnect flow.
- [Removing a media stream](https://docs.aws.amazon.com/mediaconnect/latest/ug/media-stream-remove.html): Learn how to remove a media stream from a MediaConnect flow.
- [Best practices](https://docs.aws.amazon.com/mediaconnect/latest/ug/best-practices.html): Learn best practices for optimizing flows performance with AWS Elemental MediaConnect.


## [Using gateways](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway.html)

- [Supported OS and architectures](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-prerequisites.html)
- [Networks](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-networks.html): Learn how a MediaConnect Gateway network is used to communicate on your local data center network.

### [Gateways](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-gateways.html)

Learn how to create and manage MediaConnect Gateway gateways.

- [Setting up a gateway](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-create.html)
- [Removing a gateway](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-cleanup-console.html)

### [Instances](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-instances.html)

Learn how MediaConnect Gateway uses on-premises computing resources to connect your data center to AWS.

- [Registering an instance](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-instances-create.html)
- [Deregistering an instance](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-instances-delete.html)

### [Bridges](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-bridges.html)

Learn how MediaConnect Gateway uses bridges to connect your data center to AWS.

- [Creating a bridge](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-bridges-create.html): After you have registered at least one instance to your gateway, you can create a bridge.


## [Reservations](https://docs.aws.amazon.com/mediaconnect/latest/ug/reservations.html)

- [Viewing reservations](https://docs.aws.amazon.com/mediaconnect/latest/ug/reservations-view.html): On the console, you can view the reservations that you have purchased.

### [Offerings](https://docs.aws.amazon.com/mediaconnect/latest/ug/offerings.html)

Offerings are discounts that MediaConnect offers in exchange for a commitment to use a certain amount of outbound bandwidth each month.

- [Viewing offerings](https://docs.aws.amazon.com/mediaconnect/latest/ug/offerings-view.html): On the console, you can view the offerings that are available in the current AWS Region.
- [Purchasing an offering](https://docs.aws.amazon.com/mediaconnect/latest/ug/offerings-purchase.html): If your account doesn't already have an active reservation, you can purchase an offering to create a new reservation.


## [Security](https://docs.aws.amazon.com/mediaconnect/latest/ug/security.html)

### [Data protection](https://docs.aws.amazon.com/mediaconnect/latest/ug/data-protection.html)

Protect your data using tools that are provided by AWS and AWS Elemental MediaConnect.

### [Static key encryption](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-static-key.html)

Protect your content from unauthorized use through encryption.

- [Key management for static key encryption](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-static-key-key-management.html): Store your encryption keys in AWS Secrets Manager when you use static key encryption to protect your sources, outputs, entitlements and router I/O from unauthorized use.
- [Setting up static key encryption](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-static-key-set-up.html): Before you can create a flow or a router I/O with an encrypted source or an output, or an entitlement that uses static key encryption, you must set up encryption.

### [SPEKE encryption](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-speke.html)

Use Secure Packager and Encoder Key Exchange (SPEKE) with AWS Elemental MediaConnect to encrypt an entitlement.

- [Key management for SPEKE](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-speke-key-management.html): Use Secure Packager and Encoder Key Exchange (SPEKE) with AWS Elemental MediaConnect for encryption.
- [Setting up SPEKE encryption](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-speke-set-up.html): Before you can grant an entitlement that uses Secure Packager and Encoder Key Exchange (SPEKE) encryption, you must set up encryption.

### [SRT password encryption](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-srt-password.html)

Protect your content from unauthorized use through encryption.

- [Password management for SRT password encryption](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-srt-password-password-management.html): Store your passwords in AWS Secrets Manager when you use SRT password encryption to protect your sources, outputs and router I/O from unauthorized use.
- [Setting up SRT password encryption](https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-srt-password-set-up.html): Before you can create a flow or a router I/O that uses SRT password encryption, you must set up encryption.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/mediaconnect/latest/ug/internetwork-traffic-privacy.html): MediaConnect's virtual private cloud (VPC) support allows you to route traffic directly to and from your corporate network via a VPN connection over the internet or a private physical connection using Direct Connect connection.

### [Identity and access management](https://docs.aws.amazon.com/mediaconnect/latest/ug/security-iam.html)

How to authenticate requests and manage access your MediaConnect resources.

- [How MediaConnect works with IAM](https://docs.aws.amazon.com/mediaconnect/latest/ug/security_iam_service-with-iam.html): Before you use IAM to manage access to MediaConnect, you should understand what IAM features are available to use with MediaConnect.
- [Identity-based policy examples](https://docs.aws.amazon.com/mediaconnect/latest/ug/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify MediaConnect resources.
- [Resource-based policy examples](https://docs.aws.amazon.com/mediaconnect/latest/ug/security_iam_resource-based-policy-examples.html): To access the AWS Elemental MediaConnect console, you must have a minimum set of permissions that allows you to list and view details about the MediaConnect resources in your AWS account.
- [Policy examples for secrets in AWS Secrets Manager](https://docs.aws.amazon.com/mediaconnect/latest/ug/iam-policy-examples-asm-secrets.html): Learn how to create IAM policies that allow MediaConnect to read encryption keys that are stored as secrets in Secrets Manager.
- [AWS managed policies](https://docs.aws.amazon.com/mediaconnect/latest/ug/security-iam-awsmanpol.html): Learn about AWS managed policies for MediaConnect and recent changes to those policies.

### [Using service-linked roles](https://docs.aws.amazon.com/mediaconnect/latest/ug/using-service-linked-roles.html)

How to use service-linked roles to give MediaConnect access to resources in your AWS account.

- [Service-linked role permissions for MediaConnect](https://docs.aws.amazon.com/mediaconnect/latest/ug/slr-permissions.html): MediaConnect uses the service-linked role named AWSServiceRoleForMediaConnect.
- [Creating a service-linked role for MediaConnect](https://docs.aws.amazon.com/mediaconnect/latest/ug/create-slr.html): You don't need to manually create a service-linked role.
- [Editing a service-linked role](https://docs.aws.amazon.com/mediaconnect/latest/ug/edit-slr.html): MediaConnect does not allow you to edit the AWSServiceRoleForMediaConnect service-linked role.
- [Deleting a service-linked role for MediaConnect](https://docs.aws.amazon.com/mediaconnect/latest/ug/delete-slr.html): If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role.
- [Setting up MediaConnect as a trusted service](https://docs.aws.amazon.com/mediaconnect/latest/ug/security-iam-trusted-entity.html): You can use AWS Identity and Access Management (IAM) to control which AWS resources can be accessed by which users and applications.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/mediaconnect/latest/ug/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Troubleshooting](https://docs.aws.amazon.com/mediaconnect/latest/ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with MediaConnect and IAM.
- [Logging and monitoring](https://docs.aws.amazon.com/mediaconnect/latest/ug/incident-response.html): Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Elemental MediaConnect and your AWS solutions.
- [Compliance validation](https://docs.aws.amazon.com/mediaconnect/latest/ug/mediaconnect-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/mediaconnect/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Elemental MediaConnect features for data resiliency.

### [Infrastructure security](https://docs.aws.amazon.com/mediaconnect/latest/ug/infrastructure-security.html)

Learn how AWS Elemental MediaConnect isolates service traffic.

- [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/mediaconnect/latest/ug/vpc-endpoints.html): You can use a VPC endpoint to create a private connection between your VPC and MediaConnect without requiring access over the internet or through a NAT instance, a VPN connection, or Direct Connect.


## [Monitoring and tagging](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor.html)

### [Monitoring with the MediaConnect console](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-the-media-connect-console.html)

Use AWS Elemental MediaConnect to monitor your resources directly within the MediaConnect console.

### [Monitoring with content quality analysis](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-content-quality-analysis.html)

In the AWS Elemental MediaConnect console, you can use content health analysis to detect quality issues in your source streams.

- [Enabling content quality analysis](https://docs.aws.amazon.com/mediaconnect/latest/ug/enable-content-quality-analysis.html): Learn how to enable content quality analysis in the AWS Elemental MediaConnect console and the AWS CLI.
- [Viewing content quality issues](https://docs.aws.amazon.com/mediaconnect/latest/ug/content-quality-analysis-viewing.html): When you enable content quality analysis, MediaConnect starts posting warnings and alerts for the enabled metrics in your AWS account.
- [Disabling content quality analysis](https://docs.aws.amazon.com/mediaconnect/latest/ug/disable-content-quality-analysis.html): You can disable the content quality analysis feature without losing your previously configured settings for individual metrics.

### [Monitoring with thumbnails](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-thumbnails.html)

Learn how to create thumbnails in AWS Elemental MediaConnect, in order to verify that there is video in a flow.

- [Requirements](https://docs.aws.amazon.com/mediaconnect/latest/ug/thumbnails-specifications.html): Read about the requirements that the video source and the flow must meet in order for AWS Elemental MediaConnect to generate thumbnails.
- [View thumbnails using the console](https://docs.aws.amazon.com/mediaconnect/latest/ug/thumbnails-enable-view-console.html): Learn how to enable and view thumbnails so that you can use the AWS Elemental MediaConnect console to verify that video is present in the source.
- [Enabling and retrieving thumbnails programmatically](https://docs.aws.amazon.com/mediaconnect/latest/ug/thumbnails-enable-retrieve-programatically.html): Learn how to enable and retrieve thumbnails programmatically so that you can verify that video is present in the source of an AWS Elemental MediaConnect flow.
- [Monitoring using source metadata](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-source-stream-monitoring.html): Monitor AWS Elemental MediaConnect using source metadata monitoring, which displays media information about the source transport stream and its programs.

### [Monitoring flow and source health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-flow-and-source-health.html)

On the AWS Elemental MediaConnect console, you can monitor the health of your flows and their sources.

- [Monitoring flow health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-flow-health.html): On the AWS Elemental MediaConnect console, you can view a list of alerts that occurred when you started or stopped the flow.
- [Monitoring source health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-source-health.html): In the AWS Elemental MediaConnect console, you can view Amazon CloudWatch metrics that show the health of the source over a period of time.

### [Monitoring with CloudWatch metrics](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch.html)

Monitor AWS Elemental MediaConnect using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.

- [Definition of a metric](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metric-info.html): Learn some general tips about AWS Elemental MediaConnect metrics.
- [Viewing metrics](https://docs.aws.amazon.com/mediaconnect/latest/ug/emx-metrics-view.html): You can view some metrics in the MediaConnect console.
- [Metrics to monitor flow health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metrics-flow-health.html): AWS Elemental MediaConnect sends metrics to CloudWatch.
- [Metrics to monitor flow source health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metrics-source-health.html): AWS Elemental MediaConnect sends metrics to CloudWatch.
- [Metrics to monitor flow output health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metrics-output-health.html): AWS Elemental MediaConnect sends metrics to CloudWatch.
- [Metrics to monitor media health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metrics-media-health.html): AWS Elemental MediaConnect sends metrics to CloudWatch.
- [Metrics to monitor gateway health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metrics-gateway-health.html): AWS Elemental MediaConnect sends metrics to CloudWatch.
- [Metrics to monitor content quality](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metrics-content-quality.html): AWS Elemental MediaConnect sends metrics to CloudWatch.
- [Metrics to monitor router input health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metrics-router-input-health.html): AWS Elemental MediaConnect sends metrics to CloudWatch.
- [Metrics to monitor router output health](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metrics-router-output-health.html): AWS Elemental MediaConnect sends metrics to CloudWatch.
- [Using metrics to troubleshoot](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch-metrics-troubleshooting.html): You can monitor the health of your stream by reviewing the metrics that AWS Elemental MediaConnect sends to CloudWatch.

### [Monitoring with EventBridge events](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitoring-with-cloudwatch-events.html)

Automate AWS Elemental MediaConnect with other AWS services by using Amazon EventBridge.

- [Flow state change event](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitoring-cloudwatch-events-flow-state-change.html): The AWS Elemental MediaConnect Flow State Change event is published when a flow's state has changed.
- [Flow maintenance event](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitoring-cloudwatch-events-flow-maintenance.html): The AWS Elemental MediaConnect Flow Maintenance event is published when a flow's status has changed because of maintenance.
- [Flow health event](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitoring-cloudwatch-events-flow-health.html): Learn how an AWS Elemental MediaConnect flow health event is published, and how flow health indicator states affect the event.
- [Alert event](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitoring-cloudwatch-events-alert.html): Learn how to view an AWS Elemental MediaConnect alert event when an active alert is present on a running resource.
- [Source health event](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitoring-cloudwatch-events-source-health.html): The AWS Elemental MediaConnect source health event is published when a source health indicator changes state.
- [Output health event](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitoring-cloudwatch-events-output-health.html): Learn how the AWS Elemental MediaConnect output health event is published when an output health indicator changes state.
- [Content quality event](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitoring-eventbridge-events-content-quality.html): Learn how the AWS Elemental MediaConnect content quality event is published when a metric duration threshold is breached.
- [Logging API calls with AWS CloudTrail](https://docs.aws.amazon.com/mediaconnect/latest/ug/logging-using-cloudtrail.html): Learn about logging AWS Elemental MediaConnect with AWS CloudTrail.

### [Tagging resources](https://docs.aws.amazon.com/mediaconnect/latest/ug/tagging.html)

Create, view, edit, and delete tags on flows, entitlements, and outputs in AWS Elemental MediaConnect.

- [Supported resources](https://docs.aws.amazon.com/mediaconnect/latest/ug/supported-resources.html): The following resources in AWS Elemental MediaConnect support tagging:
- [Tag naming and usage conventions](https://docs.aws.amazon.com/mediaconnect/latest/ug/tagging-restrictions.html): The following basic naming and usage conventions apply to using tags with AWS Elemental MediaConnect resources:
- [Managing tags](https://docs.aws.amazon.com/mediaconnect/latest/ug/tagging-add-edit-delete.html)

### [Workflow monitor](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor.html)

Analyze AWS media services and create signal maps between those services.

### [Configuring workflow monitor](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure.html)

To setup workflow monitor for the first time; you create the alarm and event templates, and discover signal maps that are used to monitor your media workflows.

### [Getting started](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-getting-started.html)

The following steps provide a basic overview of using workflow monitor for the first time.

- [Workflow monitor IAM policies](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-getting-started-IAM.html): Workflow monitor interacts with multiple AWS services to create signal maps, build CloudWatch and EventBridge resources, and CloudFormation templates.

### [Templates](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-templates.html)

Learn how to configure the alarm and event templates that will be used to monitor your workflow.

### [CloudWatch alarms](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)

Learn how to configure the alarm groups and templates that will be used to monitor your workflow.

- [Recommended templates](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-alarms-recommended-templates.html): Learn how to use the recommended alarm templates created by AWS.
- [EventBridge rules](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-notifications.html): Learn how to configure the EventBridge groups and templates that will be used to monitor your workflow.

### [Signal maps](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-signal-maps.html)

Learn how to configure the workflow monitor signal maps.

- [Creating signal maps](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-create.html): Learn how to create the workflow monitor signal maps using the automatic discovery process.
- [Viewing signal maps](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-view.html): Workflow monitor signal maps allow you to see a visual mapping of all connected AWS resources in your media workflow.
- [Attaching templates](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-attach.html): After you have created alarm and event templates, you need to attach these to a signal map.
- [Deploying monitoring templates](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-deploy.html): After you have attached the alarm and event templates to your signal map, you must deploy the monitoring.
- [Updating signal maps](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-update.html): If a change is made to your workflow, you might need to rediscover the signal map and redeploy monitoring resources.
- [Deleting signal maps](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-delete.html): If you not longer need a signal map, it can be deleted.
- [Quotas](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-quotas.html): The following section contains quotas for workflow monitor resources.

### [Using workflow monitor](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-operate.html)

Use the overview and signal maps sections of the workflow monitor console to review the current status of the workflows and any associated alarms, metrics, and logs.

- [Overview](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-operate-overview.html): The Overview section of the workflow monitor console is a dashboard that provides at-a-glance information about your signal maps.
- [Logs and metrics](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-operate-logs-metrics.html): To view CloudWatch metrics and logs for a signal map, select the radio button next to the name of the signal map.
- [Using signal maps](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-operate-signal-maps.html): From the overview section of the console, you can select a specific signal map to view more information about that signal map and its attached monitoring resources.


## [Maintenance](https://docs.aws.amazon.com/mediaconnect/latest/ug/maintenance.html)

- [Viewing flows that require maintenance](https://docs.aws.amazon.com/mediaconnect/latest/ug/viewing-flows-maintenance.html): You can view flows that require maintenance in the MediaConnect console or by using the AWS CLI.
- [Setting maintenance windows](https://docs.aws.amazon.com/mediaconnect/latest/ug/setting-flow-maintenance.html): You can select the day and time that maintenance events occur.
