# Source: https://docs.datadoghq.com/security/default_rules/def-000-q5n.md

---
title: DMS replication tasks for the target database should have logging enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DMS replication tasks for the target
  database should have logging enabled
---

# DMS replication tasks for the target database should have logging enabled
 
## Description{% #description %}

This control verifies whether logging is enabled with at least the default severity level (`LOGGER_SEVERITY_DEFAULT`) for DMS replication tasks of the types `TARGET_APPLY` and `TARGET_LOAD`. If logging is disabled for these tasks or the severity level is below `LOGGER_SEVERITY_DEFAULT`, the control fails. Acceptable logging levels are `LOGGER_SEVERITY_DEFAULT`, `LOGGER_SEVERITY_DEBUG` or `LOGGER_SEVERITY_DETAILED_DEBUG`.

Amazon CloudWatch is used by DMS to capture log information throughout the migration process. By configuring task settings, you can determine which components are logged and the level of detail recorded. Logging is essential for DMS replication tasks, supporting activities such as monitoring, troubleshooting, auditing, performance analysis, error detection, recovery, historical reviews, and reporting.

## Remediation{% #remediation %}

For guidance on configuring replication task logging, please refer to the [Viewing and managing AWS DMS task logs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Monitoring.ManagingLogs) section of the AWS Database Migration Service User Guide.
