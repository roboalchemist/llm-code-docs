# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.logging_log_view.dataset.md

---
title: Log View
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Log View
---

# Log View

Log View in Google Cloud Platform is a configuration that defines how logs are displayed and filtered within Cloud Logging. It allows users to control which log entries are visible in a specific view by applying filters and access permissions. This helps teams focus on relevant logs for troubleshooting, monitoring, or compliance while maintaining security and data separation across projects or environments.

```
gcp.logging_log_view
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation timestamp of the view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Describes this view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| filter               | core | string        | Optional. Filter that restricts which log entries in a bucket are visible in this view.Filters must be logical conjunctions that use the AND operator, and they can use any of the following qualifiers: SOURCE(), which specifies a project, folder, organization, or billing account of origin. resource.type, which specifies the resource type. LOG_ID(), which identifies the log.They can also use the negations of these qualifiers with the NOT operator.For example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND NOT LOG_ID("stdout") |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The last update timestamp of the view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| zone_id              | core | string        |
