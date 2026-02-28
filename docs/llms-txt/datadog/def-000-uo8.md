# Source: https://docs.datadoghq.com/security/default_rules/def-000-uo8.md

---
title: 'OSSEC Alert: Attack detected'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: 'Docs > Datadog Security > OOTB Rules > OSSEC Alert: Attack detected'
---

# OSSEC Alert: Attack detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attack
## Goal{% #goal %}

Detect when an OSSEC alert of level 15 is raised.

## Strategy{% #strategy %}

This rule monitors OSSEC logs for an alert classified as level 15. [OSSEC rules](https://www.ossec.net/docs/manual/rules-decoders/rule-levels.html) are classified in multiple levels, from the lowest (00) to the maximum level 16. Level 15 references a 'severe attack' and immediate attention is necessary.

## Triage and Response{% #triage-and-response %}

1. Check the attack detected for the system: `{{@syslog.hostname}}`.
1. Analyze the rule that triggered, the brief description, and message attached with the log:
   - Rule ID: `{{@rule_id}}`
   - Description: `{{@description}}`
   - Log Message: `{{@log}}`
1. Contact the system administrator immediately to perform the necessary actions to mitigate the cause. This attack requires urgent attention and this rule has no chance of generating false positives.
