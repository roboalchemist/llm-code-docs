# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.fis_experiment_template.dataset.md

---
title: AWS FIS Experiment Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS FIS Experiment Template
---

# AWS FIS Experiment Template

An AWS FIS Experiment Template defines the configuration for a Fault Injection Simulator experiment. It specifies the actions, targets, and stop conditions used to inject faults into AWS resources to test system resilience and recovery. The template can be reused to run consistent chaos engineering experiments safely.

```
aws.fis_experiment_template
```

## Fields

| Title                               | ID   | Type       | Data Type                                                               | Description |
| ----------------------------------- | ---- | ---------- | ----------------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| account_id                          | core | string     |
| actions                             | core | string     | The actions for the experiment.                                         |
| arn                                 | core | string     | The Amazon Resource Name (ARN) of the experiment template.              |
| creation_time                       | core | timestamp  | The time the experiment template was created.                           |
| description                         | core | string     | The description for the experiment template.                            |
| experiment_options                  | core | json       | The experiment options for an experiment template.                      |
| experiment_report_configuration     | core | json       | Describes the report configuration for the experiment template.         |
| id                                  | core | string     | The ID of the experiment template.                                      |
| last_update_time                    | core | timestamp  | The time the experiment template was last updated.                      |
| log_configuration                   | core | json       | The configuration for experiment logging.                               |
| role_arn                            | core | string     | The Amazon Resource Name (ARN) of an IAM role.                          |
| stop_conditions                     | core | json       | The stop conditions for the experiment.                                 |
| tags                                | core | hstore_csv |
| target_account_configurations_count | core | int64      | The count of target account configurations for the experiment template. |
| targets                             | core | string     | The targets for the experiment.                                         |
