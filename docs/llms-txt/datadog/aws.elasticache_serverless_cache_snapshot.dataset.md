# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elasticache_serverless_cache_snapshot.dataset.md

---
title: ElastiCache Serverless Cache Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > ElastiCache Serverless Cache
  Snapshot
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.elasticache_serverless_cache_snapshot.dataset/index.html
---

# ElastiCache Serverless Cache Snapshot

An ElastiCache Serverless Cache Snapshot is a point-in-time backup of a serverless cache in Amazon ElastiCache. It allows you to preserve the state of your cache data without managing infrastructure, making it easier to restore or clone environments for recovery, testing, or migration.

```
aws.elasticache_serverless_cache_snapshot
```

## Fields

| Title                          | ID   | Type      | Data Type                                                                                                                                                                      | Description |
| ------------------------------ | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                           | core | string    |
| account_id                     | core | string    |
| arn                            | core | string    | The Amazon Resource Name (ARN) of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.                                                  |
| bytes_used_for_cache           | core | string    | The total size of a serverless cache snapshot, in bytes. Available for Valkey, Redis OSS and Serverless Memcached only.                                                        |
| create_time                    | core | timestamp | The date and time that the source serverless cache's metadata and cache data set was obtained for the snapshot. Available for Valkey, Redis OSS and Serverless Memcached only. |
| expiry_time                    | core | timestamp | The time that the serverless cache snapshot will expire. Available for Valkey, Redis OSS and Serverless Memcached only.                                                        |
| kms_key_id                     | core | string    | The ID of the Amazon Web Services Key Management Service (KMS) key of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.              |
| serverless_cache_configuration | core | json      | The configuration of the serverless cache, at the time the snapshot was taken. Available for Valkey, Redis OSS and Serverless Memcached only.                                  |
| serverless_cache_snapshot_name | core | string    | The identifier of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.                                                                  |
| snapshot_type                  | core | string    | The type of snapshot of serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.                                                                       |
| status                         | core | string    | The current status of the serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.                                                                     |
| tags                           | core | hstore    |
