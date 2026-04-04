# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_channel.dataset.md

---
title: Elemental MediaLive Channel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaLive Channel
---

# Elemental MediaLive Channel

AWS Elemental MediaLive Channel is a resource that represents a live video channel used to encode and deliver real-time video streams. It ingests live video from sources, processes it into multiple formats and bitrates, and outputs it for distribution to viewers across devices. This service is commonly used for live events, streaming platforms, and broadcast workflows, providing high availability and scalability for professional-grade live video delivery.

```
aws.medialive_channel
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                               | Description |
| ---------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| anywhere_settings            | core | json       | AnywhereSettings settings for this channel.                                                                                                                             |
| arn                          | core | string     | The unique arn of the channel.                                                                                                                                          |
| cdi_input_specification      | core | json       | Specification of CDI inputs for this channel                                                                                                                            |
| channel_class                | core | string     | The class for this channel. STANDARD for a channel with two pipelines or SINGLE_PIPELINE for a channel with one pipeline.                                               |
| channel_engine_version       | core | json       | The engine version that you requested for this channel.                                                                                                                 |
| destinations                 | core | json       | A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager. |
| egress_endpoints             | core | json       | The endpoints where outgoing connections initiate from                                                                                                                  |
| id                           | core | string     | The unique id of the channel.                                                                                                                                           |
| input_attachments            | core | json       | List of input attachments for channel.                                                                                                                                  |
| input_specification          | core | json       | Specification of network and file inputs for this channel                                                                                                               |
| log_level                    | core | string     | The log level being written to CloudWatch Logs.                                                                                                                         |
| maintenance                  | core | json       | Maintenance settings for this channel.                                                                                                                                  |
| name                         | core | string     | The name of the channel. (user-mutable)                                                                                                                                 |
| pipelines_running_count      | core | int64      | The number of currently healthy pipelines.                                                                                                                              |
| role_arn                     | core | string     | The Amazon Resource Name (ARN) of the role assumed when running the Channel.                                                                                            |
| state                        | core | string     | Placeholder documentation for ChannelState                                                                                                                              |
| tags                         | core | hstore_csv |
| used_channel_engine_versions | core | json       | The engine version that the running pipelines are using.                                                                                                                |
| vpc                          | core | json       | Settings for any VPC outputs.                                                                                                                                           |
