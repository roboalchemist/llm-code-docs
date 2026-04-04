# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediatailor_channel.dataset.md

---
title: AWS Elemental MediaTailor Channel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS Elemental MediaTailor Channel
---

# AWS Elemental MediaTailor Channel

AWS Elemental MediaTailor Channel is a resource that defines a linear streaming channel for delivering video content with server-side ad insertion. It allows you to schedule and assemble live or on-demand content into a continuous stream, manage playback configurations, and integrate personalized ads. This service helps create broadcast-like experiences over the internet while optimizing ad delivery and viewer engagement.

```
aws.mediatailor_channel
```

## Fields

| Title              | ID   | Type          | Data Type                                                                                                                                                                                                                                               | Description |
| ------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string        |
| account_id         | core | string        |
| arn                | core | string        | The ARN of the channel.                                                                                                                                                                                                                                 |
| audiences          | core | array<string> | The list of audiences defined in channel.                                                                                                                                                                                                               |
| channel_name       | core | string        | The name of the channel.                                                                                                                                                                                                                                |
| channel_state      | core | string        | Returns the state whether the channel is running or not.                                                                                                                                                                                                |
| creation_time      | core | timestamp     | The timestamp of when the channel was created.                                                                                                                                                                                                          |
| filler_slate       | core | json          | The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the LINEAR PlaybackMode. MediaTailor doesn't support filler slate for channels using the LOOP PlaybackMode.                          |
| last_modified_time | core | timestamp     | The timestamp of when the channel was last modified.                                                                                                                                                                                                    |
| log_configuration  | core | json          | The log configuration.                                                                                                                                                                                                                                  |
| outputs            | core | json          | The channel's output properties.                                                                                                                                                                                                                        |
| playback_mode      | core | string        | The type of playback mode for this channel. LINEAR - Programs play back-to-back only once. LOOP - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule. |
| tags               | core | hstore_csv    |
| tier               | core | string        | The tier for this channel. STANDARD tier channels can contain live programs.                                                                                                                                                                            |
