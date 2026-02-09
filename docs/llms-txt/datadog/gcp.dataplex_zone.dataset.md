# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_zone.dataset.md

---
title: Dataplex Zone
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex Zone
---

# Dataplex Zone

A Dataplex Zone in Google Cloud is a logical subdivision within a Dataplex lake that organizes and governs data based on its purpose, sensitivity, or usage. Zones help enforce consistent security, governance, and data quality policies across datasets. They can be configured as raw zones for storing unprocessed data or curated zones for refined, trusted data ready for analytics and machine learning.

```
gcp.dataplex_zone
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| asset_status         | core | json          | Output only. Aggregated status of the underlying assets of the zone.                                                                                 |
| create_time          | core | timestamp     | Output only. The time when the zone was created.                                                                                                     |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the zone.                                                                                                                   |
| discovery_spec       | core | json          | Optional. Specification of the discovery feature applied to data in this zone.                                                                       |
| gcp_display_name     | core | string        | Optional. User friendly display name.                                                                                                                |
| labels               | core | array<string> | Optional. User defined labels for the zone.                                                                                                          |
| name                 | core | string        | Output only. The relative resource name of the zone, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| resource_spec        | core | json          | Required. Specification of the resources that are referenced by the assets within this zone.                                                         |
| state                | core | string        | Output only. Current state of the zone.                                                                                                              |
| tags                 | core | hstore_csv    |
| type                 | core | string        | Required. Immutable. The type of the zone.                                                                                                           |
| uid                  | core | string        | Output only. System generated globally unique ID for the zone. This ID will be different if the zone is deleted and re-created with the same name.   |
| update_time          | core | timestamp     | Output only. The time when the zone was last updated.                                                                                                |
| zone_id              | core | string        |
