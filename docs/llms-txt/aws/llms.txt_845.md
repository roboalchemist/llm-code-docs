# Source: https://docs.aws.amazon.com/vpc/latest/peering/llms.txt

# Amazon Virtual Private Cloud VPC Peering

> Use Amazon VPC to launch AWS resources into a virtual network that is a logically isolated section of the AWS cloud. Use Amazon VPC to launch AWS resources into a virtual network that is a logically isolated section of the AWS cloud.

- [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
- [How peering connections work](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html)
- [VPC peering scenarios](https://docs.aws.amazon.com/vpc/latest/peering/peering-scenarios.html)
- [Identity and access management](https://docs.aws.amazon.com/vpc/latest/peering/security-iam.html)
- [Quotas](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-connection-quotas.html)
- [Document history](https://docs.aws.amazon.com/vpc/latest/peering/doc-history.html)

## [Peering connections](https://docs.aws.amazon.com/vpc/latest/peering/working-with-vpc-peering.html)

- [Create](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html): Create a VPC peering connection between VPCs in the same Region or different Regions, and in the same account or different accounts.
- [Accept or reject](https://docs.aws.amazon.com/vpc/latest/peering/accept-vpc-peering-connection.html): A VPC peering connection that's in the pending-acceptance state must be accepted by the owner of the accepter VPC to be activated.
- [Update route tables](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html): Update your route tables to route traffic from your subnet over the VPC peering connection.
- [Reference peer security groups](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html): Update your security group rules to reference security groups in the peer VPC.
- [Enable DNS resolution for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-dns.html): Enable DNS resolution for VPC peering connections.
- [Delete](https://docs.aws.amazon.com/vpc/latest/peering/delete-vpc-peering-connection.html): Delete a VPC peering connection.
- [Troubleshoot](https://docs.aws.amazon.com/vpc/latest/peering/troubleshoot-vpc-peering-connections.html): Learn how to troubleshoot a VPC peering connection.


## [Common VPC peering configurations](https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations.html)

- [Route to a VPC CIDR block](https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-full-access.html): Create a VPC peering connection configuration with routes to the full CIDR block of the peer VPC.
- [Route to specific addresses](https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html): Create a VPC peering connection configuration with routes to a portion of the CIDR block of the peer VPC.
