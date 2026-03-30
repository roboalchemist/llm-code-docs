# Source: https://docs.datadoghq.com/security/default_rules/def-000-adg.md

---
title: Asana impossible travel detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Asana impossible travel detected
---

# Asana impossible travel detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Identify instances where users are accessing Asana from two distant geographical locations within an improbable timeframe, potentially indicating credential theft or account compromise.

## Strategy{% #strategy %}

This rule analyzes Asana audit events to identify cases where a user appears to perform activities from two different countries or cities within a timeframe that would make physical travel between those locations impossible.

## Triage and response{% #triage-and-response %}

1. Review the events and identify the user `{{@usr.email}}` associated with the impossible travel behavior.
1. Determine if this user has triggered similar alerts in the past or has exhibited unusual audit activity patterns recently.
1. If suspicious behavior is confirmed, restrict access for `{{@usr.email}}`, reset the account's credentials, and notify the user.
