# Source: https://docs.datadoghq.com/security/default_rules/def-000-tbl.md

---
title: 'Trend Micro Vision One Endpoint Security alert: Content violation detected'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trend Micro Vision One Endpoint
  Security alert: Content violation detected
---

# Trend Micro Vision One Endpoint Security alert: Content violation detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}

## Goal{% #goal %}

Detect events related to content violations as identified by Trend Micro Vision One Endpoint Security.

## Strategy{% #strategy %}

Monitor endpoint security events for indications of content violations. Focus on analyzing the context of the event, including the specific policy settings that were breached and the affected endpoints. These events may indicate breaches of security policies, such as the inappropriate access to or transmission of sensitive or confidential information, which could pose significant security risks and necessitate immediate attention.

## Triage and Response{% #triage-and-response %}

1. Confirm the policy settings associated with the content violation (`{{@policy_settings}}`).
1. Review the event details to understand the nature of the violation.
1. Examine the impacted endpoint using its name (`{{@source_host_name}}`) and IP address (`{{@endpoint_ip}}`).
1. If the content violation is confirmed as a security issue, take appropriate actions to address the breach, such as adjusting policies or restricting access.
1. Continue to monitor the affected endpoints for further content violations or related anomalies.
