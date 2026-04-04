# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_experiment_trial.dataset.md

---
title: SageMaker Experiment Trial
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Experiment Trial
---

# SageMaker Experiment Trial

This table represents the SageMaker Experiment Trial resource from Amazon Web Services.

```
aws.sagemaker_experiment_trial
```

## Fields

| Title               | ID   | Type       | Data Type                                        | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------ | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| created_by          | core | json       | Who created the trial.                           |
| creation_time       | core | timestamp  | When the trial was created.                      |
| experiment_name     | core | string     | The name of the experiment the trial is part of. |
| last_modified_by    | core | json       | Who last modified the trial.                     |
| last_modified_time  | core | timestamp  | When the trial was last modified.                |
| metadata_properties | core | json       |
| tags                | core | hstore_csv |
| trial_arn           | core | string     | The Amazon Resource Name (ARN) of the trial.     |
| trial_name          | core | string     | The name of the trial.                           |
