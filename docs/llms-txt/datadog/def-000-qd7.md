# Source: https://docs.datadoghq.com/security/default_rules/def-000-qd7.md

---
title: Microsoft 365 Copilot interaction flagged as indirect attack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 Copilot interaction
  flagged as indirect attack
---

# Microsoft 365 Copilot interaction flagged as indirect attack
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556)
## Goal{% #goal %}

Detect when an M365 Copilot Studio bot experiences an indirect attack as defined by Microsoft's content safety checks. The [`Microsoft generated alert`](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter-prompt-shields) attempts identify if an actor embeds instructions to the agent for the purpose of maliciously gaining access to unauthorized data or control of the system.

## Strategy{% #strategy %}

Monitor Microsoft 365 audit logs for when the `@CopilotEventData.AccessedResources.Type` includes an `IndirectAttack` flag within the Copilot service logs.

## Triage and response{% #triage-and-response %}

1. Identify what user, `{{@usr.id}}`, and action triggered the Microsoft content safety alert. The `@CopilotEventData.AccessedResources.Name` includes the user action which generated the `IndirectAttack` alert.
1. Determine if the user `{{@usr.id}}` and the action taken represents malicious behavior for your organization's bot.
1. If the interaction prompted the bot for unauthorized access or attempted to manipulate the bot, investigate surrounding events for anomalous activity. If necessary, initiate your company's incident response (IR) process.
