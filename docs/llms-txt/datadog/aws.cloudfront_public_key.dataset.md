# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_public_key.dataset.md

---
title: CloudFront Public Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Public Key
---

# CloudFront Public Key

A CloudFront Public Key is a resource used to validate signed URLs and signed cookies in Amazon CloudFront. It represents the public portion of a key pair that works with a corresponding private key to control access to content. By associating a public key with a CloudFront key group, you can enforce secure content delivery and ensure that only requests signed with the matching private key are authorized.

```
aws.cloudfront_public_key
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                               | Description |
| ------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| cloudfront_public_key_arn | core | string     |
| comment                   | core | string     | A comment to describe the public key. The comment cannot be longer than 128 characters. |
| created_time              | core | timestamp  | The date and time when the public key was uploaded.                                     |
| id                        | core | string     | The identifier of the public key.                                                       |
| name                      | core | string     | A name to help identify the public key.                                                 |
| tags                      | core | hstore_csv |
