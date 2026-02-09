# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_automljob.dataset.md

---
title: SageMaker AutoML Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker AutoML Job
---

# SageMaker AutoML Job

This table represents the SageMaker AutoML Job resource from Amazon Web Services.

```
aws.sagemaker_automljob
```

## Fields

| Title                               | ID   | Type       | Data Type                                                                                                                                                                                                                                       | Description |
| ----------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| account_id                          | core | string     |
| auto_ml_job_arn                     | core | string     | Returns the ARN of the AutoML job.                                                                                                                                                                                                              |
| auto_ml_job_artifacts               | core | json       | Returns information on the job's artifacts found in <code>AutoMLJobArtifacts</code>.                                                                                                                                                            |
| auto_ml_job_config                  | core | json       | Returns the configuration for the AutoML job.                                                                                                                                                                                                   |
| auto_ml_job_name                    | core | string     | Returns the name of the AutoML job.                                                                                                                                                                                                             |
| auto_ml_job_objective               | core | json       | Returns the job's objective.                                                                                                                                                                                                                    |
| auto_ml_job_secondary_status        | core | string     | Returns the secondary status of the AutoML job.                                                                                                                                                                                                 |
| auto_ml_job_status                  | core | string     | Returns the status of the AutoML job.                                                                                                                                                                                                           |
| best_candidate                      | core | json       | The best model candidate selected by SageMaker AI Autopilot using both the best objective metric and lowest <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html">InferenceLatency</a> for an experiment. |
| creation_time                       | core | timestamp  | Returns the creation time of the AutoML job.                                                                                                                                                                                                    |
| end_time                            | core | timestamp  | Returns the end time of the AutoML job.                                                                                                                                                                                                         |
| failure_reason                      | core | string     | Returns the failure reason for an AutoML job, when applicable.                                                                                                                                                                                  |
| generate_candidate_definitions_only | core | bool       | Indicates whether the output for an AutoML job generates candidate definitions only.                                                                                                                                                            |
| input_data_config                   | core | json       | Returns the input data configuration for the AutoML job.                                                                                                                                                                                        |
| last_modified_time                  | core | timestamp  | Returns the job's last modified time.                                                                                                                                                                                                           |
| model_deploy_config                 | core | json       | Indicates whether the model was deployed automatically to an endpoint and the name of that endpoint if deployed automatically.                                                                                                                  |
| model_deploy_result                 | core | json       | Provides information about endpoint for the model deployment.                                                                                                                                                                                   |
| output_data_config                  | core | json       | Returns the job's output data config.                                                                                                                                                                                                           |
| partial_failure_reasons             | core | json       | Returns a list of reasons for partial failures within an AutoML job.                                                                                                                                                                            |
| problem_type                        | core | string     | Returns the job's problem type.                                                                                                                                                                                                                 |
| resolved_attributes                 | core | json       | Contains <code>ProblemType</code>, <code>AutoMLJobObjective</code>, and <code>CompletionCriteria</code>. If you do not provide these values, they are inferred.                                                                                 |
| role_arn                            | core | string     | The ARN of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3.                                                                                                      |
| tags                                | core | hstore_csv |
