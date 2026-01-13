# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dms_data_migration.dataset.md

---
title: Database Migration Service Data Migration Task
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Database Migration Service Data
  Migration Task
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.dms_data_migration.dataset/index.html
---

# Database Migration Service Data Migration Task

An AWS Database Migration Service Data Migration Task defines the actual migration job that moves data between a source and target database. It specifies details such as the migration type (full load, ongoing replication, or both), the mapping of tables, and transformation rules. This task runs within a replication instance and manages the flow of data, ensuring that databases are synchronized with minimal downtime during migration.

```
aws.dms_data_migration
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                 | Description |
| -------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string        |
| account_id                 | core | string        |
| data_migration_arn         | core | string        | The Amazon Resource Name (ARN) that identifies this replication.                                                          |
| data_migration_cidr_blocks | core | array<string> | The CIDR blocks of the endpoints for the data migration.                                                                  |
| data_migration_create_time | core | timestamp     | The UTC time when DMS created the data migration.                                                                         |
| data_migration_end_time    | core | timestamp     | The UTC time when data migration ended.                                                                                   |
| data_migration_name        | core | string        | The user-friendly name for the data migration.                                                                            |
| data_migration_settings    | core | json          | Specifies CloudWatch settings and selection rules for the data migration.                                                 |
| data_migration_start_time  | core | timestamp     | The UTC time when DMS started the data migration.                                                                         |
| data_migration_statistics  | core | json          | Provides information about the data migration's run, including start and stop time, latency, and data migration progress. |
| data_migration_status      | core | string        | The current status of the data migration.                                                                                 |
| data_migration_type        | core | string        | Specifies whether the data migration is full-load only, change data capture (CDC) only, or full-load and CDC.             |
| last_failure_message       | core | string        | Information about the data migration's most recent error or failure.                                                      |
| migration_project_arn      | core | string        | The Amazon Resource Name (ARN) of the data migration's associated migration project.                                      |
| public_ip_addresses        | core | array<string> | The IP addresses of the endpoints for the data migration.                                                                 |
| service_access_role_arn    | core | string        | The IAM role that the data migration uses to access Amazon Web Services resources.                                        |
| source_data_settings       | core | json          | Specifies information about the data migration's source data provider.                                                    |
| stop_reason                | core | string        | The reason the data migration last stopped.                                                                               |
| tags                       | core | hstore        |
| target_data_settings       | core | json          | Specifies information about the data migration's target data provider.                                                    |
