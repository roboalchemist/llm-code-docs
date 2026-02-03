# Source: https://docs.datadoghq.com/security/default_rules/def-000-pp9.md

---
title: GitHub MFA requirement disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub MFA requirement disabled
---

# GitHub MFA requirement disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## Goal{% #goal %}

Detect when a GitHub multi-factor authentication (MFA) requirement has been disabled.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a GitHub MFA requirement has been disabled. The requirement for members to have two-factor authentication enabled to access an enterprise/organization was disabled. Attackers may may disable or modify MFA mechanisms to enable persistent access to compromised accounts.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
