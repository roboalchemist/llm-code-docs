# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_origin_request_policy.dataset.md

---
title: CloudFront Origin Request Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Origin Request Policy
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_origin_request_policy.dataset/index.html
---

# CloudFront Origin Request Policy

A CloudFront Origin Request Policy in AWS defines the information that CloudFront includes in requests it sends to your origin. It controls which headers, cookies, and query strings are forwarded, allowing you to optimize caching behavior and reduce unnecessary data transfer. This helps improve performance, security, and cost efficiency by ensuring only the required request data is passed to the origin.

```
aws.cloudfront_origin_request_policy
```

## Fields

| Title                 | ID   | Type   | Data Type                                         | Description |
| --------------------- | ---- | ------ | ------------------------------------------------- | ----------- |
| _key                  | core | string |
| account_id            | core | string |
| e_tag                 | core | string | The current version of the origin request policy. |
| origin_request_policy | core | json   | The origin request policy.                        |
| tags                  | core | hstore |
