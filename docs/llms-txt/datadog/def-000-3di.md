# Source: https://docs.datadoghq.com/security/default_rules/def-000-3di.md

---
title: 'Mimecast Alert: email contains malicious file'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Mimecast Alert: email contains
  malicious file
---

# Mimecast Alert: email contains malicious file

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566)
## Goal{% #goal %}

Detect an email which contains a malicious attachment.

## Strategy{% #strategy %}

Targeted Threat Protection - Attachment Protection is an advanced service that protects customers from the growing risk of spear phishing and other targeted attacks using email attachments. This rule can be used to detect and strip attachments from inbound messages that could potentially contain malicious code. For example, PDFs and Microsoft Office files.

For more details: [Click here](https://community.mimecast.com/s/article/email-security-cloud-gateway-targeted-threat-protection-attachment-protection-overview)

## Triage and response{% #triage-and-response %}

1. Inspect the email for sender information `{{@senderAddress}}` and review the action taken by Mimecast `{{@actionTriggered}}`.
1. If the attachment was not blocked or removed, quarantine the email and conduct a thorough analysis of the attachment.
1. Execute the company's incident response protocol, which may include:
   - Notifying the intended recipient and warning against opening the attachment.
   - Scanning affected systems for malware.
   - Updating security filters to detect and block similar threats in the future.
