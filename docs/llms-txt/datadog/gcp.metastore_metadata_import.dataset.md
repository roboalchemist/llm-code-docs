# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.metastore_metadata_import.dataset.md

---
title: Dataproc Metastore Metadata Import
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataproc Metastore Metadata Import
---

# Dataproc Metastore Metadata Import

Dataproc Metastore Metadata Import in Google Cloud is a feature that allows users to import metadata from external sources into a Dataproc Metastore service. It helps migrate or synchronize metadata such as table definitions, schemas, and other catalog information from existing Hive Metastores or compatible systems, enabling seamless integration and consistent data management across analytics and data processing environments.

```
gcp.metastore_metadata_import
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time when the metadata import was started.                                                                                                                                         |
| database_dump        | core | json          | Immutable. A database dump from a pre-existing metastore's database.                                                                                                                                |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. The description of the metadata import.                                                                                                                                                   |
| end_time             | core | timestamp     | Output only. The time when the metadata import finished.                                                                                                                                            |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. Identifier. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The current state of the metadata import.                                                                                                                                              |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The time when the metadata import was last updated.                                                                                                                                    |
| zone_id              | core | string        |
