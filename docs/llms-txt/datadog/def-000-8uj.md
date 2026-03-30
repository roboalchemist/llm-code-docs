# Source: https://docs.datadoghq.com/security/default_rules/def-000-8uj.md

---
title: Tailscale user role updated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Tailscale user role updated
---

# Tailscale user role updated
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when a Tailscale user's role is updated.

## Strategy{% #strategy %}

This rule monitors Tailscale logs for when a user's role is updated. This could be a privilege escalation vector for an attacker looking to bypass restrictions from a lower privileged user.

## Triage and response{% #triage-and-response %}

1. Investigate the user `{{@usr.email}}` that performed the UPDATE action on user `{{@target.name}}`.
1. Compare the previous roles `{{@old}}` with the new role updates containing the `{{@new}}` role and confirm that they should be assigned to the user `{{@target.name}}`.
1. If the activity is deemed malicious:
   - Begin your organization's incident response process and investigate.
