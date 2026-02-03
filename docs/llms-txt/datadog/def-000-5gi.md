# Source: https://docs.datadoghq.com/security/default_rules/def-000-5gi.md

---
title: Forcepoint Security Service Edge alert event
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Forcepoint Security Service Edge alert
  event
---

# Forcepoint Security Service Edge alert event

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attack 
## Goal{% #goal %}

Detects Forcepoint SSE logs with an Alert action.

## Strategy{% #strategy %}

This rule monitors all the Forcepoint SSE logs for which the Alert action is enforced by Forcepoint ONE SSE according to the set policy.

## Triage and Response{% #triage-and-response %}

1. Review the specific alert action enforced by Forcepoint ONE SSE from IP Address - `{{@network.client.ip}}` to analyze the corresponding log entry to understand the context of the alert.
1. Determine the affected system, user, or resource related to the alert and assess the potential risk or impact based on the policy violation or enforced action. Analyze activity performed by which user and the application detail as below:Activity- `{{@activity}}` | Performed By- `{{@usr.name}}` | Application- `{{@application}}`
1. If necessary, update or refine the policy in Forcepoint ONE SSE to prevent false positives or improve enforcement.
1. If the alert indicates a critical security threat or unusual activity, escalate it to the security operations team for further investigation.
