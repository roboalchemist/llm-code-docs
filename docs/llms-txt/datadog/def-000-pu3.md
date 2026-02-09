# Source: https://docs.datadoghq.com/security/default_rules/def-000-pu3.md

---
title: Ivanti connect secure severe events detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ivanti connect secure severe events
  detected
---

# Ivanti connect secure severe events detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attack 
## Goal{% #goal %}

Detects critical, major and minor severity events on the Ivanti Connect Secure platform, such as system errors, service disruptions, or security alerts, which may indicate system vulnerabilities or active threats.

## Strategy{% #strategy %}

This rule monitors logs for critical, major and minor severity events flagged by the system and raises an alert when such events are detected, signaling the need for immediate investigation and response.

## Triage and Response{% #triage-and-response %}

1. Review the events in the system logs to identify their nature (for example, service errors, security breaches, or misconfigurations.
1. Check for related anomalies, such as high resource usage, unauthorized access attempts, or unusual traffic patterns.
1. Investigate recent changes or updates to the platform that could have triggered the events.
1. Take corrective actions such as patching vulnerabilities, restarting affected services, or escalating to the security team for further analysis.
