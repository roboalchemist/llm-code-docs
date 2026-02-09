# Source: https://docs.datadoghq.com/security/default_rules/def-000-v1v.md

---
title: Trellix Endpoint Security blocked web control violation detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trellix Endpoint Security blocked web
  control violation detected
---

# Trellix Endpoint Security blocked web control violation detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
## Goal{% #goal %}

Detect threats related to web control violations which are blocked by Trellix Endpoint Security.

## Strategy{% #strategy %}

Monitor endpoint security events for indications of blocked web control violations. Focus on analyzing the context of the event, including the specific website or URL that was blocked, and the affected endpoints.

## Triage and Response{% #triage-and-response %}

1. Confirm the details of the blocked web control violation, such as the restricted URL or category.
1. Review the event details to understand the nature of the violation.
1. Examine the impacted endpoint using its hostname - `{{@attributes.analyzerhostname}}` and IP address - `{{@attributes.analyzeripv4}}`.
1. Ensure the web control policies are properly enforced to prevent access to restricted content in the future.
1. Continue to monitor the affected endpoints for further violations or related anomalies.
