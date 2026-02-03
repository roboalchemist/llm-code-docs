# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataform_workflow_config.dataset.md

---
title: Dataform Workflow Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataform Workflow Config
---

# Dataform Workflow Config

Dataform Workflow Config in Google Cloud defines the configuration for running Dataform workflows, which manage SQL-based data transformation pipelines in BigQuery. It specifies workflow settings such as environment, scheduling, and execution parameters to automate and orchestrate data transformations efficiently.

```
gcp.dataform_workflow_config
```

## Fields

| Title                              | ID   | Type          | Data Type                                                                                                                                                                                                                                   | Description |
| ---------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string        |
| ancestors                          | core | array<string> |
| create_time                        | core | timestamp     | Output only. The timestamp of when the WorkflowConfig was created.                                                                                                                                                                          |
| cron_schedule                      | core | string        | Optional. Optional schedule (in cron format) for automatic execution of this workflow config.                                                                                                                                               |
| datadog_display_name               | core | string        |
| internal_metadata                  | core | string        | Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.                                                     |
| invocation_config                  | core | json          | Optional. If left unset, a default InvocationConfig will be used.                                                                                                                                                                           |
| labels                             | core | array<string> |
| name                               | core | string        | Identifier. The workflow config's name.                                                                                                                                                                                                     |
| organization_id                    | core | string        |
| parent                             | core | string        |
| project_id                         | core | string        |
| project_number                     | core | string        |
| recent_scheduled_execution_records | core | json          | Output only. Records of the 10 most recent scheduled execution attempts, ordered in descending order of `execution_time`. Updated whenever automatic creation of a workflow invocation is triggered by cron_schedule.                       |
| region_id                          | core | string        |
| release_config                     | core | string        | Required. The name of the release config whose release_compilation_result should be executed. Must be in the format `projects/*/locations/*/repositories/*/releaseConfigs/*`.                                                               |
| resource_name                      | core | string        |
| tags                               | core | hstore_csv    |
| time_zone                          | core | string        | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC. |
| update_time                        | core | timestamp     | Output only. The timestamp of when the WorkflowConfig was last updated.                                                                                                                                                                     |
| zone_id                            | core | string        |
