# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.memorydb_subnet_group.dataset.md

---
title: MemoryDB Subnet Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MemoryDB Subnet Group
---

# MemoryDB Subnet Group

A MemoryDB Subnet Group in AWS is a collection of subnets within a Virtual Private Cloud (VPC) that you designate for your MemoryDB clusters. It defines the network boundaries where the clusters can be deployed, ensuring they are placed in the specified subnets across different Availability Zones for high availability and fault tolerance.

```
aws.memorydb_subnet_group
```

## Fields

| Title       | ID   | Type       | Data Type                                                                 | Description |
| ----------- | ---- | ---------- | ------------------------------------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| arn         | core | string     | The ARN (Amazon Resource Name) of the subnet group.                       |
| description | core | string     | A description of the subnet group                                         |
| name        | core | string     | The name of the subnet group                                              |
| subnets     | core | json       | A list of subnets associated with the subnet group.                       |
| tags        | core | hstore_csv |
| vpc_id      | core | string     | The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group. |
