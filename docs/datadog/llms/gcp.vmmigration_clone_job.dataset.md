# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmmigration_clone_job.dataset.md

---
title: CloneJob
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloneJob
---

# CloneJob

CloneJob is a Google Cloud resource used in the Migrate to Virtual Machines service. It represents a specific cloning operation that copies data and configuration from a source machine to a target environment in Google Cloud. The resource tracks the progress, status, and details of the migration process, helping users manage and monitor the cloning of workloads during migration.

```
gcp.vmmigration_clone_job
```

## Fields

| Title                               | ID   | Type          | Data Type                                                                                                         | Description |
| ----------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string        |
| ancestors                           | core | array<string> |
| compute_engine_disks_target_details | core | json          | Output only. Details of the target Persistent Disks in Compute Engine.                                            |
| compute_engine_target_details       | core | json          | Output only. Details of the target VM in Compute Engine.                                                          |
| create_time                         | core | timestamp     | Output only. The time the clone job was created (as an API call, not when it was actually created in the target). |
| datadog_display_name                | core | string        |
| end_time                            | core | timestamp     | Output only. The time the clone job was ended.                                                                    |
| error                               | core | json          | Output only. Provides details for the errors that led to the Clone Job's state.                                   |
| labels                              | core | array<string> |
| name                                | core | string        | Output only. The name of the clone.                                                                               |
| organization_id                     | core | string        |
| parent                              | core | string        |
| project_id                          | core | string        |
| project_number                      | core | string        |
| region_id                           | core | string        |
| resource_name                       | core | string        |
| state                               | core | string        | Output only. State of the clone job.                                                                              |
| state_time                          | core | timestamp     | Output only. The time the state was last updated.                                                                 |
| steps                               | core | json          | Output only. The clone steps list representing its progress.                                                      |
| tags                                | core | hstore_csv    |
| zone_id                             | core | string        |
