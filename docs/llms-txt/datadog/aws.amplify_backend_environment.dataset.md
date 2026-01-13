# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.amplify_backend_environment.dataset.md

---
title: Amplify Backend Environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amplify Backend Environment
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.amplify_backend_environment.dataset/index.html
---

# Amplify Backend Environment

An Amplify Backend Environment in AWS represents an isolated backend setup for an Amplify app, allowing developers to manage and deploy different stages such as development, testing, or production. It includes configurations for resources like authentication, APIs, storage, and functions, enabling teams to collaborate and iterate without affecting other environments.

```
aws.amplify_backend_environment
```

## Fields

| Title                   | ID   | Type      | Data Type                                                                                | Description |
| ----------------------- | ---- | --------- | ---------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string    |
| account_id              | core | string    |
| backend_environment_arn | core | string    | The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app. |
| create_time             | core | timestamp | The creation date and time for a backend environment that is part of an Amplify app.     |
| deployment_artifacts    | core | string    | The name of deployment artifacts.                                                        |
| environment_name        | core | string    | The name for a backend environment that is part of an Amplify app.                       |
| stack_name              | core | string    | The AWS CloudFormation stack name of a backend environment.                              |
| tags                    | core | hstore    |
| update_time             | core | timestamp | The last updated date and time for a backend environment that is part of an Amplify app. |
