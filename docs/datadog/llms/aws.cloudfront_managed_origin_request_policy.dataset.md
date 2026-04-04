# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_managed_origin_request_policy.dataset.md

---
title: CloudFront Managed Origin Request Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > CloudFront Managed Origin Request
  Policy
---

# CloudFront Managed Origin Request Policy

A CloudFront Managed Origin Request Policy is a predefined configuration in Amazon CloudFront that controls the information included in requests sent from CloudFront to your origin. It specifies which headers, cookies, and query strings are forwarded, helping optimize cache behavior and reduce unnecessary data transfer. Managed policies are created and maintained by AWS, offering common configurations that simplify setup and ensure best practices without requiring custom policy creation.

```
aws.cloudfront_managed_origin_request_policy
```

## Fields

| Title                 | ID   | Type       | Data Type                                         | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| e_tag                 | core | string     | The current version of the origin request policy. |
| origin_request_policy | core | json       | The origin request policy.                        |
| tags                  | core | hstore_csv |
