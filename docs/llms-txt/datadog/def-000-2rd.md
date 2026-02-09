# Source: https://docs.datadoghq.com/security/default_rules/def-000-2rd.md

---
title: Keycloak multiple users impersonated by single user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Keycloak multiple users impersonated by
  single user
---

# Keycloak multiple users impersonated by single user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detects when there are multiple impersonated events from the same impersonator.

## Strategy{% #strategy %}

This rule monitors logs to identify impersonated events to detect if those events are from the same impersonator.

## Triage and Response{% #triage-and-response %}

1. Identify the user who is performing the impersonation: `{{@impersonator}}`.
1. Determine the number of users that have been impersonated and the time frame of these actions.
1. Notify the impersonator about the activity.
1. If the impersonation appears unauthorized or suspicious, consider blocking the impersonator's account and review their recent activity for any potential security breaches.
1. Inform the affected users about the impersonation.
