# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_mlflow_tracking_server.dataset.md

---
title: SageMaker MLflow Tracking Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker MLflow Tracking Server
---

# SageMaker MLflow Tracking Server

The SageMaker MLflow Tracking Server is a managed service in AWS that integrates MLflow with Amazon SageMaker. It provides a centralized tracking server for logging, organizing, and querying machine learning experiment metadata such as parameters, metrics, and artifacts. This allows data scientists and ML engineers to manage experiments at scale without the overhead of deploying and maintaining their own MLflow infrastructure.

```
aws.sagemaker_mlflow_tracking_server
```

## Fields

| Title                              | ID   | Type       | Data Type                                                                                                                                                | Description |
| ---------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string     |
| account_id                         | core | string     |
| artifact_store_uri                 | core | string     | The S3 URI of the general purpose bucket used as the MLflow Tracking Server artifact store.                                                              |
| automatic_model_registration       | core | bool       | Whether automatic registration of new MLflow models to the SageMaker Model Registry is enabled.                                                          |
| created_by                         | core | json       | Information about the user who created or modified a SageMaker resource.                                                                                 |
| creation_time                      | core | timestamp  | The timestamp of when the described MLflow Tracking Server was created.                                                                                  |
| is_active                          | core | string     | Whether the described MLflow Tracking Server is currently active.                                                                                        |
| last_modified_by                   | core | json       | Information about the user who created or modified a SageMaker resource.                                                                                 |
| last_modified_time                 | core | timestamp  | The timestamp of when the described MLflow Tracking Server was last modified.                                                                            |
| mlflow_version                     | core | string     | The MLflow version used for the described tracking server.                                                                                               |
| role_arn                           | core | string     | The Amazon Resource Name (ARN) for an IAM role in your account that the described MLflow Tracking Server uses to access the artifact store in Amazon S3. |
| tags                               | core | hstore_csv |
| tracking_server_arn                | core | string     | The ARN of the described tracking server.                                                                                                                |
| tracking_server_maintenance_status | core | string     | The current maintenance status of the described MLflow Tracking Server.                                                                                  |
| tracking_server_name               | core | string     | The name of the described tracking server.                                                                                                               |
| tracking_server_size               | core | string     | The size of the described tracking server.                                                                                                               |
| tracking_server_status             | core | string     | The current creation status of the described MLflow Tracking Server.                                                                                     |
| tracking_server_url                | core | string     | The URL to connect to the MLflow user interface for the described tracking server.                                                                       |
| weekly_maintenance_window_start    | core | string     | The day and time of the week when weekly maintenance occurs on the described tracking server.                                                            |
