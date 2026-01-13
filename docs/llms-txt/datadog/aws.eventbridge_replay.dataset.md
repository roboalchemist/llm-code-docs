# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eventbridge_replay.dataset.md

---
title: EventBridge Replay
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Replay
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.eventbridge_replay.dataset/index.html
---

# EventBridge Replay

EventBridge Replay in AWS allows you to reprocess past events by replaying them from an archive to event buses or other targets. This is useful for testing, troubleshooting, or recovering from errors by ensuring events are delivered again as if they were new.

```
aws.eventbridge_replay
```

## Fields

| Title                    | ID   | Type      | Data Type                                                                                                                            | Description |
| ------------------------ | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                     | core | string    |
| account_id               | core | string    |
| event_end_time           | core | timestamp | A time stamp for the time to start replaying events. Any event with a creation time prior to the EventEndTime specified is replayed. |
| event_last_replayed_time | core | timestamp | A time stamp for the time that the last event was replayed.                                                                          |
| event_source_arn         | core | string    | The ARN of the archive to replay event from.                                                                                         |
| event_start_time         | core | timestamp | A time stamp for the time to start replaying events. This is determined by the time in the event as described in Time.               |
| replay_end_time          | core | timestamp | A time stamp for the time that the replay completed.                                                                                 |
| replay_name              | core | string    | The name of the replay.                                                                                                              |
| replay_start_time        | core | timestamp | A time stamp for the time that the replay started.                                                                                   |
| state                    | core | string    | The current state of the replay.                                                                                                     |
| state_reason             | core | string    | A description of why the replay is in the current state.                                                                             |
| tags                     | core | hstore    |
