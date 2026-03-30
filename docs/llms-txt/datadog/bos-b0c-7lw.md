# Source: https://docs.datadoghq.com/security/default_rules/bos-b0c-7lw.md

---
title: >-
  Network Security Group Flow Log retention period should be 'greater than 90
  days'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Network Security Group Flow Log
  retention period should be 'greater than 90 days'
---

# Network Security Group Flow Log retention period should be 'greater than 90 days'

## Description{% #description %}

To ensure sufficient data retention, it is recommended to set the retention period for your Network Security Group Flow Logs to a minimum of 90 days. By default, the flow logs for Network Security Groups are disabled, so it is essential to enable them to capture information about IP traffic. The logs provide valuable insights into any anomalies or potential breaches, helping you in monitoring and securing your network. However, it is important to consider that increasing the data retention period may lead to higher monthly storage costs based on your data usage.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **Network Watcher** and select **NSG flow logs** blade in the Logs section.
1. Select each Network Security Group from the list.
1. Ensure **Status** is set to **On**.
1. Ensure **Retention (days)** setting is greater than 90 days.
1. Select your storage account in the **Storage account** field.
