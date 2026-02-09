# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.workstations_workstation.dataset.md

---
title: Workstation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Workstation
---

# Workstation

A Google Cloud Workstation is a managed development environment that provides secure, scalable, and preconfigured workspaces for developers. It allows users to quickly spin up cloud-based workstations with consistent configurations, integrated authentication, and access controls. This helps teams collaborate efficiently while maintaining security and compliance.

```
gcp.workstations_workstation
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Client-specified annotations.                                                                                                                                                                                                                                                                  |
| create_time          | core | timestamp     | Output only. Time when this workstation was created.                                                                                                                                                                                                                                                     |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. Time when this workstation was soft-deleted.                                                                                                                                                                                                                                                |
| etag                 | core | string        | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding.                                                                                                                                             |
| gcp_display_name     | core | string        | Optional. Human-readable name for this workstation.                                                                                                                                                                                                                                                      |
| host                 | core | string        | Output only. Host to which clients can send HTTPS traffic that will be received by the workstation. Authorized traffic will be received to the workstation as HTTP on port 80. To send traffic to a different port, clients may prefix the host with the destination port in the format `{port}-{host}`. |
| labels               | core | array<string> | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation and that are also propagated to the underlying Compute Engine resources.                                                                                                              |
| name                 | core | string        | Identifier. Full name of this workstation.                                                                                                                                                                                                                                                               |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. Indicates whether this workstation is currently being updated to match its intended state.                                                                                                                                                                                                  |
| region_id            | core | string        |
| resource_name        | core | string        |
| runtime_host         | core | json          | Optional. Output only. Runtime host for the workstation when in STATE_RUNNING.                                                                                                                                                                                                                           |
| source_workstation   | core | string        | Optional. The source workstation from which this workstation's persistent directories were cloned on creation.                                                                                                                                                                                           |
| start_time           | core | timestamp     | Output only. Time when this workstation was most recently successfully started, regardless of the workstation's initial state.                                                                                                                                                                           |
| state                | core | string        | Output only. Current state of the workstation.                                                                                                                                                                                                                                                           |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. A system-assigned unique identifier for this workstation.                                                                                                                                                                                                                                   |
| update_time          | core | timestamp     | Output only. Time when this workstation was most recently updated.                                                                                                                                                                                                                                       |
| zone_id              | core | string        |
