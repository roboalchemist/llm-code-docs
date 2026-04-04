# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elasticache_serverless_cache.dataset.md

---
title: ElastiCache Serverless Cache
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ElastiCache Serverless Cache
---

# ElastiCache Serverless Cache

ElastiCache Serverless Cache is a fully managed, serverless caching option in AWS that automatically scales capacity based on application demand. It removes the need to manage nodes or clusters, providing instant availability and high performance for caching workloads. This service is designed to simplify operations, reduce costs, and deliver low-latency access to frequently used data without manual provisioning or scaling.

```
aws.elasticache_serverless_cache
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                                                                                                                        | Description |
| ------------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| account_id               | core | string        |
| arn                      | core | string        | The Amazon Resource Name (ARN) of the serverless cache.                                                                                                                                                                                                          |
| cache_usage_limits       | core | json          | The cache usage limit for the serverless cache.                                                                                                                                                                                                                  |
| create_time              | core | timestamp     | When the serverless cache was created.                                                                                                                                                                                                                           |
| daily_snapshot_time      | core | string        | The daily time that a cache snapshot will be created. Default is NULL, i.e. snapshots will not be created at a specific time on a daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.                                                    |
| description              | core | string        | A description of the serverless cache.                                                                                                                                                                                                                           |
| endpoint                 | core | json          | Represents the information required for client programs to connect to a cache node. This value is read-only.                                                                                                                                                     |
| engine                   | core | string        | The engine the serverless cache is compatible with.                                                                                                                                                                                                              |
| full_engine_version      | core | string        | The name and version number of the engine the serverless cache is compatible with.                                                                                                                                                                               |
| kms_key_id               | core | string        | The ID of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt data at rest in the serverless cache.                                                                                                                                 |
| major_engine_version     | core | string        | The version number of the engine the serverless cache is compatible with.                                                                                                                                                                                        |
| reader_endpoint          | core | json          | Represents the information required for client programs to connect to a cache node. This value is read-only.                                                                                                                                                     |
| security_group_ids       | core | array<string> | The IDs of the EC2 security groups associated with the serverless cache.                                                                                                                                                                                         |
| serverless_cache_name    | core | string        | The unique identifier of the serverless cache.                                                                                                                                                                                                                   |
| snapshot_retention_limit | core | int64         | The current setting for the number of serverless cache snapshots the system will retain. Available for Valkey, Redis OSS and Serverless Memcached only.                                                                                                          |
| status                   | core | string        | The current status of the serverless cache. The allowed values are CREATING, AVAILABLE, DELETING, CREATE-FAILED and MODIFYING.                                                                                                                                   |
| subnet_ids               | core | array<string> | If no subnet IDs are given and your VPC is in us-west-1, then ElastiCache will select 2 default subnets across AZs in your VPC. For all other Regions, if no subnet IDs are given then ElastiCache will select 3 default subnets across AZs in your default VPC. |
| tags                     | core | hstore_csv    |
| user_group_id            | core | string        | The identifier of the user group associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.                                                                                                                                 |
