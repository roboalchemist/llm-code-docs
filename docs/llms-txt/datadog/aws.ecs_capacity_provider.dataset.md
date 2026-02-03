# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ecs_capacity_provider.dataset.md

---
title: ECS Capacity Provider
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ECS Capacity Provider
---

# ECS Capacity Provider

An ECS Capacity Provider in AWS defines how Amazon ECS manages the capacity of compute resources for running tasks. It allows you to associate an ECS cluster with either EC2 Auto Scaling groups or Fargate, enabling flexible scaling and placement strategies. Capacity providers help balance workloads, optimize costs, and ensure that tasks have the required infrastructure available.

```
aws.ecs_capacity_provider
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| --------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| auto_scaling_group_provider | core | json       | The Auto Scaling group settings for the capacity provider.                                                                                                                                                                                                                                                                                                                                                       |
| capacity_provider_arn       | core | string     | The Amazon Resource Name (ARN) that identifies the capacity provider.                                                                                                                                                                                                                                                                                                                                            |
| name                        | core | string     | The name of the capacity provider.                                                                                                                                                                                                                                                                                                                                                                               |
| status                      | core | string     | The current status of the capacity provider. Only capacity providers in an ACTIVE state can be used in a cluster. When a capacity provider is successfully deleted, it has an INACTIVE status.                                                                                                                                                                                                                   |
| tags                        | core | hstore_csv |
| update_status               | core | string     | The update status of the capacity provider. The following are the possible states that is returned. DELETE_IN_PROGRESS The capacity provider is in the process of being deleted. DELETE_COMPLETE The capacity provider was successfully deleted and has an INACTIVE status. DELETE_FAILED The capacity provider can't be deleted. The update status reason provides further details about why the delete failed. |
| update_status_reason        | core | string     | The update status reason. This provides further details about the update status for the capacity provider.                                                                                                                                                                                                                                                                                                       |
