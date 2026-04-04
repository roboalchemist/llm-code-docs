# Source: https://docs.datadoghq.com/security/default_rules/def-000-2ru.md

---
title: Multiple Microsoft Teams deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Multiple Microsoft Teams deleted
---

# Multiple Microsoft Teams deleted
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1531-account-access-removal](https://attack.mitre.org/techniques/T1531)
## Goal{% #goal %}

Detect when multiple Microsoft Teams are deleted. Threat actors may want to cause disruptions in work and jeopardize relevant conversation data by deleting multiple teams.

## Strategy{% #strategy %}

Monitor Microsoft Teams audit logs to look for events with an `@evt.name` value of `TeamDeleted` that are using the `UserType` value to align various levels of severity for different user types such as admin users, service principals, guest or anonymous user and so on. This activity typically should be done by an internal Admin, however, if it's observed from an external user this might indicate a higher fidelity of malicious activity.

According to [Microsoft](https://learn.microsoft.com/en-us/purview/audit-log-detailed-properties#usertype-and-userkey-scenarios), the following values indicate the user types surfaced within this detection:

- `0` - A regular user without admin permissions.
- `2` - An administrator in your M365 organization.
- `6` - A service principal.
- `10` - A guest or anonymous user.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.email}}` with `{{@UserType}}` intended to delete the following Teams `{{@TeamName}}`.
1. If `{{@usr.email}}` didn't intend to delete the observed Teams
   - Investigate other activities performed by the user `{{@usr.email}}` using the Cloud SIEM - User Investigation dashboard.
   - Begin your organization's incident response process and investigate.
