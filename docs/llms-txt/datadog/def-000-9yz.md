# Source: https://docs.datadoghq.com/security/default_rules/def-000-9yz.md

---
title: Microsoft 365 Copilot Studio agent authentication modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Copilot Studio agent
  authentication modified
---

# Microsoft 365 Copilot Studio agent authentication modified
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## Goal{% #goal %}

Detect when an M365 Copilot Studio agent policy is altered to not require authentication from a user before interaction. Unauthenticated agents allow interaction from any user. This can lead to misuse of the agent's AI functions, and attempts to exploit the agent to reveal sensitive information or perform tasks it has access to on behalf of an attacker.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs for when the `@Operation` field successfully triggers an `BotUpdateOperation-BotAuthUpdate` event within the PowerPlatform service.

## Triage and response{% #triage-and-response %}

1. Identify the user who took the action, `{{@usr.id}}`, the bot application within the value for `powerplatform.analytics.resource.bot.id` and the updated authentication related values. The property collection values will include the following fields to determine authentication changes: `AuthRedirectUrl`, `AuthenticationConnection`, `AuthenticationMode`.
1. Determine if the authentication method changes were expected for the bot by `{{@usr.id}}`.
1. If the setting change was unintended or unauthorized interactions occurred, investigate surrounding events for anomalous activity. If necessary, initiate your company's incident response (IR) process.
