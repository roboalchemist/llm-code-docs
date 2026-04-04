# Source: https://docs.datadoghq.com/security/default_rules/def-000-fcx.md

---
title: Forcepoint Security Service Edge high volume of emails from a sender
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Forcepoint Security Service Edge high
  volume of emails from a sender
---

# Forcepoint Security Service Edge high volume of emails from a sender

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566)
## Goal{% #goal %}

Identify and respond to incidents where a high volume of emails are sent from a single sender, which may indicate spam activity, compromised accounts, or policy violations.

## Strategy{% #strategy %}

Monitor Forcepoint SSE logs for high email volumes from individual senders.

## Triage and Response{% #triage-and-response %}

1. Review the log details to identify the sender - `{{@emailfrom}}` responsible for the high email volume.
1. Confirm whether the sender is an internal user, an authorized external contact, or an unknown entity and also check for any recent changes to the sender's account, such as password resets or suspicious login locations.
1. Analyze the content and recipients of the emails to determine if they align with normal business activity.
1. Cross-check the sender's recent activity logs for other anomalies, such as unusual login times or IP addresses and determine if the activity was intentional (e.g., a legitimate bulk email campaign) or accidental (e.g., a misconfiguration).
1. If the sender is an internal user and the activity is suspicious, disable the account temporarily and strengthen authentication measures (e.g., multi-factor authentication) for user accounts.
