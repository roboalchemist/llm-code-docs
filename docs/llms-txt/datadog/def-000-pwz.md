# Source: https://docs.datadoghq.com/security/default_rules/def-000-pwz.md

---
title: GitHub audit log streaming endpoint was deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub audit log streaming endpoint was
  deleted
---

# GitHub audit log streaming endpoint was deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when a GitHub audit log stream has been deleted.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when an audit log stream is deleted. An attacker may remove an audit log stream to evade defenses set up by a security team.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
