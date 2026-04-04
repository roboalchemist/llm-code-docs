# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.aiplatform_hyperparameter_tuning_job.dataset.md

---
title: Vertex AI Hyperparameter Tuning Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Vertex AI Hyperparameter Tuning Job
---

# Vertex AI Hyperparameter Tuning Job

Vertex AI Hyperparameter Tuning Job automatically searches for the best hyperparameter values for a machine learning model on Google Cloud. It runs multiple training trials in parallel, each with different hyperparameter combinations, and uses optimization algorithms to find the configuration that yields the best model performance.

```
gcp.aiplatform_hyperparameter_tuning_job
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                | Description |
| ---------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| ancestors              | core | array<string> |
| create_time            | core | timestamp     | Output only. Time when the HyperparameterTuningJob was created.                                                                                                                                                                                                                                                                                          |
| datadog_display_name   | core | string        |
| encryption_spec        | core | json          | Customer-managed encryption key options for a HyperparameterTuningJob. If this is set, then all resources created by the HyperparameterTuningJob will be encrypted with the provided encryption key.                                                                                                                                                     |
| end_time               | core | timestamp     | Output only. Time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.                                                                                                                                                                                                |
| error                  | core | json          | Output only. Only populated when job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED.                                                                                                                                                                                                                                                                 |
| gcp_display_name       | core | string        | Required. The display name of the HyperparameterTuningJob. The name can be up to 128 characters long and can consist of any UTF-8 characters.                                                                                                                                                                                                            |
| labels                 | core | array<string> | The labels with user-defined metadata to organize HyperparameterTuningJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| max_failed_trial_count | core | int64         | The number of failed Trials that need to be seen before failing the HyperparameterTuningJob. If set to 0, Vertex AI decides how many Trials must fail before the whole job fails.                                                                                                                                                                        |
| max_trial_count        | core | int64         | Required. The desired total number of Trials.                                                                                                                                                                                                                                                                                                            |
| name                   | core | string        | Output only. Resource name of the HyperparameterTuningJob.                                                                                                                                                                                                                                                                                               |
| organization_id        | core | string        |
| parallel_trial_count   | core | int64         | Required. The desired number of Trials to run in parallel.                                                                                                                                                                                                                                                                                               |
| parent                 | core | string        |
| project_id             | core | string        |
| project_number         | core | string        |
| region_id              | core | string        |
| resource_name          | core | string        |
| satisfies_pzi          | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                                                                    |
| satisfies_pzs          | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                                                                    |
| start_time             | core | timestamp     | Output only. Time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state.                                                                                                                                                                                                                                             |
| state                  | core | string        | Output only. The detailed state of the job.                                                                                                                                                                                                                                                                                                              |
| study_spec             | core | json          | Required. Study configuration of the HyperparameterTuningJob.                                                                                                                                                                                                                                                                                            |
| tags                   | core | hstore_csv    |
| trial_job_spec         | core | json          | Required. The spec of a trial job. The same spec applies to the CustomJobs created in all the trials.                                                                                                                                                                                                                                                    |
| trials                 | core | json          | Output only. Trials of the HyperparameterTuningJob.                                                                                                                                                                                                                                                                                                      |
| update_time            | core | timestamp     | Output only. Time when the HyperparameterTuningJob was most recently updated.                                                                                                                                                                                                                                                                            |
| zone_id                | core | string        |
