# Source: https://docs.datadoghq.com/security/default_rules/def-000-9mn.md

---
title: Security groups should restrict traffic to trusted IPv6 addresses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Security groups should restrict traffic
  to trusted IPv6 addresses
---

# Security groups should restrict traffic to trusted IPv6 addresses
 
## Description{% #description %}

Security groups provide stateful filtering of ingress and egress network traffic to AWS resources. Allowing unrestricted ingress access to remote server administration ports, such as SSH (port 22) and RDP (port 3389), increases the attack surface and raises the risk of resource compromise. It is recommended to restrict access to these ports to maintain secure environments. Before making changes, ensure that administrators have alternative access to remote server administration ports.

## Remediation{% #remediation %}

For guidance on modifying security groups to restrict access, refer to the [AWS Security Groups documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html).
