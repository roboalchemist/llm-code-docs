# Source: https://docs.datadoghq.com/security/default_rules/def-000-g5w.md

---
title: Crowdstrike Alerts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Crowdstrike Alerts
---

# Crowdstrike Alerts
Classification:attack 
## Goal{% #goal %}

Detect when Crowdstrike raises an alert.

## Strategy{% #strategy %}

CrowdStrike provides a centralized platform for monitoring and managing security-related notifications, alerts, and actions across endpoints and cloud workloads. This rule uses the third-party detection method to identify the following Crowdstrike events:

- DetectionSummaryEvent
- FirewallMatchEvent
- IdentityProtectionEvent
- IdpDetectionSummaryEvent
- IncidentSummaryEvent
- EppDetectionSummaryEvent

## Triage and response{% #triage-and-response %}

1. Investigate the Crowdstrike alert to determine if it is malicious or benign.
1. If the alert is benign, consider including the user, host or IP address in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#customize-security-signal-messages-to-fit-your-environment) for more information.

## Changelog{% #changelog %}

30 June 2025 - Updated rule to include an additional query for `@evt.type:EppDetectionSummaryEvent`. 15 July 2025 - Updated rule to include additional capitalized severity fields.
