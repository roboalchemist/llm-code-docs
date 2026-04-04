# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.aiplatform_custom_job.dataset.md

---
title: Vertex AI Custom Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Vertex AI Custom Job
---

# Vertex AI Custom Job

Vertex AI Custom Job is a managed Google Cloud resource that allows users to run custom machine learning training or batch processing tasks on Google Cloud infrastructure. It provides flexibility to specify custom containers, machine types, accelerators, and distributed training configurations. This resource integrates with Vertex AI for experiment tracking, model management, and deployment workflows, enabling scalable and reproducible ML workloads.

```
gcp.aiplatform_custom_job
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                  | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Time when the CustomJob was created.                                                                                                                                                                                                                                                                                          |
| datadog_display_name | core | string        |
| encryption_spec      | core | json          | Customer-managed encryption key options for a CustomJob. If this is set, then all resources created by the CustomJob will be encrypted with the provided encryption key.                                                                                                                                                                   |
| end_time             | core | timestamp     | Output only. Time when the CustomJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.                                                                                                                                                                                                |
| error                | core | json          | Output only. Only populated when job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.                                                                                                                                                                                                                                               |
| gcp_display_name     | core | string        | Required. The display name of the CustomJob. The name can be up to 128 characters long and can consist of any UTF-8 characters.                                                                                                                                                                                                            |
| job_spec             | core | json          | Required. Job spec.                                                                                                                                                                                                                                                                                                                        |
| labels               | core | array<string> | The labels with user-defined metadata to organize CustomJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| name                 | core | string        | Output only. Resource name of a CustomJob.                                                                                                                                                                                                                                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                                                      |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                                                      |
| start_time           | core | timestamp     | Output only. Time when the CustomJob for the first time entered the `JOB_STATE_RUNNING` state.                                                                                                                                                                                                                                             |
| state                | core | string        | Output only. The detailed state of the job.                                                                                                                                                                                                                                                                                                |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time when the CustomJob was most recently updated.                                                                                                                                                                                                                                                                            |
| zone_id              | core | string        |
