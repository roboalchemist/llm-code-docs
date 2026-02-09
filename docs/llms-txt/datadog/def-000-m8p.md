# Source: https://docs.datadoghq.com/security/default_rules/def-000-m8p.md

---
title: >-
  Microsoft 365 Exchange inbox rule name associated with business email
  compromise attacks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Exchange inbox rule name
  associated with business email compromise attacks
---

# Microsoft 365 Exchange inbox rule name associated with business email compromise attacks
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1564-hide-artifacts](https://attack.mitre.org/techniques/T1564) 
## Goal{% #goal %}

Detect when a user configures an inbox rule with a name commonly associated with business email compromises.

## Strategy{% #strategy %}

Monitor Microsoft 365 Exchange audit logs to look for the operation [`New-InboxRule`](https://learn.microsoft.com/en-us/powershell/module/exchange/new-inboxrule?view=exchange-ps) or [`Set-InboxRule`](https://learn.microsoft.com/en-us/powershell/module/exchange/set-inboxrule?view=exchange-ps). Attackers might set up email rules to hide incoming emails in a compromised user mailbox to hide their activities or maintain access to the victim's inbox. Attackers may use simple names like `.` or `...` for their malicious inbox rules, which are uncommon in most environments.

## Triage and response{% #triage-and-response %}

1. Inspect the inbox rule for any indicators:
   - Suspicious keywords in the filter.
   - The rule name.
1. Determine if there is a legitimate use case for the inbox rule by contacting the user `{{@usr.email}}`.
1. If `{{@usr.email}}` is not aware of the inbox rule:
   - Investigate other activities performed by the user `{{@usr.email}}` using the **Cloud SIEM - User Investigation** dashboard.
   - Begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 1 July 2024 - Updated rule query.
- 23 July 2024 - Updated rule query.
