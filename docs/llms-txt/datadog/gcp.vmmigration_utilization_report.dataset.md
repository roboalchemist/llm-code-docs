# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmmigration_utilization_report.dataset.md

---
title: VM Migration Utilization Report
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VM Migration Utilization Report
---

# VM Migration Utilization Report

VM Migration Utilization Report in Google Cloud provides detailed insights into the performance and resource usage of virtual machines being assessed or migrated. It helps identify CPU, memory, and storage utilization patterns to optimize migration planning and right-size target instances. This report supports data-driven decisions for efficient workload migration to Google Cloud.

```
gcp.vmmigration_utilization_report
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                        | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time the report was created (this refers to the time of the request, not the time the report creation completed).                                                                                                                               |
| datadog_display_name | core | string        |
| error                | core | json          | Output only. Provides details on the state of the report in case of an error.                                                                                                                                                                                    |
| frame_end_time       | core | timestamp     | Output only. The point in time when the time frame ends. Notice that the time frame is counted backwards. For instance if the "frame_end_time" value is 2021/01/20 and the time frame is WEEK then the report covers the week between 2021/01/20 and 2021/01/14. |
| gcp_display_name     | core | string        | The report display name, as assigned by the user.                                                                                                                                                                                                                |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The report unique name.                                                                                                                                                                                                                             |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. Current state of the report.                                                                                                                                                                                                                        |
| state_time           | core | timestamp     | Output only. The time the state was last set.                                                                                                                                                                                                                    |
| tags                 | core | hstore_csv    |
| time_frame           | core | string        | Time frame of the report.                                                                                                                                                                                                                                        |
| vm_count             | core | int64         | Output only. Total number of VMs included in the report.                                                                                                                                                                                                         |
| vms                  | core | json          | List of utilization information per VM. When sent as part of the request, the "vm_id" field is used in order to specify which VMs to include in the report. In that case all other fields are ignored.                                                           |
| zone_id              | core | string        |
