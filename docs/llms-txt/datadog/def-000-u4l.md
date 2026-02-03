# Source: https://docs.datadoghq.com/security/default_rules/def-000-u4l.md

---
title: >-
  Check Point Harmony Email & Collaboration multiple spam emails from external
  sender
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Check Point Harmony Email &
  Collaboration multiple spam emails from external sender
---

# Check Point Harmony Email & Collaboration multiple spam emails from external sender

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566) 
## Goal{% #goal %}

Detects when multiple spam emails are received from an external sender within a short period, which may indicate a spam campaign, potential phishing attempt, or an attempt to evade email filtering.

## Strategy{% #strategy %}

This rule monitors inbound emails and raises an alert when multiple spam emails originate from an external sender, suggesting possible malicious intent or an improperly configured email system.

## Triage and Response{% #triage-and-response %}

1. Review the sender email address `{{@event.entity.entity_payload.from_email}}` and analyze the spam emails.
1. Move similar emails to the spam or junk folder to reduce further risk.
1. If confirmed malicious, initiate the security incident response process.
