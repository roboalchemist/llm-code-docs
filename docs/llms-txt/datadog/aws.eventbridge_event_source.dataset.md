# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eventbridge_event_source.dataset.md

---
title: EventBridge Event Source
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Event Source
---

# EventBridge Event Source

An EventBridge Event Source in AWS represents an external or internal service that can publish events into Amazon EventBridge. It defines where events originate, such as AWS services, SaaS applications, or custom applications, enabling event-driven architectures. Event sources feed events into event buses, which can then be routed to targets like Lambda functions, Step Functions, or other AWS services for processing.

```
aws.eventbridge_event_source
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                         | Description |
| --------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| arn             | core | string     | The ARN of the event source.                                                                                                                                                                                                                                                                                                                                      |
| created_by      | core | string     | The name of the partner that created the event source.                                                                                                                                                                                                                                                                                                            |
| creation_time   | core | timestamp  | The date and time the event source was created.                                                                                                                                                                                                                                                                                                                   |
| expiration_time | core | timestamp  | The date and time that the event source will expire, if the Amazon Web Services account doesn't create a matching event bus for it.                                                                                                                                                                                                                               |
| name            | core | string     | The name of the event source.                                                                                                                                                                                                                                                                                                                                     |
| state           | core | string     | The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven't yet created a matching event bus, or that event bus is deactivated. If it is DELETED, you have created a matching event bus, but the event source has since been deleted. |
| tags            | core | hstore_csv |
