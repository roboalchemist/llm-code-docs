# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_pool.dataset.md

---
title: WorkSpaces Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > WorkSpaces Pool
---

# WorkSpaces Pool

WorkSpaces Pool in AWS is a resource that manages a collection of pre-provisioned WorkSpaces that can be quickly assigned to users on demand. It helps reduce provisioning time and optimize costs by maintaining a pool of ready-to-use virtual desktops. The pool automatically scales based on usage patterns and policies, ensuring users get fast access while minimizing idle resources.

```
aws.workspaces_pool
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                  | Description |
| -------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| application_settings | core | json       | The persistent application settings for users of the pool.                                                                                                                                                                                                                                                                 |
| bundle_id            | core | string     | The identifier of the bundle used by the pool.                                                                                                                                                                                                                                                                             |
| capacity_status      | core | json       | The capacity status for the pool                                                                                                                                                                                                                                                                                           |
| created_at           | core | timestamp  | The time the pool was created.                                                                                                                                                                                                                                                                                             |
| description          | core | string     | The description of the pool.                                                                                                                                                                                                                                                                                               |
| directory_id         | core | string     | The identifier of the directory used by the pool.                                                                                                                                                                                                                                                                          |
| errors               | core | json       | The pool errors.                                                                                                                                                                                                                                                                                                           |
| pool_arn             | core | string     | The Amazon Resource Name (ARN) for the pool.                                                                                                                                                                                                                                                                               |
| pool_id              | core | string     | The identifier of a pool.                                                                                                                                                                                                                                                                                                  |
| pool_name            | core | string     | The name of the pool.                                                                                                                                                                                                                                                                                                      |
| state                | core | string     | The current state of the pool.                                                                                                                                                                                                                                                                                             |
| tags                 | core | hstore_csv |
| timeout_settings     | core | json       | The amount of time that a pool session remains active after users disconnect. If they try to reconnect to the pool session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new pool instance. |
