# Source: https://docs.datadoghq.com/security/default_rules/def-000-8jx.md

---
title: 'OSSEC Alert: Possible attack detected'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: 'Docs > Datadog Security > OOTB Rules > OSSEC Alert: Possible attack detected'
---

# OSSEC Alert: Possible attack detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attack
## Goal{% #goal %}

Detect when an OSSEC alert of level 13 or 14 is raised.

## Strategy{% #strategy %}

This rule monitors unusual and high importance events with severity level 13 or 14. [OSSEC rules](https://www.ossec.net/docs/manual/rules-decoders/rule-levels.html) are classified in multiple levels, from the lowest (00) to the maximum level 16.

- Severity level 13 signifies `Unusual error (high importance)` - Most of the times it matches a common attack pattern.
- Severity level 14 signifies `High importance security event` - Most of the times done with correlation and indicative of an attack.

## Triage and Response{% #triage-and-response %}

1. Check the attack detected for the system: `{{@syslog.hostname}}`.
1. Analyze the rule that triggered, the brief description, and message attached with the log:
   - Rule ID: `{{@rule_id}}`
   - Description: `{{@description}}`
   - Log Message:`{{@log}}`
1. Contact your system administrator in order to perform the necessary actions to mitigate the issue.
