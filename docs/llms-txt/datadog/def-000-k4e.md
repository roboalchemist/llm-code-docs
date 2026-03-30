# Source: https://docs.datadoghq.com/security/default_rules/def-000-k4e.md

---
title: Microsoft Defender for SQL Server should be on for critical SQL Servers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft Defender for SQL Server
  should be on for critical SQL Servers
---

# Microsoft Defender for SQL Server should be on for critical SQL Servers

## Description{% #description %}

Enabling 'Microsoft Defender for SQL' on critical SQL Servers is highly recommended. By default, this feature is set to 'Off'. Microsoft Defender for SQL is a unified package that provides advanced SQL security capabilities, including sensitive data discovery, vulnerability mitigation, and anomaly detection. It is available for Azure SQL Database, Azure SQL Managed Instance, and Azure Synapse Analytics, offering a comprehensive solution for securing your databases. Enabling this feature provides a centralized location for managing and enabling these capabilities. However, it is important to note that Microsoft Defender for SQL is a paid feature and may incur additional costs for each SQL server. It can be enabled at the SQL server level, and the same settings will be applied to the hosted SQL databases.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to SQL servers.
1. For each production SQL server instance, click **Microsoft Defender for Cloud**, then click **Enable Microsoft Defender for SQL**.
