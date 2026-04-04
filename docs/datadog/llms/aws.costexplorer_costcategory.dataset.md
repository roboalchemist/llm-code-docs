# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.costexplorer_costcategory.dataset.md

---
title: Costexplorer Cost Category
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Costexplorer Cost Category
---

# Costexplorer Cost Category

This table represents the Costexplorer Cost Category resource from Amazon Web Services.

```
aws.costexplorer_costcategory
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                           | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| cost_category_arn  | core | string     | The unique identifier for your Cost Category.                                                                                                                       |
| default_value      | core | string     |
| effective_end      | core | string     | The effective end date of your Cost Category.                                                                                                                       |
| effective_start    | core | string     | The effective start date of your Cost Category.                                                                                                                     |
| name               | core | string     |
| processing_status  | core | json       | The list of processing statuses for Cost Management products for a specific cost category.                                                                          |
| rule_version       | core | string     |
| rules              | core | json       | The rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value. |
| split_charge_rules | core | json       | The split charge rules that are used to allocate your charges between your Cost Category values.                                                                    |
| tags               | core | hstore_csv |
