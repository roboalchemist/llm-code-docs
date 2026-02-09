# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_task.dataset.md

---
title: Dataplex Task
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex Task
---

# Dataplex Task

A Dataplex Task in Google Cloud is a scheduled or on-demand job that runs data processing workloads within a Dataplex lake or zone. It is commonly used to automate data quality checks, transformations, or other custom operations using Spark or other supported execution environments. Tasks help maintain data consistency, enforce governance, and streamline data preparation across distributed datasets.

```
gcp.dataplex_task
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time when the task was created.                                                                                                      |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the task.                                                                                                                    |
| execution_spec       | core | json          | Required. Spec related to how a task is executed.                                                                                                     |
| execution_status     | core | json          | Output only. Status of the latest task executions.                                                                                                    |
| gcp_display_name     | core | string        | Optional. User friendly display name.                                                                                                                 |
| labels               | core | array<string> | Optional. User-defined labels for the task.                                                                                                           |
| name                 | core | string        | Output only. The relative resource name of the task, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/ tasks/{task_id}. |
| notebook             | core | json          | Config related to running scheduled Notebooks.                                                                                                        |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| spark                | core | json          | Config related to running custom Spark tasks.                                                                                                         |
| state                | core | string        | Output only. Current state of the task.                                                                                                               |
| tags                 | core | hstore_csv    |
| trigger_spec         | core | json          | Required. Spec related to how often and when a task should be triggered.                                                                              |
| uid                  | core | string        | Output only. System generated globally unique ID for the task. This ID will be different if the task is deleted and re-created with the same name.    |
| update_time          | core | timestamp     | Output only. The time when the task was last updated.                                                                                                 |
| zone_id              | core | string        |
