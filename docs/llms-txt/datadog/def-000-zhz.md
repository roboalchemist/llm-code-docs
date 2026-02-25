# Source: https://docs.datadoghq.com/security/default_rules/def-000-zhz.md

---
title: Microsoft 365 Exchange junk email settings modified by a suspicious VPN
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Exchange junk email
  settings modified by a suspicious VPN
---

# Microsoft 365 Exchange junk email settings modified by a suspicious VPN
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1564-hide-artifacts](https://attack.mitre.org/techniques/T1564)
## Goal{% #goal %}

Detect when the Exchange junk email settings have been modified by a suspicious VPN.

## Strategy{% #strategy %}

Monitor Microsoft 365 Exchange audit logs to look for the operation `Set-MailboxJunkEmailConfiguration`. Attackers who have gained unauthorized access to a victim's account may modify junk email settings to redirect incoming emails. This technique could be used by an attacker to avoid detections focussing on email inbox rules.

## Triage and response{% #triage-and-response %}

1. Identify any additional unusual behaviors:
   - Previous failed logins.
   - Unexpected VPN usage.
   - Unusual user agent.
1. Contact the user `{{@usr.email}}` to determine if they made the change to the junk email configuration.
1. If `{{@usr.email}}` is not aware of the activity:
   - Investigate other activities performed by the user `{{@usr.email}}` using the **Cloud SIEM - User Investigation** dashboard.
   - Begin your organization's incident response process and investigate.
