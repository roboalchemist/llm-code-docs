# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.aiplatform_metadata_store.dataset.md

---
title: Vertex AI Metadata Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Vertex AI Metadata Store
---

# Vertex AI Metadata Store

Vertex AI Metadata Store is a managed service in Google Cloud that tracks and organizes metadata for machine learning workflows. It helps users record lineage, parameters, metrics, and artifacts generated during model development and training. This enables reproducibility, collaboration, and governance across ML experiments.

```
gcp.aiplatform_metadata_store
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                       | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Timestamp when this MetadataStore was created.                                                                                                     |
| datadog_display_name | core | string        |
| dataplex_config      | core | json          | Optional. Dataplex integration settings.                                                                                                                        |
| description          | core | string        | Description of the MetadataStore.                                                                                                                               |
| encryption_spec      | core | json          | Customer-managed encryption key spec for a Metadata Store. If set, this Metadata Store and all sub-resources of this Metadata Store are secured using this key. |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The resource name of the MetadataStore instance.                                                                                                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | json          | Output only. State information of the MetadataStore.                                                                                                            |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Timestamp when this MetadataStore was last updated.                                                                                                |
| zone_id              | core | string        |
