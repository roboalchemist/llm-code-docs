# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_user_profile.dataset.md

---
title: SageMaker User Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker User Profile
---

# SageMaker User Profile

SageMaker User Profile is a resource in Amazon SageMaker that represents an individual user's settings and configurations within a SageMaker Domain. It defines user-specific preferences such as execution roles, security settings, and application access. This allows organizations to manage multiple users in a shared SageMaker environment while maintaining personalized workspaces and permissions.

```
aws.sagemaker_user_profile
```

## Fields

| Title                          | ID   | Type       | Data Type                                                              | Description |
| ------------------------------ | ---- | ---------- | ---------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| creation_time                  | core | timestamp  | The creation time.                                                     |
| domain_id                      | core | string     | The ID of the domain that contains the profile.                        |
| failure_reason                 | core | string     | The failure reason.                                                    |
| home_efs_file_system_uid       | core | string     | The ID of the user's profile in the Amazon Elastic File System volume. |
| last_modified_time             | core | timestamp  | The last modified time.                                                |
| single_sign_on_user_identifier | core | string     | The IAM Identity Center user identifier.                               |
| single_sign_on_user_value      | core | string     | The IAM Identity Center user value.                                    |
| status                         | core | string     | The status.                                                            |
| tags                           | core | hstore_csv |
| user_profile_arn               | core | string     | The user profile Amazon Resource Name (ARN).                           |
| user_profile_name              | core | string     | The user profile name.                                                 |
| user_settings                  | core | json       | A collection of settings.                                              |
