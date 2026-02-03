# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.datastream_stream.dataset.md

---
title: Datastream Stream
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Datastream Stream
---

# Datastream Stream

Datastream Stream in Google Cloud is a serverless change data capture and replication service that lets you synchronize data across databases, storage systems, and applications in real time. It supports sources like Oracle, MySQL, and PostgreSQL, and can deliver data to destinations such as BigQuery, Cloud Storage, and Cloud Spanner. This enables low-latency analytics, event-driven architectures, and seamless data integration without managing infrastructure.

```
gcp.datastream_stream
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                            | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| backfill_all         | core | json          | Automatically backfill objects included in the stream source configuration. Specific objects can be excluded.        |
| backfill_none        | core | json          | Do not automatically backfill any objects.                                                                           |
| create_time          | core | timestamp     | Output only. The creation time of the stream.                                                                        |
| datadog_display_name | core | string        |
| destination_config   | core | json          | Required. Destination connection profile configuration.                                                              |
| errors               | core | json          | Output only. Errors on the Stream.                                                                                   |
| gcp_display_name     | core | string        | Required. Display name.                                                                                              |
| labels               | core | array<string> | Labels.                                                                                                              |
| last_recovery_time   | core | timestamp     | Output only. If the stream was recovered, the time of the last recovery. Note: This field is currently experimental. |
| name                 | core | string        | Output only. Identifier. The stream's name.                                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                |
| source_config        | core | json          | Required. Source connection profile configuration.                                                                   |
| state                | core | string        | The state of the stream.                                                                                             |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The last update time of the stream.                                                                     |
| zone_id              | core | string        |
