# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_routing_profile.dataset.md

---
title: Connect Routing Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Routing Profile
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.connect_routing_profile.dataset/index.html
---

# Connect Routing Profile

An AWS Connect Routing Profile defines how incoming contacts are routed to agents within an Amazon Connect contact center. It specifies queues, priority levels, and routing behaviors to ensure that customer interactions are directed to the most suitable available agent. This helps optimize agent utilization and improve customer experience.

```
aws.connect_routing_profile
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                              | Description |
| --------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| agent_availability_timer    | core | string        | Whether agents with this routing profile will have their routing order calculated based on time since their last inbound contact or longest idle time. |
| associated_queue_ids        | core | array<string> | The IDs of the associated queue.                                                                                                                       |
| default_outbound_queue_id   | core | string        | The identifier of the default outbound queue for this routing profile.                                                                                 |
| description                 | core | string        | The description of the routing profile.                                                                                                                |
| instance_id                 | core | string        | The identifier of the Amazon Connect instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.                         |
| is_default                  | core | bool          | Whether this a default routing profile.                                                                                                                |
| last_modified_region        | core | string        | The Amazon Web Services Region where this resource was last modified.                                                                                  |
| last_modified_time          | core | timestamp     | The timestamp when this resource was last modified.                                                                                                    |
| media_concurrencies         | core | json          | The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.                                                            |
| name                        | core | string        | The name of the routing profile.                                                                                                                       |
| number_of_associated_queues | core | int64         | The number of associated queues in routing profile.                                                                                                    |
| number_of_associated_users  | core | int64         | The number of associated users in routing profile.                                                                                                     |
| routing_profile_arn         | core | string        | The Amazon Resource Name (ARN) of the routing profile.                                                                                                 |
| routing_profile_id          | core | string        | The identifier of the routing profile.                                                                                                                 |
| tags                        | core | hstore        |
