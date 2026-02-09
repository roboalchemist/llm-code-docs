# Source: https://docs.datadoghq.com/security/default_rules/0cg-j5s-svt.md

---
title: Anomalous amount of Autoscaling Group events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous amount of Autoscaling Group
  events
---

# Anomalous amount of Autoscaling Group events
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## Goal{% #goal %}

Detect when an attacker is attempting to hijack an EC2 AutoScaling Group.

## Strategy{% #strategy %}

This rule lets you monitor AWS EC2 Autoscaling logs (`@eventSource:autoscaling.amazonaws.com`) to detect when an Autoscaling group receives an anomalous amount of API calls (`{{@evt.name}}`).

## Triage and response{% #triage-and-response %}

1. Confirm if the user `{{@userIdentity.arn}}` intended to make the `{{@evt.name}}` API calls.
1. If the user did not make the API calls:
   - Rotate the credentials.
   - Investigate if the same credentials made other unauthorized API calls.
