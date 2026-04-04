# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.integrations_execution.dataset.md

---
title: Integration Execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Integration Execution
---

# Integration Execution

Integration Execution in Google Cloud refers to the runtime instance of an integration flow within Application Integration. It represents the execution of a defined integration process that connects and automates data or service interactions across systems. Each execution tracks inputs, outputs, and status, enabling monitoring and troubleshooting of integration workflows.

```
gcp.integrations_execution
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                                                      | Description |
| ------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| ancestors                 | core | array<string> |
| cloud_logging_details     | core | json          | Cloud Logging details for the integration version                                                                                                                                                                                              |
| create_time               | core | timestamp     | Output only. Created time of the execution.                                                                                                                                                                                                    |
| datadog_display_name      | core | string        |
| event_execution_details   | core | json          | The execution info about this event.                                                                                                                                                                                                           |
| execution_details         | core | json          | Detailed info of this execution.                                                                                                                                                                                                               |
| execution_method          | core | string        | The ways user posts this event.                                                                                                                                                                                                                |
| integration_version_state | core | string        | Output only. State of the integration version                                                                                                                                                                                                  |
| labels                    | core | array<string> |
| name                      | core | string        | Auto-generated primary key.                                                                                                                                                                                                                    |
| organization_id           | core | string        |
| parent                    | core | string        |
| project_id                | core | string        |
| project_number            | core | string        |
| region_id                 | core | string        |
| replay_info               | core | json          | Output only. Replay info for the execution                                                                                                                                                                                                     |
| request_params            | core | json          | Event parameters come in as part of the request.                                                                                                                                                                                               |
| resource_name             | core | string        |
| response_params           | core | json          |
| snapshot_number           | core | int64         | Output only. An increasing sequence that is set when a new snapshot is created                                                                                                                                                                 |
| tags                      | core | hstore_csv    |
| trigger_id                | core | string        | The trigger id of the integration trigger config. If both trigger_id and client_id is present, the integration is executed from the start tasks provided by the matching trigger config otherwise it is executed from the default start tasks. |
| update_time               | core | timestamp     | Output only. Last modified time of the execution.                                                                                                                                                                                              |
| zone_id                   | core | string        |
