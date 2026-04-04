# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.fis_experiment.dataset.md

---
title: AWS Fault Injection Simulator Experiment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > AWS Fault Injection Simulator
  Experiment
---

# AWS Fault Injection Simulator Experiment

AWS Fault Injection Simulator Experiment is a managed service resource that allows users to run controlled chaos engineering experiments on AWS workloads. It helps identify weaknesses by injecting faults such as latency, instance termination, or API throttling into applications. The experiment defines actions, targets, and stop conditions to safely test system resilience and improve reliability.

```
aws.fis_experiment
```

## Fields

| Title                               | ID   | Type       | Data Type                                                                                                                       | Description |
| ----------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| account_id                          | core | string     |
| actions                             | core | string     | The actions for the experiment.                                                                                                 |
| arn                                 | core | string     | The Amazon Resource Name (ARN) of the experiment.                                                                               |
| creation_time                       | core | timestamp  | The time that the experiment was created.                                                                                       |
| end_time                            | core | timestamp  | The time that the experiment ended.                                                                                             |
| experiment_options                  | core | json       | The experiment options for the experiment.                                                                                      |
| experiment_report                   | core | json       | The experiment report for the experiment.                                                                                       |
| experiment_report_configuration     | core | json       | The experiment report configuration for the experiment.                                                                         |
| experiment_template_id              | core | string     | The ID of the experiment template.                                                                                              |
| id                                  | core | string     | The ID of the experiment.                                                                                                       |
| log_configuration                   | core | json       | The configuration for experiment logging.                                                                                       |
| role_arn                            | core | string     | The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf. |
| start_time                          | core | timestamp  | The time that the experiment started.                                                                                           |
| state                               | core | json       | The state of the experiment.                                                                                                    |
| stop_conditions                     | core | json       | The stop conditions for the experiment.                                                                                         |
| tags                                | core | hstore_csv |
| target_account_configurations_count | core | int64      | The count of target account configurations for the experiment.                                                                  |
| targets                             | core | string     | The targets for the experiment.                                                                                                 |
