# Source: https://docs.datadoghq.com/security/default_rules/def-000-ihv.md

---
title: >-
  Consent given to application associated with business email compromise attacks
  in Microsoft 365
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Consent given to application associated
  with business email compromise attacks in Microsoft 365
---

# Consent given to application associated with business email compromise attacks in Microsoft 365
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1114-email-collection](https://attack.mitre.org/techniques/T1114) 
## Goal{% #goal %}

Detect when a user consents to an application associated with business email compromise.

## Strategy{% #strategy %}

Monitor Microsoft 365 Exchange audit logs to look for the operation `Consent to application.`. Attackers who have gained unauthorized access to a victim's account may add applications in order to collect emails or send out further phishing emails. In this detection, we try to identify the following applications:

- eM Client - a desktop email client with full Microsoft Office 365 synchronization.
- PerfectData Software - exports mailboxes for backup purposes.
- Newsletter Software Supermailer - email newsletter software to send out high volume emails.
- SigParser - email signature contact scraping and parsing.
- CloudSponge - allows you to export all contacts from an inbox.
- rclone - is a command-line program to manage files on cloud storage.

## Triage and response{% #triage-and-response %}

1. Identify any additional unusual behaviors:
   - Previous failed logins.
   - Anomalous geo-location.
   - VPN usage.
1. Determine if there is a legitimate use case for the new application by contacting the user `{{@usr.email}}`.
1. If `{{@usr.email}}` is not aware of the application:
   - Investigate other activities performed by the user `{{@usr.email}}` using the **Cloud SIEM - User Investigation** dashboard.
   - Begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 29 July 2024 - Added additional application ID for SigParser.
- 13 August 2024 - Added additional application to markdown.
- 10 April 2025 - Added additional applications, CloudSponge and rclone.
