# Source: https://docs.datadoghq.com/security/default_rules/def-000-ugf.md

---
title: >-
  Cisco Secure Email Threat Defense high number of threat emails received from a
  particular domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Secure Email Threat Defense high
  number of threat emails received from a particular domain
---

# Cisco Secure Email Threat Defense high number of threat emails received from a particular domain

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566) 
## Goal{% #goal %}

Detects when threat emails are received more than 10 times from a particular domain.

## Strategy{% #strategy %}

This rule monitors emails to detect a high number of threat emails received from a specific domain.

## Triage and response{% #triage-and-response %}

1. Investigate the threat emails sent from domain - `{{@senderDomain}}`.
1. Take necessary and appropriate actions according to company policy to block that domain.
1. Alert users about the identified threat domain. Advise them to be cautious and not interact with any suspicious emails from this domain.
1. Review internal logs to gather details on recipients, delivery statuses, and any user interactions.
