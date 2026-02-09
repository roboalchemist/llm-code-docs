# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.resourceexplorer2_view.dataset.md

---
title: Resource Explorer View
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Resource Explorer View
---

# Resource Explorer View

Resource Explorer View in AWS provides a way to define and retrieve a specific view configuration for AWS Resource Explorer. A view determines which resources are included in search results and how they are filtered or grouped. This allows users to customize searches across accounts and regions, making it easier to discover and manage resources at scale.

```
aws.resourceexplorer2_view
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| filters             | core | json       | An array of SearchFilter objects that specify which resources can be included in the results of queries made using this view.                                                                                                                                                                                                                                                                                   |
| included_properties | core | json       | A structure that contains additional information about the view.                                                                                                                                                                                                                                                                                                                                                |
| last_updated_at     | core | timestamp  | The date and time when this view was last modified.                                                                                                                                                                                                                                                                                                                                                             |
| owner               | core | string     | The Amazon Web Services account that owns this view.                                                                                                                                                                                                                                                                                                                                                            |
| scope               | core | string     | An Amazon resource name (ARN) of an Amazon Web Services account, an organization, or an organizational unit (OU) that specifies whether this view includes resources from only the specified Amazon Web Services account, all accounts in the specified organization, or all accounts in the specified OU. If not specified, the value defaults to the Amazon Web Services account used to call this operation. |
| tags                | core | hstore_csv |
| view_arn            | core | string     | The Amazon resource name (ARN) of the view.                                                                                                                                                                                                                                                                                                                                                                     |
