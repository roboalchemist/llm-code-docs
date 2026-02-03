# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_aspect_type.dataset.md

---
title: Dataplex Aspect Type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex Aspect Type
---

# Dataplex Aspect Type

Dataplex Aspect Type in Google Cloud defines a reusable schema that describes a specific aspect of data assets, such as quality, lineage, or classification. It allows organizations to standardize metadata structures across datasets and automate governance processes. Aspect Types help ensure consistent metadata management and improve data discoverability within Dataplex.

```
gcp.dataplex_aspect_type
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| authorization        | core | json          | Immutable. Defines the Authorization for this type.                                                                                                                |
| create_time          | core | timestamp     | Output only. The time when the AspectType was created.                                                                                                             |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the AspectType.                                                                                                                           |
| etag                 | core | string        | The service computes this checksum. The client may send it on update and delete requests to ensure it has an up-to-date value before proceeding.                   |
| gcp_display_name     | core | string        | Optional. User friendly display name.                                                                                                                              |
| labels               | core | array<string> | Optional. User-defined labels for the AspectType.                                                                                                                  |
| metadata_template    | core | json          | Required. MetadataTemplate of the aspect.                                                                                                                          |
| name                 | core | string        | Output only. The relative resource name of the AspectType, of the form: projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}.            |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| transfer_status      | core | string        | Output only. Denotes the transfer status of the Aspect Type. It is unspecified for Aspect Types created from Dataplex API.                                         |
| uid                  | core | string        | Output only. System generated globally unique ID for the AspectType. If you delete and recreate the AspectType with the same name, then this ID will be different. |
| update_time          | core | timestamp     | Output only. The time when the AspectType was last updated.                                                                                                        |
| zone_id              | core | string        |
