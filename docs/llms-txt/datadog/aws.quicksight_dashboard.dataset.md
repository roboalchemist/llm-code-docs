# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_dashboard.dataset.md

---
title: QuickSight Dashboard
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Dashboard
---

# QuickSight Dashboard

An AWS QuickSight Dashboard is an interactive, shareable visualization that presents data insights through charts, graphs, and tables. It allows users to explore and analyze datasets in real time, enabling better decision-making. Dashboards can be customized, secured with permissions, and embedded into applications or portals for broader access.

```
aws.quicksight_dashboard
```

## Fields

| Title      | ID   | Type       | Data Type                                              | Description |
| ---------- | ---- | ---------- | ------------------------------------------------------ | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| dashboard  | core | json       | Information about the dashboard.                       |
| request_id | core | string     | The Amazon Web Services request ID for this operation. |
| status     | core | int64      | The HTTP status of this request.                       |
| tags       | core | hstore_csv |
