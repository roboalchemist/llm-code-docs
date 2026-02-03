# Source: https://docs.datadoghq.com/security/default_rules/def-000-ot4.md

---
title: Jamf Protect alerts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Jamf Protect alerts
---

# Jamf Protect alerts
Classification:attack 
## Goal{% #goal %}

Detect when a [Jamf Protect alert](https://learn.jamf.com/bundle/jamf-protect-documentation/page/Alerts.html) with a severity greater than `0` has been raised.

## Strategy{% #strategy %}

Alerts are how Jamf Protect analytics, threat prevention database matches, and removable storage control events are reported.

## Triage and response{% #triage-and-response %}

1. Investigate the threat event to determine if it is malicious or benign.
1. If the alert is benign, consider including the user, host, or IP address in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#customize-security-signal-messages-to-fit-your-environment).

## Changelog{% #changelog %}

- 2 Jul 2025 - Updated the groupby of the rule from host to input.host.hostname and to exclude alerts with severity `0`.
