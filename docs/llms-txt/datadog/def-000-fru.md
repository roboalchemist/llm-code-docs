# Source: https://docs.datadoghq.com/security/default_rules/def-000-fru.md

---
title: Jamf Protect threat events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Jamf Protect threat events
---

# Jamf Protect threat events
Classification:attack
## Goal{% #goal %}

Detect when a [Jamf Protect threat event](https://developer.jamf.com/developer-guide/docs/data-streams#:~:text=The%20Threat%20Event%20Stream%20is,vulnerabilities%2C%20malware%20and%20risky%20apps.) has been raised.

## Strategy{% #strategy %}

The Threat Event Stream is a feature of Jamf Protect and Jamf Threat Defense, which detects and remediates endpoint threats, including malicious network communications, device vulnerabilities, malware, and risky apps.

## Triage and response{% #triage-and-response %}

1. Investigate the threat event to determine if it is malicious or benign.
1. If the alert is benign, consider including the user, host, or IP address in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#customize-security-signal-messages-to-fit-your-environment).
