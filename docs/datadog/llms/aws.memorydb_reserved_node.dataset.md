# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.memorydb_reserved_node.dataset.md

---
title: MemoryDB Reserved Node
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MemoryDB Reserved Node
---

# MemoryDB Reserved Node

A MemoryDB Reserved Node is a pricing option in Amazon MemoryDB for Redis that allows you to reserve a specific node type for a one- or three-year term. By committing to a reserved node, you can significantly reduce costs compared to on-demand pricing while maintaining the same performance and capacity. This option is ideal for steady-state workloads that require predictable usage of MemoryDB clusters.

```
aws.memorydb_reserved_node
```

## Fields

| Title                      | ID   | Type       | Data Type                                                  | Description |
| -------------------------- | ---- | ---------- | ---------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| arn                        | core | string     | The Amazon Resource Name (ARN) of the reserved node.       |
| duration                   | core | int64      | The duration of the reservation in seconds.                |
| fixed_price                | core | float64    | The fixed price charged for this reserved node.            |
| node_count                 | core | int64      | The number of nodes that have been reserved.               |
| node_type                  | core | string     | The node type for the reserved nodes.                      |
| offering_type              | core | string     | The offering type of this reserved node.                   |
| recurring_charges          | core | json       | The recurring price charged to run this reserved node.     |
| reservation_id             | core | string     | A customer-specified identifier to track this reservation. |
| reserved_nodes_offering_id | core | string     | The ID of the reserved node offering to purchase.          |
| start_time                 | core | timestamp  | The time the reservation started.                          |
| state                      | core | string     | The state of the reserved node.                            |
| tags                       | core | hstore_csv |
