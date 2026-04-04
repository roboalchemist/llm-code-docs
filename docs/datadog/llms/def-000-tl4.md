# Source: https://docs.datadoghq.com/security/default_rules/def-000-tl4.md

---
title: 'Trend Micro Email Security alert: High volume of emails to recipient'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trend Micro Email Security alert: High
  volume of emails to recipient
---

# Trend Micro Email Security alert: High volume of emails to recipient

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566)
## Goal{% #goal %}

Detect an unusually high volume of emails received, which could indicate a potential spam campaign, compromised email account, or other malicious activities aimed at overwhelming email infrastructure or distributing harmful content.

## Strategy{% #strategy %}

Monitor Trend Micro Email Security mail tracking logs to identify instances where a high volume of emails is received by a single recipient within a short period. This detection rule aims to identify potential threats early, enabling timely investigation and mitigation to protect email systems and recipients from spam or malicious content.

## Triage and response{% #triage-and-response %}

1. Analyze email volume and pattern to differentiate between legitimate activities and potential threats.
1. Look after the recipient email address `{{@recipient}}` for signs of compromise.
1. Review the email content for indicators of malicious activity, like suspicious links, attachments, or unusual requests. Identify patterns such as similar subject lines, repetitive content, or external links.
1. If the activity is deemed malicious, block the sender(s) and quarantine or delete the emails.
1. Inform the recipient about the potential threat and provide guidance on handling similar emails in the future.
