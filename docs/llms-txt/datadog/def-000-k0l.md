# Source: https://docs.datadoghq.com/security/default_rules/def-000-k0l.md

---
title: >-
  SQL Server Vulnerability Assessments should send scan reports to subscribed
  admins
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL Server Vulnerability Assessments
  should send scan reports to subscribed admins
---

# SQL Server Vulnerability Assessments should send scan reports to subscribed admins

## Description{% #description %}

Vulnerability Assessment (VA) scan reports and alerts will be sent to email addresses configured at 'Send scan reports to'. This may help in reducing time required for identifying risks and taking corrective measures. Enabling these features on Microsoft Defender for SQL incurs additional costs per SQL server.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Azure is transitioning from Classic Configuration to Express Configuration. For specific configuration instructions that fit your use case, see [Enable vulnerability assessment on your Azure SQL databases and servers](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable#express-configuration).
