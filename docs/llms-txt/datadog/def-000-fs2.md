# Source: https://docs.datadoghq.com/security/default_rules/def-000-fs2.md

---
title: GitHub Dependabot configuration changed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub Dependabot configuration changed
---

# GitHub Dependabot configuration changed
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a GitHub Dependabot setting has been disabled.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a Dependabot setting has been disabled. Dependabot will alert developers when a repository is using a software dependency with a known vulnerability. Disabling these settings could lead to a degradation in the organization's security posture.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.

- 3 January 2025 - update detection rule severity from High to Medium and Medium to Low on several cases.
- 3 January 2025 - update naming of rule.
