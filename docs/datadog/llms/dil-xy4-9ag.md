# Source: https://docs.datadoghq.com/security/default_rules/dil-xy4-9ag.md

---
title: Jumpcloud policy modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Jumpcloud policy modified
---

# Jumpcloud policy modified
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1484-domain-or-tenant-policy-modification](https://attack.mitre.org/techniques/T1484)
## Goal{% #goal %}

Detect when a JumpCloud policy is modified.

## Strategy{% #strategy %}

This rule lets you monitor the following JumpCloud event to detect when a policy is modified:

- `@evt.name:policy_update`

## Triage and response{% #triage-and-response %}

1. Contact the JumpCloud administrator `{{@usr.email}}` to confirm if the policy modification(s) was intended.
1. If the change was **not** authorized, verify there are no other signals from the administrator:`{{@usr.email}}`.
