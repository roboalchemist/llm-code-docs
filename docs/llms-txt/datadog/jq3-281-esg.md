# Source: https://docs.datadoghq.com/security/default_rules/jq3-281-esg.md

---
title: Microsoft 365 Anomalous Amount of Deleted Emails
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Anomalous Amount of
  Deleted Emails
---

# Microsoft 365 Anomalous Amount of Deleted Emails
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1485-data-destruction](https://attack.mitre.org/techniques/T1485) 
## Goal{% #goal %}

Detect when an anomalous amount of emails are deleted from Microsoft 365 Exchange.

## Strategy{% #strategy %}

Monitor Microsoft 365 Exchange audit logs to look for events with an `@evt.name` value of `HardDelete`, where the `@Folder.Path` is the inbox (`*Inbox*`).

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.id}}` intended to delete the observed emails.
1. If `{{@usr.id}}` is not responsible for the email deletions, investigate `{{@usr.id}}` for anomalous activity. If necessary, initiate your company's incident response (IR) process.
