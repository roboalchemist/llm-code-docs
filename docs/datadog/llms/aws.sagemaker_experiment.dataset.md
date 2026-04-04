# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_experiment.dataset.md

---
title: SageMaker Experiment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Experiment
---

# SageMaker Experiment

SageMaker Experiment in AWS is a resource that helps organize, track, and compare machine learning experiments. It allows you to group related training runs, capture metadata such as parameters, metrics, and artifacts, and manage them in a structured way. This makes it easier to reproduce results, analyze performance, and collaborate across teams.

```
aws.sagemaker_experiment
```

## Fields

| Title              | ID   | Type       | Data Type                                         | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| created_by         | core | json       | Who created the experiment.                       |
| creation_time      | core | timestamp  | When the experiment was created.                  |
| description        | core | string     | The description of the experiment.                |
| experiment_arn     | core | string     | The Amazon Resource Name (ARN) of the experiment. |
| experiment_name    | core | string     | The name of the experiment.                       |
| last_modified_by   | core | json       | Who last modified the experiment.                 |
| last_modified_time | core | timestamp  | When the experiment was last modified.            |
| tags               | core | hstore_csv |
