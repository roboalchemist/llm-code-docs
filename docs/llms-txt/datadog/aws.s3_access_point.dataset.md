# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3_access_point.dataset.md

---
title: S3 Access Point
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > S3 Access Point
---

# S3 Access Point

This table represents the S3 Access Point resource from Amazon Web Services.

```
aws.s3_access_point
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| access_point_arn  | core | string     | The ARN for the access point.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| account_id        | core | string     |
| alias             | core | string     | The name or alias of the access point.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| bucket            | core | string     | The name of the bucket associated with this access point.                                                                                                                                                                                                                                                                                                                                                                                                      |
| bucket_account_id | core | string     | The Amazon Web Services account ID associated with the S3 bucket associated with this access point.                                                                                                                                                                                                                                                                                                                                                            |
| name              | core | string     | The name of this access point.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| network_origin    | core | string     | Indicates whether this access point allows access from the public internet. If <code>VpcConfiguration</code> is specified for this access point, then <code>NetworkOrigin</code> is <code>VPC</code>, and the access point doesn't allow access from the public internet. Otherwise, <code>NetworkOrigin</code> is <code>Internet</code>, and the access point allows access from the public internet, subject to the access point and bucket access policies. |
| tags              | core | hstore_csv |
| vpc_configuration | core | json       | The virtual private cloud (VPC) configuration for this access point, if one exists. <note> This element is empty if this access point is an Amazon S3 on Outposts access point that is used by other Amazon Web Services. </note>                                                                                                                                                                                                                              |
