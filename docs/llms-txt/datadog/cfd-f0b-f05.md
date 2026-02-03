# Source: https://docs.datadoghq.com/security/default_rules/cfd-f0b-f05.md

---
title: Outbound access on all ports should be restricted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Outbound access on all ports should be
  restricted
---

# Outbound access on all ports should be restricted
 
## Description{% #description %}

Reduce the probability of a breach by checking [EC2 security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) for outbound rules that allow unfettered access to any TCP/UDP ports and restrict access to IP addresses that require this port.

## Rationale{% #rationale %}

Malicious activity, such as denial-of-service (DoS) and distributed denial-of-service (DDoS) attacks, can occur when permitting unfettered outbound access.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules) docs to learn how to add a security group rule that will restrict access to IP addresses that require a specific port.

### From the command line{% #from-the-command-line %}

1. Run `revoke-security-group-egress` to remove IP permissions for the selected EC2 security group.

In the `revoke-security-group-egress.sh` file:

   ```bash
       aws ec2 revoke-security-group-egress
           --group-id your-group-id
           --ip-permissions '[{"IpProtocol": "tcp", "FromPort": 22, "ToPort": 22, "IpRanges": [{"CidrIp": "0.0.0.0/0"}]}]'
       
```

1. Run `authorize-security-group-egress` with new parameters to restrict outbound access to specific destinations.

In the `authorize-security-group-egress.sh` file:

   ```bash
       aws ec2 authorize-security-group-egress
           --group-id your-group-id
           --ip-permissions '[{"IpProtocol": "tcp", "FromPort": 22, "ToPort": 22, "IpRanges": [{"CidrIp": "0.0.0.0/0"}]}]'
       
```
