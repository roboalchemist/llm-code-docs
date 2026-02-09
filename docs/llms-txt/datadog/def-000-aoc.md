# Source: https://docs.datadoghq.com/security/default_rules/def-000-aoc.md

---
title: >-
  GitHub a branch protection requirement was overridden by a repository
  administrator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub a branch protection requirement
  was overridden by a repository administrator
---

# GitHub a branch protection requirement was overridden by a repository administrator
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when GitHub branch protection has been overridden by a repository administrator.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when GitHub branch protection has been overridden by a repository administrator. By default, the restrictions of a branch protection rule do not apply to users with administrative permissions to the repository or users with custom roles with the "bypass branch protections" permission. Overriding this protection could lead to degradation in the security posture of an organization.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
