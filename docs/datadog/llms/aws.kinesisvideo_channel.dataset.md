# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kinesisvideo_channel.dataset.md

---
title: Kinesis Video Streams Signaling Channel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Kinesis Video Streams Signaling
  Channel
---

# Kinesis Video Streams Signaling Channel

Kinesis Video Streams Signaling Channel is an AWS resource that enables secure, real-time communication between applications using WebRTC. It provides the signaling infrastructure needed for peer-to-peer media streaming, such as video, audio, or data, without requiring a custom signaling service. This resource manages channel creation, configuration, and metadata to support low-latency, interactive streaming use cases like video conferencing, remote monitoring, or IoT device communication.

```
aws.kinesisvideo_channel
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                       | Description |
| --------------------------- | ---- | ---------- | ------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| channel_arn                 | core | string     | The Amazon Resource Name (ARN) of the signaling channel.                        |
| channel_name                | core | string     | The name of the signaling channel.                                              |
| channel_status              | core | string     | Current status of the signaling channel.                                        |
| channel_type                | core | string     | The type of the signaling channel.                                              |
| creation_time               | core | timestamp  | The time at which the signaling channel was created.                            |
| single_master_configuration | core | json       | A structure that contains the configuration for the SINGLE_MASTER channel type. |
| tags                        | core | hstore_csv |
| version                     | core | string     | The current version of the signaling channel.                                   |
