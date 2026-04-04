# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_filter.dataset.md

---
title: Personalize Filter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Filter
---

# Personalize Filter

Personalize Filter in AWS is a resource used within Amazon Personalize to define filtering criteria for recommendations. It allows you to include or exclude specific items from recommendation results based on conditions you set, such as item attributes or user interactions. This helps tailor recommendations to business rules or user needs, ensuring more relevant and controlled outputs.

```
aws.personalize_filter
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                       | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| creation_date_time     | core | timestamp  | The time at which the filter was created.                                                                                                                                                                                       |
| dataset_group_arn      | core | string     | The ARN of the dataset group to which the filter belongs.                                                                                                                                                                       |
| failure_reason         | core | string     | If the filter failed, the reason for its failure.                                                                                                                                                                               |
| filter_arn             | core | string     | The ARN of the filter.                                                                                                                                                                                                          |
| filter_expression      | core | string     | Specifies the type of item interactions to filter out of recommendation results. The filter expression must follow specific format rules. For information about filter expression structure and syntax, see Filter expressions. |
| last_updated_date_time | core | timestamp  | The time at which the filter was last updated.                                                                                                                                                                                  |
| name                   | core | string     | The name of the filter.                                                                                                                                                                                                         |
| status                 | core | string     | The status of the filter.                                                                                                                                                                                                       |
| tags                   | core | hstore_csv |
