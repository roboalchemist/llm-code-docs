# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.apphub_service.dataset.md

---
title: App Hub Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Hub Service
---

# App Hub Service

App Hub Service in Google Cloud is a managed platform that helps organize, manage, and monitor applications across multiple environments. It provides a unified view of application components, their dependencies, and associated services, enabling better governance and operational visibility. It integrates with other GCP services to simplify application lifecycle management.

```
gcp.apphub_service
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                   | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| attributes           | core | json          | Optional. Consumer provided attributes.                                                                                                                     |
| create_time          | core | timestamp     | Output only. Create time.                                                                                                                                   |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. User-defined description of a Service. Can have a maximum length of 2048 characters.                                                              |
| discovered_service   | core | string        | Required. Immutable. The resource name of the original discovered service.                                                                                  |
| gcp_display_name     | core | string        | Optional. User-defined name for the Service. Can have a maximum length of 63 characters.                                                                    |
| labels               | core | array<string> |
| name                 | core | string        | Identifier. The resource name of a Service. Format: `"projects/{host-project-id}/locations/{location}/applications/{application-id}/services/{service-id}"` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| service_properties   | core | json          | Output only. Properties of an underlying compute resource that can comprise a Service. These are immutable.                                                 |
| service_reference    | core | json          | Output only. Reference to an underlying networking resource that can comprise a Service. These are immutable.                                               |
| state                | core | string        | Output only. Service state.                                                                                                                                 |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. A universally unique identifier (UUID) for the `Service` in the UUID4 format.                                                                  |
| update_time          | core | timestamp     | Output only. Update time.                                                                                                                                   |
| zone_id              | core | string        |
