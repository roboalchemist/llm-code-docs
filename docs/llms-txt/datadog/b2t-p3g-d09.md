# Source: https://docs.datadoghq.com/security/default_rules/b2t-p3g-d09.md

---
title: OneLogin user granted administrative privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OneLogin user granted administrative
  privileges
---

# OneLogin user granted administrative privileges
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a OneLogin administrator grants additional privileges to another OneLogin user.

## Strategy{% #strategy %}

This rule lets you monitor the following OneLogin events to detect when an administrator grants additional privileges to another OneLogin user:

- `@evt.name:PRIVILEGE_GRANTED_TO_USER`

## Triage and response{% #triage-and-response %}

1. Determine whether the user (`{{@actor_user_name}}`) should be legitimately adding additional roles to `@usr.name`. **Note:** The role granted to the user is not available in OneLogin logs.
1. If the activity was not legitimate, review all activity from `{{@actor_user_name}}` and the IP (`{{@network.client.ip}}`) associated with this signal.
