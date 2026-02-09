# Source: https://docs.datadoghq.com/security/default_rules/def-000-p9r.md

---
title: GitHub enterprise or organization recovery codes activity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub enterprise or organization
  recovery codes activity
---

# GitHub enterprise or organization recovery codes activity
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when a GitHub enterprise or organization recovery code has been interacted with by a user.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a Github recovery code is generated, viewed, downloaded, or printed. Attackers may use recovery codes to establish an administrator account and allow persistent access to the Github organization.

## Triage and response{% #triage-and-response %}

1. Determine if the action taken by `{{@github.actor}}` is expected and/or authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
