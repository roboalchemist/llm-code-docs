# Source: https://docs.datadoghq.com/security/default_rules/mex-to8-3fa.md

---
title: Jumpcloud policy created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Jumpcloud policy created
---

# Jumpcloud policy created
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1484-domain-or-tenant-policy-modification](https://attack.mitre.org/techniques/T1484)
## Goal{% #goal %}

Detect when a JumpCloud policy is created.

## Strategy{% #strategy %}

This rule lets you monitor the following JumpCloud event to detect when a policy is created:

- `@evt.name:policy_create`

## Triage and response{% #triage-and-response %}

1. Contact the JumpCloud administrator `{{@usr.email}}` to confirm if the policy creation was intended.
1. If the change was **not** authorized, verify there are no other signals from the administrator:`{{@usr.email}}`.
