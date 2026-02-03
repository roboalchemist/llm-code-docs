# Source: https://docs.datadoghq.com/security/default_rules/def-000-oto.md

---
title: Snowflake UI login via password
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Snowflake UI login via password
---

# Snowflake UI login via password
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect a user account login using a password for authentication directly into the Snowflake UI.

## Strategy{% #strategy %}

This rule allows you to detect when an account uses a password to login to the Snowflake UI.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to identify the user or service account and associated IP address.
1. Review the IP address against other logs associated with that user.
1. Investigate whether that user has MFA enabled.
1. If the IP address has not been observed in the past and MFA is not enabled, disable the user and rotate credentials.
