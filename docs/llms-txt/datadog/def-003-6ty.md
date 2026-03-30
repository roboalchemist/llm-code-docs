# Source: https://docs.datadoghq.com/security/default_rules/def-003-6ty.md

---
title: Brute force attempt from suspicious IP by user email
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Brute force attempt from suspicious IP
  by user email
---

# Brute force attempt from suspicious IP by user email

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect a brute force attack on a user across log sources.

## Strategy{% #strategy %}

To identify a successful attempt: Detect when the same user fails to log in five times, and then successfully logs in. This generates a `MEDIUM` severity signal.

To identify an unsuccessful attempt: Detect when the same user fails to log in ten times. This generates an `INFO` severity signal.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to see if this was a valid login attempt.
1. Verify if 2FA was authenticated.
1. If the user was compromised, rotate user credentials.
