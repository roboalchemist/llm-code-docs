# Source: https://docs.datadoghq.com/security/default_rules/sl8-aa0-qkv.md

---
title: Windows Net command executed to enumerate administrators
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows Net command executed to
  enumerate administrators
---

# Windows Net command executed to enumerate administrators
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1087-account-discovery](https://attack.mitre.org/techniques/T1087)
## Goal{% #goal %}

Detect when a user runs the `net` command to enumerate the `Administrators` group, which could be indicative of adversarial reconnaissance activity.

## Strategy{% #strategy %}

Monitoring of Windows event logs where `@evt.id` is `4799`, `@Event.EventData.Data.CallerProcessName` is `*net1.exe` and `@Event.EventData.Data.TargetUserName` is `Administrators`.

## Triage and response{% #triage-and-response %}

Verify if `{{@Event.EventData.Data.SubjectUserName}}` has a legitimate reason to check for users in the Administrator group on `{{host}}`.
