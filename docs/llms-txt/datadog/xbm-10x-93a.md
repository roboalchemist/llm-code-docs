# Source: https://docs.datadoghq.com/security/default_rules/xbm-10x-93a.md

---
title: OneLogin user viewed secure note
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > OneLogin user viewed secure note
---

# OneLogin user viewed secure note
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526) 
## Goal{% #goal %}

Detect when a OneLogin user views a secure note.

## Strategy{% #strategy %}

This rule lets you monitor the following OneLogin events to detect when a user views a secure note:

- `@evt.name:PRIVILEGE_GRANTED_TO_USER`

This rule is useful when correlating its findings with other anomalous events from the same OneLogin user (`{{@actor_user_name}}`).

## Triage and response{% #triage-and-response %}

1. Determine whether the OneLogin user (`{{@actor_user_name}}`) should be legitimately accessing secure notes.
1. If the activity was not legitimate, review all activity from `{{@actor_user_name}}` and the IP (`{{@network.client.ip}}`) associated with this signal.
