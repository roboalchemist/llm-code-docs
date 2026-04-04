# Source: https://docs.datadoghq.com/security/default_rules/def-000-xcb.md

---
title: 1Password service account token activity observed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 1Password service account token
  activity observed
---

# 1Password service account token activity observed
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when a 1Password service account token activity is observed.

## Strategy{% #strategy %}

This rule monitors 1Password audit logs to determine when any of the following [actions](https://developer.1password.com/docs/events-api/audit-events#service-account-tokens) is observed for a 1Password service account token:

- **create**: A service account token was registered.
- **trename**: A service account token name was updated.
- **tverify**: A service account token signature was registered.
- **trevoke**: A service account token was revoked.

[1Password Service Accounts](https://developer.1password.com/docs/service-accounts/) help automate secrets management in your applications and infrastructure without the need to deploy additional services.

Token activity from these service accounts could indicate an attacker using a non-user identity to compromise a 1Password tenant.

## Triage & response{% #triage--response %}

- Investigate the user `{{@usr.email}}` performing the service account token activity `{{@evt.name}}`.
- In the event of an accidental credentials exposure follow the 1Password Service Account security [recommendation](https://developer.1password.com/docs/service-accounts/security/).
  - You must create a new service account with the same permissions, and delete the 1Password service account with the exposed credentials.
