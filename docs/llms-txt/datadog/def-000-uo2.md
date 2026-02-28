# Source: https://docs.datadoghq.com/security/default_rules/def-000-uo2.md

---
title: Microsoft graph security alerts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Microsoft graph security alerts
---

# Microsoft graph security alerts

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attack
## Goal{% #goal %}

Detect when a Microsoft security product sends an alert to the Microsoft Graph security API.

## Strategy{% #strategy %}

Microsoft Graph is the gateway to data and intelligence in Microsoft 365. It provides a unified programmability model that you can use to access the data in Microsoft 365, Windows, and Enterprise Mobility + Security. This detection identifies when an alert from a Microsoft security product is raised and queried through the Microsoft Graph security API.

## Triage and response{% #triage-and-response %}

1. Investigate the alert to determine if it is malicious or benign.
1. If the alert is deemed malicious, follow any recommended actions provided by Microsoft on the alert and also any internal incident response processes.
1. If the alert is benign, consider including the user, host, or IP address in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#customize-security-signal-messages-to-fit-your-environment) for more information.
