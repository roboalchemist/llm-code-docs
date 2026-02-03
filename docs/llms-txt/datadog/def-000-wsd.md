# Source: https://docs.datadoghq.com/security/default_rules/def-000-wsd.md

---
title: >-
  Azure should be configured to send email notifications about security alerts
  with High severity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure should be configured to send
  email notifications about security alerts with High severity
---

# Azure should be configured to send email notifications about security alerts with High severity
 
## Description{% #description %}

Turning on the email alert feature ensures the subscription owner or chosen security contacts receive important security alerts. These alerts are delivered directly to your inbox to ensure the right people are immediately aware of security issues.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. From the [Azure Portal](https://portal.azure.com/#home) select the Portal menu.
1. Select **Microsoft Defender for Cloud**.
1. Click **Environment Settings** on the left side menu.
1. Click on the appropriate management group, subscription, or workspace.
1. Click **Email notifications**.
1. Ensure that the **Notify about alerts with the following severity (or higher):** setting is checked and set to **High**
