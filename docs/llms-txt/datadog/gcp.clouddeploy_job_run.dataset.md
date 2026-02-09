# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.clouddeploy_job_run.dataset.md

---
title: Cloud Deploy JobRun
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Deploy JobRun
---

# Cloud Deploy JobRun

Cloud Deploy JobRun in Google Cloud represents an execution instance of a deployment job within a delivery pipeline. It tracks the progress, status, and results of a specific job execution, such as deploying an application to a target environment. Each JobRun provides details about the job configuration, execution logs, and outcomes, helping users monitor and troubleshoot deployment processes.

```
gcp.clouddeploy_job_run
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                              | Description |
| ----------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                          | core | string        |
| advance_child_rollout_job_run | core | json          | Output only. Information specific to an advanceChildRollout `JobRun`                                                                                                                                   |
| ancestors                     | core | array<string> |
| create_child_rollout_job_run  | core | json          | Output only. Information specific to a createChildRollout `JobRun`.                                                                                                                                    |
| create_time                   | core | timestamp     | Output only. Time at which the `JobRun` was created.                                                                                                                                                   |
| datadog_display_name          | core | string        |
| deploy_job_run                | core | json          | Output only. Information specific to a deploy `JobRun`.                                                                                                                                                |
| end_time                      | core | timestamp     | Output only. Time at which the `JobRun` ended.                                                                                                                                                         |
| etag                          | core | string        | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| job_id                        | core | string        | Output only. ID of the `Rollout` job this `JobRun` corresponds to.                                                                                                                                     |
| labels                        | core | array<string> |
| name                          | core | string        | Output only. Name of the `JobRun`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{releases}/rollouts/{rollouts}/jobRuns/{uuid}`.                    |
| organization_id               | core | string        |
| parent                        | core | string        |
| phase_id                      | core | string        | Output only. ID of the `Rollout` phase this `JobRun` belongs in.                                                                                                                                       |
| postdeploy_job_run            | core | json          | Output only. Information specific to a postdeploy `JobRun`.                                                                                                                                            |
| predeploy_job_run             | core | json          | Output only. Information specific to a predeploy `JobRun`.                                                                                                                                             |
| project_id                    | core | string        |
| project_number                | core | string        |
| region_id                     | core | string        |
| resource_name                 | core | string        |
| start_time                    | core | timestamp     | Output only. Time at which the `JobRun` was started.                                                                                                                                                   |
| state                         | core | string        | Output only. The current state of the `JobRun`.                                                                                                                                                        |
| tags                          | core | hstore_csv    |
| uid                           | core | string        | Output only. Unique identifier of the `JobRun`.                                                                                                                                                        |
| verify_job_run                | core | json          | Output only. Information specific to a verify `JobRun`.                                                                                                                                                |
| zone_id                       | core | string        |
