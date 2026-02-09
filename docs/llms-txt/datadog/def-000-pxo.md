# Source: https://docs.datadoghq.com/security/default_rules/def-000-pxo.md

---
title: >-
  Server parameter 'log_checkpoints' should be enabled for PostgreSQL Database
  Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Server parameter 'log_checkpoints'
  should be enabled for PostgreSQL Database Server
---

# Server parameter 'log_checkpoints' should be enabled for PostgreSQL Database Server
 
## Description{% #description %}

Enable `log_checkpoints` on PostgreSQL Servers. Enabling `log_checkpoints` helps the PostgreSQL Database to log each checkpoint and generate query and error logs. Access to transaction logs is not supported. Query and error logs can be used to identify, troubleshoot, and repair configuration errors and sub-optimal performance.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Log in to [Azure Portal](https://portal.azure.com).
1. Go to **Azure Database for PostgreSQL server**.
1. For each database, click **Server parameters**.
1. Search for `log_checkpoints`.
1. Click **ON** and save
