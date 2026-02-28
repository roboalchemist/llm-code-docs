# Source: https://docs.datadoghq.com/security/default_rules/def-000-fuz.md

---
title: >-
  Ivanti connect secure multiple failed login attempts followed by successful
  login
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ivanti connect secure multiple failed
  login attempts followed by successful login
---

# Ivanti connect secure multiple failed login attempts followed by successful login

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Identify cases where a user experiences multiple failed login attempts followed by a successful login, potentially indicating a brute-force attack, credential stuffing, or unauthorized access.

## Strategy{% #strategy %}

This rule monitors failed login attempts and detects cases where a user successfully logs in after several failures. This pattern may indicate that an attacker has successfully guessed or obtained valid credentials.

## Triage and Response{% #triage-and-response %}

1. Identify the user `{{@usr.name}}` associated with the failed login attempts followed by a successful login.
1. Determine if the login attempts are clustered within a short period or if they follow a gradual pattern, as this can help distinguish between brute-force and accidental lockouts.
1. Investigate if there are any ongoing system issues or maintenance activities that could account for increased login failures.
1. If suspicious behavior is detected, consider locking the affected accounts, notifying users, and requiring additional authentication steps.
