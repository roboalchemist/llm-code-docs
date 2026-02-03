# Source: https://docs.datadoghq.com/security/default_rules/def-000-b0v.md

---
title: 'Trend Micro Email Security alert: High volume of emails from sender'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trend Micro Email Security alert: High
  volume of emails from sender
---

# Trend Micro Email Security alert: High volume of emails from sender

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566) 
## Goal{% #goal %}

Detect an unusually high volume of emails sent, which could indicate a potential spam campaign, compromised email account, or other malicious activities aimed at overwhelming email infrastructure or distributing harmful content.

## Strategy{% #strategy %}

Monitor Trend Micro Email Security mail tracking logs to identify instances where a single sender email address sends a high volume of emails within a short period. This detection rule aims to identify potential threats early, enabling timely investigation and mitigation to protect email systems and recipients from spam or malicious content.

## Triage and response{% #triage-and-response %}

1. Analyze email volume and pattern to differentiate between legitimate activities and potential threats.
1. Investigate the sender email address `{{@sender}}` for signs of compromise.
1. Evaluate email content for indicators of spam or malicious intent.
1. Add the sender's email to your block list and implement security measures like changing passwords and enabling MFA if suspicious activity is confirmed.
