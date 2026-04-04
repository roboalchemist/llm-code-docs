# Source: https://docs.datadoghq.com/security/default_rules/def-000-6hx.md

---
title: Network Firewall firewalls should have deletion protection enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Network Firewall firewalls should have
  deletion protection enabled
---

# Network Firewall firewalls should have deletion protection enabled

## Description{% #description %}

This control verifies if deletion protection is activated for an AWS Network Firewall.

AWS Network Firewall is a managed stateful network security service, offering traffic inspection and filtering for traffic flowing into, out of, or between Virtual Private Clouds (VPCs). Enabling deletion protection safeguards the firewall from being unintentionally deleted.

## Remediation{% #remediation %}

For guidance on configuring deletion protection, please refer to the [Updating a firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-updating.html) section of the AWS Network Firewall Developer Guide.
