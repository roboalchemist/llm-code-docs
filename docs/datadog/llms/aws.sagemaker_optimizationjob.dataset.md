# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_optimizationjob.dataset.md

---
title: SageMaker Optimization Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Optimization Job
---

# SageMaker Optimization Job

This table represents the SageMaker Optimization Job resource from Amazon Web Services.

```
aws.sagemaker_optimizationjob
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                      | Description |
| ------------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| creation_time            | core | timestamp  | The time when you created the optimization job.                                                |
| deployment_instance_type | core | string     | The type of instance that hosts the optimized model that you create with the optimization job. |
| failure_reason           | core | string     | If the optimization job status is <code>FAILED</code>, the reason for the failure.             |
| last_modified_time       | core | timestamp  | The time when the optimization job was last updated.                                           |
| model_source             | core | json       | The location of the source model to optimize with an optimization job.                         |
| optimization_configs     | core | json       | Settings for each of the optimization techniques that the job applies.                         |
| optimization_end_time    | core | timestamp  | The time when the optimization job finished processing.                                        |
| optimization_environment | core | hstore     | The environment variables to set in the model container.                                       |
| optimization_job_arn     | core | string     | The Amazon Resource Name (ARN) of the optimization job.                                        |
| optimization_job_name    | core | string     | The name that you assigned to the optimization job.                                            |
| optimization_job_status  | core | string     | The current status of the optimization job.                                                    |
| optimization_output      | core | json       | Output values produced by an optimization job.                                                 |
| optimization_start_time  | core | timestamp  | The time when the optimization job started.                                                    |
| output_config            | core | json       | Details for where to store the optimized model that you create with the optimization job.      |
| role_arn                 | core | string     | The ARN of the IAM role that you assigned to the optimization job.                             |
| stopping_condition       | core | json       |
| tags                     | core | hstore_csv |
| vpc_config               | core | json       | A VPC in Amazon VPC that your optimized model has access to.                                   |
