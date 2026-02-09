# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_quick_connect.dataset.md

---
title: Connect Quick Connect
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Quick Connect
---

# Connect Quick Connect

Connect Quick Connect in AWS is a resource within Amazon Connect that provides a shortcut for agents to quickly transfer calls, chats, or tasks to a specific destination. This destination can be another agent, a queue, or an external phone number. It simplifies the agent experience by reducing steps needed to route interactions, improving efficiency and customer service.

```
aws.connect_quick_connect
```

## Fields

| Title                | ID   | Type       | Data Type                                                             | Description |
| -------------------- | ---- | ---------- | --------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| description          | core | string     | The description.                                                      |
| last_modified_region | core | string     | The Amazon Web Services Region where this resource was last modified. |
| last_modified_time   | core | timestamp  | The timestamp when this resource was last modified.                   |
| name                 | core | string     | The name of the quick connect.                                        |
| quick_connect_arn    | core | string     | The Amazon Resource Name (ARN) of the quick connect.                  |
| quick_connect_config | core | json       | Contains information about the quick connect.                         |
| quick_connect_id     | core | string     | The identifier for the quick connect.                                 |
| tags                 | core | hstore_csv |
