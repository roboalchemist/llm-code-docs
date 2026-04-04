# Source: https://docs.datadoghq.com/security/default_rules/def-000-ehy.md

---
title: Ivanti connect secure multiple blocked web requests detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ivanti connect secure multiple blocked
  web requests detected
---

# Ivanti connect secure multiple blocked web requests detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071)
## Goal{% #goal %}

Detects a high frequency of blocked web requests, which may indicate potential security incidents, such as unauthorized access attempts, reconnaissance activities, or misconfigured systems generating anomalous traffic.

## Strategy{% #strategy %}

This rule monitors blocked web requests across users and raises an alert if the count exceeds the threshold, which may signify suspicious activity or operational anomalies that require investigation.

## Triage and Response{% #triage-and-response %}

1. Identify the user `{{@usr.name}}` associated with the blocked requests.
1. Check for patterns like repeated login failures, unusual request volumes, or connections from suspicious IPs.
1. Investigate recent policy changes or misconfigurations that might explain the activity.
1. If malicious behavior is detected, block offending IPs, restrict access, and review account and access controls.
