# Source: https://docs.datadoghq.com/security/default_rules/def-000-mrm.md

---
title: Site-to-Site VPN connection tunnels should be online
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Site-to-Site VPN connection tunnels
  should be online
---

# Site-to-Site VPN connection tunnels should be online
 
## Description{% #description %}

A VPN tunnel is an encrypted pathway that allows data to move securely between the customer network and AWS within an AWS Site-to-Site VPN connection. Each VPN connection includes two tunnels, which can operate simultaneously to ensure high availability. Keeping both VPN tunnels active is essential for maintaining a secure and resilient connection between an AWS VPC and your remote network.

## Remediation{% #remediation %}

For instructions on configuring VPN tunnel options, refer to the [Modifying Site-to-Site VPN tunnel options](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-tunnel-options.html) section in the AWS Site-to-Site VPN User Guide.
