# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_custom_permission.dataset.md

---
title: QuickSight Custom Permission
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Custom Permission
---

# QuickSight Custom Permission

This table represents the QuickSight Custom Permission resource from Amazon Web Services.

```
aws.quicksight_custom_permission
```

## Fields

| Title                   | ID   | Type       | Data Type                                                         | Description |
| ----------------------- | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| arn                     | core | string     | The Amazon Resource Name (ARN) of the custom permissions profile. |
| capabilities            | core | json       | A set of actions in the custom permissions profile.               |
| custom_permissions_name | core | string     | The name of the custom permissions profile.                       |
| tags                    | core | hstore_csv |
