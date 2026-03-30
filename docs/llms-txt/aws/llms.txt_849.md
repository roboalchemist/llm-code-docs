# Source: https://docs.aws.amazon.com/vpc/latest/userguide/llms.txt

# Amazon Virtual Private Cloud User Guide

> Use Amazon VPC to launch AWS resources into a virtual network that is a logically isolated section of the AWS cloud. Use Amazon VPC to launch AWS resources into a virtual network that is a logically isolated section of the AWS cloud.

- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [How Amazon VPC works](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html)
- [Plan your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html)
- [Quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html)
- [Document history](https://docs.aws.amazon.com/vpc/latest/userguide/WhatsNew.html)

## [IP addressing](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html)

- [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html): VPCs use CIDR notation to represent IP addresses.
- [Subnet CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html): Subnets within a VPC are represented using CIDR notation.
- [Compare IPv4 and IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/ipv4-ipv6-comparison.html): The following table summarizes the differences between IPv4 and IPv6 in Amazon EC2 and Amazon VPC.

### [Managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)

Use managed prefix lists to group your IPv4 and IPv6 CIDR blocks, and reference them in security groups and route tables.

### [Customer-managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-managed-prefix-lists.html)

Customer-managed prefix lists allow you to define and maintain your own sets of IP address ranges, known as prefixes, within AWS.

### [Work with customer-managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/work-with-cust-managed-prefix-lists.html)

This section describes how to work with customer-managed prefix lists.

### [Share customer-managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/sharing-managed-prefix-lists.html)

Use AWS RAM to share prefix lists with accounts, organizational units, or an entire organization.

- [Shared prefix list permissions](https://docs.aws.amazon.com/vpc/latest/userguide/sharing-perms.html): Permissions for owners
- [Work with shared prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/work-with-shared-prefixes.html): AWS prefix lists provide a convenient way to manage and reference the IP address ranges used by various AWS services.
- [AWS-managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html): AWS-managed prefix lists are sets of IP address ranges for AWS services.
- [Optimize AWS infrastructure management with prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists-referencing.html): You can reference a prefix list in the following AWS resources.

### [AWS IP address ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html)

Identify and control traffic to/from AWS services using the published IP address ranges in the ip-ranges.json file.

- [Find address ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-work-with.html): Learn how to use jq or PowerShell to find specific IP address ranges in ip-ranges.json.
- [Syntax](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-syntax.html): Understand the syntax of the AWS IP address ranges provided in the ip-ranges.json file.
- [Subscribe to notifications](https://docs.aws.amazon.com/vpc/latest/userguide/subscribe-notifications.html): AWS publishes its current IP address ranges in JSON format.

### [IPv6 support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html)

Enable dual-stack IPv4/IPv6 support for your existing VPC and resources.

- [Add IPv6 support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-add.html): The following table provides an overview of the process to enable IPv6 for your VPC.
- [Example dual-stack VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-example.html): With a dual-stack configuration, you can use both IPv4 and IPv6 addresses for communication between resources in your VPC and resources over the internet.
- [IPv6 support on AWS](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ipv6-support.html): Computers use IPv4 and IPv6 to communicate.


## [Virtual private clouds](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html)

- [VPC basics](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-subnet-basics.html): A VPC spans all of the Availability Zones in a Region.
- [VPC configuration options](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc-options.html): You can specify the following configuration options when you create a VPC.

### [Default VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html)

Launch EC2 instances into a default VPC with public subnets, internet gateway, and DNS resolution.

- [Default VPC components](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc-components.html): When we create a default VPC, we do the following to set it up for you:
- [Default subnets](https://docs.aws.amazon.com/vpc/latest/userguide/default-subnet.html): By default, a default subnet is a public subnet, because the main route table sends the subnet's traffic that is destined for the internet to the internet gateway.
- [Work with your default VPC and default subnets](https://docs.aws.amazon.com/vpc/latest/userguide/work-with-default-vpc.html): This section describes how to work with default VPCs and default subnets.
- [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html): Create a VPC - configure options like IP CIDR blocks, subnets, route tables, and gateways.
- [Visualize the resources in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/view-vpc-resource-map.html): This section describes how you can see a visual representation of the resources in your VPC using the Resource map tab.
- [Add or remove CIDR block](https://docs.aws.amazon.com/vpc/latest/userguide/add-ipv4-cidr.html): This section describes how to add or remove IPv4 and IPv6 CIDR blocks from a VPC.

### [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html)

Configure DHCP options to control DNS, domain, and NTP settings for network devices in your VPC.

- [DHCP option set concepts](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSetConcepts.html): A DHCP option set is a group of network settings used by resources in your VPC, such as EC2 instances, to communicate over your virtual network.
- [Work with DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html): Use the following procedures to view and work with DHCP option sets.

### [DNS attributes](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html)

DNS translates hostnames to IP addresses, enabling internet and internal network communication.

- [Understanding Amazon DNS](https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html): As an AWS architect or administrator, one of the foundational networking components you'll encounter is the Amazon DNS server, also known as the Route 53 Resolver.
- [View DNS hostnames for your EC2 instance](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns-viewing.html): You can view the DNS hostnames for a running instance or a network interface using the Amazon EC2 console or the command line.
- [View and update DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns-updating.html): You can view and update the DNS support attributes for your VPC using the Amazon VPC console.
- [Network Address Usage](https://docs.aws.amazon.com/vpc/latest/userguide/network-address-usage.html): Enable Network Address Usage to monitor the size of your VPCs.

### [Share a VPC subnet](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html)

VPC subnet sharing allows multiple AWS accounts to create resources in a centrally-managed, shared VPC.

- [Shared subnet prerequisites](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-share-prerequisites.html): This section contains prerequisites for working with shared subnets:
- [Working with shared subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing-share-subnet-working-with.html): This section describes how to work with shared subnets in the AWS console and AWS CLI.
- [Billing and metering for owner and participants](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-share-billing.html): This section contains billing and metering details for those who own the shared subnet and for those working with the shared subnet:
- [Responsibilities and permissions for owners and participants](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-share-limitations.html): This section includes details about the responsibilities and permissions for those who own the shared subnet (owner) and for those who are using the shared subnet (participant).
- [AWS resources and shared VPC subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing-service-behavior.html): The following AWS services support resources in shared VPC subnets.

### [Extend a VPC to other Zones](https://docs.aws.amazon.com/vpc/latest/userguide/Extend_VPCs.html)

Extend your VPCs to Local Zones, Wavelength Zones, and Outposts.

- [Subnets in AWS Local Zones](https://docs.aws.amazon.com/vpc/latest/userguide/local-zone.html): AWS Local Zones allow you to place resources closer to your users, and seamlessly connect to the full range of services in the AWS Region, using familiar APIs and tool sets.
- [Subnets in AWS Wavelength](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-wavelength.html): AWS Wavelength allows developers to build applications that deliver ultra-low latencies to mobile devices and end-users.
- [Subnets in AWS Outposts](https://docs.aws.amazon.com/vpc/latest/userguide/outposts.html): AWS Outposts offers you the same AWS hardware infrastructure, services, APIs, and tools to build and run your applications on premises and in the cloud.
- [Delete your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/delete-vpc.html): Learn how to delete your a virtual private cloud.
- [Generate IaC from console actions](https://docs.aws.amazon.com/vpc/latest/userguide/vpcs-automate-c2c.html): Use Console-to-Code to generate code for your Amazon VPC console actions.


## [Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)

- [Create a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html): Create VPC subnets, specify IPv4/IPv6 CIDR, choose AZs, use VPC IPAM.
- [Add or remove an IPv6 CIDR block from your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-associate-ipv6-cidr.html): You can associate an IPv6 CIDR block with an existing subnet in your VPC.
- [Modify the IP addressing attributes of your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-public-ip.html): By default, nondefault subnets have the IPv4 public addressing attribute set to false, and default subnets have this attribute set to true.
- [Subnet CIDR reservations](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html): Learn how to reserve a CIDR block in your subnet for Prefix Delegation or to manually assign it to your resources.

### [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

Configure route tables to control where network traffic is directed.

- [Route table concepts](https://docs.aws.amazon.com/vpc/latest/userguide/RouteTables.html): The following are the key concepts for route tables:
- [Subnet route tables](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-route-tables.html): Your VPC has an implicit router, and you use route tables to control where network traffic is directed.
- [Gateway route tables](https://docs.aws.amazon.com/vpc/latest/userguide/gateway-route-tables.html): You can associate a route table with an internet gateway or a virtual private gateway.
- [Route priority](https://docs.aws.amazon.com/vpc/latest/userguide/route-tables-priority.html): In general, we direct traffic using the most specific route that matches the traffic.
- [Example routing options](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html): Routing configurations for VPC connectivity options, including internet gateways, NAT devices, virtual private gateways, and transit gateways.
- [Create a route table and routes](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc-route-table.html): Complete the following tasks to create and configure a custom route table for your VPC.
- [Manage subnet route tables](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html): Learn about VPC subnet route table associations and manage VPC routing using route tables.
- [Replace the main route table](https://docs.aws.amazon.com/vpc/latest/userguide/Route_Replacing_Main_Table.html): This section describes how to change which route table is the main route table in your VPC.
- [Associate a route table with a gateway](https://docs.aws.amazon.com/vpc/latest/userguide/associate-route-table-gateway.html): To control traffic entering your VPC with a gateway route table, you can associate or disassociate an internet gateway or a virtual private gateway with a route table.
- [Replace or restore the target for a local route](https://docs.aws.amazon.com/vpc/latest/userguide/replace-local-route-target.html): You can change the target of the default local route.

### [Advanced routing](https://docs.aws.amazon.com/vpc/latest/userguide/advanced-routing.html)

Configure advanced routing scenarios for your VPC.

- [Route traffic to single network interface](https://docs.aws.amazon.com/vpc/latest/userguide/igw-ingress-routing.html): Learn how to route internet traffic destined for large IP pools to a single elastic network interface using internet gateway ingress routing.

### [Dynamic routing in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/dynamic-routing-route-server.html)

Use Amazon VPC Route Server for dynamic routing

- [Terminology](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-terms.html): Understand Amazon VPC Route Server terms
- [How Amazon VPC Route Server works](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-how-it-works.html): Understand how Amazon VPC Route Server handles routing failures.
- [Route server peer logging](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-peer-logging.html): Use VPC Route Server peer logging when you need to:

### [Get started tutorial](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial.html)

Learn how to create, manage, and use components in Amazon VPC Route Server;.

- [Step 1: Configure required IAM Role permissions](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-iam.html): To use VPC Route Server, ensure that the IAM user or role you are using has the required IAM permissions.
- [Step 2: Create a route server](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-create.html): Complete the steps in this section to create a route server.
- [Step 3: Associate route server with a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-associate.html): Complete the steps in this section to associate the route server with a VPC.
- [Step 4: Create route server endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-create-endpoints.html): Complete the steps in this section to create route server endpoints.
- [Step 5: Enable route server propagation](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-enable-prop.html): Complete this step to enable route server propagation.
- [Step 6: Create route server peer](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-create-peer.html): A route server peer is a session between a route server endpoint and the device deployed in AWS (such as a firewall appliance or other network security function running on an EC2 instance).
- [Step 7: Initiate BGP sessions from the devices](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-initiate-bgp.html): When the status of route server peer is available, configure your workload to initiate the BGP session with the route server endpoint.
- [Step 8: Cleanup](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-cleanup.html): The building portion of the tutorial is complete.
- [Troubleshoot reachability issues](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-routes-troubleshoot.html): Reachability Analyzer is a static configuration analysis tool.

### [Middlebox routing wizard](https://docs.aws.amazon.com/vpc/latest/userguide/middlebox-routing-console.html)

Learn how the middlebox routing wizard helps you by automatically creating the necessary route tables.

- [Redirect VPC traffic to a security appliance](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-routing-console.html): The middlebox routing wizard is available in the Amazon VPC console.

### [Middlebox scenarios](https://docs.aws.amazon.com/vpc/latest/userguide/middlebox-routing-examples.html)

Learn how the middlebox routing wizard can help with the following scenarios.

- [Inspect traffic destined for a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/internet-gateway-subnet.html): Use a security appliance to inspect all traffic that enters and leaves the VPC through the internet gateway.
- [Inspect traffic using security appliances](https://docs.aws.amazon.com/vpc/latest/userguide/gwlb-route.html): Use a fleet of security appliances to inspect all traffic that enters and leaves the VPC through the internet gateway.
- [Inspect traffic between subnets](https://docs.aws.amazon.com/vpc/latest/userguide/intra-vpc-route.html): Use a security appliance to inspect all traffic between subnets.
- [Delete a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-deleting.html): To delete a VPC subnet, first terminate any resources (such as instances) it contains, then delete the subnet through the VPC console.


## [Connect your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/extend-intro.html)

### [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)

Enable access to the internet from your VPC by attaching an internet gateway.

- [Create an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-igw.html): Learn how to create an internet gateway and configure internet access for a subnet.
- [Delete an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/delete-igw.html): Learn how to delete an internet gateway.

### [Egress-only internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html)

Enable outbound access to the internet over IPv6 from your VPC by creating an egress-only internet gateway.

- [Add egress-only internet access to a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway-working-with.html): The following tasks describe how to create an egress-only (outbound) internet gateway for your private subnet and to configure routing for the subnet.

### [NAT devices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html)

Enable access to the internet or other VPCs from private subnets using NAT devices.

### [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)

Use a NAT gateway in a public VPC subnet to enable outbound internet traffic from instances in a private subnet.

- [NAT gateway basics](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html): Each NAT gateway is created in a specific Availability Zone and implemented with redundancy in that zone.
- [Work with NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html): You can use the Amazon VPC console to create and manage your NAT gateways.
- [Regional NAT gateways for automatic multi-AZ expansion](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html): Use regional NAT gateways when you want to simplify your network architecture, improve security posture, and configure high availability by default.
- [Use cases](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-scenarios.html): The following are example use cases for public and private NAT gateways.
- [DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-nat64-dns64.html): Use NAT gateways to enable IPv6 AWS resources to communicate with IPv4 resources using NAT64 translation.
- [Inspect traffic from NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-inspect-traffic.html): You can attach Network Firewall Proxy to your NAT Gateway to inspect and filter traffic on your NAT Gateway.

### [CloudWatch metrics](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway-cloudwatch.html)

Monitor your NAT gateway with Amazon CloudWatch metrics.

- [NAT gateway metrics and dimensions](https://docs.aws.amazon.com/vpc/latest/userguide/metrics-dimensions-nat-gateway.html): The following metrics are available for your NAT gateways.
- [View NAT gateway CloudWatch metrics](https://docs.aws.amazon.com/vpc/latest/userguide/viewing-metrics.html): NAT gateway metrics are sent to CloudWatch at 1-minute intervals.
- [Create CloudWatch alarms to monitor a NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/creating-alarms-nat-gateway.html): You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state.
- [Troubleshooting](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-troubleshooting.html): Troubleshoot common issues with NAT gateways - creation failures, quota limits, unsupported Availability Zones, visibility, connectivity problems, and more.
- [Pricing](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html): When you provision a NAT gateway, you are charged for each hour that your NAT gateway is available and each gigabyte of data that it processes.

### [NAT instances](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html)

Use a NAT instance in a public VPC subnet to enable outbound internet traffic from instances in a private subnet.

- [NAT instance tutorial](https://docs.aws.amazon.com/vpc/latest/userguide/work-with-nat-instances.html): This section describes how to create and work with NAT instances to enable resources in a private subnet to communicate outside the virtual private cloud.
- [Compare NAT devices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html): Learn about the differences between NAT gateways and NAT instances.

### [Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html)

Use Elastic IP addresses to remap public IPv4 addresses between instances in your VPC.

- [Elastic IP address concepts and rules](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eip-overview.html): To use an Elastic IP address, you first allocate it for use in your account.
- [Start using Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithEIPs.html): The following sections describe how you can get started using Elastic IP addresses.
- [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/extend-tgw.html): Use a transit gateway to connect VPCs and on-premises networks as a centralized router, or configure multiple isolated transit gateways with shared services.
- [AWS Virtual Private Network](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html): Establish VPN connectivity with remote networks using options like AWS Site-to-Site VPN, AWS VPN CloudHub, third-party VPN appliances, and Direct Connect.
- [VPC peering connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html): Create a VPC peering connection with another VPC in order to share resources.


## [Monitoring](https://docs.aws.amazon.com/vpc/latest/userguide/monitoring.html)

### [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

Create a flow log to capture information about IP traffic going to and from your network interfaces.

- [Flow logs basics](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-basics.html): You can create a flow log for a VPC, a subnet, or a network interface.
- [Flow log records](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html): A flow log record represents a network flow in your VPC.
- [Flow log record examples](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html): The following are examples of flow log records that capture specific traffic flows.
- [Flow log limitations](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-limitations.html): To use flow logs, you need to be aware of the following limitations:
- [Work with flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-flow-logs.html): Manage VPC flow logs - create, view, tag, and delete flow logs using the Amazon EC2 and Amazon VPC consoles.

### [Publish to CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html)

Flow logs can publish flow log data directly to Amazon CloudWatch.

- [IAM role for publishing flow logs to CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-iam-role.html): The IAM role that's associated with your flow log must have sufficient permissions to publish flow logs to the specified log group in CloudWatch Logs.
- [Create a flow log that publishes to CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl-create-flow-log.html): You can create flow logs for your VPCs, subnets, or network interfaces.
- [View flow log records with CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/view-flow-log-records-cwl.html): You can view your flow log records using the CloudWatch Logs console.
- [Search flow log records](https://docs.aws.amazon.com/vpc/latest/userguide/search-flow-log-records-cwl.html): You can search your flow log records that are published to CloudWatch Logs using the CloudWatch Logs console.
- [Process flow log records in CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/process-records-cwl.html): You can process flow log records as you would with any other log events collected by CloudWatch Logs.

### [Publish to Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html)

VPC flow logs can publish network traffic data to Amazon S3.

- [Flow log files](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3-path.html): VPC Flow Logs collects data about the IP traffic going to and from your VPC into log records, aggregates those records into log files, and then publishes the log files to the Amazon S3 bucket at 5-minute intervals.
- [Amazon S3 bucket permissions for flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3-permissions.html): By default, Amazon S3 buckets and the objects they contain are private.
- [Required key policy for use with SSE-KMS](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3-cmk-policy.html): You can protect the data in your Amazon S3 bucket by enabling either Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3) or Server-Side Encryption with KMS Keys (SSE-KMS) on your S3 bucket.
- [Amazon S3 log file permissions](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-file-permissions.html): In addition to the required bucket policies, Amazon S3 uses access control lists (ACLs) to manage access to the log files created by a flow log.
- [Create a flow log that publishes to Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3-create-flow-log.html): After you have created and configured your Amazon S3 bucket, you can create flow logs for your network interfaces, subnets, and VPCs.
- [View flow log records with Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/view-flow-log-records-s3.html): You can view your flow log records using the Amazon S3 console.

### [Publish to Amazon Data Firehose](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-firehose.html)

Flow logs can publish flow log data directly to Amazon Data Firehose.

- [IAM roles for cross account delivery](https://docs.aws.amazon.com/vpc/latest/userguide/firehose-cross-account-delivery.html): When you publish to Amazon Data Firehose, you can choose a delivery stream that's in the same account as the resource to monitor (the source account), or in a different account (the destination account).
- [Create a flow log that publishes to Amazon Data Firehose](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-firehose-create-flow-log.html): You can create flow logs for your VPCs, subnets, or network interfaces.

### [Query using Athena](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-athena.html)

Analyze VPC flow logs with Athena - use SQL to identify top talkers, rejected connections.

- [Generate the CloudFormation template using the console](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-generate-template-console.html): After the first flow logs are delivered to your S3 bucket, you can integrate with Athena by generating a CloudFormation template and using the template to create a stack.
- [Generate the CloudFormation template using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-generate-template-cli.html): After the first flow logs are delivered to your S3 bucket, you can generate and use a CloudFormation template to integrate with Athena.
- [Run a predefined query](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-run-athena-query.html): The generated CloudFormation template provides a set of predefined queries that you can run to quickly get meaningful insights about the traffic in your AWS network.
- [Troubleshoot](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-troubleshooting.html): The following are possible issues you might have when working with flow logs.
- [CloudWatch metrics](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cloudwatch.html): Learn about the metrics sent by Amazon VPC to Amazon CloudWatch.
- [Billing and usage reports](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-billing-usage-reports.html): Learn about activity related to Amazon VPC in the AWS billing and usage reports.
- [Describe your VPC network](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-inventory.html): Learn how to identify key characteristics of your VPC network architecture so that you can recreate it.


## [Security](https://docs.aws.amazon.com/vpc/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/vpc/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Virtual Private Cloud.

- [Internetwork traffic privacy](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html): Enhance VPC security with security groups, network ACLs, Flow Logs, and Traffic Mirroring to control, monitor, and replicate traffic.
- [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html): VPC Encryption Controls is a security and compliance feature that offers you centralized authoritative control to monitor the encryption status of your traffic flows, helps you identify resources that allow cleartext communication, and eventually gives you mechanisms to enforce encryption in transit within and across your VPCs in a region.

### [Identity and access management](https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Amazon VPC resources.

- [How Amazon VPC works with IAM](https://docs.aws.amazon.com/vpc/latest/userguide/security_iam_service-with-iam.html): Manage VPC access with IAM identity-based policies.
- [Policy examples](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-policy-examples.html): By default, IAM roles lack permissions to create or modify VPC resources.
- [Troubleshoot](https://docs.aws.amazon.com/vpc/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon VPC and IAM.
- [AWS managed policies](https://docs.aws.amazon.com/vpc/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon VPC and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/vpc/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give VPC access to resources in your AWS account.
- [Infrastructure security](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html): Learn how Amazon Virtual Private Cloud isolates service traffic.

### [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)

Security groups act as virtual firewalls, controlling inbound and outbound traffic for associated VPC resources like EC2 instances.

- [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html): Control inbound and outbound traffic for VPC resources using security group rules.
- [Default security groups](https://docs.aws.amazon.com/vpc/latest/userguide/default-security-group.html): Learn about the default security groups for your VPCs.
- [Create a security group](https://docs.aws.amazon.com/vpc/latest/userguide/creating-security-groups.html): Learn how to create a security group to control traffic to your resources in a VPC.
- [Configure security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-group-rules.html): Learn how to add, edit, and delete security group rules.
- [Delete a security group](https://docs.aws.amazon.com/vpc/latest/userguide/deleting-security-groups.html): Learn how to delete a security group for your VPC.
- [Associate security groups with multiple VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-assoc.html): Learn how to associate security group with multiple VPCs
- [Share security groups with AWS Organizations](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-sharing.html): Learn how to share security groups with AWS Organizations

### [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

Use network access control lists to control traffic in and out of a subnet.

- [Network ACL rules](https://docs.aws.amazon.com/vpc/latest/userguide/nacl-rules.html): Understand how network ACL rules work.
- [Default network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/default-network-acl.html): Learn about the default rules for a default network ACL for your VPC.
- [Custom network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/custom-network-acl.html): Learn about custom network ACLs for your VPC.
- [Path MTU Discovery](https://docs.aws.amazon.com/vpc/latest/userguide/path_mtu_discovery.html): Path MTU Discovery is used to determine the path MTU between two devices.
- [Create a network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/create-network-acl.html): Learn how to create a network ACL for your VPC, add rules, and associate it with a subnet.
- [Manage network ACL associations](https://docs.aws.amazon.com/vpc/latest/userguide/network-acl-associations.html): Each subnet is associated with one network ACL.
- [Delete a network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/delete-network-acl.html): Learn how to delete a network ACL for your VPC.
- [Example: Control access to instances in a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/nacl-examples.html): In this example, instances in the subnet can communicate with each other, and are accessible from a trusted remote computer in order to perform administrative tasks.
- [Resilience](https://docs.aws.amazon.com/vpc/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Virtual Private Cloud features for data resiliency.
- [Compliance validation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC-compliance.html): Learn what AWS services are in scope of a specific compliance program.

### [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html)

How to block public access to your Amazon VPC resources.

- [VPC BPA basics](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa-basics.html): How to assess the impact of blocking public access to your Amazon VPC resources.
- [Assess impact of VPC BPA and monitor VPC BPA](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa-assess-impact-main.html): How to assess the impact of blocking public access to your Amazon VPC resources.
- [Advanced example](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa-example.html): This section contains an advanced example that will help you understand how VPC Block Public Access feature works in different scenarios.
- [Best practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html): VPC security best practices: use multi-AZ, security groups, ACLs, IAM, Flow Logs, Network Access Analyzer, Firewall, and GuardDuty.


## [Use with other services](https://docs.aws.amazon.com/vpc/latest/userguide/related-services.html)

- [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html): Use a VPC endpoint to privately connect your VPC to other AWS services and endpoint services.
- [AWS Network Firewall](https://docs.aws.amazon.com/vpc/latest/userguide/network-firewall.html): Implement network protection with AWS Network Firewall - configure firewalls, firewall policies, and stateful/stateless rule groups to inspect VPC traffic.
- [Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/vpc/latest/userguide/resolver-dns-firewall.html): Enable DNS Firewall filtering for outbound DNS traffic for your VPCs.
- [Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/userguide/reachability-analyzer.html): Reachability Analyzer is a static configuration analysis tool.


## [Examples](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-examples-intro.html)

- [Test environment](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-dev-test.html): Learn how to create a VPC that is suitable for a development or test environment.
- [Web and database servers](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-web-database-servers.html): Learn how to create a VPC to host web servers in public subnets and database servers in private subnets.
- [Private servers](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html): Create a VPC to host servers in private subnets and configure a NAT gateway and a gateway VPC endpoint so tservers can connect to resources outside the VPC.


## [Tutorials](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-tutorials-intro.html)

- [Getting started with Amazon VPC using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/userguide/getting-started-with-amazon-vpc-using-the-aws-cli.html): This tutorial guides you through creating a Virtual Private Cloud (VPC) using the AWS Command Line Interface (AWS CLI).
- [Create a VPC with private subnets and NAT gateways using AWS CLI](https://docs.aws.amazon.com/vpc/latest/userguide/create-a-vpc-with-private-subnets-and-nat-gateways-using-aws-cli.html): This tutorial demonstrates how to create a VPC that you can use for servers in a production environment using the AWS CLI.
