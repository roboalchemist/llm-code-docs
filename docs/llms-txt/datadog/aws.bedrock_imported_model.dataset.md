# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_imported_model.dataset.md

---
title: Bedrock Imported Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Imported Model
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_imported_model.dataset/index.html
---

# Bedrock Imported Model

Bedrock Imported Model in AWS represents a foundation model that has been imported into Amazon Bedrock for use in applications. It provides details about the model's configuration, metadata, and availability, enabling developers to integrate and manage third-party or custom models within the Bedrock environment.

```
aws.bedrock_imported_model
```

## Fields

| Title              | ID   | Type      | Data Type                                                                  | Description |
| ------------------ | ---- | --------- | -------------------------------------------------------------------------- | ----------- |
| _key               | core | string    |
| account_id         | core | string    |
| creation_time      | core | timestamp | Creation time of the imported model.                                       |
| custom_model_units | core | json      | Information about the hardware utilization for a single copy of the model. |
| instruct_supported | core | bool      | Specifies if the imported model supports converse.                         |
| job_arn            | core | string    | Job Amazon Resource Name (ARN) associated with the imported model.         |
| job_name           | core | string    | Job name associated with the imported model.                               |
| model_architecture | core | string    | The architecture of the imported model.                                    |
| model_arn          | core | string    | The Amazon Resource Name (ARN) associated with this imported model.        |
| model_data_source  | core | json      | The data source for this imported model.                                   |
| model_kms_key_arn  | core | string    | The imported model is encrypted at rest using this key.                    |
| model_name         | core | string    | The name of the imported model.                                            |
| tags               | core | hstore    |
