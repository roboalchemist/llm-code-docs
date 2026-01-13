# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appstream_app_block_builder.dataset.md

---
title: AppStream 2.0 App Block Builder
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppStream 2.0 App Block Builder
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.appstream_app_block_builder.dataset/index.html
---

# AppStream 2.0 App Block Builder

AppStream 2.0 App Block Builder is an AWS resource that lets you create and manage App Blocks, which package applications and dependencies for use with AppStream 2.0 fleets and stacks. It provides a managed environment to build, test, and maintain these application blocks, simplifying the process of delivering applications securely to end users without requiring local installation.

```
aws.appstream_app_block_builder
```

## Fields

| Title                          | ID   | Type      | Data Type                                                                                                                                                  | Description |
| ------------------------------ | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string    |
| access_endpoints               | core | json      | The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints. |
| account_id                     | core | string    |
| app_block_builder_errors       | core | json      | The app block builder errors.                                                                                                                              |
| arn                            | core | string    | The ARN of the app block builder.                                                                                                                          |
| created_time                   | core | timestamp | The creation time of the app block builder.                                                                                                                |
| description                    | core | string    | The description of the app block builder.                                                                                                                  |
| enable_default_internet_access | core | bool      | Indicates whether default internet access is enabled for the app block builder.                                                                            |
| iam_role_arn                   | core | string    | The ARN of the IAM role that is applied to the app block builder.                                                                                          |
| instance_type                  | core | string    | The instance type of the app block builder.                                                                                                                |
| name                           | core | string    | The name of the app block builder.                                                                                                                         |
| platform                       | core | string    | The platform of the app block builder. WINDOWS_SERVER_2019 is the only valid value.                                                                        |
| state                          | core | string    | The state of the app block builder.                                                                                                                        |
| state_change_reason            | core | json      | The state change reason.                                                                                                                                   |
| tags                           | core | hstore    |
| vpc_config                     | core | json      | The VPC configuration for the app block builder.                                                                                                           |
