# Source: https://docs.datadoghq.com/security/default_rules/34e-bda-42c.md

---
title: Azure Network Security Group Open to the World
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure Network Security Group Open to
  the World
---

# Azure Network Security Group Open to the World
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when an Azure network security group allows inbound traffic from all IP Addresses.

## Strategy{% #strategy %}

This rule monitors Azure Activity logs for network changes and detects when the `@evt.name` has a value of `MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/WRITE`, `@properties.securityRules.properties.direction` has a value of `Inbound`, `@properties.securityRules.properties.access` has a value of `Allow`, and `@properties.securityRules.properties.sourceAddressPrefix` has a value of either `0.0.0.0/0` OR `*`.

## Triage and response{% #triage-and-response %}

1. Inspect which Virtual Machines are associated with this security group.
1. Determine whether this security group and the VMs should permit inbound traffic from all IP addresses.
