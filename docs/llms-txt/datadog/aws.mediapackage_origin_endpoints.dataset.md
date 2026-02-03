# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_origin_endpoints.dataset.md

---
title: Mediapackage Origin Endpoints
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediapackage Origin Endpoints
---

# Mediapackage Origin Endpoints

This table represents the mediapackage_origin_endpoints resource from Amazon Web Services.

```
aws.mediapackage_origin_endpoints
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                    | Description |
| ------------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| account_id               | core | string        |
| arn                      | core | string        | The Amazon Resource Name (ARN) assigned to the OriginEndpoint.                                                                                                                                                                                                                                                               |
| authorization            | core | json          |
| channel_id               | core | string        | The ID of the Channel the OriginEndpoint is associated with.                                                                                                                                                                                                                                                                 |
| cmaf_package             | core | json          |
| created_at               | core | string        | The date and time the OriginEndpoint was created.                                                                                                                                                                                                                                                                            |
| dash_package             | core | json          |
| description              | core | string        | A short text description of the OriginEndpoint.                                                                                                                                                                                                                                                                              |
| hls_package              | core | json          |
| id                       | core | string        | The ID of the OriginEndpoint.                                                                                                                                                                                                                                                                                                |
| manifest_name            | core | string        | A short string appended to the end of the OriginEndpoint URL.                                                                                                                                                                                                                                                                |
| mss_package              | core | json          |
| origination              | core | string        | Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpointmay by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not berequested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination |
| startover_window_seconds | core | int64         | Maximum duration (seconds) of content to retain for startover playback.If not specified, startover playback will be disabled for the OriginEndpoint.                                                                                                                                                                         |
| tags                     | core | hstore_csv    |
| time_delay_seconds       | core | int64         | Amount of delay (seconds) to enforce on the playback of live content.If not specified, there will be no time delay in effect for the OriginEndpoint.                                                                                                                                                                         |
| url                      | core | string        | The URL of the packaged OriginEndpoint for consumption.                                                                                                                                                                                                                                                                      |
| whitelist                | core | array<string> | A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.                                                                                                                                                                                                                                           |
