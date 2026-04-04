# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_channel.dataset.md

---
title: IVS Channel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IVS Channel
---

# IVS Channel

An IVS Channel in AWS is a resource that represents a live video streaming channel using Amazon Interactive Video Service. It defines the configuration for ingesting live video, including settings like latency mode, type, and authorized playback. Channels provide endpoints for streaming input and playback, enabling developers to build interactive, low-latency live video experiences without managing streaming infrastructure.

```
aws.ivs_channel
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                                                                                                                                                                                                             | Description |
| ------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| arn                             | core | string     | Channel ARN.                                                                                                                                                                                                                                                                          |
| authorized                      | core | bool       | Whether the channel is private (enabled for playback authorization). Default: false.                                                                                                                                                                                                  |
| container_format                | core | string     | Indicates which content-packaging format is used (MPEG-TS or fMP4). If multitrackInputConfiguration is specified and enabled is true, then containerFormat is required and must be set to FRAGMENTED_MP4. Otherwise, containerFormat may be set to TS or FRAGMENTED_MP4. Default: TS. |
| ingest_endpoint                 | core | string     | Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.                                                                                                                                                                         |
| insecure_ingest                 | core | bool       | Whether the channel allows insecure RTMP ingest. Default: false.                                                                                                                                                                                                                      |
| latency_mode                    | core | string     | Channel latency mode. Use NORMAL to broadcast and deliver live video up to Full HD. Use LOW for near-real-time interaction with viewers. Default: LOW.                                                                                                                                |
| multitrack_input_configuration  | core | json       | Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.                                                                                                                                                                            |
| name                            | core | string     | Channel name.                                                                                                                                                                                                                                                                         |
| playback_restriction_policy_arn | core | string     | Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. Default: "" (empty string, no playback restriction policy is applied).                                                                                               |
| playback_url                    | core | string     | Channel playback URL.                                                                                                                                                                                                                                                                 |
| preset                          | core | string     | Optional transcode preset for the channel. This is selectable only for ADVANCED_HD and ADVANCED_SD channel types. For those channel types, the default preset is HIGHER_BANDWIDTH_DELIVERY. For other channel types (BASIC and STANDARD), preset is the empty string ("").            |
| recording_configuration_arn     | core | string     | Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. Default: "" (empty string, recording is disabled).                                                                                                                                  |
| srt                             | core | json       | Specifies the endpoint and optional passphrase for streaming with the SRT protocol.                                                                                                                                                                                                   |
| tags                            | core | hstore_csv |
| type                            | core | string     | Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately. Default: STANDARD. For details, see Channel Types.                                                     |
