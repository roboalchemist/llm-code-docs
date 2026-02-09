# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3express_bucket.dataset.md

---
title: S3 Express One Zone Bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > S3 Express One Zone Bucket
---

# S3 Express One Zone Bucket

S3 Express One Zone Bucket is a high-performance Amazon S3 storage option designed for workloads that need very low latency and high request rates. Data is stored in a single Availability Zone, making it cost-effective compared to multi-zone storage, but with less redundancy. It is ideal for applications that require fast access to frequently changing data, such as analytics or machine learning, where durability across multiple zones is not critical.

```
aws.s3express_bucket
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                                                                                                                | Description |
| ------------------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                 | core | string     |
| account_id                           | core | string     |
| bucket_region                        | core | string     | BucketRegion indicates the Amazon Web Services region where the bucket is located. If the request contains at least one valid parameter, it is included in the response. |
| creation_date                        | core | timestamp  | Date the bucket was created. This date can change when making changes to your bucket, such as editing its bucket policy.                                                 |
| name                                 | core | string     | The name of the bucket.                                                                                                                                                  |
| policy                               | core | string     | The bucket policy as a JSON document.                                                                                                                                    |
| server_side_encryption_configuration | core | json       | Specifies the default server-side-encryption configuration.                                                                                                              |
| tags                                 | core | hstore_csv |
