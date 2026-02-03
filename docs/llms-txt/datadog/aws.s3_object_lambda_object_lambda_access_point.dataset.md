# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3_object_lambda_object_lambda_access_point.dataset.md

---
title: S3 Object Lambda Object Lambda Access Point
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > S3 Object Lambda Object Lambda
  Access Point
---

# S3 Object Lambda Object Lambda Access Point

This table represents the S3 Object Lambda Object Lambda Access Point resource from Amazon Web Services.

```
aws.s3_object_lambda_object_lambda_access_point
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                  | Description |
| --------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------ | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| alias                             | core | json       | The alias of the Object Lambda Access Point.                                               |
| creation_date                     | core | timestamp  | The date and time when the specified Object Lambda Access Point was created.               |
| name                              | core | string     | The name of the Object Lambda Access Point.                                                |
| public_access_block_configuration | core | json       | Configuration to block all public access. This setting is turned on and can not be edited. |
| tags                              | core | hstore_csv |
