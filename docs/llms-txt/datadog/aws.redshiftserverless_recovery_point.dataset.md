# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshiftserverless_recovery_point.dataset.md

---
title: Redshift Serverless Recovery Point
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Serverless Recovery Point
---

# Redshift Serverless Recovery Point

A Redshift Serverless Recovery Point in AWS represents a saved snapshot of data from a Redshift Serverless workgroup at a specific point in time. It allows you to restore your data to that state in case of accidental changes, failures, or for testing purposes. Recovery points help ensure business continuity and data protection without requiring manual snapshot management.

```
aws.redshiftserverless_recovery_point
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                              | Description |
| -------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| namespace_arn              | core | string     | The Amazon Resource Name (ARN) of the namespace the recovery point is associated with. |
| namespace_name             | core | string     | The name of the namespace the recovery point is associated with.                       |
| recovery_point_create_time | core | timestamp  | The time the recovery point is created.                                                |
| recovery_point_id          | core | string     | The unique identifier of the recovery point.                                           |
| tags                       | core | hstore_csv |
| total_size_in_mega_bytes   | core | float64    | The total size of the data in the recovery point in megabytes.                         |
| workgroup_name             | core | string     | The name of the workgroup the recovery point is associated with.                       |
