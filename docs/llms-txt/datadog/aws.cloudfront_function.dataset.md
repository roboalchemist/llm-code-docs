# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_function.dataset.md

---
title: CloudFront Function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront Function
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_function.dataset/index.html
---

# CloudFront Function

CloudFront Function is a lightweight, serverless code execution environment in Amazon CloudFront. It allows you to run JavaScript functions at CloudFront edge locations to customize content delivery with low latency. Common use cases include URL rewrites, header manipulation, access control, and request or response modifications. It is optimized for high performance and cost efficiency, making it suitable for simple, short-running logic close to users.

```
aws.cloudfront_function
```

## Fields

| Title             | ID   | Type   | Data Type                                                       | Description |
| ----------------- | ---- | ------ | --------------------------------------------------------------- | ----------- |
| _key              | core | string |
| account_id        | core | string |
| function_arn      | core | string |
| function_config   | core | json   | Contains configuration information about a CloudFront function. |
| function_metadata | core | json   | Contains metadata about a CloudFront function.                  |
| name              | core | string | The name of the CloudFront function.                            |
| status            | core | string | The status of the CloudFront function.                          |
| tags              | core | hstore |
