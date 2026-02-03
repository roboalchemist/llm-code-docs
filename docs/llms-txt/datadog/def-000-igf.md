# Source: https://docs.datadoghq.com/security/default_rules/def-000-igf.md

---
title: Snowflake user granted admin role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Snowflake user granted admin role
---

# Snowflake user granted admin role
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect a new admin grant to a user in your Snowflake environment.

## Strategy{% #strategy %}

This rule allows you to detect when a user acccount gains adminstrator privileges in Snowflake. If an attacker gains administrative access, they may grant admin-level access to a second compromised user in an attempt to fly under the radar. The following admin permissions are available: AccountAdmin, OrgAdmin, SysAdmin, and SecurityAdmin.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to identify the user, role granted, and timestamp.
1. Investigate whether the user's elevated permissions are expected.
1. If there are signs of compromise, disable the user associated with the admin grant and rotate credentials.
