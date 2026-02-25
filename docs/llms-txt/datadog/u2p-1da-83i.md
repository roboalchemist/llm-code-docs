# Source: https://docs.datadoghq.com/security/default_rules/u2p-1da-83i.md

---
title: The network security group should allow specific port rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The network security group should allow
  specific port rules
---

# The network security group should allow specific port rules

## Description{% #description %}

Azure Network Security Group (NSG) is configured to allow specific ports rather than all ports or port ranges.

## Rationale{% #rationale %}

NSGs should be configured as granularly as possible, allowing only specific and necessary ports. Leaving ranges of ports open can allow access to ports that are vulnerabile to attack.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Work with security rules guide](https://docs.microsoft.com/en-us/azure/virtual-network/manage-network-security-group#work-with-security-rules) to modify the port ranges associated with a NSG using the Microsoft Azure Console.

### From the command line{% #from-the-command-line %}

Use the [Microsft Azure az network nsg rule update module](https://docs.microsoft.com/en-us/cli/azure/network/nsg/rule?view=azure-cli-latest#az-network-nsg-rule-update) to update the ports associated with a NSG using the Microsoft Azure CLI.

## References{% #references %}
