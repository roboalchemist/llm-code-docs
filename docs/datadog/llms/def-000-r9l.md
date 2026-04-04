# Source: https://docs.datadoghq.com/security/default_rules/def-000-r9l.md

---
title: Check Point Harmony Email & Collaboration impossible travel detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Check Point Harmony Email &
  Collaboration impossible travel detected
---

# Check Point Harmony Email & Collaboration impossible travel detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detects geo-suspicious activity flagged by Check Point, where a user performs actions from two geographically distant locations within an improbable time frame. This behavior may indicate credential theft, session hijacking, or unauthorized account access.

## Strategy{% #strategy %}

This is a threshold-based rule that alerts when Check Point generates a Superman anomaly event, which is the same as an impossible travel detection. The event indicates that the user's activity cannot logically originate from both observed locations within the given timeframe.

## Triage and Response{% #triage-and-response %}

1. Review the user email address `{{@usr.email}}` and analyze the locations of the flagged events.
1. Determine if the user has a history of similar anomalies or if they are using a known VPN or remote access service.
1. If unauthorized access is suspected, force a logout from all active sessions, reset the user's credentials, and enable multi-factor authentication (MFA) if not already enforced.
1. Monitor for additional suspicious activity and restrict access if necessary to prevent further unauthorized use.
