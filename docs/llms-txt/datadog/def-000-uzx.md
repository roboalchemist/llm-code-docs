# Source: https://docs.datadoghq.com/security/default_rules/def-000-uzx.md

---
title: 'OSSEC Alert: Multiple authentication failures followed by a success'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OSSEC Alert: Multiple authentication
  failures followed by a success
---

# OSSEC Alert: Multiple authentication failures followed by a success

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect when multiple authentication attempts have failed, followed by one successful authentication.

## Strategy{% #strategy %}

This rule monitors logs, and is triggered when there are multiple authentication failures followed by a successful authentication from the user. This could be indicative of a brute force attack against your system.

## Triage and Response{% #triage-and-response %}

1. Check the activity detected on the system `{{@syslog.hostname}}` by the user `{{@usr.name}}`.
1. Note the activity performed from `{{@network.client.ip}}`.
1. You can either block the user `{{@usr.name}}` from further accessing the system or contact your administrator to take further action.
