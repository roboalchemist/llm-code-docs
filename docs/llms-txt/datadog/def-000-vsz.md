# Source: https://docs.datadoghq.com/security/default_rules/def-000-vsz.md

---
title: SQL database instances should enforce SSL for all incoming connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL database instances should enforce
  SSL for all incoming connections
---

# SQL database instances should enforce SSL for all incoming connections
 
## Description{% #description %}

This control ensures that SSL encryption is enabled for SQL database connections, which include PostgreSQL, MySQL (generation 1 and 2), and SQL Server 2017 instances. Using SSL encryption protects sensitive data such as credentials, database queries, and query outputs from being intercepted through a Man-in-the-Middle (MITM) attack. Enforcing SSL encryption enhances the security of database connections by ensuring that all data exchanged between clients and the Cloud SQL database instance is securely transmitted.

## Remediation{% #remediation %}

To enforce SSL encryption for your database connections, follow the instructions in the [Configure SSL for a Cloud SQL instance](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/) section of the Google Cloud documentation.
