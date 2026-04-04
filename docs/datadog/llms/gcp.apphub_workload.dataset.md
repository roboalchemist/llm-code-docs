# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.apphub_workload.dataset.md

---
title: App Hub Workload
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Hub Workload
---

# App Hub Workload

App Hub Workload in Google Cloud is a managed resource that represents an application's deployed components and their relationships within App Hub. It helps organize, monitor, and manage workloads across environments by providing visibility into service dependencies, configurations, and runtime states. This resource supports consistent governance and operational insights for distributed applications.

```gdscript3
gcp.apphub_workload
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                        | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| attributes           | core | json          | Optional. Consumer provided attributes.                                                                                                                          |
| create_time          | core | timestamp     | Output only. Create time.                                                                                                                                        |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. User-defined description of a Workload. Can have a maximum length of 2048 characters.                                                                  |
| discovered_workload  | core | string        | Required. Immutable. The resource name of the original discovered workload.                                                                                      |
| gcp_display_name     | core | string        | Optional. User-defined name for the Workload. Can have a maximum length of 63 characters.                                                                        |
| labels               | core | array<string> |
| name                 | core | string        | Identifier. The resource name of the Workload. Format: `"projects/{host-project-id}/locations/{location}/applications/{application-id}/workloads/{workload-id}"` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. Workload state.                                                                                                                                     |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. A universally unique identifier (UUID) for the `Workload` in the UUID4 format.                                                                      |
| update_time          | core | timestamp     | Output only. Update time.                                                                                                                                        |
| workload_properties  | core | json          | Output only. Properties of an underlying compute resource represented by the Workload. These are immutable.                                                      |
| workload_reference   | core | json          | Output only. Reference of an underlying compute resource represented by the Workload. These are immutable.                                                       |
| zone_id              | core | string        |
