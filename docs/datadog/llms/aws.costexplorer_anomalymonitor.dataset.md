# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.costexplorer_anomalymonitor.dataset.md

---
title: Costexplorer Anomaly Monitor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Costexplorer Anomaly Monitor
---

# Costexplorer Anomaly Monitor

This table represents the Costexplorer Anomaly Monitor resource from Amazon Web Services.

```
aws.costexplorer_anomalymonitor
```

## Fields

| Title                   | ID   | Type       | Data Type                                               | Description |
| ----------------------- | ---- | ---------- | ------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| creation_date           | core | string     | The date when the monitor was created.                  |
| dimensional_value_count | core | int64      | The value for evaluated dimensions.                     |
| last_evaluated_date     | core | string     | The date when the monitor last evaluated for anomalies. |
| last_updated_date       | core | string     | The date when the monitor was last updated.             |
| monitor_arn             | core | string     | The Amazon Resource Name (ARN) value.                   |
| monitor_dimension       | core | string     | The dimensions to evaluate.                             |
| monitor_name            | core | string     | The name of the monitor.                                |
| monitor_specification   | core | json       |
| monitor_type            | core | string     | The possible type values.                               |
| tags                    | core | hstore_csv |
