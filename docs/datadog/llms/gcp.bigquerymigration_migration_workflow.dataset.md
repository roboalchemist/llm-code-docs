# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.bigquerymigration_migration_workflow.dataset.md

---
title: BigQuery Migration Workflow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > BigQuery Migration Workflow
---

# BigQuery Migration Workflow

BigQuery Migration Workflow in Google Cloud helps automate and manage the process of migrating data warehouses to BigQuery. It provides tools to assess existing environments, translate SQL queries, and transfer data efficiently. The workflow coordinates different migration steps, ensuring consistency, validation, and minimal downtime during the transition.

```
gcp.bigquerymigration_migration_workflow
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Time when the workflow was created.                                                                                                                     |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | The display name of the workflow. This can be set to give a workflow a descriptive name. There is no guarantee or enforcement of uniqueness.                         |
| labels               | core | array<string> |
| last_update_time     | core | timestamp     | Output only. Time when the workflow was last updated.                                                                                                                |
| name                 | core | string        | Output only. Immutable. Identifier. The unique identifier for the migration workflow. The ID is server-generated. Example: `projects/123/locations/us/workflows/345` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. That status of the workflow.                                                                                                                            |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
