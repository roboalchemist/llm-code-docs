# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_vod_assets.dataset.md

---
title: Mediapackage Vod Assets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediapackage Vod Assets
---

# Mediapackage Vod Assets

This table represents the mediapackage_vod_assets resource from Amazon Web Services.

```
aws.mediapackage_vod_assets
```

## Fields

| Title              | ID   | Type       | Data Type                                              | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The ARN of the Asset.                                  |
| created_at         | core | string     | The time the Asset was initially submitted for Ingest. |
| egress_endpoints   | core | json       | The list of egress endpoints available for the Asset.  |
| id                 | core | string     | The unique identifier for the Asset.                   |
| packaging_group_id | core | string     | The ID of the PackagingGroup for the Asset.            |
| resource_id        | core | string     | The resource ID to include in SPEKE key requests.      |
| source_arn         | core | string     | ARN of the source object in S3.                        |
| source_role_arn    | core | string     | The IAM role_arn used to access the source S3 bucket.  |
| tags               | core | hstore_csv |
