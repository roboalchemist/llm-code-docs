# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_query_logging_config.dataset.md

---
title: "Route\_53 Query Logging Configuration"
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: "Docs > DDSQL Reference > Data Directory > Route\_53 Query Logging Configuration"
---

# Route 53 Query Logging Configuration

Route 53 Query Logging Configuration in AWS enables you to capture detailed information about DNS queries made to a specific hosted zone. By configuring query logging, you can send logs to a CloudWatch Logs log group, where they can be monitored, analyzed, and retained. This helps with troubleshooting, security analysis, and gaining insights into DNS traffic patterns.

```
aws.route53_query_logging_config
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                   | Description |
| ------------------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| cloud_watch_logs_log_group_arn | core | string     | The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to. |
| hosted_zone_id                 | core | string     | The ID of the hosted zone that CloudWatch Logs is logging queries for.                                      |
| id                             | core | string     | The ID for a configuration for DNS query logging.                                                           |
| query_logging_config_arn       | core | string     |
| tags                           | core | hstore_csv |
