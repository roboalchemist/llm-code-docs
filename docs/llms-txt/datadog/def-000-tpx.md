# Source: https://docs.datadoghq.com/security/default_rules/def-000-tpx.md

---
title: GitLab user's multi-factor authentication disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitLab user's multi-factor
  authentication disabled
---

# GitLab user's multi-factor authentication disabled

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556)
## Goal{% #goal %}

Detects when a user disables Multi-Factor Authentication (MFA) on their GitLab account.

## Strategy{% #strategy %}

This rule monitors GitLab audit events `user_disable_two_factor`. When MFA is disabled, it reduces the account's security posture and may indicate potential account compromise.

## Triage & Response{% #triage--response %}

- Review recent authentication logs for the affected user account to identify any suspicious login patterns or locations.
- Examine any recent password changes or account modifications that may indicate unauthorized access.
- Verify if the user `{{@details.target_details}}` has a legitimate business reason to disable MFA on their GitLab account.
