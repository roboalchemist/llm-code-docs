# Source: https://docs.datadoghq.com/security/default_rules/def-000-lyy.md

---
title: Auditing on SQL Server should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Auditing on SQL Server should be
  enabled
---

# Auditing on SQL Server should be enabled
 
## Description{% #description %}

Enabling auditing on SQL Servers in the Azure platform ensures that all databases on the server instance are audited, maintaining regulatory compliance and providing insight into database activity to detect anomalies and security violations. Auditing policies applied at the database level do not override the policies and settings set at the server level.

### Remediation{% #remediation %}

To [enable auditing](https://docs.microsoft.com/en-us/azure/azure-sql/database/auditing-overview) on your Azure SQL Server, you can follow these steps:

1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to your SQL server.
1. Go to the left-hand menu, scroll down, and select **Auditing** under the **Security** section.
1. In the Auditing window, click on **Turn On Auditing** or **Configure Auditing** to set up the auditing settings.
1. Configure the desired settings, such as choosing the storage account to store the audit logs, setting auditing retention, and selecting specific events to audit.
1. Once you have configured the auditing settings, click **Save** or **Apply** to enable auditing on the SQL server.
