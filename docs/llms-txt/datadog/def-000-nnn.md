# Source: https://docs.datadoghq.com/security/default_rules/def-000-nnn.md

---
title: Set Default iptables Policy for Incoming Packets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set Default iptables Policy for
  Incoming Packets
---

# Set Default iptables Policy for Incoming Packets

## Description{% #description %}

To set the default policy to DROP (instead of ACCEPT) for the built-in INPUT chain which processes incoming packets, add or correct the following line in `/etc/iptables/rules.v4`:

```
:INPUT DROP [0:0]
```

## Rationale{% #rationale %}

In `iptables` the default policy is applied only after all the applicable rules in the table are examined for a match. Setting the default policy to `DROP` implements proper design for a firewall, i.e. any packets which are not explicitly permitted should not be accepted.

## Warning{% #warning %}

Automated remediation for this rule is disabled. Changing firewall settings while connected over network can result in being locked out of the system.
