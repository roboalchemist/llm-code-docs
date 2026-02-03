# Source: https://docs.datadoghq.com/security/default_rules/def-000-kic.md

---
title: >-
  EKS Cluster should have public access limited and managed nodegroups should
  use private subnets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EKS Cluster should have public access
  limited and managed nodegroups should use private subnets
---

# EKS Cluster should have public access limited and managed nodegroups should use private subnets
 
## Description{% #description %}

This rule ensures EKS clusters and nodegroups follow security best practices for network access control. Only clusters in the `ACTIVE` status are assessed. The rule performs two main checks and will **FAIL** if any of these conditions are true:

**Cluster endpoint is publicly accessible** When control plane public access is enabled in an EKS cluster, it should be limited to a specific set of CIDRs. For security, public access should be limited to only the bare minimum set of IPs.

This part of the check will fail if any of these conditions are true:

- Private endpoint access is disabled (`resources_vpc_config.endpoint_private_access: false`).
- Public access is enabled with unrestricted CIDRs (`0.0.0.0/0` in `resources_vpc_config.public_access_cidrs`).
- Public access is enabled but no CIDRs are specified (`resources_vpc_config.public_access_cidrs` is null/undefined).

**Nodegroup places instances in public subnet** EKS nodes should not be placed in public subnets. Nodes in public subnets may have inbound internet access, which increases attack surface and violates security best practices. A subnet is considered public if it automatically assigns public IP addresses and has a route to an internet gateway (IGW).

This part of the check will fail if any managed nodegroup is configured to deploy instances in a public subnet.

**Note**: Only nodes from EKS managed nodegroups (including EKS Auto Mode) are assessed. Nodes created through the following mechanisms are not assessed:

- Self-managed EC2 nodes
- Amazon EKS Hybrid Nodes
- Amazon EKS on AWS Outposts
- AWS Fargate
- EKS Anywhere

## Remediation{% #remediation %}

For guidance on remediating clusters with endpoint configuration issues, refer to the [Modifying cluster endpoint access](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html#modify-endpoint-access) section of the Amazon EKS User Guide. For guidance on nodegroup VPC configuration, refer to the [VPC and Subnet Considerations](https://docs.aws.amazon.com/eks/latest/best-practices/subnets.html) section of the Amazon EKS User Guide.
