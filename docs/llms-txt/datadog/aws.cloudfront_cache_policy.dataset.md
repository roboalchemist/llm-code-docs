# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_cache_policy.dataset.md

---
title: CloudFront Cache Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Cache Policy
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_cache_policy.dataset/index.html
---

# CloudFront Cache Policy

CloudFront Cache Policy in AWS defines how CloudFront caches content based on request headers, cookies, and query strings. It controls what values are included in the cache key and how long objects stay in the cache. By customizing cache policies, you can optimize performance, reduce origin load, and fine-tune content delivery behavior for different applications.

```
aws.cloudfront_cache_policy
```

## Fields

| Title        | ID   | Type   | Data Type                                | Description |
| ------------ | ---- | ------ | ---------------------------------------- | ----------- |
| _key         | core | string |
| account_id   | core | string |
| cache_policy | core | json   | The cache policy.                        |
| e_tag        | core | string | The current version of the cache policy. |
| tags         | core | hstore |
