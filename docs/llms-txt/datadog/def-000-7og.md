# Source: https://docs.datadoghq.com/security/default_rules/def-000-7og.md

---
title: Network Firewall logging should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Network Firewall logging should be
  enabled
---

# Network Firewall logging should be enabled
 
## Description{% #description %}

This control verifies whether at least one type of logging is enabled for an AWS Network Firewall.

Enabling logging is essential for ensuring the reliability, availability, and performance of your firewalls. AWS Network Firewall logging provides detailed insights into network traffic, including timestamps of when the stateful engine processed a packet flow, detailed packet flow information, and any actions taken by stateful rules against the packet flow.

## Remediation{% #remediation %}

For guidance on configuring firewall logging, please refer to the [Updating a firewall's logging configuration](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-update-logging-configuration.html) section of the AWS Network Firewall Developer Guide.
