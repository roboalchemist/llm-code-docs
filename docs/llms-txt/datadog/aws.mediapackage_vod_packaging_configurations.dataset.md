# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_vod_packaging_configurations.dataset.md

---
title: Mediapackage Vod Packaging Configurations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Mediapackage Vod Packaging
  Configurations
---

# Mediapackage Vod Packaging Configurations

This table represents the mediapackage_vod_packaging_configurations resource from Amazon Web Services.

```
aws.mediapackage_vod_packaging_configurations
```

## Fields

| Title              | ID   | Type       | Data Type                                        | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The ARN of the PackagingConfiguration.           |
| cmaf_package       | core | json       |
| created_at         | core | string     | The time the PackagingConfiguration was created. |
| dash_package       | core | json       |
| hls_package        | core | json       |
| id                 | core | string     | The ID of the PackagingConfiguration.            |
| mss_package        | core | json       |
| packaging_group_id | core | string     | The ID of a PackagingGroup.                      |
| tags               | core | hstore_csv |
