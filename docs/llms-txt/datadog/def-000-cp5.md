# Source: https://docs.datadoghq.com/security/default_rules/def-000-cp5.md

---
title: GitHub payment method removed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub payment method removed
---

# GitHub payment method removed
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a GitHub payment method has been removed.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a GitHub payment method has been removed.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or unexpected, begin your organization's incident response process and investigate.
