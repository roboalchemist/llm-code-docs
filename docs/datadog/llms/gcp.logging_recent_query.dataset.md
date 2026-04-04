# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.logging_recent_query.dataset.md

---
title: Recent query in Logs Explorer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Recent query in Logs Explorer
---

# Recent query in Logs Explorer

Recent query in Logs Explorer in GCP allows users to quickly access and rerun their most recent log queries within the Cloud Logging interface. It helps streamline troubleshooting and analysis by saving time when investigating recurring issues or monitoring specific log patterns.

```
gcp.logging_recent_query
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                 | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| last_run_time        | core | timestamp     | Output only. The timestamp when this query was last run.                                                                                                                                                                                                                                                  |
| logging_query        | core | json          | Logging query that can be executed in Logs Explorer or via Logging API.                                                                                                                                                                                                                                   |
| name                 | core | string        | Output only. Resource name of the recent query.In the format: "projects/[PROJECT_ID]/locations/[LOCATION_ID]/recentQueries/[QUERY_ID]" For a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support)The QUERY_ID is a system generated alphanumeric ID. |
| ops_analytics_query  | core | json          | Analytics query that can be executed in Log Analytics.                                                                                                                                                                                                                                                    |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
