# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_channel.dataset.md

---
title: Elemental MediaPackage Channel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaPackage Channel
---

# Elemental MediaPackage Channel

An Elemental MediaPackage Channel is a resource in AWS that defines the input for video content to be ingested and prepared for streaming. It serves as the entry point where live video streams are received, processed, and made available for packaging into different streaming formats. Channels can be paired with endpoints to deliver content securely and reliably to a wide range of devices.

```
aws.mediapackage_channel
```

## Fields

| Title               | ID   | Type       | Data Type                                                   | Description |
| ------------------- | ---- | ---------- | ----------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| arn                 | core | string     | The Amazon Resource Name (ARN) assigned to the Channel.     |
| created_at          | core | string     | The date and time the Channel was created.                  |
| description         | core | string     | A short text description of the Channel.                    |
| egress_access_logs  | core | json       | Configure egress access logging.                            |
| hls_ingest          | core | json       | An HTTP Live Streaming (HLS) ingest resource configuration. |
| id                  | core | string     | The ID of the Channel.                                      |
| ingress_access_logs | core | json       | Configure ingress access logging.                           |
| tags                | core | hstore_csv |
