# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.datamigration_conversion_workspace.dataset.md

---
title: Conversion Workspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Conversion Workspace
---

# Conversion Workspace

Conversion Workspace in Google Cloud is a managed environment used for database migration and modernization. It allows users to assess, convert, and transform database schemas and code from source databases to target databases supported by Google Cloud. The workspace provides tools for analyzing compatibility, applying conversion rules, and previewing changes before deployment, helping streamline the migration process and reduce manual effort.

```
gcp.datamigration_conversion_workspace
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                 | Description |
| ----------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| ancestors               | core | array<string> |
| create_time             | core | timestamp     | Output only. The timestamp when the workspace resource was created.                                                                       |
| datadog_display_name    | core | string        |
| destination             | core | json          | Required. The destination engine details.                                                                                                 |
| gcp_display_name        | core | string        | Optional. The display name for the workspace.                                                                                             |
| gcp_source              | core | json          | Required. The source engine details.                                                                                                      |
| has_uncommitted_changes | core | bool          | Output only. Whether the workspace has uncommitted changes (changes which were made after the workspace was committed).                   |
| labels                  | core | array<string> |
| latest_commit_id        | core | string        | Output only. The latest commit ID.                                                                                                        |
| latest_commit_time      | core | timestamp     | Output only. The timestamp when the workspace was committed.                                                                              |
| name                    | core | string        | Full name of the workspace resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. |
| organization_id         | core | string        |
| parent                  | core | string        |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| resource_name           | core | string        |
| tags                    | core | hstore_csv    |
| update_time             | core | timestamp     | Output only. The timestamp when the workspace resource was last updated.                                                                  |
| zone_id                 | core | string        |
