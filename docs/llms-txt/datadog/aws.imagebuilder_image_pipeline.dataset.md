# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.imagebuilder_image_pipeline.dataset.md

---
title: EC2 Image Builder Image Pipeline
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Image Builder Image Pipeline
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.imagebuilder_image_pipeline.dataset/index.html
---

# EC2 Image Builder Image Pipeline

An EC2 Image Builder Image Pipeline is a resource in AWS that automates the creation, management, and deployment of customized machine images. It defines the workflow for building images, including the source image, build components, tests, and distribution settings. The pipeline ensures images are kept up to date with the latest patches and configurations, reducing manual effort and improving consistency across environments.

```
aws.imagebuilder_image_pipeline
```

## Fields

| Title                            | ID   | Type   | Data Type                                                                                                                                                                                                                               | Description |
| -------------------------------- | ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string |
| account_id                       | core | string |
| arn                              | core | string | The Amazon Resource Name (ARN) of the image pipeline.                                                                                                                                                                                   |
| container_recipe_arn             | core | string | The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.                                                                                                                                                  |
| date_created                     | core | string | The date on which this image pipeline was created.                                                                                                                                                                                      |
| date_last_run                    | core | string | This is no longer supported, and does not return a value.                                                                                                                                                                               |
| date_next_run                    | core | string | The next date when the pipeline is scheduled to run.                                                                                                                                                                                    |
| date_updated                     | core | string | The date on which this image pipeline was last updated.                                                                                                                                                                                 |
| description                      | core | string | The description of the image pipeline.                                                                                                                                                                                                  |
| distribution_configuration_arn   | core | string | The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.                                                                                                                                   |
| enhanced_image_metadata_enabled  | core | bool   | Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default. |
| execution_role                   | core | string | The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.                                                                                                        |
| image_recipe_arn                 | core | string | The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.                                                                                                                                                 |
| image_scanning_configuration     | core | json   | Contains settings for vulnerability scans.                                                                                                                                                                                              |
| image_tests_configuration        | core | json   | The image tests configuration of the image pipeline.                                                                                                                                                                                    |
| infrastructure_configuration_arn | core | string | The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.                                                                                                                                 |
| name                             | core | string | The name of the image pipeline.                                                                                                                                                                                                         |
| platform                         | core | string | The platform of the image pipeline.                                                                                                                                                                                                     |
| schedule                         | core | json   | The schedule of the image pipeline.                                                                                                                                                                                                     |
| status                           | core | string | The status of the image pipeline.                                                                                                                                                                                                       |
| tags                             | core | hstore |
| workflows                        | core | json   | Contains the workflows that run for the image pipeline.                                                                                                                                                                                 |
