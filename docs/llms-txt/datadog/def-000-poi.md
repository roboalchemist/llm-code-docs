# Source: https://docs.datadoghq.com/security/default_rules/def-000-poi.md

---
title: A Microsoft Teams member was made owner of multiple teams
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A Microsoft Teams member was made owner
  of multiple teams
---

# A Microsoft Teams member was made owner of multiple teams
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when a user is made owner of multiple Microsoft Teams. This could indicate an adversary or insider threat attempting to escalate the privileges of the assigned user with regard to various teams chats, as most users tend to own few teams curated to specific topics.

## Strategy{% #strategy %}

Monitor Microsoft Teams audit logs to look for events with an `@evt.name` value of `MemberRoleChanged` and a `@Members.Role` value of `2` indicating the change to an Owner role. Generally, most users will own a few teams related to specific topics that correlate with that job role. However, if this activity is observed from an external user or a user whose job function does not correlate with the assigned team, this might be an indicator of malicious activity.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.email}}` intended to make the assigned user `{{@Member.UPN}}` the owner of the teams within the`{{TeamName}}` attribute.
1. If the `{{@usr.email}}` didn't intend to assign the owner privileges to `{{@Member.UPN}}`:
   - Investigate other activities performed by the user `{{@usr.email}}` using the Cloud SIEM - User Investigation dashboard.
   - Investigate other activities performed by the source IP `{{@network.client.ip}}` using the Cloud SIEM - IP Investigation dashboard.
   - Investigate the activities that might have been performed by the subject user `{{@Member.UPN}}` after they were assigned the owner privileges.
   - Begin your organization's incident response process and investigate.
