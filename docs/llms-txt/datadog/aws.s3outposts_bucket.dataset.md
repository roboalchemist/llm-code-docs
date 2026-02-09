# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3outposts_bucket.dataset.md

---
title: S3 on Outposts Bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > S3 on Outposts Bucket
---

# S3 on Outposts Bucket

This table represents the S3 on Outposts Bucket resource from Amazon Web Services.

```
aws.s3outposts_bucket
```

## Fields

| Title                       | ID   | Type       | Data Type                                               | Description |
| --------------------------- | ---- | ---------- | ------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| bucket                      | core | string     | <p/>                                                    |
| bucket_arn                  | core | string     | The Amazon Resource Name (ARN) for the regional bucket. |
| creation_date               | core | timestamp  | The creation date of the regional bucket                |
| outpost_id                  | core | string     | The Outposts ID of the regional bucket.                 |
| public_access_block_enabled | core | bool       | <p/>                                                    |
| tags                        | core | hstore_csv |
