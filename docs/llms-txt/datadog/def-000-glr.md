# Source: https://docs.datadoghq.com/security/default_rules/def-000-glr.md

---
title: Azure should use the latest HTTP version available
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure should use the latest HTTP
  version available
---

# Azure should use the latest HTTP version available

## Description{% #description %}

Ensure use of the latest **HTTP** version. Using the latest version of **HTTP** is recommended to leverage securityenhancements and new capabilities.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Log into [Azure Portal](https://portal.azure.com).
1. Go to **App Services**.
1. Click on each app.
1. Under **Settings**, click *Configuration*\*.
1. Set HTTP version to `2.0` under **General settings**.
