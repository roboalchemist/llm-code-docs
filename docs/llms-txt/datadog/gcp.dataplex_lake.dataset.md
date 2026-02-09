# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_lake.dataset.md

---
title: Dataplex Lake
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex Lake
---

# Dataplex Lake

Dataplex Lake in Google Cloud is a centralized data repository that organizes, secures, and manages data across storage systems. It provides a logical container for structured and unstructured data, enabling consistent governance, metadata management, and access control. This helps teams discover, curate, and analyze data at scale while maintaining compliance and security.

```
gcp.dataplex_lake
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                              | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| asset_status         | core | json          | Output only. Aggregated status of the underlying assets of the lake.                                                                                   |
| create_time          | core | timestamp     | Output only. The time when the lake was created.                                                                                                       |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the lake.                                                                                                                     |
| gcp_display_name     | core | string        | Optional. User friendly display name.                                                                                                                  |
| labels               | core | array<string> | Optional. User-defined labels for the lake.                                                                                                            |
| metastore            | core | json          | Optional. Settings to manage lake and Dataproc Metastore service instance association.                                                                 |
| metastore_status     | core | json          | Output only. Metastore status of the lake.                                                                                                             |
| name                 | core | string        | Output only. The relative resource name of the lake, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}.                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| service_account      | core | string        | Output only. Service account associated with this lake. This service account must be authorized to access or operate on resources managed by the lake. |
| state                | core | string        | Output only. Current state of the lake.                                                                                                                |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. System generated globally unique ID for the lake. This ID will be different if the lake is deleted and re-created with the same name.     |
| update_time          | core | timestamp     | Output only. The time when the lake was last updated.                                                                                                  |
| zone_id              | core | string        |
