# Source: https://docs.datadoghq.com/security/default_rules/def-000-uk6.md

---
title: Azure should be configured with a security contact email
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure should be configured with a
  security contact email
---

# Azure should be configured with a security contact email

## Description{% #description %}

Microsoft Defender for Cloud notifies subscription owners via email about high-severity alerts. An additional security contact email address should be provided for prompt notification about security alerts. This allows the organization's security team to be aware of potential risks.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. From the [Azure Portal](https://portal.azure.com/#home) select the Portal menu.
1. Select **Microsoft Defender for Cloud**.
1. Click **Environment Settings** on the left side menu.
1. Click on the appropriate management group, subscription, or workspace.
1. Click **Email notifications**.
1. Enter a valid security contact email address (or multiple addresses separated by commas) in the **additional email addresses** field.
1. Click **Save**
1.
