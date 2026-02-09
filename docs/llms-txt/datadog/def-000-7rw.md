# Source: https://docs.datadoghq.com/security/default_rules/def-000-7rw.md

---
title: >-
  Delinea Privilege Manager detected a suspicious application justification
  event based on VirusTotal rating
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Delinea Privilege Manager detected a
  suspicious application justification event based on VirusTotal rating
---

# Delinea Privilege Manager detected a suspicious application justification event based on VirusTotal rating

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Detects application justification events for suspicious rated applications by VirusTotal.

## Strategy{% #strategy %}

This rule monitors Delinea Privilege Manager logs to detect application justification events for suspicious rated applications by VirusTotal.

## Triage and Response{% #triage-and-response %}

1. Investigate the application justification event for file `{{@FileName}}` on system `{{@ComputerName}}`, including details like filepath: `{{@FilePath}}` and user: `{{@usr.name}}`.
1. Determine if the endpoint is critical or frequently targeted.
1. Review the justification: `{{@UserReason}}` to verify alignment with legitimate business needs.
1. Validate the justification directly with the user to confirm intent.
1. Block the application if unauthorized, and isolate the endpoint if suspicious activity is detected.
1. For repeatedly flagged applications, enforce stricter controls or require administrator approval.
