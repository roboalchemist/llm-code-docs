# Source: https://docs.datadoghq.com/security/default_rules/def-000-apr.md

---
title: Asana user multi-factor authentication method disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Asana user multi-factor authentication
  method disabled
---

# Asana user multi-factor authentication method disabled

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556)
## Goal{% #goal %}

Detect when a user has disabled two-factor authentication (2FA) for their account. This could indicate an attacker who is maintaining access to a compromised user account by weakening the account's security controls.

## Strategy{% #strategy %}

This rule monitors multi-factor authentication removal events across users and raises an alert if a user disables their registered method.

## Triage and response{% #triage-and-response %}

1. Review logs to identify the user `{{@usr.email}}` who has disabled multi-factor authentication.
1. Determine if the action was user-initiated or performed by an administrator by checking if the log indicates a specific initiator `{{@resource.email}}`.
1. Investigate any recent login and action-related event logs within the Asana platform by `{{@usr.email}}` that could demonstrate anomalous behavior.
1. If the change appears malicious, invoke your security incident response process. Next steps could include:
   - Temporarily suspend the affected account.
   - Rotate user credentials.
   - Work with the user to re-enroll in multi-factor authentication.
