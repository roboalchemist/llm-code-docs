# Source: https://docs.datadoghq.com/security/default_rules/def-000-gkg.md

---
title: >-
  Server parameter 'log_connections' should be enabled for PostgreSQL Database
  Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Server parameter 'log_connections'
  should be enabled for PostgreSQL Database Server
---

# Server parameter 'log_connections' should be enabled for PostgreSQL Database Server

## Description{% #description %}

Enabling `log_connections` helps PostgreSQL Database to log attempted connection to the server, as well as successful completion of client authentication. Log data can be used to identify, troubleshoot, and repair configuration errors and suboptimal performance.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Log in to [Azure Portal](https://portal.azure.com).
1. Go to **Azure Database for PostgreSQL server**.
1. For each database, click **Server parameters**.
1. Search for `log_connections`.
1. Click **ON** and save.
