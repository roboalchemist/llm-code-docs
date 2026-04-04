# Source: https://docs.datadoghq.com/security/default_rules/def-000-vq0.md

---
title: GitLab password reset from suspicious IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitLab password reset from suspicious
  IP
---

# GitLab password reset from suspicious IP

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detects when a GitLab user requests a password reset from an IP address flagged as suspicious or malicious.

## Strategy{% #strategy %}

This rule monitors `password_reset_requested` audit events where the source IP address is flagged as suspicious or malicious. Password reset requests from known malicious IP addresses may indicate account takeover attempts, credential stuffing attacks, or reconnaissance activities by threat actors attempting to gain unauthorized access to GitLab accounts.

## Triage & Response{% #triage--response %}

- Verify if the password reset request for `{{@usr.name}}` was initiated by the legitimate account owner through analysis of previous IP addresses and user agents. Verify with the user directly, if needed.
- Review authentication logs for `{{@usr.name}}` to identify any successful login attempts from the same suspicious IP address.
- Check for any recent suspicious activities or access patterns associated with the user account prior to the password reset request.
- Determine if the password reset was completed and if any unauthorized access occurred to the GitLab account.
