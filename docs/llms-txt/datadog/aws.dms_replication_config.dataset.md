# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dms_replication_config.dataset.md

---
title: DMS Replication Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DMS Replication Configuration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.dms_replication_config.dataset/index.html
---

# DMS Replication Configuration

DMS Replication Configuration in AWS defines the settings for a Database Migration Service replication task. It specifies how data is migrated or replicated between source and target databases, including task settings, migration type, and replication instance details. This configuration controls the behavior of ongoing replication or one-time migrations.

```
aws.dms_replication_config
```

## Fields

| Title                          | ID   | Type      | Data Type                                                                                                | Description |
| ------------------------------ | ---- | --------- | -------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string    |
| account_id                     | core | string    |
| compute_config                 | core | json      | Configuration parameters for provisioning an DMS serverless replication.                                 |
| replication_config_arn         | core | string    | The Amazon Resource Name (ARN) of this DMS Serverless replication configuration.                         |
| replication_config_create_time | core | timestamp | The time the serverless replication config was created.                                                  |
| replication_config_identifier  | core | string    | The identifier for the ReplicationConfig associated with the replication.                                |
| replication_config_update_time | core | timestamp | The time the serverless replication config was updated.                                                  |
| replication_settings           | core | string    | Configuration parameters for an DMS serverless replication.                                              |
| replication_type               | core | string    | The type of the replication.                                                                             |
| source_endpoint_arn            | core | string    | The Amazon Resource Name (ARN) of the source endpoint for this DMS serverless replication configuration. |
| supplemental_settings          | core | string    | Additional parameters for an DMS serverless replication.                                                 |
| table_mappings                 | core | string    | Table mappings specified in the replication.                                                             |
| tags                           | core | hstore    |
| target_endpoint_arn            | core | string    | The Amazon Resource Name (ARN) of the target endpoint for this DMS serverless replication configuration. |
