# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.livestream_input.dataset.md

---
title: Livestream Input
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Livestream Input
---

# Livestream Input

Livestream Input in Google Cloud is a resource that represents an input endpoint for ingesting live video streams into the Livestream API. It defines how video content is received, including input type, protocol, and security settings. This input can be connected to a channel for processing, transcoding, and delivering live video to viewers.

```
gcp.livestream_input
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                      | Description |
| --------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| create_time           | core | timestamp     | Output only. The creation time.                                                                                                                                                                                                                |
| datadog_display_name  | core | string        |
| input_stream_property | core | json          | Output only. The information for the input stream. This field will be present only when this input receives the input stream.                                                                                                                  |
| labels                | core | array<string> | User-defined key/value metadata.                                                                                                                                                                                                               |
| name                  | core | string        | The resource name of the input, in the form of: `projects/{project}/locations/{location}/inputs/{inputId}`.                                                                                                                                    |
| organization_id       | core | string        |
| parent                | core | string        |
| preprocessing_config  | core | json          | Preprocessing configurations.                                                                                                                                                                                                                  |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| security_rules        | core | json          | Security rule for access control.                                                                                                                                                                                                              |
| tags                  | core | hstore_csv    |
| tier                  | core | string        | Tier defines the maximum input specification that is accepted by the video pipeline. The billing is charged based on the tier specified here. See [Pricing](https://cloud.google.com/livestream/pricing) for more detail. The default is `HD`. |
| type                  | core | string        | Source type.                                                                                                                                                                                                                                   |
| update_time           | core | timestamp     | Output only. The update time.                                                                                                                                                                                                                  |
| uri                   | core | string        | Output only. URI to push the input stream to. Its format depends on the input type, for example: * `RTMP_PUSH`: `rtmp://1.2.3.4/live/{STREAM-ID}` * `SRT_PUSH`: `srt://1.2.3.4:4201?streamid={STREAM-ID}`                                      |
| zone_id               | core | string        |
