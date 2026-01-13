# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_storage_configuration.dataset.md

---
title: Ivs Storage Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ivs Storage Configuration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ivs_storage_configuration.dataset/index.html
---

# Ivs Storage Configuration

This table represents the ivs_storage_configuration resource from Amazon Web Services.

```
aws.ivs_storage_configuration
```

## Fields

| Title      | ID   | Type   | Data Type                                                             | Description |
| ---------- | ---- | ------ | --------------------------------------------------------------------- | ----------- |
| _key       | core | string |
| account_id | core | string |
| arn        | core | string | ARN of the storage configuration.                                     |
| name       | core | string | Name of the storage configuration.                                    |
| s3         | core | json   | An S3 destination configuration where recorded videos will be stored. |
| tags       | core | hstore |
