# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotsitewise_dashboard.dataset.md

---
title: IoT SiteWise Dashboard
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT SiteWise Dashboard
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotsitewise_dashboard.dataset/index.html
---

# IoT SiteWise Dashboard

IoT SiteWise Dashboard in AWS is a managed visualization resource that lets you create and view dashboards for industrial IoT data collected through IoT SiteWise. It provides a way to monitor equipment, processes, and operations in real time using charts and visual widgets, without needing to build custom applications.

```
aws.iotsitewise_dashboard
```

## Fields

| Title                      | ID   | Type      | Data Type                                                                                                                            | Description |
| -------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                       | core | string    |
| account_id                 | core | string    |
| dashboard_arn              | core | string    | The ARN of the dashboard, which has the following format. arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId} |
| dashboard_creation_date    | core | timestamp | The date the dashboard was created, in Unix epoch time.                                                                              |
| dashboard_definition       | core | string    | The dashboard's definition JSON literal. For detailed information, see Creating dashboards (CLI) in the IoT SiteWise User Guide.     |
| dashboard_description      | core | string    | The dashboard's description.                                                                                                         |
| dashboard_id               | core | string    | The ID of the dashboard.                                                                                                             |
| dashboard_last_update_date | core | timestamp | The date the dashboard was last updated, in Unix epoch time.                                                                         |
| dashboard_name             | core | string    | The name of the dashboard.                                                                                                           |
| project_id                 | core | string    | The ID of the project that the dashboard is in.                                                                                      |
| tags                       | core | hstore    |
