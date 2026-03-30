# Source: https://docs.datadoghq.com/security/default_rules/def-000-otj.md

---
title: Snowflake login from anomalous location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Snowflake login from anomalous location
---

# Snowflake login from anomalous location
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect a user account login from an abnormal country in your Snowflake environment.

## Strategy{% #strategy %}

This rule allows you to detect when an account uses an anomalous geolocation to login.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to identify the user or service account and associated IP address.
1. Investigate whether that user is expected to be in that location.
1. Reach out to user if there are no signs of compromise and validate business use case.
1. If there are signs of compromise, disable the user and rotate credentials.
