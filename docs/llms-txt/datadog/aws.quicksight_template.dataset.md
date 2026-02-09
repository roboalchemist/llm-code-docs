# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_template.dataset.md

---
title: QuickSight Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Template
---

# QuickSight Template

An AWS QuickSight Template is a reusable blueprint for creating dashboards and analyses in Amazon QuickSight. It captures the layout, visuals, and configurations of a dashboard without including the underlying data. Templates allow you to standardize reporting, share designs across accounts, and quickly deploy consistent analytics experiences.

```
aws.quicksight_template
```

## Fields

| Title      | ID   | Type       | Data Type                                                   | Description |
| ---------- | ---- | ---------- | ----------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| request_id | core | string     | The Amazon Web Services request ID for this operation.      |
| status     | core | int64      | The HTTP status of the request.                             |
| tags       | core | hstore_csv |
| template   | core | json       | The template structure for the object you want to describe. |
