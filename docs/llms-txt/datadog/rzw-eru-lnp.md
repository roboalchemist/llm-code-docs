# Source: https://docs.datadoghq.com/security/default_rules/rzw-eru-lnp.md

---
title: Azure Network Security Groups or Rules Created, Modified, or Deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure Network Security Groups or Rules
  Created, Modified, or Deleted
---

# Azure Network Security Groups or Rules Created, Modified, or Deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when an Azure network security group or an Azure network security rule has been created, modified, or deleted.

## Strategy{% #strategy %}

Monitor Azure activity logs and detect when the `@evt.name` is equal to any one of the following names:

- `MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/WRITE`
- `MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/DELETE`
- `MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/SECURITYRULES/WRITE`
- `MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/SECURITYRULES/DELETE`

and `@evt.outcome` is equal to `Success`.

## Triage and response{% #triage-and-response %}

Inspect the security group or security rule and determine if it exposes any Azure resources that should not be exposed.
