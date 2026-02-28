# Source: https://docs.datadoghq.com/security/default_rules/def-000-6gy.md

---
title: Have I Been Pwned latest breach detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Have I Been Pwned latest breach
  detected
---

# Have I Been Pwned latest breach detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1552-unsecured-credentials](https://attack.mitre.org/techniques/T1552)
## Goal{% #goal %}

Detect breaches reported by Have I Been Pwned, and enable timely triage and remediation based on severity.

## Strategy{% #strategy %}

Monitor incoming breaches that contain the targeted email field to assess the impact and initiate security actions such as user notification, password resets, and incident escalation.

## Triage and Response{% #triage-and-response %}

1. Review the breach details `{{@Name}}` on `{{@BreachDate}}` to confirm the exposure and its recency.
1. Validate the targeted email `{{usr.email}}` against active user accounts and check recent login activity for anomalies.
1. Reset credentials, revoke active sessions, notify user and SOC team, or log for monitoring.
