# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kinesisvideo_stream.dataset.md

---
title: Kinesis Video Streams Stream
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Kinesis Video Streams Stream
---

# Kinesis Video Streams Stream

Kinesis Video Streams Stream is an AWS resource that enables you to capture, process, and store video streams for real-time and on-demand access. It securely ingests video from devices, cameras, or other sources and makes it available for playback, analytics, and machine learning applications.

```
aws.kinesisvideo_stream
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                     | Description |
| ----------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| creation_time           | core | timestamp  | A time stamp that indicates when the stream was created.                                                      |
| data_retention_in_hours | core | int64      | How long the stream retains data, in hours.                                                                   |
| device_name             | core | string     | The name of the device that is associated with the stream.                                                    |
| kms_key_id              | core | string     | The ID of the Key Management Service (KMS) key that Kinesis Video Streams uses to encrypt data on the stream. |
| media_type              | core | string     | The MediaType of the stream.                                                                                  |
| status                  | core | string     | The status of the stream.                                                                                     |
| stream_arn              | core | string     | The Amazon Resource Name (ARN) of the stream.                                                                 |
| stream_name             | core | string     | The name of the stream.                                                                                       |
| tags                    | core | hstore_csv |
| version                 | core | string     | The version of the stream.                                                                                    |
