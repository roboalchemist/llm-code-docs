# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_field_level_encryption_config.dataset.md

---
title: CloudFront Field-Level Encryption Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > CloudFront Field-Level Encryption
  Configuration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_field_level_encryption_config.dataset/index.html
---

# CloudFront Field-Level Encryption Configuration

CloudFront Field-Level Encryption Configuration in AWS defines how sensitive data in HTTP requests is protected at the edge. It allows you to specify which fields in a request should be encrypted using public key encryption before being forwarded to your origin. This ensures that only authorized applications with the corresponding private key can decrypt and access the protected data, helping maintain compliance and security for sensitive information such as personal identifiers or payment details.

```
aws.cloudfront_field_level_encryption_config
```

## Fields

| Title                         | ID   | Type   | Data Type                                                                                                  | Description |
| ----------------------------- | ---- | ------ | ---------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string |
| account_id                    | core | string |
| e_tag                         | core | string | The current version of the field level encryption configuration. For example: <code>E2QWRUHAPOMQZL</code>. |
| field_level_encryption_config | core | json   | Return the field-level encryption configuration information.                                               |
| tags                          | core | hstore |
