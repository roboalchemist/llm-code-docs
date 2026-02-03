# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmmigration_target_project.dataset.md

---
title: Target Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Target Project
---

# Target Project

A Target Project in Google Cloud is a project that serves as the destination for network or service configurations, such as Private Service Connect or Shared VPC setups. It defines where resources like forwarding rules or service attachments are deployed, allowing controlled connectivity and resource sharing between different projects while maintaining isolation and security boundaries.

```
gcp.vmmigration_target_project
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                 | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time this target project resource was created (not related to when the Compute Engine project it points to was created). |
| datadog_display_name | core | string        |
| description          | core | string        | The target project's description.                                                                                                         |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The name of the target project.                                                                                              |
| organization_id      | core | string        |
| parent               | core | string        |
| project              | core | string        | Required. The target project ID (number) or project name.                                                                                 |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The last time the target project resource was updated.                                                                       |
| zone_id              | core | string        |
