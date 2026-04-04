# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.proton_environment_template.dataset.md

---
title: Proton Environment Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Proton Environment Template
---

# Proton Environment Template

An AWS Proton Environment Template defines the blueprint for creating and managing environments in AWS Proton. It specifies the infrastructure and shared resources that applications will run on, such as networking, compute, and monitoring configurations. Templates provide a standardized way for platform teams to define best practices and ensure consistency across multiple environments, while enabling application teams to quickly provision and deploy their workloads without needing to manage the underlying infrastructure details.

```
aws.proton_environment_template
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                      | Description |
| ------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| arn                 | core | string     | The Amazon Resource Name (ARN) of the environment template.                                                    |
| created_at          | core | timestamp  | The time when the environment template was created.                                                            |
| description         | core | string     | A description of the environment template.                                                                     |
| last_modified_at    | core | timestamp  | The time when the environment template was last modified.                                                      |
| name                | core | string     | The name of the environment template.                                                                          |
| provisioning        | core | string     | When included, indicates that the environment template is for customer provisioned and managed infrastructure. |
| recommended_version | core | string     | The ID of the recommended version of the environment template.                                                 |
| tags                | core | hstore_csv |
