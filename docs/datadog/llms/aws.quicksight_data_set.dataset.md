# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_data_set.dataset.md

---
title: QuickSight Data Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Data Set
---

# QuickSight Data Set

An AWS QuickSight Data Set is a collection of data that serves as the foundation for creating analyses, dashboards, and visualizations in Amazon QuickSight. It defines the structure, schema, and connection details of the underlying data sources, such as databases, files, or other AWS services. Data sets can include transformations, calculated fields, and joins, enabling users to prepare and model data for interactive business intelligence and reporting.

```
aws.quicksight_data_set
```

## Fields

| Title                                          | ID   | Type       | Data Type                                                                                       | Description |
| ---------------------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------- | ----------- |
| _key                                           | core | string     |
| account_id                                     | core | string     |
| arn                                            | core | string     | The Amazon Resource Name (ARN) of the dataset.                                                  |
| column_level_permission_rules_applied          | core | bool       | A value that indicates if the dataset has column level permission configured.                   |
| created_time                                   | core | timestamp  | The time that this dataset was created.                                                         |
| data_set                                       | core | json       | Information on the dataset.                                                                     |
| data_set_id                                    | core | string     | The ID of the dataset.                                                                          |
| import_mode                                    | core | string     | A value that indicates whether you want to import the data into SPICE.                          |
| last_updated_time                              | core | timestamp  | The last time that this dataset was updated.                                                    |
| name                                           | core | string     | A display name for the dataset.                                                                 |
| request_id                                     | core | string     | The Amazon Web Services request ID for this operation.                                          |
| row_level_permission_data_set                  | core | json       | The row-level security configuration for the dataset in the legacy data preparation experience. |
| row_level_permission_tag_configuration_applied | core | bool       | Whether or not the row level permission tags are applied.                                       |
| status                                         | core | int64      | The HTTP status of the request.                                                                 |
| tags                                           | core | hstore_csv |
| use_as                                         | core | string     | The usage of the dataset.                                                                       |
