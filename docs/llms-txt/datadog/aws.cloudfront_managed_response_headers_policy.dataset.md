# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_managed_response_headers_policy.dataset.md

---
title: CloudFront Managed Response Headers Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > CloudFront Managed Response Headers
  Policy
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_managed_response_headers_policy.dataset/index.html
---

# CloudFront Managed Response Headers Policy

A CloudFront Managed Response Headers Policy is a predefined configuration in Amazon CloudFront that automatically adds and manages common HTTP response headers for your distributions. These policies help improve security, privacy, and performance by standardizing headers such as security controls, CORS settings, and caching directives without requiring custom configuration.

```
aws.cloudfront_managed_response_headers_policy
```

## Fields

| Title                   | ID   | Type   | Data Type                                                                      | Description |
| ----------------------- | ---- | ------ | ------------------------------------------------------------------------------ | ----------- |
| _key                    | core | string |
| account_id              | core | string |
| e_tag                   | core | string | The version identifier for the current version of the response headers policy. |
| response_headers_policy | core | json   | Contains a response headers policy.                                            |
| tags                    | core | hstore |
