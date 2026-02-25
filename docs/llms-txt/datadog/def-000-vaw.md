# Source: https://docs.datadoghq.com/security/default_rules/def-000-vaw.md

---
title: >-
  Symantec VIP multiple mobile push request denied by the user followed by
  successful login
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Symantec VIP multiple mobile push
  request denied by the user followed by successful login
---

# Symantec VIP multiple mobile push request denied by the user followed by successful login

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect multiple denied mobile push requests followed by successful login, which could indicate unauthorized access attempts, phishing attacks, or user confusion.

## Strategy{% #strategy %}

Monitor and identify unusual patterns of denied mobile push requests in Symantec VIP. This helps detect potential security threats, such as adversary-in-the-middle attacks or unintentional user errors, and allows timely response.

## Triage and response{% #triage-and-response %}

1. Identify the client IP `{{@network.client.ip}}` and user name `{{@usr.name}}`. Analyze the frequency, timing, and sources of the failed number challenge attempts.
1. Determine if the denials are due to user errors or indicate unauthorized access attempts, such as phishing or adversary-in-the-middle attacks.
1. For suspected malicious activity, block source IPs or devices, notify the user, and prompt them to reset credentials.
1. If user error is identified, provide guidance on proper mobile push authentication practices.
1. Document the incident, escalate confirmed threats, and update detection rules to enhance monitoring and minimize false positives.
