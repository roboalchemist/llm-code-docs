# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elasticache_subnet_group.dataset.md

---
title: ElastiCache Subnet Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ElastiCache Subnet Group
---

# ElastiCache Subnet Group

This table represents the ElastiCache Subnet Group resource from Amazon Web Services.

```
aws.elasticache_subnet_group
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                         | Description |
| ------------------------------ | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string        |
| account_id                     | core | string        |
| arn                            | core | string        | The ARN (Amazon Resource Name) of the cache subnet group.                                                                                                                                                                                                                                                         |
| cache_subnet_group_description | core | string        | The description of the cache subnet group.                                                                                                                                                                                                                                                                        |
| cache_subnet_group_name        | core | string        | The name of the cache subnet group.                                                                                                                                                                                                                                                                               |
| subnets                        | core | json          | A list of subnets associated with the cache subnet group.                                                                                                                                                                                                                                                         |
| supported_network_types        | core | array<string> | Either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 and above or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>. |
| tags                           | core | hstore_csv    |
| vpc_id                         | core | string        | The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.                                                                                                                                                                                                                                   |
