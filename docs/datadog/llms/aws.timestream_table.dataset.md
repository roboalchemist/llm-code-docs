# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.timestream_table.dataset.md

---
title: Timestream Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Timestream Table
---

# Timestream Table

This table represents the Timestream Table resource from Amazon Web Services.

```
aws.timestream_table
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                                                                                              | Description |
| ------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| arn                             | core | string     | The Amazon Resource Name that uniquely identifies this table.                                                                                                          |
| creation_time                   | core | timestamp  | The time when the Timestream table was created.                                                                                                                        |
| database_name                   | core | string     | The name of the Timestream database that contains this table.                                                                                                          |
| last_updated_time               | core | timestamp  | The time when the Timestream table was last updated.                                                                                                                   |
| magnetic_store_write_properties | core | json       | Contains properties to set on the table when enabling magnetic store writes.                                                                                           |
| retention_properties            | core | json       | The retention duration for the memory store and magnetic store.                                                                                                        |
| schema                          | core | json       | The schema of the table.                                                                                                                                               |
| table_name                      | core | string     | The name of the Timestream table.                                                                                                                                      |
| table_status                    | core | string     | The current state of the table: <ul> <li> <code>DELETING</code> - The table is being deleted. </li> <li> <code>ACTIVE</code> - The table is ready for use. </li> </ul> |
| tags                            | core | hstore_csv |
