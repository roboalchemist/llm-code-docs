# Source: https://docs.datadoghq.com/security/default_rules/def-000-yxc.md

---
title: SQL database instances should have automated backups enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL database instances should have
  automated backups enabled
---

# SQL database instances should have automated backups enabled
 
## Description{% #description %}

This check ensures that Cloud SQL database instances are configured with automated backups. It is recommended that all SQL database instances enable automated backups to provide a way to restore an instance and recover lost data. This recommendation applies to SQL Server, PostgreSQL, MySQL Generation 1, and MySQL Generation 2 instances.

Automated backups are essential for protecting data from loss or damage, although they will increase the required storage size and associated costs. This check does not assess Read Replicas as backup is not possible for them.

## Remediation{% #remediation %}

For instructions on enabling automated backups for Cloud SQL instances, refer to [Enabling Automated Backups](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups) in the Google Cloud documentation.
