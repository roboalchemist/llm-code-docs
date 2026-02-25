# Source: https://docs.datadoghq.com/security/default_rules/def-000-vx1.md

---
title: >-
  Server parameter 'connection_throttling' should be enabled for PostgreSQL
  Database Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Server parameter
  'connection_throttling' should be enabled for PostgreSQL Database Server
---

# Server parameter 'connection_throttling' should be enabled for PostgreSQL Database Server

## Description{% #description %}

Enabling `connection_throttling` helps the PostgreSQL Database to set the verbosity of logged messages. This in turn generates query and error logs with respect to concurrent connections that could lead to a successful Denial of Service (DoS) attack by exhausting connection resources. A system can also fail or be degraded by an overload of legitimate users. Query and error logs can be used to identify, troubleshoot, and repair configuration errors and sub-optimal performance.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Log in to [Azure Portal](https://portal.azure.com).
1. Go to **Azure Database for PostgreSQL server**.
1. For each database, click **Server parameters**.
1. Search for `connection_throttling`.
1. Click **ON** and save.
