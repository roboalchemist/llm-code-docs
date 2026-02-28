# Source: https://docs.datadoghq.com/security/default_rules/def-000-g1u.md

---
title: EC2 instances should not be publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 instances should not be publicly
  accessible
---

# EC2 instances should not be publicly accessible

## Description{% #description %}

This validation examines whether EC2 instances are publicly accessible. Private IPv4 addresses can be used for communication within the same VPC or connected private network.

IPv6 addresses are globally unique and reachable from the internet, although by default, subnets have the IPv6 addressing attribute set to false. For further details on IPv6, refer to IP addressing in your VPC in the Amazon VPC User Guide.

If public accessibility for an EC2 instance is intentional, you have the option to mute the findings from this validation.

## Remediation{% #remediation %}

Refer to the section on [Modifying the public IPv4 addressing attribute for your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#subnet-public-ip) in the Amazon VPC User Guide for detailed instructions.

Choose to enable or disable the public IP addressing feature during the instance launch process, which overrides the subnet's default setting. See [Assign a public IPv4 address during instance launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#public-ip-addresses) in the Amazon EC2 User Guide for Linux Instances for more information.

For more guidance on public IPv4 addresses and external DNS hostnames, see the [Amazon EC2 User Guide for Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html).
