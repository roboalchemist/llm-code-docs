# Source: https://docs.datadoghq.com/security/default_rules/def-000-jhy.md

---
title: Microsoft 365 Copilot Studio agent sign-in topic modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Copilot Studio agent
  sign-in topic modified
---

# Microsoft 365 Copilot Studio agent sign-in topic modified
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## Goal{% #goal %}

Detect when the M365 Copilot Studio agent's system "Sign in" topic is modified. When a customer begins a conversation with the agent, the "Sign in" topic triggers and prompts the user to sign in. Modification of system sign in topics may indicate an attacker adding actions to manipulate the agent's login process, which may include compromising the `User.AccessToken` variable. The `User.AccessToken` variable contains the user's token, which is obtained after the user is signed in.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs for when the `@Operation` field successfully triggers an `BotComponentUpdate` event within the PowerPlatform service. Filter by values within the property collection fields where the `Signin` topic is referenced.

## Triage and response{% #triage-and-response %}

1. Identify the user who took the action, `{{@usr.id}}`, the bot application within the value for `powerplatform.analytics.resource.bot.id` and the sign in state new value.
1. Determine if the sign in topic is moved to `Inactive` or `Active` state.
1. Investigate if the user `{{@usr.id}}` is the bot owner or is expected to modify the bot application's login process.
1. If the setting change was unintended or unauthorized interactions occurred, investigate surrounding events for anomalous activity. If necessary, initiate your company's incident response (IR) process.
