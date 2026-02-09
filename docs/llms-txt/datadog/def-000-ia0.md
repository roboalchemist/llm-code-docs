# Source: https://docs.datadoghq.com/security/default_rules/def-000-ia0.md

---
title: Extrahop security risk detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Extrahop security risk detected
---

# Extrahop security risk detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attack 
## Goal{% #goal %}

Detect when ExtraHop raises a security risk event.

## Strategy{% #strategy %}

Trigger notifications for security risk events detected by ExtraHop.

## Triage and Response{% #triage-and-response %}

1. Review the log detected with title: `{{@title}}` and with risk score: `{{@risk_score}}`.
1. Determine the potential impact and legitimacy of the event. If the activity is deemed benign, log the event for future reference.
