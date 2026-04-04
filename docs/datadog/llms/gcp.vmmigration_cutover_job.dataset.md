# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmmigration_cutover_job.dataset.md

---
title: CutoverJob
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CutoverJob
---

# CutoverJob

CutoverJob in Google Cloud is a resource used in the Migrate to Virtual Machines service to manage the final migration step of a source machine to Google Cloud. It coordinates the cutover process, ensuring that the source system is stopped, data is synchronized, and the target virtual machine is started in the cloud. This resource helps automate and track the transition from on-premises or other environments to Google Cloud with minimal downtime.

```
gcp.vmmigration_cutover_job
```

## Fields

| Title                               | ID   | Type          | Data Type                                                                                                           | Description |
| ----------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string        |
| ancestors                           | core | array<string> |
| compute_engine_disks_target_details | core | json          | Output only. Details of the target Persistent Disks in Compute Engine.                                              |
| compute_engine_target_details       | core | json          | Output only. Details of the target VM in Compute Engine.                                                            |
| create_time                         | core | timestamp     | Output only. The time the cutover job was created (as an API call, not when it was actually created in the target). |
| datadog_display_name                | core | string        |
| end_time                            | core | timestamp     | Output only. The time the cutover job had finished.                                                                 |
| error                               | core | json          | Output only. Provides details for the errors that led to the Cutover Job's state.                                   |
| labels                              | core | array<string> |
| name                                | core | string        | Output only. The name of the cutover job.                                                                           |
| organization_id                     | core | string        |
| parent                              | core | string        |
| progress_percent                    | core | int64         | Output only. The current progress in percentage of the cutover job.                                                 |
| project_id                          | core | string        |
| project_number                      | core | string        |
| region_id                           | core | string        |
| resource_name                       | core | string        |
| state                               | core | string        | Output only. State of the cutover job.                                                                              |
| state_message                       | core | string        | Output only. A message providing possible extra details about the current state.                                    |
| state_time                          | core | timestamp     | Output only. The time the state was last updated.                                                                   |
| steps                               | core | json          | Output only. The cutover steps list representing its progress.                                                      |
| tags                                | core | hstore_csv    |
| zone_id                             | core | string        |
