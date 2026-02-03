# Source: https://docs.datadoghq.com/security/default_rules/p9l-g28-nxb.md

---
title: Windows Domain Admin group changed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows Domain Admin group changed
---

# Windows Domain Admin group changed
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when the Domain Administrator group is modified.

## Strategy{% #strategy %}

Monitoring of Windows event logs where `@evt.id` is 4737 and the `@Event.EventData.Data.TargetUserName:"Domain Admins"`

## Triage & Response{% #triage--response %}

Verify if `{{@Event.EventData.Data.SubjectUserName}}` has a legitimate reason for changing the `Domain Admins` group
