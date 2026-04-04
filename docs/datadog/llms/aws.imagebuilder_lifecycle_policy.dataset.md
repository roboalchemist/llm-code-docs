# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.imagebuilder_lifecycle_policy.dataset.md

---
title: Image Builder Lifecycle Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Image Builder Lifecycle Policy
---

# Image Builder Lifecycle Policy

Image Builder Lifecycle Policy in AWS defines rules for managing the lifecycle of images created with EC2 Image Builder. It allows you to automate the retention, expiration, and cleanup of images based on criteria such as age or count, helping reduce storage costs and maintain compliance by ensuring only relevant images are kept.

```
aws.imagebuilder_lifecycle_policy
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                          | Description |
| ------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The Amazon Resource Name (ARN) of the lifecycle policy resource.                                                                                   |
| date_created       | core | timestamp  | The timestamp when Image Builder created the lifecycle policy resource.                                                                            |
| date_last_run      | core | timestamp  | The timestamp for the last time Image Builder ran the lifecycle policy.                                                                            |
| date_updated       | core | timestamp  | The timestamp when Image Builder updated the lifecycle policy resource.                                                                            |
| description        | core | string     | Optional description for the lifecycle policy.                                                                                                     |
| execution_role     | core | string     | The name or Amazon Resource Name (ARN) of the IAM role that Image Builder uses to run the lifecycle policy. This is a custom role that you create. |
| name               | core | string     | The name of the lifecycle policy.                                                                                                                  |
| policy_details     | core | json       | The configuration details for a lifecycle policy resource.                                                                                         |
| resource_selection | core | json       | Resource selection criteria used to run the lifecycle policy.                                                                                      |
| resource_type      | core | string     | The type of resources the lifecycle policy targets.                                                                                                |
| status             | core | string     | Indicates whether the lifecycle policy resource is enabled.                                                                                        |
| tags               | core | hstore_csv |
