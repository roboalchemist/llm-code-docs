# Source: https://docs.datadoghq.com/security/default_rules/def-000-0dj.md

---
title: Zendesk account assumption is enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Zendesk account assumption is enabled
---

# Zendesk account assumption is enabled
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when the Zendesk account assumption setting is enabled.

## Strategy{% #strategy %}

Monitor Zendesk audit logs to look for events with an `@source_label` value of `"Security: Enable Account assumption"`. Account assumption grants Zendesk the ability to access your account to troubleshoot an issue. It allows Zendesk to assume the role of an agent for a specified amount of time.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` intended to enable the account assumption setting.
1. If Zendesk support should not have the ability to assume the role of an agent, disable the setting.
