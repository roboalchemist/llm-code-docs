# Source: https://docs.datadoghq.com/security/default_rules/def-000-0an.md

---
title: Network Firewall policies should have at least one associated rule group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Network Firewall policies should have
  at least one associated rule group
---

# Network Firewall policies should have at least one associated rule group

## Description{% #description %}

This control verifies if a Network Firewall policy includes at least one stateful or stateless rule group.

A firewall policy dictates how traffic is monitored and managed within an Amazon Virtual Private Cloud (Amazon VPC). Configuring stateful and stateless rule groups enables packet filtering, regulates traffic flow, and establishes default traffic handling rules.

## Remediation{% #remediation %}

For guidance on configuring firewall logging, refer to the [Firewall policy settings in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-settings.html) section of the AWS Network Firewall Developer Guide.
