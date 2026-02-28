# Source: https://docs.datadoghq.com/security/default_rules/def-000-7dd.md

---
title: >-
  Check Point Harmony Email & Collaboration multiple phishing emails from
  external sender
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Check Point Harmony Email &
  Collaboration multiple phishing emails from external sender
---

# Check Point Harmony Email & Collaboration multiple phishing emails from external sender

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566)
## Goal{% #goal %}

Detects when multiple phishing emails are received from an external sender within a short period, which may indicate an ongoing phishing campaign targeting users.

## Strategy{% #strategy %}

This rule monitors inbound emails and raises an alert when multiple phishing emails originate from an external sender, potentially signalling a coordinated attack or a compromised sender account. Emails that are quarantined or deleted do not raise an alert.

## Triage and Response{% #triage-and-response %}

1. Review the sender email address `{{@event.entity.entity_payload.from_email}}` to determine legitimacy.
1. Quarantine or delete the detected phishing emails to prevent user interaction.
1. Investigate if the sender is a compromised legitimate account or part of a larger phishing campaign.
1. If confirmed malicious, begin the security incident response process.
