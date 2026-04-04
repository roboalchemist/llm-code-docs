# Source: https://docs.datadoghq.com/security/default_rules/def-000-dgk.md

---
title: The app service should enable registration with Azure Active Directory
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The app service should enable
  registration with Azure Active Directory
---

# The app service should enable registration with Azure Active Directory

## Description{% #description %}

Managed service identity in App Service makes an app more secure by eliminating secrets from the app, such as credentials in the connection strings. When registering with Azure Active Directory in the app service, the app connects to other Azure services securely without the need for a username and password. App Service provides a highly scalable, self-patching web hosting service in Azure. It also provides a managed identity for apps, which is a turn-key solution for securing access to Azure SQL Database and other Azure services.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Log in to Azure Portal using [https://portal.azure.com](https://portal.azure.com).
1. Go to **App Services**.
1. Click on each App.
1. Under **Settings** section, click on **Identity**.
1. Set **Status** to **On**.
