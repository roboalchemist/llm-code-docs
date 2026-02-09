# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.apphub_application.dataset.md

---
title: Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Application
---

# Application

Represents the App Engine application for a Google Cloud project. It is a global, per-project resource that sets the region, serving status, authentication domain, default Cloud Storage bucket, and other metadata, and serves as the container for all App Engine services and versions.

```
gcp.apphub_application
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                  | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| attributes           | core | json          | Optional. Consumer provided attributes.                                                                                                    |
| create_time          | core | timestamp     | Output only. Create time.                                                                                                                  |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. User-defined description of an Application. Can have a maximum length of 2048 characters.                                        |
| gcp_display_name     | core | string        | Optional. User-defined name for the Application. Can have a maximum length of 63 characters.                                               |
| labels               | core | array<string> |
| name                 | core | string        | Identifier. The resource name of an Application. Format: `"projects/{host-project-id}/locations/{location}/applications/{application-id}"` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| scope                | core | json          | Required. Immutable. Defines what data can be included into this Application. Limits which Services and Workloads can be registered.       |
| state                | core | string        | Output only. Application state.                                                                                                            |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. A universally unique identifier (in UUID4 format) for the `Application`.                                                      |
| update_time          | core | timestamp     | Output only. Update time.                                                                                                                  |
| zone_id              | core | string        |
