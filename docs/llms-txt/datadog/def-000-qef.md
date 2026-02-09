# Source: https://docs.datadoghq.com/security/default_rules/def-000-qef.md

---
title: Vulnerability Assessment should be enabled for SQL server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Vulnerability Assessment should be
  enabled for SQL server
---

# Vulnerability Assessment should be enabled for SQL server
 
## Description{% #description %}

The Vulnerability Assessment service is a valuable tool that analyzes SQL databases to identify security issues and deviations from best practices. It helps identify misconfigurations, excessive permissions, and other potential vulnerabilities. The service provides remediation steps, customizable scripts, and assessment reports with customizable baseline settings. Enabling these features in Microsoft Defender for SQL comes with additional costs per SQL server.

## Remediation{% #remediation %}

Azure is transitioning from Classic Configuration to Express Configuration. For specific configuration instructions that fit your use case, see [Enable vulnerability assessment on your Azure SQL databases and servers](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable#express-configuration).
