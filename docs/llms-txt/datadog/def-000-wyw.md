# Source: https://docs.datadoghq.com/security/default_rules/def-000-wyw.md

---
title: Keeper brute force attempt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Keeper brute force attempt
---

# Keeper brute force attempt

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect a high number of failed login attempts for the user: `{{@usr.email}}` followed by a successful login.

## Strategy{% #strategy %}

Monitor Keeper logs for a significant rise in failed login attempts along with successful logins for a user. This may indicate potential unauthorized access attempts or brute force attacks.

## Triage and response{% #triage-and-response %}

- Investigate the source of the failed login attempts to determine whether they are legitimate users experiencing issues or potential attackers.
- Analyze the patterns of failed login attempts for the user: `{{@usr.email}}`, including IP addresses and timestamps, to identify any common characteristics.
- Implement additional security measures, such as account lockouts or deactivations, multi-factor authentication enforcement, and notifications to users about suspicious login attempts.
