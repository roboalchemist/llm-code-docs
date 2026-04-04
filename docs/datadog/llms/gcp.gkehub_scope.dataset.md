# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkehub_scope.dataset.md

---
title: GKE Hub Scope
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GKE Hub Scope
---

# GKE Hub Scope

GKE Hub Scope is a Google Cloud resource that groups multiple GKE clusters into a logical scope for centralized management. It enables consistent policy application, configuration, and access control across clusters within the same scope. This helps simplify multi-cluster operations and governance.

```
gcp.gkehub_scope
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. When the scope was created.                                                                                                                                                                     |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. When the scope was deleted.                                                                                                                                                                     |
| labels               | core | array<string> | Optional. Labels for this Scope.                                                                                                                                                                             |
| name                 | core | string        | The resource name for the scope `projects/{project}/locations/{location}/scopes/{scope}`                                                                                                                     |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | json          | Output only. State of the scope resource.                                                                                                                                                                    |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Google-generated UUID for this resource. This is unique across all scope resources. If a scope resource is deleted and another resource with the same name is created, it gets a different uid. |
| update_time          | core | timestamp     | Output only. When the scope was last updated.                                                                                                                                                                |
| zone_id              | core | string        |
