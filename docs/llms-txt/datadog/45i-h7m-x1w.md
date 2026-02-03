# Source: https://docs.datadoghq.com/security/default_rules/45i-h7m-x1w.md

---
title: Remote administration port access should be restricted to trusted networks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Remote administration port access
  should be restricted to trusted networks
---

# Remote administration port access should be restricted to trusted networks
 
## Description{% #description %}

The Network Access Control List (NACL) provides stateless filtering of ingress and egress network traffic to AWS resources. Allowing unrestricted ingress access to remote server administration ports, such as SSH (port 22) and RDP (port 3389), can significantly increase the risk of unauthorized access and potential compromise of resources. It is recommended to restrict access to these ports to minimize the attack surface and enhance security.

## Remediation{% #remediation %}

For detailed guidance on configuring network ACLs to restrict access, refer to the [VPC Network ACLs documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html).
