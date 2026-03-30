# Source: https://docs.datadoghq.com/security/default_rules/def-000-dzm.md

---
title: SentinelOne Alerts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > SentinelOne Alerts
---

# SentinelOne Alerts
Classification:attack
## Goal{% #goal %}

Detect when SentinelOne raises a custom alert.

## Strategy{% #strategy %}

SentinelOne allows users to create custom rules from event search queries, that trigger alerts and response when the rule matches on the specified criteria.

## Triage and response{% #triage-and-response %}

1. Investigate the SentinelOne custom alert to determine if it is malicious or benign.
1. If the alert is benign, consider including the user, host or IP address in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#customize-security-signal-messages-to-fit-your-environment) for more information.
