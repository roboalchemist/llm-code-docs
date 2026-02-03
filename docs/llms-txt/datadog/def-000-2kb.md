# Source: https://docs.datadoghq.com/security/default_rules/def-000-2kb.md

---
title: Delinea Privilege Manager detected a bad-rated application action event
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Delinea Privilege Manager detected a
  bad-rated application action event
---

# Delinea Privilege Manager detected a bad-rated application action event

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Detects bad-rated application action events.

## Strategy{% #strategy %}

This rule monitors the Delinea Privilege Manager logs to detect bad-rated application action events.

## Triage and Response{% #triage-and-response %}

1. Analyze the bad-rated application action event on the computer: `{{@ComputerName}}`.
1. Determine whether the flagged application `{{@FileName}}` located at `{{@FilePath}}` was executed or installed on other systems.
1. Temporarily isolate the affected system to prevent potential spread or harm.
1. Update the application control policy to block the flagged application.
1. Notify the user to avoid similar activities and ensure compliance with application usage policies.
