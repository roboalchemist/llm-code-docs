# Source: https://docs.datadoghq.com/security/default_rules/ab5-5lm-x2n.md

---
title: Google Workspace admin role created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Workspace admin role created
---

# Google Workspace admin role created
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Create a signal when Google Workspace detects a new Google Workspace administrative role.

## Strategy{% #strategy %}

Monitor Google Workspace logs to detect `CREATE_ROLE` events.

## Triage and response{% #triage-and-response %}

1. Determine if there is a legitimate reason for the new administrator role (`@event.parameters.ROLE_NAME`).
1. If there is not a legitimate reason, investigate activity from around the Google Workspace administrator (`{{@usr.email}}`) and IP that created the role (`{{@network.client.ip}}`).

## Changelog{% #changelog %}

- 17 October 2022 - Updated tags.
