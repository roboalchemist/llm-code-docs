# Source: https://docs.datadoghq.com/security/default_rules/def-000-g1e.md

---
title: AWS Verified Access anomalous failed authentication attempts by host
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Verified Access anomalous failed
  authentication attempts by host
---

# AWS Verified Access anomalous failed authentication attempts by host
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1199-trusted-relationship](https://attack.mitre.org/techniques/T1199)
## Goal{% #goal %}

Detect when access is denied to a host authenticating using AWS Verified Access.

## Strategy{% #strategy %}

The anomaly detection generates a security signal when a host's authentication failure requests deviates from its baseline.

For more information about the anomaly detection method, see [Detect security threats with anomaly detection rules](https://www.datadoghq.com/blog/anomaly-detection-rules-datadog/).

## Triage and response{% #triage-and-response %}

Determine if the host `{{@host}}` should have access.
