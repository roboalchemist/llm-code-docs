# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_agent_status.dataset.md

---
title: Connect Agent Status
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Agent Status
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.connect_agent_status.dataset/index.html
---

# Connect Agent Status

Connect Agent Status in AWS provides details about an agent's current status within Amazon Connect. It returns information such as the agent's availability state, custom status configurations, and related metadata. This helps administrators and supervisors monitor agent activity, manage workloads, and ensure efficient contact center operations.

```
aws.connect_agent_status
```

## Fields

| Title                | ID   | Type      | Data Type                                                             | Description |
| -------------------- | ---- | --------- | --------------------------------------------------------------------- | ----------- |
| _key                 | core | string    |
| account_id           | core | string    |
| agent_status_arn     | core | string    | The Amazon Resource Name (ARN) of the agent status.                   |
| agent_status_id      | core | string    | The identifier of the agent status.                                   |
| description          | core | string    | The description of the agent status.                                  |
| display_order        | core | int64     | The display order of the agent status.                                |
| last_modified_region | core | string    | The Amazon Web Services Region where this resource was last modified. |
| last_modified_time   | core | timestamp | The timestamp when this resource was last modified.                   |
| name                 | core | string    | The name of the agent status.                                         |
| state                | core | string    | The state of the agent status.                                        |
| tags                 | core | hstore    |
| type                 | core | string    | The type of agent status.                                             |
