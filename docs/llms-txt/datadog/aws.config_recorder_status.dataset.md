# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.config_recorder_status.dataset.md

---
title: Config Recorder Status
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Config Recorder Status
---

# Config Recorder Status

This table represents the Config Recorder Status resource from Amazon Web Services.

```
aws.config_recorder_status
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                | Description |
| ----------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| last_error_code         | core | string     | The latest error code from when the recorder last failed.                                |
| last_error_message      | core | string     | The latest error message from when the recorder last failed.                             |
| last_start_time         | core | timestamp  | The time the recorder was last started.                                                  |
| last_status             | core | string     | The status of the latest recording event processed by the recorder.                      |
| last_status_change_time | core | timestamp  | The time of the latest change in status of an recording event processed by the recorder. |
| last_stop_time          | core | timestamp  | The time the recorder was last stopped.                                                  |
| name                    | core | string     | The name of the configuration recorder.                                                  |
| recording               | core | bool       | Specifies whether or not the recorder is currently recording.                            |
| tags                    | core | hstore_csv |
