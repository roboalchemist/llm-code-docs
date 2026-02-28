# Source: https://docs.datadoghq.com/security/default_rules/def-000-sup.md

---
title: Aurora MySQL clusters should publish audit logs to CloudWatch Logs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Aurora MySQL clusters should publish
  audit logs to CloudWatch Logs
---

# Aurora MySQL clusters should publish audit logs to CloudWatch Logs

## Description{% #description %}

This check verifies the Aurora MySQL DB cluster is configured to send audit logs to CloudWatch Logs. This check does not apply to Aurora Serverless v1 DB clusters.

Audit logs capture and record database activities such as login attempts, data changes, schema modifications, and other events related to security and compliance auditing. By configuring an Aurora MySQL DB cluster to send audit logs to a log group in Amazon CloudWatch Logs, you enable real-time analysis of the log data. CloudWatch Logs offers highly durable storage for logs, allowing you to create alerts and monitor metrics in CloudWatch.

## Remediation{% #remediation %}

For an alternate method to publish audit logs to CloudWatch Logs:

- Enable advanced auditing, and
- Set the cluster-level DB parameter `server_audit_logs_upload` to `1`.

By default, the `server_audit_logs_upload` parameter is set to `0`. Datadog does not recommend using the default setting. Instead, follow the method specified in [Publishing Amazon Aurora MySQL logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.CloudWatch.html).
