# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_v2_origin_endpoint.dataset.md

---
title: Mediapackage V2 Origin Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediapackage V2 Origin Endpoint
---

# Mediapackage V2 Origin Endpoint

This table represents the mediapackage_v2_origin_endpoint resource from Amazon Web Services.

```
aws.mediapackage_v2_origin_endpoint
```

## Fields

| Title                              | ID   | Type       | Data Type                                                                                                                                                                                     | Description |
| ---------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string     |
| account_id                         | core | string     |
| arn                                | core | string     | The Amazon Resource Name (ARN) associated with the resource.                                                                                                                                  |
| channel_group_name                 | core | string     | The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.                                   |
| channel_name                       | core | string     | The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.                             |
| container_type                     | core | string     | The type of container attached to this origin endpoint.                                                                                                                                       |
| created_at                         | core | timestamp  | The date and time the origin endpoint was created.                                                                                                                                            |
| dash_manifests                     | core | json       | A DASH manifest configuration.                                                                                                                                                                |
| description                        | core | string     | The description for your origin endpoint.                                                                                                                                                     |
| e_tag                              | core | string     | The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.                                                    |
| force_endpoint_error_configuration | core | json       | The failover settings for the endpoint.                                                                                                                                                       |
| hls_manifests                      | core | json       | An HTTP live streaming (HLS) manifest configuration.                                                                                                                                          |
| low_latency_hls_manifests          | core | json       | A low-latency HLS manifest configuration.                                                                                                                                                     |
| modified_at                        | core | timestamp  | The date and time the origin endpoint was modified.                                                                                                                                           |
| mss_manifests                      | core | json       | The Microsoft Smooth Streaming (MSS) manifest configurations associated with this origin endpoint.                                                                                            |
| origin_endpoint_name               | core | string     | The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.               |
| policy                             | core | string     | The policy assigned to the origin endpoint.                                                                                                                                                   |
| reset_at                           | core | timestamp  | The time that the origin endpoint was last reset.                                                                                                                                             |
| segment                            | core | json       |
| startover_window_seconds           | core | int64      | The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. |
| tags                               | core | hstore_csv |
