# Source: https://docs.datadoghq.com/security/default_rules/aoc-jdx-q3d.md

---
title: Azure SQL Server Firewall Rules Created or Modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure SQL Server Firewall Rules Created
  or Modified
---

# Azure SQL Server Firewall Rules Created or Modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when an Azure network security rule has been created, modified, or deleted.

## Strategy{% #strategy %}

Monitor Azure activity logs and detect when the `@evt.name` is equal to any of the following names:

- `MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/SECURITYRULES/WRITE`
- `MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/SECURITYRULES/DELETE`

and `@evt.outcome` is equal to `Success`.

## Triage and response{% #triage-and-response %}

Inspect the security rule and determine if it exposes any Azure resources that should not be made public.
