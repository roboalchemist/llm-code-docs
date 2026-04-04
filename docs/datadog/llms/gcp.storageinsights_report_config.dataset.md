# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.storageinsights_report_config.dataset.md

---
title: Storage Insights ReportConfig
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Insights ReportConfig
---

# Storage Insights ReportConfig

Storage Insights ReportConfig in Google Cloud is a configuration resource that defines how storage usage and performance reports are generated for Cloud Storage. It allows users to specify report parameters such as frequency, data scope, and destination. This helps organizations gain visibility into storage consumption, optimize costs, and monitor data access patterns across buckets.

```
gcp.storageinsights_report_config
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                                            | Description |
| ------------------------------ | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string        |
| ancestors                      | core | array<string> |
| create_time                    | core | timestamp     | Output only. The UTC time at which the inventory report configuration was created. This is auto-populated.           |
| csv_options                    | core | json          | Options for CSV formatted reports.                                                                                   |
| datadog_display_name           | core | string        |
| frequency_options              | core | json          | The frequency of the inventory report generation.                                                                    |
| gcp_display_name               | core | string        | User provided display name that can be empty and limited to 256 characters that is editable..                        |
| labels                         | core | array<string> | Labels as key value pairs                                                                                            |
| name                           | core | string        | Identifier. Name of resource. Format: `projects/{project_id}/locations/{location}/reportConfigs/{report-config-id}`. |
| object_metadata_report_options | core | json          | Options for including object metadata in an inventory report.                                                        |
| organization_id                | core | string        |
| parent                         | core | string        |
| parquet_options                | core | json          | Options for Parquet formatted reports.                                                                               |
| project_id                     | core | string        |
| project_number                 | core | string        |
| region_id                      | core | string        |
| resource_name                  | core | string        |
| tags                           | core | hstore_csv    |
| update_time                    | core | timestamp     | Output only. The UTC time at which the inventory report configuration was updated. This is auto-populated.           |
| zone_id                        | core | string        |
