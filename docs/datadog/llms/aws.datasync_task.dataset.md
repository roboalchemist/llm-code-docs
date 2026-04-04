# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_task.dataset.md

---
title: DataSync Task
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync Task
---

# DataSync Task

An AWS DataSync Task defines the configuration for transferring data between storage locations, such as on-premises systems, Amazon S3, Amazon EFS, or Amazon FSx. It specifies the source and destination, transfer options, and performance settings. Tasks can be scheduled or run on demand to securely and efficiently move large amounts of data.

```
aws.datasync_task
```

## Fields

| Title                              | ID   | Type          | Data Type                                                                                                                                                                                                                     | Description |
| ---------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string        |
| account_id                         | core | string        |
| cloud_watch_log_group_arn          | core | string        | The Amazon Resource Name (ARN) of an Amazon CloudWatch log group for monitoring your task. For more information, see Monitoring data transfers with CloudWatch Logs.                                                          |
| creation_time                      | core | timestamp     | The time that the task was created.                                                                                                                                                                                           |
| current_task_execution_arn         | core | string        | The ARN of the most recent task execution.                                                                                                                                                                                    |
| destination_location_arn           | core | string        | The ARN of your transfer's destination location.                                                                                                                                                                              |
| destination_network_interface_arns | core | array<string> | The ARNs of the network interfaces that DataSync created for your destination location.                                                                                                                                       |
| error_code                         | core | string        | If there's an issue with your task, you can use the error code to help you troubleshoot the problem. For more information, see Troubleshooting issues with DataSync transfers.                                                |
| error_detail                       | core | string        | If there's an issue with your task, you can use the error details to help you troubleshoot the problem. For more information, see Troubleshooting issues with DataSync transfers.                                             |
| excludes                           | core | json          | The exclude filters that define the files, objects, and folders in your source location that you don't want DataSync to transfer. For more information and examples, see Specifying what DataSync transfers by using filters. |
| includes                           | core | json          | The include filters that define the files, objects, and folders in your source location that you want DataSync to transfer. For more information and examples, see Specifying what DataSync transfers by using filters.       |
| manifest_config                    | core | json          | The configuration of the manifest that lists the files or objects that you want DataSync to transfer. For more information, see Specifying what DataSync transfers by using a manifest.                                       |
| name                               | core | string        | The name of your task.                                                                                                                                                                                                        |
| options                            | core | json          | The task's settings. For example, what file metadata gets preserved, how data integrity gets verified at the end of your transfer, bandwidth limits, among other options.                                                     |
| schedule                           | core | json          | The schedule for when you want your task to run. For more information, see Scheduling your task.                                                                                                                              |
| schedule_details                   | core | json          | The details about your task schedule.                                                                                                                                                                                         |
| source_location_arn                | core | string        | The ARN of your transfer's source location.                                                                                                                                                                                   |
| source_network_interface_arns      | core | array<string> | The ARNs of the network interfaces that DataSync created for your source location.                                                                                                                                            |
| status                             | core | string        | The status of your task. For information about what each status means, see Task statuses.                                                                                                                                     |
| tags                               | core | hstore_csv    |
| task_arn                           | core | string        | The ARN of your task.                                                                                                                                                                                                         |
| task_mode                          | core | string        | The task mode that you're using. For more information, see Choosing a task mode for your data transfer.                                                                                                                       |
| task_report_config                 | core | json          | The configuration of your task report, which provides detailed information about your DataSync transfer. For more information, see Monitoring your DataSync transfers with task reports.                                      |
