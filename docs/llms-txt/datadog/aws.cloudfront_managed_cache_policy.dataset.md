# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_managed_cache_policy.dataset.md

---
title: CloudFront Managed Cache Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Managed Cache Policy
---

# CloudFront Managed Cache Policy

A CloudFront Managed Cache Policy in AWS defines how CloudFront caches content based on request headers, cookies, and query strings. These managed policies are preconfigured by AWS to cover common caching scenarios, helping you optimize performance and reduce latency without needing to create custom policies. They simplify cache management and ensure best practices are applied consistently.

```
aws.cloudfront_managed_cache_policy
```

## Fields

| Title        | ID   | Type       | Data Type                                | Description |
| ------------ | ---- | ---------- | ---------------------------------------- | ----------- |
| _key         | core | string     |
| account_id   | core | string     |
| cache_policy | core | json       | The cache policy.                        |
| e_tag        | core | string     | The current version of the cache policy. |
| tags         | core | hstore_csv |
