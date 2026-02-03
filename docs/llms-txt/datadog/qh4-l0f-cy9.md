# Source: https://docs.datadoghq.com/security/default_rules/qh4-l0f-cy9.md

---
title: Azure Datadog Log Forwarder Deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure Datadog Log Forwarder Deleted
---

# Azure Datadog Log Forwarder Deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when the Datadog Azure function is deleted which will prevent Azure logs from being sent to Datadog.

## Strategy{% #strategy %}

Monitor Azure logs where `@evt.name` is `"MICROSOFT.WEB/SITES/DELETE"`, `@evt.outcome` is `Success`, and the `@resourceID` contains `DATADOG` and `LOG`. This rule does not work if the the Azure resource group or Azure function does not contain `DATADOG` or `LOG`.

## Triage and response{% #triage-and-response %}

1. Verify the Azure function (`@resourceId`) is responsible for forwarding logs to Datadog.
1. Determine if there is a legitimate reason for deleting the Azure function.
1. If activity is not expected, investigate activity from the service principal (`@identity.authorization.evidence`) or user (`{{@usr.id}}`).
