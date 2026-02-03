# Source: https://docs.datadoghq.com/security/default_rules/def-000-olr.md

---
title: Delinea Privilege Manager unusual spike in application justification events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Delinea Privilege Manager unusual spike
  in application justification events
---

# Delinea Privilege Manager unusual spike in application justification events

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Detects an unusual spike in application justification events.

## Strategy{% #strategy %}

This rule monitors the Delinea Privilege Manager logs to detect an unusual spike in application justification events.

## Triage and Response{% #triage-and-response %}

1. Analyze the application justification events to identify the users, applications, and computers that are contributing significantly to the spike.
1. Identify whether the spike involves applications flagged as suspicious or bad.
1. Determine if these justifications (user reasons) were for legitimate business needs or potential misuse.
1. If suspicious or unauthorized justifications are identified, revoke or restrict the privileges granted to the affected applications.
1. Review change history logs to identify any recent modifications to policies or permissions causing spike and if a misconfiguration is found, revert to a more secure policy.
