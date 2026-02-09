# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediatailor_sourcelocation.dataset.md

---
title: Mediatailor Sourcelocation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediatailor Sourcelocation
---

# Mediatailor Sourcelocation

This table represents the mediatailor_sourcelocation resource from Amazon Web Services.

```
aws.mediatailor_sourcelocation
```

## Fields

| Title                                  | ID   | Type       | Data Type                                                               | Description |
| -------------------------------------- | ---- | ---------- | ----------------------------------------------------------------------- | ----------- |
| _key                                   | core | string     |
| access_configuration                   | core | json       | The access configuration for the source location.                       |
| account_id                             | core | string     |
| arn                                    | core | string     | The ARN for the VOD source.                                             |
| creation_time                          | core | timestamp  | The timestamp that indicates when the VOD source was created.           |
| default_segment_delivery_configuration | core | json       | The default segment delivery configuration.                             |
| http_configuration                     | core | json       | The HTTP configuration for the source location.                         |
| http_package_configurations            | core | json       | The HTTP package configurations for the VOD source.                     |
| last_modified_time                     | core | timestamp  | The timestamp that indicates when the VOD source was last modified.     |
| live_source_name                       | core | string     | The name that's used to refer to a live source.                         |
| segment_delivery_configurations        | core | json       | The segment delivery configurations for the source location.            |
| source_location_name                   | core | string     | The name of the source location that the VOD source is associated with. |
| tags                                   | core | hstore_csv |
| vod_source_name                        | core | string     | The name of the VOD source.                                             |
