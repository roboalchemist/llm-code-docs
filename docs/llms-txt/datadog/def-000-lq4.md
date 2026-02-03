# Source: https://docs.datadoghq.com/security/default_rules/def-000-lq4.md

---
title: >-
  Check Point Harmony Email & Collaboration DLP policy violation in outgoing
  email
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Check Point Harmony Email &
  Collaboration DLP policy violation in outgoing email
---

# Check Point Harmony Email & Collaboration DLP policy violation in outgoing email

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1036-masquerading](https://attack.mitre.org/techniques/T1036) 
## Goal{% #goal %}

Detects outgoing emails that violate Data Loss Prevention (DLP) policies, indicating potential accidental data exposure, policy misconfiguration, or intentional data exfiltration.

## Strategy{% #strategy %}

This rule monitors outgoing emails flagged by DLP policies and raises an alert when sensitive data is shared in violation of security controls, helping to prevent unauthorized data leaks.

## Triage and Response{% #triage-and-response %}

1. Review the sender email address `{{@event.entity.entity_payload.from_email}}` and analyze the email content for policy violations.
1. Determine the recipient (`{{@event.entity.entity_payload.to_email}}`) of the email content and assess whether the detected violation was intentional or accidental.
1. Quarantine or block the email to prevent data exfiltration if necessary.
1. If unauthorized data sharing is suspected, escalate to your security incident response process.
