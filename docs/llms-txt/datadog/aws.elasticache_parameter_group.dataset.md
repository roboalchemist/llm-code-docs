# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elasticache_parameter_group.dataset.md

---
title: ElastiCache Parameter Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ElastiCache Parameter Group
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.elasticache_parameter_group.dataset/index.html
---

# ElastiCache Parameter Group

This table represents the ElastiCache Parameter Group resource from Amazon Web Services.

```
aws.elasticache_parameter_group
```

## Fields

| Title                        | ID   | Type   | Data Type                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ---------------------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string |
| account_id                   | core | string |
| arn                          | core | string | The ARN (Amazon Resource Name) of the cache parameter group.                                                                                                                                                                                                                                                                                                               |
| cache_parameter_group_family | core | string | The name of the cache parameter group family that this cache parameter group is compatible with. Valid values are: <code>memcached1.4</code> | <code>memcached1.5</code> | <code>memcached1.6</code> | <code>redis2.6</code> | <code>redis2.8</code> | <code>redis3.2</code> | <code>redis4.0</code> | <code>redis5.0</code> | <code>redis6.x</code> | <code>redis7</code> |
| cache_parameter_group_name   | core | string | The name of the cache parameter group.                                                                                                                                                                                                                                                                                                                                     |
| description                  | core | string | The description for this cache parameter group.                                                                                                                                                                                                                                                                                                                            |
| is_global                    | core | bool   | Indicates whether the parameter group is associated with a Global datastore                                                                                                                                                                                                                                                                                                |
| tags                         | core | hstore |
