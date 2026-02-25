# Source: https://docs.datadoghq.com/security/default_rules/f72-zu8-tjj.md

---
title: Azure Policy Assignment Created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure Policy Assignment Created
---

# Azure Policy Assignment Created
Classification:complianceTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when an Azure policy assignment has been created.

## Strategy{% #strategy %}

Monitor Azure activity logs and detect when the `@evt.name` is equal to `MICROSOFT.AUTHORIZATION/POLICYASSIGNMENTS/WRITE` and `@evt.outcome` is equal to `Success`.

## Triage and response{% #triage-and-response %}

Inspect the policy assignment and determine if an unsolicited change was made on any Azure resources.
