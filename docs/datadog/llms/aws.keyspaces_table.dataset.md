# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.keyspaces_table.dataset.md

---
title: Keyspaces Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Keyspaces Table
---

# Keyspaces Table

An AWS Keyspaces Table is a managed, serverless Apache Cassandraâcompatible table that lets you store and query wide-column data at scale. It automatically handles replication, scaling, and availability across multiple AWS Availability Zones. You can define schema, set throughput capacity modes, and configure encryption and point-in-time recovery. This service removes the need to manage Cassandra clusters while providing familiar APIs and query language support.

```
aws.keyspaces_table
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                       | Description |
| ------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| capacity_specification   | core | json       | The read/write throughput capacity mode for a table. The options are: throughputMode:PAY_PER_REQUEST throughputMode:PROVISIONED |
| client_side_timestamps   | core | json       | The client-side timestamps setting of the table.                                                                                |
| comment                  | core | json       | The the description of the specified table.                                                                                     |
| creation_timestamp       | core | timestamp  | The creation timestamp of the specified table.                                                                                  |
| default_time_to_live     | core | int64      | The default Time to Live settings in seconds of the specified table.                                                            |
| encryption_specification | core | json       | The encryption settings of the specified table.                                                                                 |
| keyspace_name            | core | string     | The name of the keyspace that the specified table is stored in.                                                                 |
| point_in_time_recovery   | core | json       | The point-in-time recovery status of the specified table.                                                                       |
| replica_specifications   | core | json       | Returns the Amazon Web Services Region specific settings of all Regions a multi-Region table is replicated in.                  |
| resource_arn             | core | string     | The Amazon Resource Name (ARN) of the specified table.                                                                          |
| schema_definition        | core | json       | The schema definition of the specified table.                                                                                   |
| status                   | core | string     | The current status of the specified table.                                                                                      |
| table_name               | core | string     | The name of the specified table.                                                                                                |
| tags                     | core | hstore_csv |
| ttl                      | core | json       | The custom Time to Live settings of the specified table.                                                                        |
