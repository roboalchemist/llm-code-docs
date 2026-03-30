# Source: https://docs.datadoghq.com/security/default_rules/def-000-tq6.md

---
title: Microsoft 365 Full Access delegate permissions added
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Full Access delegate
  permissions added
---

# Microsoft 365 Full Access delegate permissions added
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when a user adds FullAccess permissions.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs to look for the operation [`Add-MailboxPermission`](https://learn.microsoft.com/en-us/powershell/module/exchange/add-mailboxpermission?view=exchange-ps). FullAccess permission allows the assigned user to read the mailbox and manage emails in the user's mailbox that the permission is assigned to. Full Access permission does not grant Send as or Send on behalf permissions. Attackers may configure this to allow them to impersonate a user and read messages from their mailbox, allowing the attacker to persist in the organization.

## Triage and response{% #triage-and-response %}

1. Inspect the `@Parameters.User` field to identify which user is getting access to the mailbox specified in `@Parameters.Identity`.
1. Determine if there is a legitimate use case for adding FullAccess permissions by contacting the user `{{@usr.email}}`.
1. If `{{@usr.email}}` is not aware of the action:
   - Investigate other activities performed by users at the following attributes `@usr.email`, `@Parameters.User`, and `@Parameters.Identity` using the Cloud SIEM - User Investigation dashboard.
   - Begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 18 December 2024 - remove duplicate rule query.
- 18 December 2025 - Removed corporate VPNs as a threat intel source.
