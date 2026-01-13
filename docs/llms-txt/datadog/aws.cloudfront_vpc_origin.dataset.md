# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudfront_vpc_origin.dataset.md

---
title: CloudFront VPC Origin
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFront VPC Origin
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudfront_vpc_origin.dataset/index.html
---

# CloudFront VPC Origin

CloudFront VPC Origin allows Amazon CloudFront to securely connect to resources inside a Virtual Private Cloud (VPC) as the origin for content delivery. This enables distribution of private content hosted within a VPC without exposing it directly to the public internet, improving security and control.

```
aws.cloudfront_vpc_origin
```

## Fields

| Title      | ID   | Type   | Data Type            | Description |
| ---------- | ---- | ------ | -------------------- | ----------- |
| _key       | core | string |
| account_id | core | string |
| e_tag      | core | string | The VPC origin ETag. |
| tags       | core | hstore |
| vpc_origin | core | json   | The VPC origin.      |
