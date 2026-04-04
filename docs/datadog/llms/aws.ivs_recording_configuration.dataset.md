# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_recording_configuration.dataset.md

---
title: IVS Recording Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IVS Recording Configuration
---

# IVS Recording Configuration

IVS Recording Configuration in AWS defines how Amazon Interactive Video Service (IVS) records live streams. It specifies settings such as the destination storage location in Amazon S3, thumbnail generation options, and recording behavior. This configuration allows you to control how live video content is captured, stored, and made available for playback or further processing.

```
aws.ivs_recording_configuration
```

## Fields

| Title                              | ID   | Type       | Data Type                                                                                                                                                                       | Description |
| ---------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string     |
| account_id                         | core | string     |
| arn                                | core | string     | Recording-configuration ARN.                                                                                                                                                    |
| destination_configuration          | core | json       | A complex type that contains information about where recorded video will be stored.                                                                                             |
| name                               | core | string     | Recording-configuration name. The value does not need to be unique.                                                                                                             |
| recording_reconnect_window_seconds | core | int64      | If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0.       |
| rendition_configuration            | core | json       | Object that describes which renditions should be recorded for a stream.                                                                                                         |
| state                              | core | string     | Indicates the current state of the recording configuration. When the state is ACTIVE, the configuration is ready for recording a channel stream.                                |
| tags                               | core | hstore_csv |
| thumbnail_configuration            | core | json       | A complex type that allows you to enable/disable the recording of thumbnails for a live session and modify the interval at which thumbnails are generated for the live session. |
