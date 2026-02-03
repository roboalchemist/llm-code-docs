# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.logging_saved_query.dataset.md

---
title: Logging Saved Query
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Logging Saved Query
---

# Logging Saved Query

A Logging Saved Query in Google Cloud is a reusable query definition that allows users to store and manage log queries in Cloud Logging. It helps streamline log analysis by saving frequently used queries for quick access, sharing, and consistent monitoring across projects or teams.

```
gcp.logging_saved_query
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The timestamp when the saved query was created.                                                                                                                                                                                                                                                                                                                                                             |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. A human readable description of the saved query.                                                                                                                                                                                                                                                                                                                                                               |
| gcp_display_name     | core | string        | Required. The user specified title for the SavedQuery.                                                                                                                                                                                                                                                                                                                                                                   |
| labels               | core | array<string> |
| logging_query        | core | json          | Logging query that can be executed in Logs Explorer or via Logging API.                                                                                                                                                                                                                                                                                                                                                  |
| name                 | core | string        | Output only. Resource name of the saved query.In the format: "projects/[PROJECT_ID]/locations/[LOCATION_ID]/savedQueries/[QUERY_ID]" For a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support#bucket-regions)After the saved query is created, the location cannot be changed.If the user doesn't provide a QUERY_ID, the system will generate an alphanumeric ID. |
| ops_analytics_query  | core | json          | Analytics query that can be executed in Log Analytics.                                                                                                                                                                                                                                                                                                                                                                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The timestamp when the saved query was last updated.                                                                                                                                                                                                                                                                                                                                                        |
| visibility           | core | string        | Required. The visibility status of this query, which determines its ownership.                                                                                                                                                                                                                                                                                                                                           |
| zone_id              | core | string        |
