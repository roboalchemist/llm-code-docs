# Source: https://docs.datadoghq.com/security/default_rules/def-000-pkt.md

---
title: Audit data for Azure SQL Server should be retained for greater than 90 days
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Audit data for Azure SQL Server should
  be retained for greater than 90 days
---

# Audit data for Azure SQL Server should be retained for greater than 90 days

## Description{% #description %}

To ensure effective monitoring and detection of anomalies or breaches, it is recommended to configure SQL Server Audit Retention to be greater than 90 days. By doing so, audit logs are retained for a prolonged period, allowing for thorough investigation and analysis in cases of suspected misuse or security incidents. It is important to note that the default value for SQL Server audit storage is disabled, meaning that no logs are retained unless explicitly enabled and configured with a retention period.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **SQL servers**
1. For each server instance, click on **Auditing**
1. If storage is selected, expand **Advanced properties**
1. Set the **Retention (days)** setting greater than **90** days or **0** for unlimited retention
1. Select **Save**
