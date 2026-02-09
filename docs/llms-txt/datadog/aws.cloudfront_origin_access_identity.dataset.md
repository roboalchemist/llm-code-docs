# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_origin_access_identity.dataset.md

---
title: Amazon CloudFront Origin Access Identity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Amazon CloudFront Origin Access
  Identity
---

# Amazon CloudFront Origin Access Identity

Amazon CloudFront Origin Access Identity is a special CloudFront user that allows secure access to private content stored in Amazon S3. It ensures that only CloudFront can retrieve objects from the S3 bucket, preventing direct public access. This helps enforce content delivery through CloudFront while maintaining data privacy and security.

```
aws.cloudfront_origin_access_identity
```

## Fields

| Title                              | ID   | Type       | Data Type                                                                                                  | Description |
| ---------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string     |
| account_id                         | core | string     |
| cloud_front_origin_access_identity | core | json       | The origin access identity's information.                                                                  |
| e_tag                              | core | string     | The current version of the origin access identity's information. For example: <code>E2QWRUHAPOMQZL</code>. |
| tags                               | core | hstore_csv |
