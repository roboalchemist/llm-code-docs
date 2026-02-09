# Source: https://docs.datadoghq.com/security/default_rules/def-000-ies.md

---
title: Azure Active Directory Admin should be configured for Azure SQL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure Active Directory Admin should be
  configured for Azure SQL
---

# Azure Active Directory Admin should be configured for Azure SQL
 
## Description{% #description %}

By default, Azure Active Directory Authentication for SQL Database/Server is not enabled. However, utilizing Azure Active Directory (Azure AD) authentication allows for managing credentials in a centralized location. This authentication mechanism enables connecting to Microsoft Azure SQL Database and SQL Data Warehouse using Azure AD identities. By using Azure AD authentication, database users and other Microsoft services can be managed in a single central location, simplifying permission management and providing an alternative to SQL Server authentication. It also eliminates the need to store passwords by enabling integrated Windows authentication and supports various forms of authentication, including token-based authentication for applications and multi-factor authentication (MFA). To properly implement Azure AD for central authentication, it is important to configure the necessary groups and roles based on the organization's requirements.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **SQL servers**.
1. For each SQL server, click **Active Directory admin**.
1. Click **Set admin**.
1. Select an admin and click **Save**.
1. Select the **Support only Azure Active Directory authentication for this server** checkbox.
1. The **Enable Azure AD authentication only** popup appears. Click **Yes** to enable the feature and **Save** the setting.
