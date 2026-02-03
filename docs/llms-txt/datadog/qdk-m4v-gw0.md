# Source: https://docs.datadoghq.com/security/default_rules/qdk-m4v-gw0.md

---
title: A new Microsoft Teams app or bot was observed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A new Microsoft Teams app or bot was
  observed
---

# A new Microsoft Teams app or bot was observed
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1137-office-application-startup](https://attack.mitre.org/techniques/T1137) 
## Goal{% #goal %}

Detect when a new Microsoft 365 teams app or bot is installed as a means of establishing persistence.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs to look for events with an `@evt.name` value of `AppInstalled`, where the `AddOnType` has a value of `1` OR `4` and a new `@AddOnName` is observed.

According to [Microsoft](https://learn.microsoft.com/en-us/purview/audit-log-detailed-properties), the following values indicate the types of add-ons that exist:

- `1` - Indicates a bot.
- `2` - Indicates a connector.
- `3` - Indicates a tab.

However, some add-ons use the value `4` for existing teams apps that could be potentially unapproved bots or applications that could be malicious.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.email}}` intended to install `{{@AddOnName}}`.
1. If `{{@usr.email}}` is not responsible for installing `{{@AddOnName}}`, investigate `{{@usr.email}}` for anomalous activity. If necessary, initiate your company's incident response (IR) process.

## Changelog{% #changelog %}

Updated rule name and query to include bots.
