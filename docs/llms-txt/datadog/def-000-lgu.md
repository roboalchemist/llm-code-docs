# Source: https://docs.datadoghq.com/security/default_rules/def-000-lgu.md

---
title: Symantec VIP multiple numbers challenge failed events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Symantec VIP multiple numbers challenge
  failed events
---

# Symantec VIP multiple numbers challenge failed events

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect multiple failed number challenge events in Symantec VIP, which could indicate unauthorized access attempts, user errors, or potential misconfigurations in authentication policies.

## Strategy{% #strategy %}

Monitor repeated failures in the number challenge mechanism, which requires users to enter a unique two-digit number from the login screen into the VIP Access Push notification. Identify patterns of misuse, user confusion, or security threats and take prompt action to secure affected accounts.

## Triage and response{% #triage-and-response %}

1. Identify the client IP `{{@network.client.ip}}`, analyze the frequency, timing, and sources of the failed number challenge attempts.
1. Determine if the failures stem from user errors (such as incorrect input), device synchronization issues, or malicious activity like brute force attacks.
1. For suspicious activity, block the source IPs, lock the account, and notify the user to reset their credentials.
1. Assist users in resolving legitimate issues, such as troubleshooting devices or clarifying number challenge instructions.
1. Document the incident, escalate confirmed threats, and refine detection rules or policies to enhance security.
