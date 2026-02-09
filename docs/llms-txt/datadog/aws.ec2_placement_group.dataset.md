# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_placement_group.dataset.md

---
title: EC2 Placement Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Placement Group
---

# EC2 Placement Group

An EC2 Placement Group is a logical grouping of Amazon EC2 instances that influences how they are placed on underlying hardware. It helps optimize performance or availability depending on the chosen strategy: Cluster for low-latency and high-throughput workloads, Spread for distributing instances across hardware to reduce correlated failures, and Partition for isolating groups of instances across partitions.

```
aws.ec2_placement_group
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                           | Description |
| --------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| group_arn       | core | string     | The Amazon Resource Name (ARN) of the placement group.                                              |
| group_id        | core | string     | The ID of the placement group.                                                                      |
| group_name      | core | string     | The name of the placement group.                                                                    |
| partition_count | core | int64      | The number of partitions. Valid only if strategy is set to partition.                               |
| spread_level    | core | string     | The spread level for the placement group. Only Outpost placement groups can be spread across hosts. |
| state           | core | string     | The state of the placement group.                                                                   |
| strategy        | core | string     | The placement strategy.                                                                             |
| tags            | core | hstore_csv |
