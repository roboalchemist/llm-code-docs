# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eventbridge_event_bus.dataset.md

---
title: EventBridge Event Bus
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Event Bus
---

# EventBridge Event Bus

An EventBridge Event Bus is a routing layer for events in AWS. It receives events from AWS services, custom applications, or SaaS partners and delivers them to targets like Lambda, Step Functions, or SQS. Event buses help decouple event producers and consumers, enabling scalable, event-driven architectures.

```
aws.eventbridge_event_bus
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                        | Description |
| ------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The ARN of the event bus.                                                                                                        |
| creation_time      | core | timestamp  | The time the event bus was created.                                                                                              |
| description        | core | string     | The event bus description.                                                                                                       |
| last_modified_time | core | timestamp  | The time the event bus was last modified.                                                                                        |
| name               | core | string     | The name of the event bus.                                                                                                       |
| policies           | core | json       |
| policy             | core | string     | The permissions policy of the event bus, describing which other Amazon Web Services accounts can write events to this event bus. |
| tags               | core | hstore_csv |
