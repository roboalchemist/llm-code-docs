# Source: https://docs.datadoghq.com/security/default_rules/def-000-ocp.md

---
title: iboss multiple soft blocked requests detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > iboss multiple soft blocked requests
  detected
---

# iboss multiple soft blocked requests detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071)
## Goal{% #goal %}

Detects multiple soft block events from a user, which may indicate attempts to access restricted or risky content that violates security policies.

## Strategy{% #strategy %}

Monitor soft-blocked web requests to identify patterns of repeated access attempts to disallowed or potentially harmful content.

## Triage and Response{% #triage-and-response %}

1. Identify the user `{{@usr.name}}` and the device `{{@computerName}}` generating the soft-blocked requests.
1. Review the client IP address `{{@network.client.ip}}` to validate network origin and assess for unusual activity.
1. Determine whether the accessed content is harmful, miscategorized, or being intentionally bypassed.
