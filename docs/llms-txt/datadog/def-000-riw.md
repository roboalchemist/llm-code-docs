# Source: https://docs.datadoghq.com/security/default_rules/def-000-riw.md

---
title: >-
  Trellix Endpoint Security unrestricted access protection rule violation
  detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trellix Endpoint Security unrestricted
  access protection rule violation detected
---

# Trellix Endpoint Security unrestricted access protection rule violation detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Identify access protection rule violations detected by Trellix Endpoint Security that were logged but not blocked by Trellix itself. These unblocked events indicate potential security risks.

## Strategy{% #strategy %}

Monitor for violations of access protection rules that were logged but not prevented. These events may highlight attempts to access unauthorized resources or sensitive data, which could require further investigation.

## Triage and Response{% #triage-and-response %}

1. Review the details of the access protection rule violation, including the affected user or process.
1. Analyze the event information to understand the nature of the violation and why it was not blocked.
1. Investigate the impacted endpoint using its hostname - `{{@attributes.analyzerhostname}}` and IP address - `{{@attributes.analyzeripv4}}`.
1. Determine if the violation poses a security risk and consider taking immediate action, such as adjusting access policies.
1. Implement measures to strengthen access controls and monitor for any further violations.
