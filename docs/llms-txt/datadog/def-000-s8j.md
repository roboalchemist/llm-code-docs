# Source: https://docs.datadoghq.com/security/default_rules/def-000-s8j.md

---
title: >-
  Cisco Secure Email Threat Defense unusual spike found for emails having `Rare
  sender domain` detection technique
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Secure Email Threat Defense
  unusual spike found for emails having `Rare sender domain` detection technique
---

# Cisco Secure Email Threat Defense unusual spike found for emails having `Rare sender domain` detection technique

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566) 
## Goal{% #goal %}

Detects emails when there is a unusual spike in emails having `Rare sender domain` detection technique.

## Strategy{% #strategy %}

This rule monitors emails to detect spike in emails with `Rare sender domain` detection technique.

## Triage and response{% #triage-and-response %}

1. Investigate emails metadata that are: sender, receiver, sender domain to further evaluate the impact.
1. Determine the severity - `{{@verdict.techniques.severity}}` of the threat based emails and the potential impact on the organization.
1. Block these domains according to company policy if required.
1. Analyse if any sensitive data has been shared with these rare sender domain emails.
