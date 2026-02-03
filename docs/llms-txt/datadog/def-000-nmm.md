# Source: https://docs.datadoghq.com/security/default_rules/def-000-nmm.md

---
title: Set Default ip6tables Policy for Incoming Packets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set Default ip6tables Policy for
  Incoming Packets
---

# Set Default ip6tables Policy for Incoming Packets
 
## Description{% #description %}

To set the default policy to DROP (instead of ACCEPT) for the built-in INPUT chain which processes incoming packets, add or correct the following line in `/etc/iptables/rules.v6`:

```
:INPUT DROP [0:0]
```

If changes were required, reload the ip6tables rules:

```gdscript3
$ sudo service ip6tables reload
```

## Rationale{% #rationale %}

In `ip6tables`, the default policy is applied only after all the applicable rules in the table are examined for a match. Setting the default policy to `DROP` implements proper design for a firewall, i.e. any packets which are not explicitly permitted should not be accepted.

## Warning{% #warning %}

Automated remediation for this rule is disabled. Changing firewall settings while connected over network can result in being locked out of the system.
