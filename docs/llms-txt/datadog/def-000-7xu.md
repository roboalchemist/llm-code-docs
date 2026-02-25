# Source: https://docs.datadoghq.com/security/default_rules/def-000-7xu.md

---
title: 'OSSEC Alert: OSSEC agent disconnected'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: 'Docs > Datadog Security > OOTB Rules > OSSEC Alert: OSSEC agent disconnected'
---

# OSSEC Alert: OSSEC agent disconnected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

The goal is to notify the administrator when the OSSEC agent got disconnected.

## Strategy{% #strategy %}

This rule lets you monitor whether the OSSEC agent got disconnected.

## Triage and Response{% #triage-and-response %}

1. Check the log detected for the System: `{{@syslog.hostname}}`.
1. Check whether the `{{@agent-name}}` hosted on the IP `{{@agent-ip}}` is still disconnected or has recovered.
1. If the agent has disconnected unexpectedly, log in to the system and restart your agent to continue your analysis, or contact your administrator to take the necessary actions.
