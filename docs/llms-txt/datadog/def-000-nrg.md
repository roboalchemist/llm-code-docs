# Source: https://docs.datadoghq.com/security/default_rules/def-000-nrg.md

---
title: Diagnostic Setting should capture appropriate categories
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Diagnostic Setting should capture
  appropriate categories
---

# Diagnostic Setting should capture appropriate categories

## Description{% #description %}

Before proceeding with the recommendation, it is important to ensure that a Diagnostic Setting already exists. This allows for the appropriate navigation and options mentioned in the recommendation. Diagnostic settings should be configured to log the relevant activities from the control/management plane. By capturing the appropriate diagnostic setting categories for these activities, it enables effective alerting and monitoring. For single resources, refer to the [Diagnostic settings in Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings) documentation, and for multiple resource types at scale, refer to [Create diagnostic settings at scale using Azure Policies and Initiatives](https://docs.microsoft.com/en-us/azure/governance/policy/samples/apply-diagnostic-settings-at-scale).

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **Azure Monitor**.
1. Click **Activity log**, then click **Export Activity Logs**.
1. Select the **Subscription** from the drop-down menu.
1. Click **Add diagnostic setting** and enter a name for the Diagnostic Setting.
1. Check the following categories: **Administrative**, **Alert**, **Policy**, and **Security**.
1. Choose the log destination details according to your organization's needs.
