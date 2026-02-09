# Source: https://docs.datadoghq.com/security/default_rules/def-000-cf1.md

---
title: FTP deployments should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > FTP deployments should be disabled
---

# FTP deployments should be disabled
 
## Description{% #description %}

By default, Azure Functions, App Service applications, and API Apps can be deployed over FTP. If an essential deployment workflow requires FTP, your system should enforce FTPS for FTP login for all App Service applications and functions.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the Azure Portal
1. Select **App Services**
1. Click on an app
1. Select **Settings** and then **Configuration**
1. Under **General Settings**, for the **Platform Settings**, the **FTP state** should not be set to **All allowed**
