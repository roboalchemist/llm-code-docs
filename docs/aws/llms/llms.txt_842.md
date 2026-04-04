# Source: https://docs.aws.amazon.com/vpc/latest/ipam/llms.txt

# Amazon Virtual Private Cloud IP Address Manager

> Use Amazon VPC to launch AWS resources into a virtual network that is a logically isolated section of the AWS cloud. Use Amazon VPC to launch AWS resources into a virtual network that is a logically isolated section of the AWS cloud.

- [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)
- [How IPAM works](https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html)
- [Quotas](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html)
- [Pricing](https://docs.aws.amazon.com/vpc/latest/ipam/pricing-ipam.html)
- [Related information](https://docs.aws.amazon.com/vpc/latest/ipam/related-info.html)
- [Document history](https://docs.aws.amazon.com/vpc/latest/ipam/doc-history-ipam.html)

## [Getting started with IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/getting-started-ipam.html)

- [Access IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/access-ipam.html): Learn how to access IPAM to manage IP addresses.

### [Configure integration options for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/choose-single-user-or-orgs-ipam.html)

Learn more about IPAM integrations with IAM and other AWS accounts.

- [Integrate IPAM with accounts in an AWS Organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam.html): Learn how to integrate IPAM with AWS Organizations

### [Integrate IPAM with accounts outside of your organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html)

Learn how to integrate IPAM with accounts outside of your AWS organization

- [Considerations and limitations](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org-considerations.html): Considerations and limitations when integrating IPAM with accounts outside of your AWS organization
- [Process overview](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org-process.html): Steps for integrating IPAM with accounts outside of your AWS organization
- [Use IPAM with a single account](https://docs.aws.amazon.com/vpc/latest/ipam/enable-single-user-ipam.html): Learn about using IPAM with a single AWS account.
- [Create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html): create an IPAM.

### [Plan for IP address provisioning](https://docs.aws.amazon.com/vpc/latest/ipam/planning-ipam.html)

Plan for your IPAM.

- [Example IPAM pool plans](https://docs.aws.amazon.com/vpc/latest/ipam/planning-examples-ipam.html): Plan for your IPAM by viewing example plans.

### [Create IPv4 pools](https://docs.aws.amazon.com/vpc/latest/ipam/intro-create-ipv4-pools.html)

Learn how to create IPv4 IPAM pools.

- [Create a top-level IPv4 pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-top-ipam.html): Learn how to create a top-level IPAM pool within your private scope.
- [Create a Regional IPv4 pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-reg-ipam.html): Learn how to create a Regional IPAM pool within a top-level pool.
- [Create a development IPv4 pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-dev-ipam.html): Learn how to create a development IPAM pool within your Regional pool.

### [Create IPv6 pools](https://docs.aws.amazon.com/vpc/latest/ipam/intro-create-ipv6-pools.html)

Learn how to create IPv6 IPAM pools.

- [Create a regional IPv6 pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipv6-reg-pool.html): Learn how to create an IPv6 regional IPAM pool within your private scope.
- [Create a development IPv6 pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipv6-dev-pool.html): Learn how to create an IPv6 development IPAM pool.

### [Allocate CIDRs](https://docs.aws.amazon.com/vpc/latest/ipam/allocate-cidrs-ipam.html)

Learn how to allocate a CIDR from a pool.

- [Create a VPC that uses an IPAM pool CIDR](https://docs.aws.amazon.com/vpc/latest/ipam/create-vpc-ipam.html): Learn how to create a VPC that uses an IPAM pool CIDR.
- [Manually allocate a CIDR to a pool to reserve IP address space](https://docs.aws.amazon.com/vpc/latest/ipam/manually-allocate-ipam.html): Learn how to manually allocate a CIDR to a pool.


## [Managing IP address space in IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/managing-ip-space-ipam.html)

- [Automate prefix list updates with IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/automate-prefix-list-updates.html): Learn how to use IPAM to automatically manage customer-managed prefix lists by keeping your CIDR entries synchronized with your network changes.
- [Change the monitoring state of VPC CIDRs](https://docs.aws.amazon.com/vpc/latest/ipam/change-monitoring-state-ipam.html): Learn how to change the monitoring state of a VPC CIDR
- [Create additional scopes](https://docs.aws.amazon.com/vpc/latest/ipam/add-scope-ipam.html): Learn how to add an additional scope.
- [Delete an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/delete-ipam.html): Learn how to delete an IPAM.
- [Delete a pool](https://docs.aws.amazon.com/vpc/latest/ipam/delete-pool-ipam.html): Learn how to delete a pool.
- [Delete a scope](https://docs.aws.amazon.com/vpc/latest/ipam/delete-scope-ipam.html): Learn how to delete a scope.
- [Deprovision CIDRs from a pool](https://docs.aws.amazon.com/vpc/latest/ipam/depro-pool-cidr-ipam.html): Learn how to deprovision an IPAM pool CIDR.
- [Edit an IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/mod-pool-ipam.html): Learn how to edit an IPAM pool.
- [Enable cost distribution](https://docs.aws.amazon.com/vpc/latest/ipam/ipam-enable-cost-distro.html): Learn how to modify IPAM charges.
- [Integrate VPC IPAM with Infoblox infrastructure](https://docs.aws.amazon.com/vpc/latest/ipam/integrate-infoblox-ipam.html): Amazon VPC IPAM and Infoblox integration connects your AWS VPC IP Address Manager (IPAM) with Infoblox, enabling you to manage AWS IP addresses through your existing Infoblox workflows while gaining cloud-native AWS capabilities.
- [Enable provisioning private IPv6 GUA CIDRs](https://docs.aws.amazon.com/vpc/latest/ipam/enable-prov-ipv6-gua.html): Learn how to enable provisioning private IPv6 GUA CIDRs to IPAM pools.
- [Enforce IPAM use for VPC creation with SCPs](https://docs.aws.amazon.com/vpc/latest/ipam/scp-ipam.html): Learn about enforcing IPAM use for VPC creation
- [Exclude organizational units from IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html): If you integrate your IPAM with AWS Organizations, learn how to exclude organizational units from IPAM.
- [Modify IPAM tier](https://docs.aws.amazon.com/vpc/latest/ipam/mod-ipam-tier.html): Learn how to modify an IPAM tier to be either Free Tier or Advanced Tier.
- [Modify IPAM operating Regions](https://docs.aws.amazon.com/vpc/latest/ipam/mod-ipam-region.html): Learn how to modify an IPAM operating Regions.
- [Provision CIDRs to a pool](https://docs.aws.amazon.com/vpc/latest/ipam/prov-cidr-ipam.html): Learn how to provision a CIDR to an IPAM pool.
- [Move VPC CIDRs between scopes](https://docs.aws.amazon.com/vpc/latest/ipam/move-resource-ipam.html): Learn how to move a VPC CIDR to another scope
- [Define IPv4 allocation strategy](https://docs.aws.amazon.com/vpc/latest/ipam/define-public-ipv4-allocation-strategy-with-ipam-policies.html): An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated.
- [Release an allocation](https://docs.aws.amazon.com/vpc/latest/ipam/release-alloc-ipam.html): Learn how to release an allocation from an IPAM pool.
- [Share an IPAM pool using AWS RAM](https://docs.aws.amazon.com/vpc/latest/ipam/share-pool-ipam.html): Learn how to share an IPAM pool with RAM.

### [Work with resource discoveries](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with.html)

Learn how to work with resource discoveries

- [Create a resource discovery](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with-create.html): Steps for creating resource discoveries
- [View resource discovery details](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with-view.html): Steps for viewing resource discovery details and IP address insights.
- [Share a resource discovery](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with-share.html): Steps for sharing a resource discovery with another AWS account.
- [Associate a resource discovery with an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with-associate.html): Steps for associating a resource discovery with an IPAM
- [Disassociate a resource discovery](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with-disassociate.html): Steps for disassociating a resource discovery with an IPAM
- [Delete a resource discovery](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with-delete.html): Steps for deleting a resource discovery


## [Tracking IP address usage in IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tracking-ip-addresses-ipam.html)

- [Monitor CIDR usage with the IPAM dashboard](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-usage-ipam.html): Learn how to monitor CIDR usage.
- [Monitor CIDR usage by resource](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html): Learn how to monitor CIDR compliance and IP usage per resource.

### [Monitor IPAM with Amazon CloudWatch](https://docs.aws.amazon.com/vpc/latest/ipam/cloudwatch-ipam.html)

Monitor IPAM with CloudWatch and use alarms to monitor address usage

- [Manage alarms](https://docs.aws.amazon.com/vpc/latest/ipam/cloudwatch-ipam-manage-alarms.html): Manage CloudWatch alarms directly from the IPAM console.
- [Pool and scope metrics](https://docs.aws.amazon.com/vpc/latest/ipam/cloudwatch-ipam-ip-address-usage.html): Use CloudWatch with IPAM metrics.
- [Resource utilization metrics](https://docs.aws.amazon.com/vpc/latest/ipam/cloudwatch-ipam-res-util.html): Use CloudWatch with IPAM for resource metrics.
- [View IP address history](https://docs.aws.amazon.com/vpc/latest/ipam/view-history-cidr-ipam.html): Learn how to view IP address history with IPAM.
- [View public IP insights](https://docs.aws.amazon.com/vpc/latest/ipam/view-public-ip-insights.html): Learn how to view all public IPv4 addresses in your account.


## [Tutorials](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-ipam.html)

- [Getting started with IPAM using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/ipam/getting-started-with-ipam-using-the-aws-cli.html): This tutorial guides you through the process of setting up and using Amazon VPC IP Address Manager (IPAM) with the AWS CLI using a single AWS account.
- [Create an IPAM and pools using the console](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-get-started-console.html): Learn how to use IPAM to manage your IP addresses in AWS Organizations
- [Create an IPAM and pools using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-create-vpc-ipam.html): Learn how to use the AWS CLI to create an IPAM, create IP address pools, and allocate a VPC with a CIDR from an IPAM pool.
- [View IP address history using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-historical-insights.html): Learn how to use the AWS CLI to create an IPAM, create pools, and allocate a VPC.
- [Bring your ASN to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoasn.html): Learn how to bring an ASN to IPAM.

### [Bring your IP addresses to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam.html)

Learn how to bring your own IP CIDRs to IPAM.

- [Verify domain control](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-domain-verification-methods.html): Learn how to verify domain ownership.

### [BYOIP with AWS console and CLI](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-console-intro.html)

Learn how to bring your own IP address to IPAM using both the AWS Management Console and the AWS CLI.

- [IPv4 CIDR](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-console-ipv4.html): Learn how to bring your own IPv4 address range to IPAM.
- [IPv6 CIDR](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-console-ipv6.html): Learn how to bring your own IPv6 address range to IPAM.

### [BYOIP with AWS CLI only](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-cli-only-intro.html)

Learn how to bring your own IP address to IPAM using only the AWS CLI.

- [IPv4 CIDR](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-ipv4.html): Learn how to bring your own IP address to IPAM.
- [IPv6 CIDR](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-ipv6.html): Learn how to bring your own IP address to IPAM.
- [Bring your own IP to CloudFront using IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-cloudfront.html): This tutorial shows how to use IPAM to manage your BYOIP CIDRs for AWS global services, starting with CloudFront anycast services.
- [Transfer a BYOIP IPv4 CIDR to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-transfer-ipv4.html): Learn how to transfer your BYOIP IPv4 CIDR to IPAM.
- [Plan VPC IP address space for subnet IP allocations](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-subnet-planning.html): Learn how to use plan for VPC subnet IP address space with IPAM.
- [Allocate sequential Elastic IP addresses from an IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-eip-pool.html): Learn how to simplify security and networking rules by allocating sequential Elastic IP addresses from an IPAM pool.


## [Identity and access management in IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam.html)

- [Service-linked roles for IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam-slr.html): Learn about service-linked roles for IPAM.
- [Managed policies for IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam-managed-pol.html): Learn about managed policies for IPAM
- [Example policy](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam-policy-examples.html): View an example IAM policy for IPAM
