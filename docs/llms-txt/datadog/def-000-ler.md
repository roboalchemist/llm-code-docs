# Source: https://docs.datadoghq.com/security/default_rules/def-000-ler.md

---
title: Subnets should be associated with a Network Security Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Subnets should be associated with a
  Network Security Group
---

# Subnets should be associated with a Network Security Group

## Description{% #description %}

This rule checks whether subnets in Azure are associated with a Network Security Group. Ensuring that subnets are associated with a Network Security Group helps enhance the security posture of the Azure environment by adding an additional layer of protection to network traffic within the subnet.

## Remediation{% #remediation %}

To associate a subnet with a Network Security Group in Azure, follow these steps:

1. Navigate to the Azure portal and open the 'Subnets' blade for the desired virtual network.
1. Select the subnet that needs to be associated with a Network Security Group, go to the 'Settings' tab, and under 'Security', associate the desired Network Security Group. For detailed instructions, see: [Associate or dissociate a network security group to or from a subnet](https://docs.microsoft.com/en-us/azure/virtual-network/manage-network-security-group#associate-or-dissociate-a-network-security-group-to-or-from-a-subnet).
