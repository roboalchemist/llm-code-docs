# Source: https://docs.datadoghq.com/security/default_rules/def-000-jyr.md

---
title: Forcepoint Security Service Edge impossible travel detected in admin portal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Forcepoint Security Service Edge
  impossible travel detected in admin portal
---

# Forcepoint Security Service Edge impossible travel detected in admin portal

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Identify instances where users are performing activities on Forcepoint SSE from geographically distant locations within an improbable time frame, potentially indicating credential theft or account compromise.

## Strategy{% #strategy %}

This rule analyzes Forcepoint SSE to identify cases where a user appears to perform actions from two different countries or cities within a time frame that would make physical travel between those locations impossible.

## Triage and Response{% #triage-and-response %}

1. Review the events and identify the user `{{@usr.name}}` associated with the impossible travel behavior.
1. Determine if this user has triggered similar alerts in the past or exhibited unusual activity patterns recently.
1. If suspicious behavior is confirmed, restrict access for `{{@usr.name}}`, reset the account's credentials, and notify the user.
