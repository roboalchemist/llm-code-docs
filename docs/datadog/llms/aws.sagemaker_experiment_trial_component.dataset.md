# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_experiment_trial_component.dataset.md

---
title: SageMaker Experiment Trial Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Experiment Trial Component
---

# SageMaker Experiment Trial Component

This table represents the SageMaker Experiment Trial Component resource from Amazon Web Services.

```
aws.sagemaker_experiment_trial_component
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                            | Description |
| -------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| created_by           | core | json       | Who created the trial component.                                                                                     |
| creation_time        | core | timestamp  | When the component was created.                                                                                      |
| end_time             | core | timestamp  | When the component ended.                                                                                            |
| input_artifacts      | core | string     | The input artifacts of the component.                                                                                |
| last_modified_by     | core | json       | Who last modified the component.                                                                                     |
| last_modified_time   | core | timestamp  | When the component was last modified.                                                                                |
| lineage_group_arn    | core | string     | The Amazon Resource Name (ARN) of the lineage group.                                                                 |
| metadata_properties  | core | json       |
| metrics              | core | json       | The metrics for the component.                                                                                       |
| output_artifacts     | core | string     | The output artifacts of the component.                                                                               |
| parameters           | core | string     | The hyperparameters of the component.                                                                                |
| sources              | core | json       | A list of ARNs and, if applicable, job types for multiple sources of an experiment run.                              |
| start_time           | core | timestamp  | When the component started.                                                                                          |
| status               | core | json       | The status of the component. States include: <ul> <li> InProgress </li> <li> Completed </li> <li> Failed </li> </ul> |
| tags                 | core | hstore_csv |
| trial_component_arn  | core | string     | The Amazon Resource Name (ARN) of the trial component.                                                               |
| trial_component_name | core | string     | The name of the trial component.                                                                                     |
