# Source: https://docs.datadoghq.com/security/default_rules/def-000-neu.md

---
title: Forcepoint Security Service Edge file quarantined event
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Forcepoint Security Service Edge file
  quarantined event
---

# Forcepoint Security Service Edge file quarantined event

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Forcepoint SSE detected file quarantined event.

## Strategy{% #strategy %}

Monitor Forcepoint SSE logs for instances where a file is quarantined.

## Triage and Response{% #triage-and-response %}

1. Review the log details to identify the user - `{{@usr.name}}` involved in the quarantined file activity.
1. Examine the user's recent actions, such as file uploads, downloads, or email attachments. Check for anomalies in the user's account, including unusual login times or locations.
1. Verify the quarantined file against threat intelligence sources.
1. Update antivirus or security policies to reduce false positives and improve detection accuracy.
