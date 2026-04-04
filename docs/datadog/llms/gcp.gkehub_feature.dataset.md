# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkehub_feature.dataset.md

---
title: GKE Hub Feature
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GKE Hub Feature
---

# GKE Hub Feature

GKE Hub Feature is a Google Cloud resource that represents a specific capability or service enabled within the GKE Hub. It allows users to manage and configure features such as service mesh, policy management, or multi-cluster services across registered Kubernetes clusters. This resource helps centralize control and visibility for distributed cluster environments.

```
gcp.gkehub_feature
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                            | Description |
| --------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                        | core | string        |
| ancestors                   | core | array<string> |
| create_time                 | core | timestamp     | Output only. When the Feature resource was created.                                                                                  |
| datadog_display_name        | core | string        |
| delete_time                 | core | timestamp     | Output only. When the Feature resource was deleted.                                                                                  |
| fleet_default_member_config | core | json          | Optional. Feature configuration applicable to all memberships of the fleet.                                                          |
| labels                      | core | array<string> | Labels for this Feature.                                                                                                             |
| name                        | core | string        | Output only. The full, unique name of this Feature resource in the format `projects/*/locations/*/features/*`.                       |
| organization_id             | core | string        |
| parent                      | core | string        |
| project_id                  | core | string        |
| project_number              | core | string        |
| region_id                   | core | string        |
| resource_name               | core | string        |
| resource_state              | core | json          | Output only. State of the Feature resource itself.                                                                                   |
| spec                        | core | json          | Optional. Fleet-wide Feature configuration. If this Feature does not support any Fleet-wide configuration, this field may be unused. |
| state                       | core | json          | Output only. The Fleet-wide Feature state.                                                                                           |
| tags                        | core | hstore_csv    |
| unreachable                 | core | array<string> | Output only. List of locations that could not be reached while fetching this feature.                                                |
| update_time                 | core | timestamp     | Output only. When the Feature resource was last updated.                                                                             |
| zone_id                     | core | string        |
