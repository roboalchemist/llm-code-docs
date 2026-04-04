# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_asset.dataset.md

---
title: Dataplex Asset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex Asset
---

# Dataplex Asset

A Dataplex Asset in Google Cloud is a data resource, such as a Cloud Storage bucket or BigQuery dataset, that is registered within a Dataplex lake. It represents the physical storage location of data and is managed through Dataplex to provide governance, security, and metadata management. Assets allow organizations to organize and control access to data across different storage systems while maintaining consistent policies and visibility.

```
gcp.dataplex_asset
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time when the asset was created.                                                                                                                            |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the asset.                                                                                                                                          |
| discovery_spec       | core | json          | Optional. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone. |
| discovery_status     | core | json          | Output only. Status of the discovery feature applied to data referenced by this asset.                                                                                       |
| gcp_display_name     | core | string        | Optional. User friendly display name.                                                                                                                                        |
| labels               | core | array<string> | Optional. User defined labels for the asset.                                                                                                                                 |
| name                 | core | string        | Output only. The relative resource name of the asset, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}.      |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| resource_spec        | core | json          | Required. Specification of the resource that is referenced by this asset.                                                                                                    |
| resource_status      | core | json          | Output only. Status of the resource referenced by this asset.                                                                                                                |
| security_status      | core | json          | Output only. Status of the security policy applied to resource referenced by this asset.                                                                                     |
| state                | core | string        | Output only. Current state of the asset.                                                                                                                                     |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name.                         |
| update_time          | core | timestamp     | Output only. The time when the asset was last updated.                                                                                                                       |
| zone_id              | core | string        |
