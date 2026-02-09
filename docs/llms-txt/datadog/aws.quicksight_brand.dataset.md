# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_brand.dataset.md

---
title: QuickSight Brand
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Brand
---

# QuickSight Brand

QuickSight Brand in AWS refers to the branding configuration for Amazon QuickSight, which allows customization of the visual identity of dashboards and reports. It includes settings such as logos, color themes, and style elements that help align QuickSight assets with an organization's brand guidelines. This resource is typically used to provide a consistent look and feel across analytics content shared with users.

```
aws.quicksight_brand
```

## Fields

| Title            | ID   | Type       | Data Type                                              | Description |
| ---------------- | ---- | ---------- | ------------------------------------------------------ | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| brand_definition | core | json       | The definition of the brand.                           |
| brand_detail     | core | json       | The details of the brand.                              |
| request_id       | core | string     | The Amazon Web Services request ID for this operation. |
| tags             | core | hstore_csv |
