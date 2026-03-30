# Source: https://docs.datadoghq.com/security/default_rules/01b-a6f-d0c.md

---
title: Network ACLs should enforce inbound traffic restrictions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Network ACLs should enforce inbound
  traffic restrictions
---

# Network ACLs should enforce inbound traffic restrictions

## Description{% #description %}

Investigate AWS Network Access Control Lists (NACLs) for rules that enable multiple open ports and limit ingress traffic access based on port range.

## Rationale{% #rationale %}

Eliminate the threat of unauthorized access malicious activities, such as Denial of Service (DoS) or Distributed Denial of Service (DDoS) attacks, by opening only the ports that are required by your application.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Adding and deleting rules](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#Rules) docs to limit ingress traffic access based on port range.

### From the command line{% #from-the-command-line %}

1. Run `replace-network-acl-entry` to create a rule that only allows ingress traffic from a specific port range.

In the `replace-network-acl-entry.sh` file:

   ```bash
       aws ec2 replace-network-acl-entry
           --network-acl-id id-01234567
           --ingress
           --rule-number 01
           --protocol tcp
           --port-range From=000,To=000
           --rule-action allow

```
