# Source: https://docs.datadoghq.com/security/default_rules/def-000-ep8.md

---
title: 'OSSEC Alert: Multiple authentication failures'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OSSEC Alert: Multiple authentication
  failures
---

# OSSEC Alert: Multiple authentication failures

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect when multiple failed authentication attempts are detected by OSSEC.

## Strategy{% #strategy %}

This rule lets you monitor if there are multiple authentication failures in a limited time interval.

## Triage and Response{% #triage-and-response %}

1. Check the activity detected on the System: `{{@syslog.hostname}}`.

1. Analyze the rule that triggered along with the brief description and log message attached with the log:

   - Rule ID: `{{@rule_id}}`
   - Description: `{{@description}}`
   - Log Message: `{{@log}}`

1. Inform your administrator to take further action for the detected failed activity.
