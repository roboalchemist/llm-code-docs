# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.resourceexplorer2_managed_view.dataset.md

---
title: Resource Explorer Managed View
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Resource Explorer Managed View
---

# Resource Explorer Managed View

Resource Explorer Managed View in AWS provides a predefined, read-only view of resources across your account. It helps you quickly search and discover resources without needing to create custom views. This managed view is automatically maintained by AWS and ensures consistent visibility into your environment.

```
aws.resourceexplorer2_managed_view
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                                                                                                                                                      | Description |
| ------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| filters             | core | json       | A search filter defines which resources can be part of a search query result set.                                                                                                                                                              |
| included_properties | core | json       | A structure that contains additional information about the managed view.                                                                                                                                                                       |
| last_updated_at     | core | timestamp  | The date and time when this managed view was last modified.                                                                                                                                                                                    |
| managed_view_arn    | core | string     | The Amazon resource name (ARN) of the managed view.                                                                                                                                                                                            |
| managed_view_name   | core | string     | The name of the managed view.                                                                                                                                                                                                                  |
| owner               | core | string     | The Amazon Web Services account that owns this managed view.                                                                                                                                                                                   |
| resource_policy     | core | string     | The resource policy that defines access to the managed view. To learn more about this policy, review Managed views.                                                                                                                            |
| scope               | core | string     | An Amazon resource name (ARN) of an Amazon Web Services account or organization that specifies whether this managed view includes resources from only the specified Amazon Web Services account or all accounts in the specified organization. |
| tags                | core | hstore_csv |
| trusted_service     | core | string     | The service principal of the Amazon Web Services service that created and manages the managed view.                                                                                                                                            |
| version             | core | string     | The version of the managed view.                                                                                                                                                                                                               |
