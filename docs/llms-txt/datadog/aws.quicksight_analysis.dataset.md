# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_analysis.dataset.md

---
title: QuickSight Analysis
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Analysis
---

# QuickSight Analysis

QuickSight Analysis in AWS represents an interactive data visualization and reporting resource within Amazon QuickSight. It allows users to build, explore, and share dashboards by combining datasets, applying filters, and creating charts or tables. An analysis is the workspace where users design and refine insights before publishing them as dashboards for broader consumption.

```
aws.quicksight_analysis
```

## Fields

| Title      | ID   | Type       | Data Type                                                                                       | Description |
| ---------- | ---- | ---------- | ----------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| analysis   | core | json       | A metadata structure that contains summary information for the analysis that you're describing. |
| request_id | core | string     | The Amazon Web Services request ID for this operation.                                          |
| status     | core | int64      | Status associated with the analysis.                                                            |
| tags       | core | hstore_csv |
