# Source: https://docs.datadoghq.com/security/default_rules/def-000-hn9.md

---
title: >-
  Cisco Secure Email Threat Defense high number of threat emails sent by an
  internal user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Secure Email Threat Defense high
  number of threat emails sent by an internal user
---

# Cisco Secure Email Threat Defense high number of threat emails sent by an internal user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566)
### Goal:{% #goal %}

Detects when a high volume of threat emails are sent by an internal user.

### Strategy:{% #strategy %}

This rule monitors emails to detect multiple threat emails sent by an internal user. This includes the mail sent within your Microsoft 365 tenant or mail sent to recipients outside of your Microsoft 365 tenant.

### Triage & Response:{% #triage--response %}

1. Investigate suspicious emails sent from the user `{{@fromAddress}}`.
1. Identify the internal user(s) responsible for sending the threat emails. Determine if the emails were intentional or due to compromised credentials.
1. Disable the internal user's email account to prevent further sending of threat emails, if necessary.
1. If possible, notify recipients who received the threat emails, advising them not to interact with any suspicious content and providing guidance on what to do if they have already done so.
1. Take the required steps in accordance with company policies.
