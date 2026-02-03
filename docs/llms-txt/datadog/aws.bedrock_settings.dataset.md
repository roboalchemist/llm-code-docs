# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_settings.dataset.md

---
title: Bedrock Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Settings
---

# Bedrock Settings

This table represents the Bedrock Settings resource from Amazon Web Services.

```
aws.bedrock_settings
```

## Fields

| Title                           | ID   | Type       | Data Type                                           | Description |
| ------------------------------- | ---- | ---------- | --------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| cloud_watch_config              | core | json       | CloudWatch logging configuration.                   |
| embedding_data_delivery_enabled | core | bool       | Set to include embeddings data in the log delivery. |
| image_data_delivery_enabled     | core | bool       | Set to include image data in the log delivery.      |
| s3_config                       | core | json       | S3 configuration for storing log data.              |
| tags                            | core | hstore_csv |
| text_data_delivery_enabled      | core | bool       | Set to include text data in the log delivery.       |
| video_data_delivery_enabled     | core | bool       | Set to include video data in the log delivery.      |
