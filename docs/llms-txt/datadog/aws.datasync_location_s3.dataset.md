# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_s3.dataset.md

---
title: DataSync Amazon S3 Location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync Amazon S3 Location
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.datasync_location_s3.dataset/index.html
---

# DataSync Amazon S3 Location

DataSync Amazon S3 Location represents a storage location in Amazon S3 that is used as a source or destination for AWS DataSync tasks. It defines the S3 bucket and optional subdirectory where data is transferred, along with configuration details such as IAM roles and S3 storage class. This resource enables secure, automated, and high-performance data movement between S3 and other supported storage systems.

```
aws.datasync_location_s3
```

## Fields

| Title            | ID   | Type          | Data Type                                                                                                                                                                                                                                                               | Description |
| ---------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string        |
| account_id       | core | string        |
| agent_arns       | core | array<string> | The ARNs of the DataSync agents deployed on your Outpost when using working with Amazon S3 on Outposts. For more information, see Deploy your DataSync agent on Outposts.                                                                                               |
| creation_time    | core | timestamp     | The time that the Amazon S3 location was created.                                                                                                                                                                                                                       |
| location_arn     | core | string        | The ARN of the Amazon S3 location.                                                                                                                                                                                                                                      |
| location_uri     | core | string        | The URL of the Amazon S3 location that was described.                                                                                                                                                                                                                   |
| s3_config        | core | json          | Specifies the Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that DataSync uses to access your S3 bucket. For more information, see Providing DataSync access to S3 buckets.                                                               |
| s3_storage_class | core | string        | When Amazon S3 is a destination location, this is the storage class that you chose for your objects. Some storage classes have behaviors that can affect your Amazon S3 storage costs. For more information, see Storage class considerations with Amazon S3 transfers. |
| tags             | core | hstore        |
