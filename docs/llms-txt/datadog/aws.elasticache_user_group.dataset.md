# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elasticache_user_group.dataset.md

---
title: ElastiCache User Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ElastiCache User Group
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.elasticache_user_group.dataset/index.html
---

# ElastiCache User Group

ElastiCache User Group in AWS is a resource that allows you to manage groups of users for Redis authentication and access control. It simplifies permission management by letting you assign multiple users to a group and then associate that group with one or more Redis clusters. This helps enforce consistent access policies and improves security by centralizing user management.

```
aws.elasticache_user_group
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                     | Description |
| ---------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| arn                    | core | string        | The Amazon Resource Name (ARN) of the user group.                                                                                             |
| engine                 | core | string        | The options are valkey or redis.                                                                                                              |
| minimum_engine_version | core | string        | The minimum engine version required, which is Redis OSS 6.0                                                                                   |
| pending_changes        | core | json          | A list of updates being applied to the user group.                                                                                            |
| replication_groups     | core | array<string> | A list of replication groups that the user group can access.                                                                                  |
| serverless_caches      | core | array<string> | Indicates which serverless caches the specified user group is associated with. Available for Valkey, Redis OSS and Serverless Memcached only. |
| status                 | core | string        | Indicates user group status. Can be "creating", "active", "modifying", "deleting".                                                            |
| tags                   | core | hstore        |
| user_group_id          | core | string        | The ID of the user group.                                                                                                                     |
| user_ids               | core | array<string> | The list of user IDs that belong to the user group.                                                                                           |
