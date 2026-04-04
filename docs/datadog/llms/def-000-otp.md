# Source: https://docs.datadoghq.com/security/default_rules/def-000-otp.md

---
title: Snowflake network policy modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Snowflake network policy modified
---

# Snowflake network policy modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect a network policy was created, modified, or deleted in your Snowflake environment.

## Strategy{% #strategy %}

This rule allows you to detect when a network policy was altered.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to identify the user that ran the query.
1. Investigate whether that user is an admin by refernecing the Grants to User table in Snowflake.
1. If the user is not an admin or has only recently been assigned admin, investigate for signs of compromise.
1. Otherwise, review internal change management to validate this was an expected change.
