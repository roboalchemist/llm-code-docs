# Source: https://docs.datadoghq.com/security/default_rules/def-000-oth.md

---
title: Snowflake abnormal usage of OAuth access token
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Snowflake abnormal usage of OAuth
  access token
---

# Snowflake abnormal usage of OAuth access token
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1528-steal-application-access-token](https://attack.mitre.org/techniques/T1528)
## Goal{% #goal %}

Detect abnormal OAuth access token usage in your Snowflake environment.

## Strategy{% #strategy %}

This rule allows you to detect when an account authenticates with an OAuth access token outside an automated service/driver.

OAuth access tokens act like digital keys that grant access to protected resources. If an attacker compromises a user account, they might steal the associated access token.

By reviewing access token usage during an incident, you can identify unusual activity patterns. This could involve:

- Access tokens being used from unexpected locations (attacker's IP address).
- Access tokens being used to access unauthorized resources.
- A sudden spike in access token usage.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to see if the IP address is aligned with expected user or service account behavior.
1. If the IP address has not been seen before and is followed by query activity, investigate the actions taken.
1. If the account was compromised, recreate the access token.

## Changelog{% #changelog %}

- 1 September 2025 - Updated rule case from `High` to `Medium` and excluded additional client types.
