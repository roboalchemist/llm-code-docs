# Source: https://docs.datadoghq.com/security/default_rules/def-000-ac6.md

---
title: >-
  Check Point Harmony Email & Collaboration malware attachments in email
  received by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Check Point Harmony Email &
  Collaboration malware attachments in email received by user
---

# Check Point Harmony Email & Collaboration malware attachments in email received by user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1036-masquerading](https://attack.mitre.org/techniques/T1036) 
## Goal{% #goal %}

Detects when emails containing malware attachments are received from an external sender, which may indicate a malware distribution campaign or a compromised sender attempting to spread malicious payloads.

## Strategy{% #strategy %}

This rule monitors inbound emails and raises an alert when emails with malware attachments originate from an external sender, suggesting a targeted attack or widespread malware distribution.

## Triage and Response{% #triage-and-response %}

1. Review the sender email address `{{@event.entity.entity_payload.from_email}}` and analyze the malware attachments.
1. Quarantine or delete the detected emails to prevent users from opening malicious attachments.
1. Notify affected users and begin a security incident response process to investigate engagement with attachment and endpoint activity.
