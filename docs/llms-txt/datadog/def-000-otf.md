# Source: https://docs.datadoghq.com/security/default_rules/def-000-otf.md

---
title: Snowflake brute force attack on user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Snowflake brute force attack on user
---

# Snowflake brute force attack on user
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect a brute force attack on a Snowflake user.

## Strategy{% #strategy %}

**To determine a successful attempt:** Detect when the same user fails to login five times and then successfully logs in. This generates a `MEDIUM` severity signal.

**To determine an unsuccessful attempt:** Detect when the same user fails to login ten times. This generates an `INFO` severity signal.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to see if this was a valid login attempt.
1. See if 2FA was authenticated.
1. If the user was compromised, rotate user credentials.

## Changelog{% #changelog %}

- 10 September 2025 - Updated rule case from `High` to `Medium`.
