# Source: https://docs.datadoghq.com/security/default_rules/npt-kg2-pv2.md

---
title: VPC flow logging should be enabled in all VPCs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > VPC flow logging should be enabled in
  all VPCs
---

# VPC flow logging should be enabled in all VPCs
 
## Description{% #description %}

VPC Flow Logs capture information about the IP traffic to and from network interfaces in your VPCs. This feature provides visibility into rejected network traffic and assists in detecting unusual traffic for enhanced security workflows. It is recommended to enable VPC Flow Logs for packet rejects to monitor and analyze network activity effectively.

## Remediation{% #remediation %}

For instructions on enabling VPC Flow Logs for packet rejects, refer to the [Amazon VPC Flow Logs Guide](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/flow-logs.html).
