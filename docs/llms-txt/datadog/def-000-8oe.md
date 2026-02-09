# Source: https://docs.datadoghq.com/security/default_rules/def-000-8oe.md

---
title: AWS Verified Access anomalous failed authentication attempts by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Verified Access anomalous failed
  authentication attempts by user
---

# AWS Verified Access anomalous failed authentication attempts by user
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when access is denied to a user authenticating using AWS Verified Access.

## Strategy{% #strategy %}

The anomaly detection generates a security signal when a user's authentication failure requests deviates from its baseline.

For more information about the anomaly detection method, see [Detect security threats with anomaly detection rules](https://www.datadoghq.com/blog/anomaly-detection-rules-datadog/).

## Triage and response{% #triage-and-response %}

Determine if the user `{{@usr.id}}` should have access.
