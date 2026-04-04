# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_streaming_distribution.dataset.md

---
title: CloudFront Streaming Distribution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Streaming Distribution
---

# CloudFront Streaming Distribution

CloudFront Streaming Distribution is an Amazon CloudFront resource used to deliver on-demand media content using Adobe Flash Media Server's RTMP protocol. It enables low-latency streaming of video and audio files stored in Amazon S3, allowing users to start playback quickly without downloading the entire file. This distribution type is designed for efficient media delivery but is considered legacy, as most modern use cases now rely on HTTP-based streaming methods.

```
aws.cloudfront_streaming_distribution
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                  | Description |
| ---------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| e_tag                  | core | string     | The current version of the streaming distribution's information. For example: <code>E2QWRUHAPOMQZL</code>. |
| streaming_distribution | core | json       | The streaming distribution's information.                                                                  |
| tags                   | core | hstore_csv |
