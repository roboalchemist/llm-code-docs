# Source: https://docs.datadoghq.com/security/default_rules/ngh-qas-7b3.md

---
title: Jumpcloud administrator role assigned
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Jumpcloud administrator role assigned
---

# Jumpcloud administrator role assigned
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when administrative privileges are provisioned to a JumpCloud user.

## Strategy{% #strategy %}

This rule lets you monitor the following JumpCloud event to detect when administrative privileges are provisioned:

- `user_admin_granted`

## Triage and response{% #triage-and-response %}

1. Contact the JumpCloud administrator: `{{@usr.email}}` to confirm that the users or devices should have administrative privileges.
1. If the change was **not** authorized, verify there are no other signals from the JumpCloud administrator: `{{@usr.email}}`.
