# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmmigration_group.dataset.md

---
title: Migration Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Migration Group
---

# Migration Group

A Migration Group in Google Cloud is a logical container used to organize and manage multiple migration sources or workloads during a migration project. It helps group related assets, such as virtual machines or applications, to streamline assessment, planning, and execution of migrations. This grouping simplifies tracking progress and applying consistent migration settings.

```
gcp.vmmigration_group
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                | Description |
| --------------------- | ---- | ------------- | ------------------------------------------------------------------------ | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| create_time           | core | timestamp     | Output only. The create time timestamp.                                  |
| datadog_display_name  | core | string        |
| description           | core | string        | User-provided description of the group.                                  |
| gcp_display_name      | core | string        | Display name is a user defined name for this group which can be updated. |
| labels                | core | array<string> |
| migration_target_type | core | string        | Immutable. The target type of this group.                                |
| name                  | core | string        | Output only. The Group name.                                             |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| tags                  | core | hstore_csv    |
| update_time           | core | timestamp     | Output only. The update time timestamp.                                  |
| zone_id               | core | string        |
