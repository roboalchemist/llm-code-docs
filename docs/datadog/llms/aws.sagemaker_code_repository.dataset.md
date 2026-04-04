# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_code_repository.dataset.md

---
title: SageMaker Code Repository
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Code Repository
---

# SageMaker Code Repository

SageMaker Code Repository in AWS is a managed integration that connects Amazon SageMaker with source code repositories such as AWS CodeCommit, GitHub, or Bitbucket. It allows you to store, version, and manage machine learning training scripts and related code directly within SageMaker. This makes it easier to track changes, collaborate with teams, and ensure reproducibility of experiments and models.

```
aws.sagemaker_code_repository
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                                                                      | Description |
| -------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| code_repository_arn  | core | string     | The Amazon Resource Name (ARN) of the Git repository.                                                                                                                                                          |
| code_repository_name | core | string     | The name of the Git repository.                                                                                                                                                                                |
| creation_time        | core | timestamp  | The date and time that the Git repository was created.                                                                                                                                                         |
| git_config           | core | json       | Configuration details for the Git repository, including the URL where it is located and the ARN of the Amazon Web Services Secrets Manager secret that contains the credentials used to access the repository. |
| last_modified_time   | core | timestamp  | The date and time that the Git repository was last modified.                                                                                                                                                   |
| tags                 | core | hstore_csv |
