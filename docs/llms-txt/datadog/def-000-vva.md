# Source: https://docs.datadoghq.com/security/default_rules/def-000-vva.md

---
title: Trend Micro Vision One XDR impossible travel detected for identity activity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trend Micro Vision One XDR impossible
  travel detected for identity activity
---

# Trend Micro Vision One XDR impossible travel detected for identity activity

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect and respond to situations where a user account appears to be active in geographically distinct locations within an impossible time frame. Such activity may indicate account compromise, malicious access, or misconfiguration.

## Strategy{% #strategy %}

Monitor identity activities logged by Trend Micro Vision One XDR, particularly focusing on detecting impossible travel scenarios. This involves identifying instances where a single user account logs in or accesses systems from locations that are geographically far apart in a time span too short for normal travel.

## Triage and Response{% #triage-and-response %}

1. Confirm the source and nature of the event by reviewing the detectedDateTime: `{{@detectedDateTime}}` and source fields.
1. Identify the involved user(s) and associated systems:
   - User Account: `{{@usr.name}}`
1. Assess the geographic locations of the activities. Look for discrepancies between locations indicated by IP addresses, considering the short time frame that suggests impossible travel.
1. If impossible travel is confirmed,
   - Investigate potential compromise of the user account. Review recent activities, changes, and potential unauthorized access.
   - Lock or reset the affected account to prevent further unauthorized actions.
   - Notify the affected user and relevant security teams of the suspicious activity.
