# Source: https://docs.datadoghq.com/security/default_rules/def-000-p9z.md

---
title: GitHub audit log streaming endpoint was modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub audit log streaming endpoint was
  modified
---

# GitHub audit log streaming endpoint was modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when GitHub audit log streaming settings have been modified.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs streaming settings when altered. A modification in this setting could cause degradation in the security posture of an organization as audit logs would cease to flow into centralized storage.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
