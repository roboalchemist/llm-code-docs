# Source: https://docs.datadoghq.com/security/default_rules/def-000-yx8.md

---
title: EC2 subnets should not automatically assign public IP addresses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 subnets should not automatically
  assign public IP addresses
---

# EC2 subnets should not automatically assign public IP addresses
 
## Description{% #description %}

This check verifies if the configuration of public IP assignment in Amazon Virtual Private Cloud (VPC) subnets has the value of `MapPublicIpOnLaunch` set to FALSE. The validation is successful only when this attribute is configured as FALSE.

Each subnet includes an attribute that defines whether a network interface created in the subnet is assigned a public IPv4 address automatically. Subnets with this attribute enabled assign a public IP address to the primary network interface of instances launched within them.

## Remediation{% #remediation %}

For instructions on configuring a subnet to disable the automatic assignment of public IP addresses, refer to the Modify the public IPv4 addressing attribute for your subnet section in the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/modify-subnets.html#subnet-public-ip). Uncheck the box labeled `Enable auto-assign public IPv4 address`.
