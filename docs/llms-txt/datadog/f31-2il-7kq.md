# Source: https://docs.datadoghq.com/security/default_rules/f31-2il-7kq.md

---
title: Windows user added to Domain Admin group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows user added to Domain Admin
  group
---

# Windows user added to Domain Admin group
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when a user is added to the Domain Administrator group. A rogue active directory account can added to the Domain Admins group.

## Strategy{% #strategy %}

Monitoring of Windows event logs where `@evt.id` is `4728` and the `@Event.EventData.Data.TargetUserName:"Domain Admins"`

## Triage & Response{% #triage--response %}

Verify if `{{@Event.EventData.Data.TargetUserName}}` should be added to the `Domain Admins` group
