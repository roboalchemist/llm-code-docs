# Source: https://docs.datadoghq.com/security/default_rules/def-000-eg5.md

---
title: GitHub SSH certificate authority deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub SSH certificate authority
  deleted
---

# GitHub SSH certificate authority deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a GitHub SSH certificate authority has been deleted.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when GitHub SSH certificate authority has been deleted. With an SSH certificate authority organization, an enterprise account can provide SSH certificates that members can use to access its resources with Git. Any deletions should be monitored and the change should be verified to ensure it is authorized.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
