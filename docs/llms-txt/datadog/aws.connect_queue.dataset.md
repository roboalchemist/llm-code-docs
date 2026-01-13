# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_queue.dataset.md

---
title: Connect Queue
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Queue
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.connect_queue.dataset/index.html
---

# Connect Queue

Connect Queue in AWS represents a queue within Amazon Connect, which is a cloud-based contact center service. A queue determines how incoming customer contacts are routed to available agents, based on configuration such as priority, routing profiles, and wait time. It helps manage workloads, improve customer experience, and ensure efficient distribution of calls or chats to the right agents.

```
aws.connect_queue
```

## Fields

| Title                  | ID   | Type      | Data Type                                                                             | Description |
| ---------------------- | ---- | --------- | ------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| description            | core | string    | The description of the queue.                                                         |
| hours_of_operation_id  | core | string    | The identifier for the hours of operation.                                            |
| last_modified_region   | core | string    | The Amazon Web Services Region where this resource was last modified.                 |
| last_modified_time     | core | timestamp | The timestamp when this resource was last modified.                                   |
| max_contacts           | core | int64     | The maximum number of contacts that can be in the queue before it is considered full. |
| name                   | core | string    | The name of the queue.                                                                |
| outbound_caller_config | core | json      | The outbound caller ID name, number, and outbound whisper flow.                       |
| outbound_email_config  | core | json      | The outbound email address ID for a specified queue.                                  |
| queue_arn              | core | string    | The Amazon Resource Name (ARN) for the queue.                                         |
| queue_id               | core | string    | The identifier for the queue.                                                         |
| status                 | core | string    | The status of the queue.                                                              |
| tags                   | core | hstore    |
