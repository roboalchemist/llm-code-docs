# Source: https://docs.aws.amazon.com/global-accelerator/latest/dg/llms.txt

# AWS Global Accelerator Developer Guide

> AWS Global Accelerator is a network layer service that you use to create accelerators that direct traffic to optimal endpoints over the AWS global network.

- [API actions](https://docs.aws.amazon.com/global-accelerator/latest/dg/global-accelerator-actions.html)
- [Quotas](https://docs.aws.amazon.com/global-accelerator/latest/dg/limits-global-accelerator.html)
- [Related information](https://docs.aws.amazon.com/global-accelerator/latest/dg/Resources.html)
- [Document history](https://docs.aws.amazon.com/global-accelerator/latest/dg/WhatsNew.html)

## [What is AWS Global Accelerator?](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

- [Components](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-components.html): AWS Global Accelerator includes the following components:
- [AWS Regions](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.regions.html): An overview of the Regional and Availability Zone support for AWS Global Accelerator.
- [How it works](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works.html): The static IP addresses provided by AWS Global Accelerator serve as single fixed entry points for your clients.
- [IP address ranges](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-ip-ranges.html): View location of and IP address ranges of the AWS Global Accelerator edge servers.
- [Use cases](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-benefits-of-migrating.html): Using AWS Global Accelerator can help you accomplish a variety of goals.
- [Speed Comparison Tool](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-speed-comparison-tool.html): You can use the AWS Global Accelerator Speed Comparison Tool to see Global Accelerator download speeds compared to direct internet downloads, across AWS Regions.
- [How to get started](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-get-started.html): You can get started with setting up AWS Global Accelerator by using the API or by using the AWS Global Accelerator console.
- [Tagging](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html): Using tagging for billing and other purposes in AWS Global Accelerator.
- [Pricing](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-pricing.html): With AWS Global Accelerator, you are charged a fixed hourly fee for each accelerator that is provisioned in your account (whether it's enabled or disabled), and an incremental charge, in addition to standard data transfer rates, for every hour of traffic in the dominant direction that flows through the accelerator.


## [Getting started](https://docs.aws.amazon.com/global-accelerator/latest/dg/getting-started.html)

- [Create a standard accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/getting-started-standard.html): This section provides steps for creating a standard accelerator, which routes traffic to an optimal endpoint.
- [Create a custom routing accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/getting-started-custom-routing.html): This section provides steps for creating a custom routing accelerator, which routes traffic deterministically to Amazon EC2 instance destinations in virtual private cloud (VPC) subnet endpoints.


## [Working with standard accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/work-with-standard-accelerators.html)

### [Standard accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html)

Create a standard accelerator in AWS Global Accelerator.

- [Create accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.creating-editing.html): This section explains how to create a standard accelerator on the console.
- [Update accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.editing.html): This section explains how to update a standard accelerator on the console.
- [Delete accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.deleting.html): If you created an accelerator as a test or if you're no longer using an accelerator, you can delete it.
- [View accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.viewing.html): You can view information about your accelerators on the console.
- [Integrate Global Accelerator with load balancer creation](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.alb-accelerator.html): When you create an Application Load Balancer or Network Load Balancer in the AWS Management Console, you can optionally add an accelerator at the same time.
- [Compare global and regional addresses](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.eip-accelerator.html): If you want to use a static IP address in front of an AWS resource, such as an Amazon EC2 instance, you have several options.

### [Listeners for standard accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.html)

With AWS Global Accelerator, you add listeners that process inbound connections from clients based on the ports and protocols that you specify.

- [Add listener](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.creating-listeners.html): This section provides the steps to create a standard listener on the AWS Global Accelerator console.
- [Edit listener](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.creating-listeners-edit.html): This section provides the steps to edit a standard listener on the AWS Global Accelerator console.
- [Remove listener](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.creating-listeners-remove.html): This section provides the steps to remove a standard listener on the AWS Global Accelerator console.
- [How client affinity works](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners-client-affinity.html): If you have stateful applications that you use with a standard accelerator, you can configure client affinity to have Global Accelerator direct all requests from a user at a specific source (client) IP address to the same endpoint resource.

### [Endpoint groups for standard accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.html)

Use an endpoint group to route requests to one or more endpoints in a standard accelerator in AWS Global Accelerator.

- [Add endpoint group](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.create-endpoint-group.html): You work with endpoint groups on the AWS Global Accelerator console or by using an API operation.
- [Edit endpoint group](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.edit-endpoint-group.html): This section explains how to edit a standard endpoint groups on the AWS Global Accelerator console.
- [Remove endpoint group](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.delete-endpoint-group.html): This section explains how to remove a standard endpoint groups on the AWS Global Accelerator console.
- [Adjust traffic flow with traffic dials](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-traffic-dial.html): For each standard endpoint group, you can set a traffic dial to control the percentage of traffic that is directed to the endpoint group (AWS Region).
- [Override listener ports](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html): By default, an accelerator routes user traffic to endpoints in AWS Regions using the protocol and port ranges that you specify when you create a listener.
- [Ensure health check access](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-health-check-options.html): Each listener for a standard accelerator routes requests only to healthy, active endpoints.

### [Endpoints for standard accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.html)

Add and remove endpoints with standard accelerators in AWS Global Accelerator.

- [Endpoint requirements](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-caveats.html): Be aware of the following requirements and limitations for different types of resources that you can add as endpoints for standard accelerators in AWS Global Accelerator.
- [Add endpoint](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-adding-endpoints.html): You add endpoints to endpoint groups so that traffic can be directed to your resources.
- [Edit endpoint](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-adding-endpoints-edit.html): This section explains how to edit an endpoint on the AWS Global Accelerator console.
- [Remove endpoint](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-adding-endpoints-remove.html): This section explains how to remove an endpoint on the AWS Global Accelerator console.
- [How endpoint weights work](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html): Weighted routing lets you choose how much traffic is routed to a specific resource (endpoint) in an endpoint group.
- [Failover for unhealthy endpoints](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.unhealthy-endpoints.html): If there are no healthy endpoints in an endpoint group that have a weight greater than zero, Global Accelerator tries to fail over to a healthy endpoint with a weight greater than zero in another endpoint group.
- [Avoid TCP connection time delays](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.avoid-connection-collisions.html): Intermittent connectivity issues can be caused by connection collisions in AWS Global Accelerator.


## [Working with custom routing accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/work-with-custom-routing-accelerators.html)

- [How custom routing accelerators work](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-how-it-works.html): Learn about how custom routing accelerators work in AWS Global Accelerator.
- [Custom routing example](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-how-it-works.example.html): As an example, let's say that you want to support 10,000 sessions where groups of users interact, such as gaming sessions or VoIP call sessions, across 1,000 Amazon EC2 instances behind Global Accelerator.
- [Custom routing guidelines](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-guidelines.html): Guidelines and restrictions for using custom routing accelerators in AWS Global Accelerator.

### [Custom routing accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.html)

Create, edit, or delete a custom routing accelerator in AWS Global Accelerator.

- [Create a custom routing accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.creating-editing.html): This section provides steps for how to create a custom accelerator on the console.
- [Edit a custom routing accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.editing.html): This section provides steps for how to update a custom accelerator on the console.
- [View custom routing accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.viewing.html): This section provides steps to view information about your custom routing accelerators on the console.
- [Delete a custom routing accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.deleting.html): If you created a custom routing accelerator as a test, or if you're no longer using an accelerator, you can delete it.

### [Listeners for custom routing accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-listeners.html)

Learn about how to configure a listener for a custom routing accelerator in AWS Global Accelerator.

- [Add listener](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-listeners.creating-custom-routing-listeners.html): This section explains how to add a listener for a custom routing accelerator on the AWS Global Accelerator console.
- [Edit listener](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-listeners.editing-custom-routing-listeners.html): This section explains how to edit a listener for a custom routing accelerator on the AWS Global Accelerator console.
- [Remove listener](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-listeners.removing-custom-routing-listeners.html): This section explains how to remove a listener for a custom routing accelerator on the AWS Global Accelerator console.

### [Endpoint groups for custom routing accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoint-groups.html)

Use a custom routing endpoint group to specify the Region for VPC subnet endpoints in your custom routing accelerator in AWS Global Accelerator.

- [Add endpoint group](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoint-groups.create-endpoint-group.html): You work with an endpoint group for your custom routing accelerator on the AWS Global Accelerator console or by using an API operation.
- [Edit endpoint group](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoint-groups.edit-endpoint-group.html): You work with an endpoint group for your custom routing accelerator on the AWS Global Accelerator console or by using an API operation.
- [Remove endpoint group](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoint-groups.remove-endpoint-group.html): You work with an endpoint group for your custom routing accelerator on the AWS Global Accelerator console or by using an API operation.

### [VPC subnet endpoints](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html)

Work with VPC subnets as custom routing endpoints in AWS Global Accelerator.

- [Add an Amazon VPC subnet endpoint](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints-adding-endpoints.html): You add Amazon Virtual Private Cloud (VPC) subnet endpoints to endpoint groups in your custom routing accelerators so that you can direct user traffic to destination Amazon EC2 instances in the subnet.
- [Edit an Amazon VPC subnet endpoint](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints-editing-endpoints.html): You can edit Amazon Virtual Private Cloud (VPC) subnet endpoints for your custom routing accelerators so that you can change where you direct user traffic to destination Amazon EC2 instances, or allow or deny traffic to all destinations in the subnet.
- [Remove an Amazon VPC subnet endpoint](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints-removing-endpoints.html): You can remove an Amazon Virtual Private Cloud (VPC) subnet endpoint from your custom routing accelerator so that user traffic no longer goes to destination Amazon EC2 instances in the subnet.


## [Configure cross-account access](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html)

- [How cross-account works](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.how-it-works.html): With cross-account support in Global Accelerator, resource owners control whether their resources are shared with accelerators owned by other accounts.

### [Work with cross-account attachments](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.work-with-attachments.html)

To allow someone to add a resource from another account as an endpoint or a BYOIP address for an accelerator, the owner of the resource must create a cross-account attachment in Global Accelerator.

- [Create cross-account attachments](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.create-attachment.html): Follow the steps in this section to create a cross-account attachment using the AWS Global Accelerator console.
- [Edit cross-account attachments](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.edit-attachment.html): Follow the steps in this section to edit a cross-account attachment using the AWS Global Accelerator console.
- [Delete cross-account attachments](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.delete-attachment.html): Follow the steps in this section to delete a cross-account attachment using the AWS Global Accelerator console.

### [Work with cross-account resources](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.work-with-resources.html)

If your account, or an accelerator that you have permission to access, is specified as a principal in a cross-account attachment in AWS Global Accelerator, you can use resources that have been shared with you from another account.

- [Add cross-account BYOIP addresses](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.add-byoip.html): Follow the steps in this section to configure cross-account bring your own IP (BYOIP) ID addresses using the Global Accelerator console.
- [Add cross-account endpoints](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.add-endpoints.html): Follow the steps in this section to add a cross-account endpoints using the Global Accelerator console.
- [Remove cross-account endpoints](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.remove-endpoints.html): Follow the steps in this section to remove a cross-account endpoints using the Global Accelerator console.
- [Identify cross-account resources](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.identify-cross-account.html): Resource owners and principals can identify shared resources by using the AWS Global Accelerator console or by using the AWS CLI with Global Accelerator operations.
- [Responsibilities and permissions](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources-endpoints.responsibilities-cross-account.html): The following sections list the permissions you have as a resource owner or as a principal for cross-account access in AWS Global Accelerator.
- [Billing costs](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources-endpoints.billing-cross-account.html): The owner of an accelerator in AWS Global Accelerator is billed for costs associated with the accelerator.
- [Quotas](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources-endpoints.quotas-cross-account.html): The following applies when you work with cross-account attachments and cross-account resources in AWS Global Accelerator:


## [DNS addressing and custom domains](https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.html)

- [Support for DNS addressing](https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html): When you create an accelerator with an IPv4 IP address type, Global Accelerator provisions two static IPv4 addresses for you.
- [Route custom domain traffic to your accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.mapping-your-custom-domain.html): In most scenarios, you can configure DNS to use your custom domain name (such as www.example.com) with your accelerator, instead of using the assigned static IP addresses or the default DNS name.

### [Bring your own IP addresses](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html)

You can bring your own IP addresses to AWS to add to an accelerator instead of, or together with, the static IP addresses that AWS Global Accelerator assigns to you.

- [Requirements](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.requirements.html): You can bring up to two qualifying IP address ranges to AWS Global Accelerator per AWS account.
- [IP address range authorization](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.prepare.html): To ensure that only you can bring your IP address space to Amazon, we require two authorizations:
- [Provision the address range](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.provision.html): When you provision an address range for use with AWS, you are confirming that you own the address range and authorize Amazon to advertise it.
- [Advertise the address range](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.advertise.html): After the address range is provisioned, it's ready to be advertised.
- [Deprovision the address range](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.deprovision.html): To stop using your address range with AWS, you first must remove any accelerators that have static IP addresses that are allocated from the address pool and stop advertising your address range.
- [Use your BYOIP address with an accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.create-accelerator.html): After you complete the steps to add an address range with BYOIP, you can create an accelerator with your BYOIP IP addresses, or you can use your BYOIP IP addresses with an existing accelerator.
- [Update an IP address](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.update-accelerator.html): After you assign BYOIP addresses as static IP addresses for an accelerator in AWS Global Accelerator, you can update the accelerator later to use different IP addresses from your address ranges.


## [Preserve client IP addresses](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.html)

- [Guidelines and restrictions](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.how-to-enable-preservation.html): As you prepare for and use client IP address preservation in AWS Global Accelerator, be aware of the following guidelines and restrictions.
- [Requirements for client IP address preservation](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.sipp-caveats.html): There are specific requirements for endpoint types that you can use with client IP address preservation. >You can use this feature with endpoints that are Application Load Balancers, Network Load Balancers with security groups, and Amazon EC2 instances, subject to the additional requirements described in this section.
- [How the client IP address is preserved](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.headers.html): AWS Global Accelerator preserves the source IP address of the client differently for Amazon EC2 instances, Network Load Balancers, and Application Load Balancers:
- [Benefits of client IP address preservation](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.benefits-of-preservation.html): You can configure client IP address preservation for specific endpoints in Global Accelerator.
- [Best practices for ENIs and security](https://docs.aws.amazon.com/global-accelerator/latest/dg/best-practices-aga.html): When you use client IP address preservation in AWS Global Accelerator, keep in mind the information and best practices in this section for elastic network interfaces (ENIs) and security groups.
- [Transition endpoints](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.sipp.html): If you haven't yet configured client IP address preservation for the endpoints in your accelerator, follow the guidance in this section add and transition one or more endpoints to endpoints that preserve the userâs client IP address.


## [Logging and monitoring](https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.html)

- [CloudWatch monitoring](https://docs.aws.amazon.com/global-accelerator/latest/dg/cloudwatch-monitoring.html): Learn about monitoring Global Accelerator with Amazon CloudWatch.
- [Troubleshooting RST issues](https://docs.aws.amazon.com/global-accelerator/latest/dg/cloudwatch-metrics-globalaccelerator-tcp-resets.html): Learn about troubleshooting TCP RSTs in Global Accelerator with Amazon CloudWatch metrics.
- [Flow logs](https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html): Flow logs enable you to capture information about the IP address traffic going to and from network interfaces in your accelerator in AWS Global Accelerator.
- [CloudTrail logging](https://docs.aws.amazon.com/global-accelerator/latest/dg/logging-using-cloudtrail.html): Learn about logging Global Accelerator with AWS CloudTrail.


## [Security](https://docs.aws.amazon.com/global-accelerator/latest/dg/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/global-accelerator/latest/dg/security-iam.html)

How to authenticate requests and manage access to your Global Accelerator resources.

- [How Global Accelerator works with IAM](https://docs.aws.amazon.com/global-accelerator/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Global Accelerator, learn what IAM features are available to use with Global Accelerator.
- [Identity-based policy examples](https://docs.aws.amazon.com/global-accelerator/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Global Accelerator resources.
- [Service-linked role](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-service-linked-roles.html): How to work with the service-linked role that gives Global Accelerator access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/global-accelerator/latest/dg/security-iam-awsmanpol-aga.html): Learn about AWS managed policies for Global Accelerator and recent changes to those policies.
- [Tag-based policies](https://docs.aws.amazon.com/global-accelerator/latest/dg/security_iam-tag-policies.html): When you design IAM policies, you might set granular permissions by granting access to specific resources.
- [Troubleshooting](https://docs.aws.amazon.com/global-accelerator/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Global Accelerator and IAM.
- [Secure VPC connections](https://docs.aws.amazon.com/global-accelerator/latest/dg/secure-vpc-connections.html): Learn how internet traffic flows directly to and from endpoints in VPCs when you use AWS Global Accelerator.
- [Logging and monitoring](https://docs.aws.amazon.com/global-accelerator/latest/dg/logging-and-monitoring.html): Learn how AWS supports you in maintaining availability and performance in AWS Global Accelerator by providing tools for logging and monitoring Global Accelerator activity.
- [Compliance validation](https://docs.aws.amazon.com/global-accelerator/latest/dg/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/global-accelerator/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as specific Global Accelerator features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/global-accelerator/latest/dg/infrastructure-security.html): Learn how AWS Global Accelerator isolates service traffic.
