# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_blueprint.dataset.md

---
title: Bedrock Blueprint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Blueprint
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_blueprint.dataset/index.html
---

# Bedrock Blueprint

This table represents the Bedrock Blueprint resource from Amazon Web Services.

```
aws.bedrock_blueprint
```

## Fields

| Title                  | ID   | Type      | Data Type | Description |
| ---------------------- | ---- | --------- | --------- | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| blueprint_arn          | core | string    |
| blueprint_name         | core | string    |
| blueprint_stage        | core | string    |
| blueprint_version      | core | string    |
| creation_time          | core | timestamp |
| kms_encryption_context | core | hstore    |
| kms_key_id             | core | string    |
| last_modified_time     | core | timestamp |
| schema                 | core | string    |
| tags                   | core | hstore    |
| type                   | core | string    |
