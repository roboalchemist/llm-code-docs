# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_inference_recommendations_job.dataset.md

---
title: SageMaker Inference Recommender Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Inference Recommender Job
---

# SageMaker Inference Recommender Job

SageMaker Inference Recommender Job is an AWS resource that helps optimize machine learning model deployment by automatically testing different instance types and configurations. It evaluates performance, cost, and latency to recommend the best inference setup for a given model. This reduces the manual effort of benchmarking and ensures efficient, cost-effective model serving in production.

```
aws.sagemaker_inference_recommendations_job
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                   | Description |
| ------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| completion_time           | core | timestamp  | A timestamp that shows when the job completed.                                                                                                                              |
| creation_time             | core | timestamp  | A timestamp that shows when the job was created.                                                                                                                            |
| endpoint_performances     | core | json       | The performance results from running an Inference Recommender job on an existing endpoint.                                                                                  |
| failure_reason            | core | string     | If the job fails, provides information why the job failed.                                                                                                                  |
| inference_recommendations | core | json       | The recommendations made by Inference Recommender.                                                                                                                          |
| input_config              | core | json       | Returns information about the versioned model package Amazon Resource Name (ARN), the traffic pattern, and endpoint configurations you provided when you initiated the job. |
| job_arn                   | core | string     | The Amazon Resource Name (ARN) of the job.                                                                                                                                  |
| job_description           | core | string     | The job description that you provided when you initiated the job.                                                                                                           |
| job_name                  | core | string     | The name of the job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.                                                       |
| job_type                  | core | string     | The job type that you provided when you initiated the job.                                                                                                                  |
| last_modified_time        | core | timestamp  | A timestamp that shows when the job was last modified.                                                                                                                      |
| role_arn                  | core | string     | The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role you provided when you initiated the job.                                |
| status                    | core | string     | The status of the job.                                                                                                                                                      |
| stopping_conditions       | core | json       | The stopping conditions that you provided when you initiated the job.                                                                                                       |
| tags                      | core | hstore_csv |
