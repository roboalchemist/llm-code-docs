# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_theme.dataset.md

---
title: QuickSight Theme
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Theme
---

# QuickSight Theme

QuickSight Theme in AWS defines the visual style settings for Amazon QuickSight dashboards and analyses. It allows customization of colors, fonts, and layout elements to ensure consistent branding and user experience across reports. Themes can be applied to multiple dashboards, making it easier to maintain a unified look and feel.

```
aws.quicksight_theme
```

## Fields

| Title      | ID   | Type       | Data Type                                                | Description |
| ---------- | ---- | ---------- | -------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| request_id | core | string     | The Amazon Web Services request ID for this operation.   |
| status     | core | int64      | The HTTP status of the request.                          |
| tags       | core | hstore_csv |
| theme      | core | json       | The information about the theme that you are describing. |
