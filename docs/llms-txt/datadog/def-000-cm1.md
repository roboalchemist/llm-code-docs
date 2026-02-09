# Source: https://docs.datadoghq.com/security/default_rules/def-000-cm1.md

---
title: >-
  Server parameter 'log_retention_days' should be greater than 3 days for
  PostgreSQL Database Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Server parameter 'log_retention_days'
  should be greater than 3 days for PostgreSQL Database Server
---

# Server parameter 'log_retention_days' should be greater than 3 days for PostgreSQL Database Server
 
## Description{% #description %}

Enabling `log_retention_days` helps PostgreSQL Database to set the number of days a log file is retained, which in turn generates query and error logs. Query and error logs can be used to identify, troubleshoot, and repair configuration errors and sub-optimal performance.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Log in to [Azure Portal](https://portal.azure.com).
1. Go to **Azure Database for PostgreSQL server**.
1. For each database, click **Server parameters**.
1. Search for `log_retention_days`.
1. Enter a value in range 4-7 (inclusive) and save.
