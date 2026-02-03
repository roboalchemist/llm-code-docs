# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.memorydb_parameter_group.dataset.md

---
title: MemoryDB Parameter Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MemoryDB Parameter Group
---

# MemoryDB Parameter Group

A MemoryDB Parameter Group in AWS is a collection of configuration settings that define the runtime behavior of MemoryDB clusters. It acts like a container for engine parameters, allowing you to customize aspects such as memory management, eviction policies, and other Redis-related settings. By applying a parameter group to a cluster, you can fine-tune performance and behavior without modifying the underlying infrastructure.

```
aws.memorydb_parameter_group
```

## Fields

| Title       | ID   | Type       | Data Type                                                                            | Description |
| ----------- | ---- | ---------- | ------------------------------------------------------------------------------------ | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| arn         | core | string     | The Amazon Resource Name (ARN) of the parameter group                                |
| description | core | string     | A description of the parameter group                                                 |
| family      | core | string     | The name of the parameter group family that this parameter group is compatible with. |
| name        | core | string     | The name of the parameter group                                                      |
| tags        | core | hstore_csv |
