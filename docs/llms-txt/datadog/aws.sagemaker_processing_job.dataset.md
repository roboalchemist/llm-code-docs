# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_processing_job.dataset.md

---
title: SageMaker Processing Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Processing Job
---

# SageMaker Processing Job

An AWS SageMaker Processing Job is a managed resource that lets you run data processing and model evaluation workloads at scale. It provides a fully managed environment to preprocess data, perform feature engineering, evaluate models, or run custom scripts using containerized code. The job runs on specified compute instances, automatically handles resource provisioning, and stores outputs in Amazon S3.

```
aws.sagemaker_processing_job
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                           | Description |
| ------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| app_specification        | core | json       | Configures the processing job to run a specified container image.                                                                                                   |
| auto_ml_job_arn          | core | string     | The ARN of an AutoML job associated with this processing job.                                                                                                       |
| creation_time            | core | timestamp  | The time at which the processing job was created.                                                                                                                   |
| environment              | core | hstore     | The environment variables set in the Docker container.                                                                                                              |
| exit_message             | core | string     | An optional string, up to one KB in size, that contains metadata from the processing container when the processing job exits.                                       |
| experiment_config        | core | json       | The configuration information used to create an experiment.                                                                                                         |
| failure_reason           | core | string     | A string, up to one KB in size, that contains the reason a processing job failed, if it failed.                                                                     |
| last_modified_time       | core | timestamp  | The time at which the processing job was last modified.                                                                                                             |
| monitoring_schedule_arn  | core | string     | The ARN of a monitoring schedule for an endpoint associated with this processing job.                                                                               |
| network_config           | core | json       | Networking options for a processing job.                                                                                                                            |
| processing_end_time      | core | timestamp  | The time at which the processing job completed.                                                                                                                     |
| processing_inputs        | core | json       | The inputs for a processing job.                                                                                                                                    |
| processing_job_arn       | core | string     | The Amazon Resource Name (ARN) of the processing job.                                                                                                               |
| processing_job_name      | core | string     | The name of the processing job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.                                    |
| processing_job_status    | core | string     | Provides the status of a processing job.                                                                                                                            |
| processing_output_config | core | json       | Output configuration for the processing job.                                                                                                                        |
| processing_resources     | core | json       | Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance. |
| processing_start_time    | core | timestamp  | The time at which the processing job started.                                                                                                                       |
| role_arn                 | core | string     | The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.                                                     |
| stopping_condition       | core | json       | The time limit for how long the processing job is allowed to run.                                                                                                   |
| tags                     | core | hstore_csv |
| training_job_arn         | core | string     | The ARN of a training job associated with this processing job.                                                                                                      |
