# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.databrew_job.dataset.md

---
title: Glue DataBrew Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Glue DataBrew Job
---

# Glue DataBrew Job

An AWS Glue DataBrew Job is a task that runs data preparation steps defined in a DataBrew project or recipe. It automates the process of cleaning, transforming, and normalizing data without writing code. Jobs can be scheduled or triggered on demand, and they output the processed data to Amazon S3 or other destinations for analytics, machine learning, or reporting.

```
aws.databrew_job
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                                                     | Description |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     | The ID of the Amazon Web Services account that owns the job.                                                                                                                                                                                                                  |
| create_date               | core | timestamp  | The date and time that the job was created.                                                                                                                                                                                                                                   |
| created_by                | core | string     | The Amazon Resource Name (ARN) of the user who created the job.                                                                                                                                                                                                               |
| data_catalog_outputs      | core | json       | One or more artifacts that represent the Glue Data Catalog output from running the job.                                                                                                                                                                                       |
| database_outputs          | core | json       | Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.                                                                                                                                               |
| dataset_name              | core | string     | A dataset that the job is to process.                                                                                                                                                                                                                                         |
| encryption_key_arn        | core | string     | The Amazon Resource Name (ARN) of an encryption key that is used to protect the job output. For more information, see Encrypting data written by DataBrew jobs                                                                                                                |
| encryption_mode           | core | string     | The encryption mode for the job, which can be one of the following: SSE-KMS - Server-side encryption with keys managed by KMS. SSE-S3 - Server-side encryption with keys managed by Amazon S3.                                                                                |
| job_sample                | core | json       | A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a JobSample value isn't provided, the default value is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter. |
| last_modified_by          | core | string     | The Amazon Resource Name (ARN) of the user who last modified the job.                                                                                                                                                                                                         |
| last_modified_date        | core | timestamp  | The modification date and time of the job.                                                                                                                                                                                                                                    |
| log_subscription          | core | string     | The current status of Amazon CloudWatch logging for the job.                                                                                                                                                                                                                  |
| max_capacity              | core | int64      | The maximum number of nodes that can be consumed when the job processes data.                                                                                                                                                                                                 |
| max_retries               | core | int64      | The maximum number of times to retry the job after a job run fails.                                                                                                                                                                                                           |
| name                      | core | string     | The unique name of the job.                                                                                                                                                                                                                                                   |
| outputs                   | core | json       | One or more artifacts that represent output from running the job.                                                                                                                                                                                                             |
| project_name              | core | string     | The name of the project that the job is associated with.                                                                                                                                                                                                                      |
| recipe_reference          | core | json       | A set of steps that the job runs.                                                                                                                                                                                                                                             |
| resource_arn              | core | string     | The unique Amazon Resource Name (ARN) for the job.                                                                                                                                                                                                                            |
| role_arn                  | core | string     | The Amazon Resource Name (ARN) of the role to be assumed for this job.                                                                                                                                                                                                        |
| tags                      | core | hstore_csv |
| timeout                   | core | int64      | The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of TIMEOUT.                                                                                                                                                       |
| type                      | core | string     | The job type of the job, which must be one of the following: PROFILE - A job to analyze a dataset, to determine its size, data types, data distribution, and more. RECIPE - A job to apply one or more transformations to a dataset.                                          |
| validation_configurations | core | json       | List of validation configurations that are applied to the profile job.                                                                                                                                                                                                        |
