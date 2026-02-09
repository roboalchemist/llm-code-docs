# Source: https://docs.datadoghq.com/security/default_rules/ypa-4t4-zo4.md

---
title: Azure new owner added for service principal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure new owner added for service
  principal
---

# Azure new owner added for service principal
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a new owner is added to a service principal, which applies to privilege escalation or persistence.

## Strategy{% #strategy %}

Monitor Azure Active Directory logs where `@evt.name` is `"Add owner to service principal"` and `@evt.outcome` of `Success`.

## Triage and response{% #triage-and-response %}

1. Inspect that the user is added to a service principal in `@properties.targetResources`.
1. Verify with the user (`{{@usr.name}}`) to determine if the owner addition is legitimate.
