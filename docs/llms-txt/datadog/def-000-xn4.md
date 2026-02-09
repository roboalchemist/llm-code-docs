# Source: https://docs.datadoghq.com/security/default_rules/def-000-xn4.md

---
title: Trellix Endpoint Security unrestricted port blocking rule violation detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trellix Endpoint Security unrestricted
  port blocking rule violation detected
---

# Trellix Endpoint Security unrestricted port blocking rule violation detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Identify port blocking rule violations detected by Trellix Endpoint Security that were logged but not blocked by Trellix itself. These unblocked may indicate potential unauthorized network access.

## Strategy{% #strategy %}

Monitor for logged violations of port blocking rules that were not acted upon. These events may indicate attempts to communicate through blocked ports, which could suggest malicious activities.

## Triage and Response{% #triage-and-response %}

1. Review the details of the port blocking rule violation, including the specific port and application involved.
1. Analyze the event information to understand why the violation was not blocked.
1. Investigate the impacted endpoint using its hostname - `{{@attributes.analyzerhostname}}` and IP address - `{{@attributes.analyzeripv4}}`.
1. Assess the risk associated with the violation and determine appropriate actions, such as enhancing network security policies.
1. Continue monitoring for similar violations to prevent unauthorized access attempts.
