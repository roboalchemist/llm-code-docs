# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.comprehend_flywheel.dataset.md

---
title: Comprehend Flywheel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Comprehend Flywheel
---

# Comprehend Flywheel

Comprehend Flywheel in AWS is a managed resource that helps organize and manage the lifecycle of custom natural language processing models built with Amazon Comprehend. It allows you to group related models, datasets, and training configurations into a single entity, making it easier to retrain, update, and deploy models consistently over time.

```
aws.comprehend_flywheel
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                            | Description |
| ------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| active_model_arn          | core | string     | The Amazon Resource Number (ARN) of the active model version.                                                        |
| creation_time             | core | timestamp  | Creation time of the flywheel.                                                                                       |
| data_access_role_arn      | core | string     | The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data. |
| data_lake_s3_uri          | core | string     | Amazon S3 URI of the data lake location.                                                                             |
| data_security_config      | core | json       | Data security configuration.                                                                                         |
| flywheel_arn              | core | string     | The Amazon Resource Number (ARN) of the flywheel.                                                                    |
| last_modified_time        | core | timestamp  | Last modified time for the flywheel.                                                                                 |
| latest_flywheel_iteration | core | string     | The most recent flywheel iteration.                                                                                  |
| message                   | core | string     | A description of the status of the flywheel.                                                                         |
| model_type                | core | string     | Model type of the flywheel's model.                                                                                  |
| status                    | core | string     | The status of the flywheel.                                                                                          |
| tags                      | core | hstore_csv |
| task_config               | core | json       | Configuration about the model associated with a flywheel.                                                            |
