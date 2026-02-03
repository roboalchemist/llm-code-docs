# Source: https://docs.datadoghq.com/security/default_rules/def-000-mqn.md

---
title: Unused Network Access Control Lists should be removed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unused Network Access Control Lists
  should be removed
---

# Unused Network Access Control Lists should be removed
 
## Description{% #description %}

This check verifies if there are any unused network access control lists (ACLs).

It examines the configuration of the `AWS::EC2::NetworkAcl` resource and identifies the connections of the network ACL.

If the only connection is the VPC of the network ACL, the check fails.

If there are other connections listed, the check passes.

## Remediation{% #remediation %}

Please refer to the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#DeleteNetworkACL) for guidance on removing an unused network ACL. Note that you cannot delete the default network ACL or an ACL that is linked to subnets.
