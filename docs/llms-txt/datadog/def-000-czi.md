# Source: https://docs.datadoghq.com/security/default_rules/def-000-czi.md

---
title: Microsoft 365 Copilot Studio agent access control policy set to open
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Copilot Studio agent
  access control policy set to open
---

# Microsoft 365 Copilot Studio agent access control policy set to open
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556)
## Goal{% #goal %}

Detect when an M365 Copilot Studio bot's access control settings are modified to `Any`. This change would indicate any user within the tenant could access the bot application.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs for when the `@Operation` field populates an `BotUpdateOperation-BotShare` event within the PowerPlatform service. Filter by values within the property collection fields where the Access Control Policy has a new value of `Any`.

## Triage and response{% #triage-and-response %}

1. Identify what bot application had their access control policy modified.
1. Determine if the user `{{@usr.id}}` is the bot owner or is expected to modify the bot application.
1. Review audit logs for the Copilot Studio bot for evidence of interactions after the access control policy was modified.
1. If the setting change was unintended or unauthorized interactions occurred, investigate surrounding events for anomalous activity. If necessary, initiate your company's incident response (IR) process.
