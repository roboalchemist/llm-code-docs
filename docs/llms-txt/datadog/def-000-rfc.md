# Source: https://docs.datadoghq.com/security/default_rules/def-000-rfc.md

---
title: EC2 Client VPN endpoints should have client connection logging enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 Client VPN endpoints should have
  client connection logging enabled
---

# EC2 Client VPN endpoints should have client connection logging enabled
 
## Description{% #description %}

This control verifies if client connection logging is enabled for an AWS Client VPN endpoint. AWS Client VPN endpoints facilitate secure connections between remote clients and resources within a Virtual Private Cloud (VPC). Enabling connection logging enhances visibility by allowing you to monitor user activity on the VPN endpoint. When connection logging is activated, you can assign a log stream name within a log group, or if none is specified, the Client VPN service automatically generates one.

## Remediation{% #remediation %}

For instructions on configuring logging, refer to the [Enable connection logging for an existing Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-with-connection-logs.html#create-connection-log-existing) section of the AWS Client VPN Administrator Guide.
