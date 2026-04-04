# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.storageinsights_report_detail.dataset.md

---
title: Storage Insights Report Detail
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Insights Report Detail
---

# Storage Insights Report Detail

Storage Insights Report Detail in Google Cloud provides detailed analytics and reporting on Cloud Storage usage. It helps users understand storage patterns, object counts, data growth, and access frequency across buckets. This resource supports cost optimization and data management by offering insights into storage efficiency and lifecycle opportunities.

```
gcp.storageinsights_report_detail
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| gcp_status           | core | json          | Status of the inventory report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| labels               | core | array<string> | Labels as key value pairs                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| name                 | core | string        | Name of resource. Format: `projects/{project_number}/locations/{location}/reportConfigs/{report-config-id}/reportDetails/{report-detail-id}`.                                                                                                                                                                                                                                                                                                                                                      |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| report_metrics       | core | json          | Metrics of the inventory report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| report_path_prefix   | core | string        | Prefix of the object name of each report's shard. This has the full prefix except the `extension` and `shard_id`. For example, if the `destination_path` is `{report-config-id}/dt={datetime}`, then the shard object name is `gs://my-insights/1A34-F2E456-12B456-1C3D/dt=2022-05-20T06:35/1A34-F2E456-12B456-1C3D_2022-05-20T06:35_5.csv` and the value of `reportPathPrefix` field is `gs://my-insights/1A34-F2E456-12B456-1C3D/dt=2022-05-20T06:35/1A34-F2E456-12B456-1C3D_2022-05-20T06:35_`. |
| resource_name        | core | string        |
| shards_count         | core | int64         | Total shards generated for the inventory report.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| snapshot_time        | core | timestamp     | The snapshot time. All the inventory report data is referenced at this point of time.                                                                                                                                                                                                                                                                                                                                                                                                              |
| tags                 | core | hstore_csv    |
| target_datetime      | core | json          | The date and time of the inventory report generation. This field is auto-populated. The time part of `target_datetime` is always `0`.                                                                                                                                                                                                                                                                                                                                                              |
| zone_id              | core | string        |
