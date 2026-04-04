# Source: https://docs.datadoghq.com/security/default_rules/def-000-u7q.md

---
title: >-
  Check Point Harmony Email & Collaboration malware file shared by user in
  internal email
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Check Point Harmony Email &
  Collaboration malware file shared by user in internal email
---

# Check Point Harmony Email & Collaboration malware file shared by user in internal email

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1080-taint-shared-content](https://attack.mitre.org/techniques/T1080)
## Goal{% #goal %}

Detects when a user uploads or shares malware-infected files within Office 365 or Google Mail. This activity may indicate a compromised account, an insider threat, or an attempt to distribute malware within the organization.

## Strategy{% #strategy %}

This rule monitors file sharing activities within Office 365 and Google Mail, raising an alert when a user sends a file identified as malicious internally. This ensures alerting on potential spread of malware within the organization.

## Triage and Response{% #triage-and-response %}

1. Review the user's account `{{@event.security_event.saas_info.saas_actor_payload.email}}` and analyze the flagged files.
1. Quarantine or delete the malicious files `{{@event.entity.entity_payload.file_name}}` to prevent access or further distribution.
1. Restrict the user's ability to upload or share files temporarily if malicious activity is confirmed.
1. If the activity appears intentional or part of a larger attack, escalate for investigation, reset credentials, and monitor for further suspicious behavior.
