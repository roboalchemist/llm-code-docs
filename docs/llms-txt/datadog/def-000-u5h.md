# Source: https://docs.datadoghq.com/security/default_rules/def-000-u5h.md

---
title: 'Trend Micro Email Security alert: Phishing email detected'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trend Micro Email Security alert:
  Phishing email detected
---

# Trend Micro Email Security alert: Phishing email detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566) 
## Goal{% #goal %}

Detect when Trend Micro Email Security identifies a threat-related email.

## Strategy{% #strategy %}

Monitor Trend Micro Email Security logs for specific threat detection events. This rule aims to identify and respond to potential email threats promptly, ensuring the security of the email infrastructure and recipients.

## Triage and Response{% #triage-and-response %}

1. Threat event of `{{@eventType}}` type detected.
1. Review the email's headers, body, and attachments for any indicators of malicious activity.
1. If malicious activity is confirmed, block the sender's email address and quarantine the affected email(s) to prevent further access and distribution of harmful content.
