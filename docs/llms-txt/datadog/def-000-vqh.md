# Source: https://docs.datadoghq.com/security/default_rules/def-000-vqh.md

---
title: Check Point Harmony Email & Collaboration malicious URL clicked by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Check Point Harmony Email &
  Collaboration malicious URL clicked by user
---

# Check Point Harmony Email & Collaboration malicious URL clicked by user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Detects instances where a user clicks on a malicious URL within an email (for example, Office 365 Mail, or Gmail) or a collaboration platform (for example, Google Drive, SharePoint, or Microsoft Teams). This may indicate a phishing attempt, malware delivery, or an attempt to steal user credentials.

## Strategy{% #strategy %}

This rule monitors user activity related to URL clicks and raises an alert when a malicious URL is accessed by the same user, suggesting potential exposure to a security threat.

## Triage and Response{% #triage-and-response %}

1. Review the user email address `{{@event.security_event.saas_info.saas_actor_payload.email}}` and the platform involved `{{@saas_name}}`, and verify the source of the malicious URL.
1. Analyze if the URL is associated with known phishing campaigns, malware distribution, or credential theft.
1. If the URL is confirmed to be malicious, initiate remediation actions such as blocking the domain, revoking access tokens, and scanning the user's device for potential compromise.
1. Notify the user and provide security awareness guidance to prevent future incidents.
