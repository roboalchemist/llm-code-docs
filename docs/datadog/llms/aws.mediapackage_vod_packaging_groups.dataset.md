# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_vod_packaging_groups.dataset.md

---
title: Mediapackage Vod Packaging Groups
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediapackage Vod Packaging Groups
---

# Mediapackage Vod Packaging Groups

This table represents the mediapackage_vod_packaging_groups resource from Amazon Web Services.

```
aws.mediapackage_vod_packaging_groups
```

## Fields

| Title                   | ID   | Type       | Data Type                                                         | Description |
| ----------------------- | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| approximate_asset_count | core | int64      | The approximate asset count of the PackagingGroup.                |
| arn                     | core | string     | The ARN of the PackagingGroup.                                    |
| authorization           | core | json       |
| created_at              | core | string     | The time the PackagingGroup was created.                          |
| domain_name             | core | string     | The fully qualified domain name for Assets in the PackagingGroup. |
| egress_access_logs      | core | json       |
| id                      | core | string     | The ID of the PackagingGroup.                                     |
| tags                    | core | hstore_csv |
