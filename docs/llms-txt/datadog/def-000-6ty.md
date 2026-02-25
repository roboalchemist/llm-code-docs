# Source: https://docs.datadoghq.com/security/default_rules/def-000-6ty.md

---
title: LastPass brute force attempt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > LastPass brute force attempt
---

# LastPass brute force attempt
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect a high number of failed login attempts for the user: `{{@usr.name}}` followed by a successful login.

## Strategy{% #strategy %}

Monitor LastPass logs for a significant rise in failed login attempts along with successful logins for a user. This may indicate potential unauthorized access attempts or brute force attacks.

## Triage and response{% #triage-and-response %}

1. Investigate the source of the failed login attempts to determine whether they are legitimate users experiencing issues or potential attackers.
1. Analyze the patterns of failed login attempts for the user: `{{@usr.name}}`, including IP addresses and timestamps, to identify any common characteristics.
1. Implement additional security measures, such as account lockouts or deactivations, multi-factor authentication enforcement, and notifications to users about suspicious login attempts.

## Changelog{% #changelog %}

- 6 August 2025 - Updated query.
