# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.bigtableadmin_table.dataset.md

---
title: Cloud Bigtable Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Bigtable Table
---

# Cloud Bigtable Table

Cloud Bigtable Table is a scalable, high-performance NoSQL table in Google Cloud Bigtable. It is designed for large analytical and operational workloads, supporting massive datasets with low-latency reads and writes. Tables are automatically sharded across nodes and can handle billions of rows and thousands of columns, making them ideal for time-series data, IoT, financial data, and personalization use cases.

```
gcp.bigtableadmin_table
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                           | Description |
| ----------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| ancestors               | core | array<string> |
| automated_backup_policy | core | json          | If specified, automated backups are enabled for this table. Otherwise, automated backups are disabled.                                                                                                                                                                                              |
| change_stream_config    | core | json          | If specified, enable the change stream on this table. Otherwise, the change stream is disabled and the change stream is not retained.                                                                                                                                                               |
| datadog_display_name    | core | string        |
| deletion_protection     | core | bool          | Set to true to make the table protected against data loss. i.e. deleting the following resources through Admin APIs are prohibited: * The table. * The column families in the table. * The instance containing the table. Note one can still delete the data stored in the table through Data APIs. |
| granularity             | core | string        | Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`.                                                |
| labels                  | core | array<string> |
| name                    | core | string        | The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `STATS_VIEW`, `FULL`                                                                                                      |
| organization_id         | core | string        |
| parent                  | core | string        |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| resource_name           | core | string        |
| restore_info            | core | json          | Output only. If this table was restored from another data source (e.g. a backup), this field will be populated with information about the restore.                                                                                                                                                  |
| stats                   | core | json          | Output only. Only available with STATS_VIEW, this includes summary statistics about the entire table contents. For statistics about a specific column family, see ColumnFamilyStats in the mapped ColumnFamily collection above.                                                                    |
| tags                    | core | hstore_csv    |
| zone_id                 | core | string        |
