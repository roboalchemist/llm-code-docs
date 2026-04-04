# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dlp_job_trigger.dataset.md

---
title: Data Loss Prevention Job Trigger
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Data Loss Prevention Job Trigger
---

# Data Loss Prevention Job Trigger

A Data Loss Prevention Job Trigger in Google Cloud automatically starts DLP inspection or risk analysis jobs based on defined conditions or schedules. It helps identify and protect sensitive data across storage systems by scanning for personally identifiable information or other confidential content. This resource enables consistent, automated data protection workflows.

```
gcp.dlp_job_trigger
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                 | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation timestamp of a triggeredJob.                                                                                                                                                                                                    |
| datadog_display_name | core | string        |
| description          | core | string        | User provided description (max 256 chars)                                                                                                                                                                                                                 |
| errors               | core | json          | Output only. A stream of errors encountered when the trigger was activated. Repeated errors may result in the JobTrigger automatically being paused. Will return the last 100 errors. Whenever the JobTrigger is modified this list will be cleared.      |
| gcp_display_name     | core | string        | Display name (max 100 chars)                                                                                                                                                                                                                              |
| gcp_status           | core | string        | Required. A status for this trigger. Possible values: ['STATUS_UNSPECIFIED', 'HEALTHY', 'PAUSED', 'CANCELLED']. Values descriptions: ['Unused.', 'Trigger is healthy.', 'Trigger is temporarily paused.', 'Trigger is cancelled and can not be resumed.'] |
| inspect_job          | core | json          | For inspect jobs, a snapshot of the configuration.                                                                                                                                                                                                        |
| labels               | core | array<string> |
| last_run_time        | core | timestamp     | Output only. The timestamp of the last time this trigger executed.                                                                                                                                                                                        |
| name                 | core | string        | Unique resource name for the triggeredJob, assigned by the service when the triggeredJob is created, for example `projects/dlp-test-project/jobTriggers/53234423`.                                                                                        |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| triggers             | core | json          | A list of triggers which will be OR'ed together. Only one in the list needs to trigger for a job to be started. The list may contain only a single Schedule trigger and must have at least one object.                                                    |
| update_time          | core | timestamp     | Output only. The last update timestamp of a triggeredJob.                                                                                                                                                                                                 |
| zone_id              | core | string        |
