# Source: https://docs.datadoghq.com/security/default_rules/def-000-e9x.md

---
title: >-
  Infrastructure double encryption for PostgreSQL Database Server should be
  enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Infrastructure double encryption for
  PostgreSQL Database Server should be enabled
---

# Infrastructure double encryption for PostgreSQL Database Server should be enabled
 
## Description{% #description %}

It is recommended to enable 'infrastructure encryption' when creating Azure Database for PostgreSQL servers. This additional layer of encryption occurs at the hardware level, ensuring that data is encrypted even before it is accessed. This prevents interception of data in motion and protects data at rest in system resources. Enabling 'infrastructure encryption' also secures database backups. To achieve the highest level of security, it is advised to use a Customer Managed asymmetric RSA 2048 bit key stored in Azure Key Vault for key-based encryption.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

**Note:** It is not possible to enable 'infrastructure encryption' on an existing Azure Database for PostgreSQL server.

The remediation steps detail the creation of a new Azure Database for PostgreSQL server with 'infrastructure double encryption' enabled.

1. Follow the normal process of database creation.
1. Under **Additional settings**, ensure that **infrastructure double encryption enabled** is checked.
1. Finish database creation as normal.
