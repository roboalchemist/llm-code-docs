# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elasticache_security_group.dataset.md

---
title: ElastiCache Security Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ElastiCache Security Group
---

# ElastiCache Security Group

This table represents the ElastiCache Security Group resource from Amazon Web Services.

```
aws.elasticache_security_group
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                | Description |
| ------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| arn                       | core | string     | The ARN of the cache security group,                                                     |
| cache_security_group_name | core | string     | The name of the cache security group.                                                    |
| description               | core | string     | The description of the cache security group.                                             |
| ec2_security_groups       | core | json       | A list of Amazon EC2 security groups that are associated with this cache security group. |
| owner_id                  | core | string     | The Amazon account ID of the cache security group owner.                                 |
| tags                      | core | hstore_csv |
