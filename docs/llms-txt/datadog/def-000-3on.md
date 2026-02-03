# Source: https://docs.datadoghq.com/security/default_rules/def-000-3on.md

---
title: RDS instances should publish logs to CloudWatch Logs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS instances should publish logs to
  CloudWatch Logs
---

# RDS instances should publish logs to CloudWatch Logs
 
## Description{% #description %}

This control verifies whether an Amazon RDS DB instance is configured to publish specific logs to Amazon CloudWatch Logs. The control fails if the instance is not configured to publish the following logs to CloudWatch Logs:

- **Oracle:** Alert, Audit, Trace, Listener
- **PostgreSQL:** Postgresql, Upgrade
- **MySQL:** Audit, Error, General, SlowQuery
- **MariaDB:** Audit, Error, General, SlowQuery
- **SQL Server:** Error, Agent
- **Aurora:** Audit, Error, General, SlowQuery
- **Aurora-MySQL:** Audit, Error, General, SlowQuery
- **Aurora-PostgreSQL:** Postgresql

It is recommended for RDS databases to have relevant logging enabled. Database logs offer detailed records of requests made to RDS, which can be invaluable for security and access audits, as well as troubleshooting availability issues.

## Remediation{% #remediation %}

To configure your RDS database to publish logs to CloudWatch Logs, refer to the [Specifying the logs to publish to CloudWatch Logs section in the Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.UploadtoCloudWatch.html#integrating_cloudwatchlogs.configure).
