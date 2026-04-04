# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.keyspaces_keyspace.dataset.md

---
title: Keyspaces Keyspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Keyspaces Keyspace
---

# Keyspaces Keyspace

Keyspaces Keyspace in AWS is a managed Apache Cassandraâcompatible database resource. It provides a scalable, highly available, and serverless keyspace that organizes tables and data within Amazon Keyspaces. This resource allows you to define logical groupings of tables, manage replication settings, and leverage the performance and security features of AWS without managing infrastructure.

```
aws.keyspaces_keyspace
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| account_id           | core | string        |
| keyspace_name        | core | string        | The name of the keyspace.                                                                                                                             |
| replication_regions  | core | array<string> | If the replicationStrategy of the keyspace is MULTI_REGION, a list of replication Regions is returned.                                                |
| replication_strategy | core | string        | This property specifies if a keyspace is a single Region keyspace or a multi-Region keyspace. The available values are SINGLE_REGION or MULTI_REGION. |
| resource_arn         | core | string        | The unique identifier of the keyspace in the format of an Amazon Resource Name (ARN).                                                                 |
| tags                 | core | hstore_csv    |
