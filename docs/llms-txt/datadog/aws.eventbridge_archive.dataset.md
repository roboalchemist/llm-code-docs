# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eventbridge_archive.dataset.md

---
title: EventBridge Archive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Archive
---

# EventBridge Archive

EventBridge Archive is an AWS resource that allows you to store and retain events published to EventBridge event buses. It enables you to capture all or filtered subsets of events for long-term storage, replay, and auditing. This helps in troubleshooting, compliance, and reprocessing use cases by letting you replay archived events back into an event bus at any time.

```
aws.eventbridge_archive
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                      | Description |
| ---------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| archive_name     | core | string     | The name of the archive.                                                                                       |
| creation_time    | core | timestamp  | The time stamp for the time that the archive was created.                                                      |
| event_count      | core | int64      | The number of events in the archive.                                                                           |
| event_source_arn | core | string     | The ARN of the event bus associated with the archive. Only events from this event bus are sent to the archive. |
| retention_days   | core | int64      | The number of days to retain events in the archive before they are deleted.                                    |
| size_bytes       | core | int64      | The size of the archive, in bytes.                                                                             |
| state            | core | string     | The current state of the archive.                                                                              |
| state_reason     | core | string     | A description for the reason that the archive is in the current state.                                         |
| tags             | core | hstore_csv |
