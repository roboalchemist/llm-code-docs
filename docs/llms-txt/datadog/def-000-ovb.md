# Source: https://docs.datadoghq.com/security/default_rules/def-000-ovb.md

---
title: 'Mimecast Alert: user responded to impersonation message'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Mimecast Alert: user responded to
  impersonation message
---

# Mimecast Alert: user responded to impersonation message

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566) 
## Goal{% #goal %}

To identify and alert on emails that contain user responses to impersonation messages, indicating a successful impersonation attempt.

## Strategy{% #strategy %}

This rule detects an email which contains impersonation attempts that have been flagged as external and malicious but have not been blocked or taken any action upon.

## Triage and response{% #triage-and-response %}

1. Verify the nature of the user's response to the impersonation email and assess the potential impact.
1. Examine the sender's details using `{{@senderIPAddress}}` to determine the source and legitimacy.
1. Execute the company's incident response protocol, which may include:
   - Alerting the affected user and providing education on recognizing impersonation attempts.
   - Revoking any credentials or access provided in response to the phishing email.
   - Strengthening email security measures to prevent similar incidents.
