# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_key_group.dataset.md

---
title: CloudFront Key Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Key Group
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_key_group.dataset/index.html
---

# CloudFront Key Group

A CloudFront Key Group is a collection of public keys that you can use with signed URLs or signed cookies to control access to your CloudFront content. By grouping keys, you can manage and rotate them more easily, ensuring secure distribution of private content while simplifying key management for trusted signers.

```
aws.cloudfront_key_group
```

## Fields

| Title                    | ID   | Type      | Data Type                                               | Description |
| ------------------------ | ---- | --------- | ------------------------------------------------------- | ----------- |
| _key                     | core | string    |
| account_id               | core | string    |
| cloudfront_key_group_arn | core | string    |
| id                       | core | string    | The identifier for the key group.                       |
| key_group_config         | core | json      | The key group configuration.                            |
| last_modified_time       | core | timestamp | The date and time when the key group was last modified. |
| tags                     | core | hstore    |
