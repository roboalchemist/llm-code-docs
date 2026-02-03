# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elasticache_user.dataset.md

---
title: ElastiCache User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ElastiCache User
---

# ElastiCache User

ElastiCache User in AWS represents an identity within Amazon ElastiCache that allows you to manage authentication and access control for Redis clusters using Role-Based Access Control (RBAC). It defines user credentials, access permissions, and associated user groups, enabling fine-grained security management for multi-tenant or shared environments.

```
aws.elasticache_user
```

## Fields

| Title                  | ID   | Type          | Data Type                                                              | Description |
| ---------------------- | ---- | ------------- | ---------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| access_string          | core | string        | Access permissions string used for this user.                          |
| account_id             | core | string        |
| arn                    | core | string        | The Amazon Resource Name (ARN) of the user.                            |
| authentication         | core | json          | Denotes whether the user requires a password to authenticate.          |
| engine                 | core | string        | The options are valkey or redis.                                       |
| minimum_engine_version | core | string        | The minimum engine version required, which is Redis OSS 6.0            |
| status                 | core | string        | Indicates the user status. Can be "active", "modifying" or "deleting". |
| tags                   | core | hstore_csv    |
| user_group_ids         | core | array<string> | Returns a list of the user group IDs the user belongs to.              |
| user_id                | core | string        | The ID of the user.                                                    |
| user_name              | core | string        | The username of the user.                                              |
