# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_field_level_encryption_profile.dataset.md

---
title: CloudFront Field-Level Encryption Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > CloudFront Field-Level Encryption
  Profile
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_field_level_encryption_profile.dataset/index.html
---

# CloudFront Field-Level Encryption Profile

A CloudFront Field-Level Encryption Profile in AWS defines the configuration used to encrypt specific data fields in HTTP requests before they reach your origin. It specifies the public key and encryption settings that CloudFront applies, ensuring sensitive information such as personal or financial data is protected in transit.

```
aws.cloudfront_field_level_encryption_profile
```

## Fields

| Title                          | ID   | Type   | Data Type                                                                                            | Description |
| ------------------------------ | ---- | ------ | ---------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string |
| account_id                     | core | string |
| e_tag                          | core | string | The current version of the field level encryption profile. For example: <code>E2QWRUHAPOMQZL</code>. |
| field_level_encryption_profile | core | json   | Return the field-level encryption profile information.                                               |
| tags                           | core | hstore |
