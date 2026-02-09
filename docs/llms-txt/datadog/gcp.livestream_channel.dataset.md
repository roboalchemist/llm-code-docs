# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.livestream_channel.dataset.md

---
title: Livestream Channel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Livestream Channel
---

# Livestream Channel

A Livestream Channel in Google Cloud is a managed resource that enables real-time video streaming. It handles live video ingestion, transcoding, packaging, and delivery to viewers through adaptive bitrate streaming. The service integrates with Cloud Storage and CDN for scalable and reliable distribution, supporting various input protocols and output formats for different devices.

```
gcp.livestream_channel
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| active_input         | core | string        | Output only. The InputAttachment.key that serves as the current input source. The first input in the input_attachments is the initial input source.                                |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation time.                                                                                                                                                    |
| datadog_display_name | core | string        |
| elementary_streams   | core | json          | List of elementary streams.                                                                                                                                                        |
| encryptions          | core | json          | Optional. Encryption configurations for this channel. Each configuration has an ID which is referred to by each MuxStream to indicate which configuration is used for that output. |
| input_attachments    | core | json          | A list of input attachments that this channel uses. One channel can have multiple inputs as the input sources. Only one input can be selected as the input source at one time.     |
| input_config         | core | json          | The configuration for input sources defined in input_attachments.                                                                                                                  |
| labels               | core | array<string> | User-defined key/value metadata.                                                                                                                                                   |
| log_config           | core | json          | Configuration of platform logs for this channel.                                                                                                                                   |
| manifests            | core | json          | List of output manifests.                                                                                                                                                          |
| mux_streams          | core | json          | List of multiplexing settings for output streams.                                                                                                                                  |
| name                 | core | string        | The resource name of the channel, in the form of: `projects/{project}/locations/{location}/channels/{channelId}`.                                                                  |
| organization_id      | core | string        |
| output               | core | json          | Required. Information about the output (that is, the Cloud Storage bucket to store the generated live stream).                                                                     |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| retention_config     | core | json          | Optional. Configuration for retention of output files for this channel.                                                                                                            |
| sprite_sheets        | core | json          | List of output sprite sheets.                                                                                                                                                      |
| static_overlays      | core | json          | Optional. List of static overlay images. Those images display over the output content for the whole duration of the live stream.                                                   |
| streaming_error      | core | json          | Output only. A description of the reason for the streaming error. This property is always present when streaming_state is STREAMING_ERROR.                                         |
| streaming_state      | core | string        | Output only. State of the streaming operation.                                                                                                                                     |
| tags                 | core | hstore_csv    |
| timecode_config      | core | json          | Configuration of timecode for this channel.                                                                                                                                        |
| update_time          | core | timestamp     | Output only. The update time.                                                                                                                                                      |
| zone_id              | core | string        |
