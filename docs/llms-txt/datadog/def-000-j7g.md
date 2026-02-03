# Source: https://docs.datadoghq.com/security/default_rules/def-000-j7g.md

---
title: SSL connection on PostgreSQL Database Server should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SSL connection on PostgreSQL Database
  Server should be enabled
---

# SSL connection on PostgreSQL Database Server should be enabled
 
## Description{% #description %}

Enable SSL connectivity on PostgreSQL Servers. SSL connectivity helps to provide a new layer of security by connecting database servers to client applications using Secure Sockets Layer (SSL). Enforcing SSL connections between a database server and its client applications helps protect against "man in the middle" attacks by encrypting the data stream between the server and application.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Login to [Azure Portal](https://portal.azure.com)
1. Go to **Azure Database for PostgreSQL server**
1. For each database, click on **Connection security**
1. In SSL settings, click on **Enabled** to enforce SSL connection
