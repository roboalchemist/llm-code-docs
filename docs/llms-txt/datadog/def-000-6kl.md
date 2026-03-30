# Source: https://docs.datadoghq.com/security/default_rules/def-000-6kl.md

---
title: Ivanti nZTA device vulnerability risk detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ivanti nZTA device vulnerability risk
  detected
---

# Ivanti nZTA device vulnerability risk detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}

## Goal{% #goal %}

Identify cases where a device is assigned a Vulnerability Risk Rating (VRR) of Critical, High, Medium, or Low. This helps detect potential security risks and prioritize remediation efforts.

## Strategy{% #strategy %}

This rule monitors vulnerability risk ratings reported by Ivanti nZTA. Devices with higher risk ratings may indicate unpatched software, misconfigurations, or exposure to known security threats.

## Triage and Response{% #triage-and-response %}

1. Identify the affected device `{{@source_name}}` and its Vulnerability Risk Rating (VRR) (Critical, High, Medium, or Low).
1. Review the specific vulnerabilities associated with the rating and assess their potential impact
1. Verify if the device `{{@source_name}}` is running outdated software, missing security patches, or has misconfigured settings.
1. If the risk is Critical or High, prioritize remediation actions such as applying patches, restricting network access, or increasing monitoring.
1. If the risk is Medium or Low, schedule remediation according to security policies while ensuring minimal business disruption.
