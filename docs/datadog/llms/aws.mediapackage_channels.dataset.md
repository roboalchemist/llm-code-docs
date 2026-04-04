# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_channels.dataset.md

---
title: Mediapackage Channels
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediapackage Channels
---

# Mediapackage Channels

This table represents the mediapackage_channels resource from Amazon Web Services.

```
aws.mediapackage_channels
```

## Fields

| Title               | ID   | Type       | Data Type                                               | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| arn                 | core | string     | The Amazon Resource Name (ARN) assigned to the Channel. |
| created_at          | core | string     | The date and time the Channel was created.              |
| description         | core | string     | A short text description of the Channel.                |
| egress_access_logs  | core | json       |
| hls_ingest          | core | json       |
| id                  | core | string     | The ID of the Channel.                                  |
| ingress_access_logs | core | json       |
| tags                | core | hstore_csv |
