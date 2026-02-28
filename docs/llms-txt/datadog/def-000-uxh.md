# Source: https://docs.datadoghq.com/security/default_rules/def-000-uxh.md

---
title: Microsoft 365 Copilot Studio Application Insights logging modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Copilot Studio
  Application Insights logging modified
---

# Microsoft 365 Copilot Studio Application Insights logging modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when an M365 Copilot Studio agent's Application Insights settings are modified. This may indicate an attacker with control over this Copilot Studio agent is attempting to disable Copilot Studio conversation logging, or exfiltrate conversation logs to an Application Insights resource under their control.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs for when the `@Operation` field includes an `BotAppInsightsUpdate` event within the PowerPlatform service.

## Triage and response{% #triage-and-response %}

1. Identify what settings were modified for the corresponding bot application.
1. Determine if the user `{{@usr.id}}` is the bot owner or is expected to modify the bot application.
1. If `{{@usr.id}}` is not responsible for or expected to be modifying the bot application, investigate surrounding events for anomalous activity. If necessary, initiate your company's incident response (IR) process.
