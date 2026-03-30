# Source: https://docs.datadoghq.com/security/default_rules/1c3-d0v-jv0.md

---
title: OneLogin administrator assumed a user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > OneLogin administrator assumed a user
---

# OneLogin administrator assumed a user
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when a OneLogin user with appropriate privileges assumes another OneLogin user's identity. Logging in as another user allows the user to view another OneLogin user's account and perform actions on their behalf.

## Strategy{% #strategy %}

This rule lets you monitor the following OneLogin events to detect when an administrator assumes another OneLogin user's identity:

- `@evt.name:USER_ASSUMED_USER`

## Triage and response{% #triage-and-response %}

1. Determine whether the user (`{{@usr.name}}`) should be legitimately assuming another user's identity.
1. If the activity was not legitimate, review all activity from `{{@usr.name}}` and the IP (`{{@network.client.ip}}`) associated with this signal.
