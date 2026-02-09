# Source: https://docs.datadoghq.com/security/default_rules/def-008-4ba.md

---
title: OneLogin API Token Created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > OneLogin API Token Created
---

# OneLogin API Token Created
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a new OneLogin API token is created.

## Strategy{% #strategy %}

This rule lets you monitor the OneLogin generated audit event to detect when a new API token is created.

## Triage and response{% #triage-and-response %}

1. Contact the user who created the API token and ensure that the API token is needed.
