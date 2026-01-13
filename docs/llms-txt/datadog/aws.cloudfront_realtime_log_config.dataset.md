# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_realtime_log_config.dataset.md

---
title: CloudFront Realtime Log Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Realtime Log Config
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_realtime_log_config.dataset/index.html
---

# CloudFront Realtime Log Config

CloudFront Realtime Log Config in AWS defines how CloudFront delivers detailed request logs in near real time. It specifies which data fields to include, the sampling rate, and the destination such as Kinesis Data Streams. This allows you to monitor, analyze, and respond to viewer requests with minimal delay, providing deeper visibility into traffic patterns and performance.

```
aws.cloudfront_realtime_log_config
```

## Fields

| Title         | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                    | Description |
| ------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key          | core | string        |
| account_id    | core | string        |
| arn           | core | string        | The Amazon Resource Name (ARN) of this real-time log configuration.                                                                                                                                                                                                                                          |
| end_points    | core | json          | Contains information about the Amazon Kinesis data stream where you are sending real-time log data for this real-time log configuration.                                                                                                                                                                     |
| fields        | core | array<string> | A list of fields that are included in each real-time log record. In an API response, the fields are provided in the same order in which they are sent to the Amazon Kinesis data stream. For more information about fields, see Real-time log configuration fields in the Amazon CloudFront Developer Guide. |
| name          | core | string        | The unique name of this real-time log configuration.                                                                                                                                                                                                                                                         |
| sampling_rate | core | int64         | The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. The sampling rate is an integer between 1 and 100, inclusive.                                                                         |
| tags          | core | hstore        |
