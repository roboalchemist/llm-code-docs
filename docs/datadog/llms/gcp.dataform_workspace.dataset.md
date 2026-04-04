# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataform_workspace.dataset.md

---
title: Dataform Workspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataform Workspace
---

# Dataform Workspace

Dataform Workspace in Google Cloud is a managed environment for developing, testing, and deploying SQL-based data transformation workflows. It integrates with BigQuery to help teams manage data pipelines using version control, modular SQL code, and automated dependency management. This workspace enables collaboration, simplifies data modeling, and ensures consistent, reliable data transformations across analytics projects.

```
gcp.dataform_workspace
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                               | Description |
| --------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| create_time           | core | timestamp     | Output only. The timestamp of when the workspace was created.                                                                                                                           |
| data_encryption_state | core | json          | Output only. A data encryption state of a Git repository if this Workspace is protected by a KMS key.                                                                                   |
| datadog_display_name  | core | string        |
| internal_metadata     | core | string        | Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string. |
| labels                | core | array<string> |
| name                  | core | string        | Identifier. The workspace's name.                                                                                                                                                       |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| tags                  | core | hstore_csv    |
| zone_id               | core | string        |
