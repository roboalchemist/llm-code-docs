# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.pipes_pipe.dataset.md

---
title: EventBridge Pipe
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Pipe
---

# EventBridge Pipe

EventBridge Pipe is an AWS resource that connects event sources to targets with optional filtering, enrichment, and transformation. It allows you to build event-driven integrations without writing custom code, simplifying the process of routing data between services. Pipes provide a managed way to reliably move events from producers to consumers while applying business logic inline.

```
aws.pipes_pipe
```

## Fields

| Title              | ID   | Type       | Data Type                                                                      | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The ARN of the pipe.                                                           |
| creation_time      | core | timestamp  | The time the pipe was created.                                                 |
| current_state      | core | string     | The state the pipe is in.                                                      |
| desired_state      | core | string     | The state the pipe should be in.                                               |
| enrichment         | core | string     | The ARN of the enrichment resource.                                            |
| last_modified_time | core | timestamp  | When the pipe was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD). |
| name               | core | string     | The name of the pipe.                                                          |
| state_reason       | core | string     | The reason the pipe is in its current state.                                   |
| tags               | core | hstore_csv |
| target             | core | string     | The ARN of the target resource.                                                |
