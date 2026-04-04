# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkehub_fleet.dataset.md

---
title: Fleet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fleet
---

# Fleet

Fleet in Google Cloud is a container management resource that allows you to organize and manage multiple Kubernetes clusters as a single logical group. It provides centralized control, consistent policy enforcement, and unified visibility across clusters, whether they are hosted on Google Kubernetes Engine or other environments.

```
gcp.gkehub_fleet
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                 | Description |
| ---------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| ancestors              | core | array<string> |
| create_time            | core | timestamp     | Output only. When the Fleet was created.                                                                                                                                                                                                                                  |
| datadog_display_name   | core | string        |
| default_cluster_config | core | json          | Optional. The default cluster configurations to apply across the fleet.                                                                                                                                                                                                   |
| delete_time            | core | timestamp     | Output only. When the Fleet was deleted.                                                                                                                                                                                                                                  |
| gcp_display_name       | core | string        | Optional. A user-assigned display name of the Fleet. When present, it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `Production Fleet` |
| labels                 | core | array<string> | Optional. Labels for this Fleet.                                                                                                                                                                                                                                          |
| name                   | core | string        | Output only. The full, unique resource name of this fleet in the format of `projects/{project}/locations/{location}/fleets/{fleet}`. Each Google Cloud project can have at most one fleet resource, named "default".                                                      |
| organization_id        | core | string        |
| parent                 | core | string        |
| project_id             | core | string        |
| project_number         | core | string        |
| region_id              | core | string        |
| resource_name          | core | string        |
| state                  | core | json          | Output only. State of the namespace resource.                                                                                                                                                                                                                             |
| tags                   | core | hstore_csv    |
| uid                    | core | string        | Output only. Google-generated UUID for this resource. This is unique across all Fleet resources. If a Fleet resource is deleted and another resource with the same name is created, it gets a different uid.                                                              |
| update_time            | core | timestamp     | Output only. When the Fleet was last updated.                                                                                                                                                                                                                             |
| zone_id                | core | string        |
