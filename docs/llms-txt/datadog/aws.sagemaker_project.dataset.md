# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_project.dataset.md

---
title: SageMaker Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Project
---

# SageMaker Project

SageMaker Project in AWS is a managed resource that helps set up and organize machine learning initiatives by providing pre-configured templates and best practices. It streamlines the creation of ML environments, enabling teams to quickly establish standardized workflows, integrate with CI/CD pipelines, and manage governance. This resource supports collaboration and consistency across ML development and deployment.

```
aws.sagemaker_project
```

## Fields

| Title                                       | ID   | Type       | Data Type                                                                                                                  | Description |
| ------------------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                        | core | string     |
| account_id                                  | core | string     |
| created_by                                  | core | json       | Information about the user who created or modified a SageMaker resource.                                                   |
| creation_time                               | core | timestamp  | The time when the project was created.                                                                                     |
| last_modified_by                            | core | json       | Information about the user who created or modified a SageMaker resource.                                                   |
| last_modified_time                          | core | timestamp  | The timestamp when project was last modified.                                                                              |
| project_arn                                 | core | string     | The Amazon Resource Name (ARN) of the project.                                                                             |
| project_description                         | core | string     | The description of the project.                                                                                            |
| project_id                                  | core | string     | The ID of the project.                                                                                                     |
| project_name                                | core | string     | The name of the project.                                                                                                   |
| project_status                              | core | string     | The status of the project.                                                                                                 |
| service_catalog_provisioned_product_details | core | json       | Information about a provisioned service catalog product.                                                                   |
| service_catalog_provisioning_details        | core | json       | Information used to provision a service catalog product. For information, see What is Amazon Web Services Service Catalog. |
| tags                                        | core | hstore_csv |
| template_provider_details                   | core | json       | An array of template providers associated with the project.                                                                |
