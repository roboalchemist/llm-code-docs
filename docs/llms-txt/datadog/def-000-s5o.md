# Source: https://docs.datadoghq.com/security/default_rules/def-000-s5o.md

---
title: 'Mimecast Alert: malicious URL clicked by user'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Mimecast Alert: malicious URL clicked
  by user
---

# Mimecast Alert: malicious URL clicked by user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566)
## Goal{% #goal %}

To detect and alert when an email contains a malicious URL, potentially indicating a phishing attempt or other security threat.

## Strategy{% #strategy %}

This rule identifies emails transiting through the organization's email gateway that contain URLs classified as malicious under a ttp definition `{{@ttpDefinition}}`. These URLs may be part of phishing campaigns, malware distribution, or other malicious activities.

## Triage and response{% #triage-and-response %}

1. Investigate the email source and content, focusing on the sender's IP address: `{{@senderIPAddress}}`.
1. Check the URL against known threat databases and analyse the email for other indicators of compromise.
1. Follow the organization's incident response protocol, which may include:
   - Isolating the email to prevent further spread.
   - Notifying affected users and guiding them on how to proceed.
   - Updating security filters to catch similar future attempts.
