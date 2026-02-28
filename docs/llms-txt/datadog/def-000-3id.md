# Source: https://docs.datadoghq.com/security/default_rules/def-000-3id.md

---
title: An external Microsoft Teams member was added then removed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An external Microsoft Teams member was
  added then removed
---

# An external Microsoft Teams member was added then removed
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1136-create-account](https://attack.mitre.org/techniques/T1136)
## Goal{% #goal %}

Detect when a Teams member is added and then removed within a short amount of time. An insider threat might add an external account to exfiltrate data then quickly remove the user to hide their tracks.

## Strategy{% #strategy %}

Using the `THEN` operator, monitor Microsoft Teams audit logs to look for events with an `@evt.name` value of `MemberAdded` then `MemberRemoved`, where the `Members.UPN` has `#EXT#` within it. The `EXT` value is used to denote that a user is an external user.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.email}}` intended to add and remove the external user and if the external user should indeed have been added.
1. If `{{@usr.email}}` didn't intend to add or remove the external user or the external user is not approved:
   - Investigate other activities performed by the user `{{@usr.email}}` using the Cloud SIEM - User Investigation dashboard.
   - Investigate the activities that were performed by the external user within the time period in which they were added and removed.
   - Begin your organization's incident response process and investigate.
