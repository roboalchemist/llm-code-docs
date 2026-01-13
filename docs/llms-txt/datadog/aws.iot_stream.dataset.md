# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_stream.dataset.md

---
title: IoT Stream
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Stream
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iot_stream.dataset/index.html
---

# IoT Stream

IoT Stream in AWS refers to an IoT data stream resource that delivers continuous data from connected devices. Using the DescribeStreamResponse, you can retrieve details about a specific stream, such as its ARN, ID, status, and associated shards. This helps manage and monitor how IoT device data is ingested and processed in real time.

```
aws.iot_stream
```

## Fields

| Title           | ID   | Type      | Data Type                                        | Description |
| --------------- | ---- | --------- | ------------------------------------------------ | ----------- |
| _key            | core | string    |
| account_id      | core | string    |
| created_at      | core | timestamp | The date when the stream was created.            |
| description     | core | string    | The description of the stream.                   |
| files           | core | json      | The files to stream.                             |
| last_updated_at | core | timestamp | The date when the stream was last updated.       |
| role_arn        | core | string    | An IAM role IoT assumes to access your S3 files. |
| stream_arn      | core | string    | The stream ARN.                                  |
| stream_id       | core | string    | The stream ID.                                   |
| stream_version  | core | int64     | The stream version.                              |
| tags            | core | hstore    |
