# Source: https://docs.datadoghq.com/security/default_rules/apn-0ib-a6f.md

---
title: Azure diagnostic setting deleted or disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure diagnostic setting deleted or
  disabled
---

# Azure diagnostic setting deleted or disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a diagnostic setting is deleted which can disable centralized logging and metrics on Azure.

## Strategy{% #strategy %}

Monitor Azure logs where `@evt.name` is `"MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/DELETE"` and `@evt.outcome` is `Success`.

## Triage and response{% #triage-and-response %}

1. Inspect the diagnostic setting resource which is found in `@resourceId`.
1. Verify that the user (`{{@usr.id}}`) to determine if the removal of the resource is legitimate.
