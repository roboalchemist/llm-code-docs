# Source: https://docs.datadoghq.com/security/default_rules/def-000-rou.md

---
title: GitHub OAuth application access restrictions disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub OAuth application access
  restrictions disabled
---

# GitHub OAuth application access restrictions disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when GitHub OAuth application access restrictions have been disabled.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when GitHub OAuth application access restrictions have been disabled. Organizations can choose which OAuth applications have access to their repositories and other resources by enabling OAuth app access restrictions. An attacker with unauthorized access could authorize a third-party OAuth application allowing them to maintain access to a GitHub environment without these restrictions.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or unexpected, begin your organization's incident response process and investigate.
