# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_response_headers_policy.dataset.md

---
title: CloudFront Response Headers Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Response Headers Policy
---

# CloudFront Response Headers Policy

CloudFront Response Headers Policy in AWS defines a set of HTTP headers that CloudFront automatically adds to responses it delivers to viewers. This allows you to control security headers, CORS settings, and custom headers consistently across your distributions without modifying the origin. It helps improve security, compliance, and performance by standardizing response behavior.

```
aws.cloudfront_response_headers_policy
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                      | Description |
| ----------------------- | ---- | ---------- | ------------------------------------------------------------------------------ | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| e_tag                   | core | string     | The version identifier for the current version of the response headers policy. |
| response_headers_policy | core | json       | Contains a response headers policy.                                            |
| tags                    | core | hstore_csv |
