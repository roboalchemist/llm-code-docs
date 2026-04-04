# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.memorydb_user.dataset.md

---
title: MemoryDB User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MemoryDB User
---

# MemoryDB User

MemoryDB User in AWS represents an identity within an Amazon MemoryDB for Redis cluster. It defines authentication and access control settings, including usernames, passwords, and access permissions. This resource allows fine-grained security by controlling which users can connect to the cluster and what actions they can perform.

```
aws.memorydb_user
```

## Fields

| Title                  | ID   | Type          | Data Type                                                              | Description |
| ---------------------- | ---- | ------------- | ---------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| access_string          | core | string        | Access permissions string used for this user.                          |
| account_id             | core | string        |
| acl_names              | core | array<string> | The names of the Access Control Lists to which the user belongs        |
| arn                    | core | string        | The Amazon Resource Name (ARN) of the user.                            |
| authentication         | core | json          | Denotes whether the user requires a password to authenticate.          |
| minimum_engine_version | core | string        | The minimum engine version supported for the user                      |
| name                   | core | string        | The name of the user                                                   |
| status                 | core | string        | Indicates the user status. Can be "active", "modifying" or "deleting". |
| tags                   | core | hstore_csv    |
