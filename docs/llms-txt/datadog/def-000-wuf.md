# Source: https://docs.datadoghq.com/security/default_rules/def-000-wuf.md

---
title: >-
  Network Firewall policy default stateless action for full packets should be
  drop or forward
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Network Firewall policy default
  stateless action for full packets should be drop or forward
---

# Network Firewall policy default stateless action for full packets should be drop or forward
 
## Description{% #description %}

This control verifies whether the default stateless action for full packets in a Network Firewall policy is set to `aws:drop` or `aws:forward_to_sfe`. The control fails if the default stateless action is `aws:pass`.

A firewall policy determines how traffic is monitored and managed within an Amazon VPC. It includes stateless and stateful rule groups to filter packets and regulate traffic flow. Setting the default action to `aws:pass` could allow unintended traffic.

## Remediation{% #remediation %}

For guidance on configuring firewall logging, refer to the [Updating a firewall policy in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-updating.html) section of the AWS Network Firewall Developer Guide.
