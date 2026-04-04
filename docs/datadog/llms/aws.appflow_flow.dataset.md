# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appflow_flow.dataset.md

---
title: Amazon AppFlow Flow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amazon AppFlow Flow
---

# Amazon AppFlow Flow

Amazon AppFlow Flow is a managed integration resource that automates data transfers between AWS services and external SaaS applications. It allows users to securely move, transform, and enrich data without writing custom code. Each flow defines the source, destination, and transformation logic, enabling scheduled or event-driven synchronization.

```
aws.appflow_flow
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                     | Description |
| --------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| created_at                        | core | timestamp  | Specifies when the flow was created.                                                                                                                                                                                                                                          |
| created_by                        | core | string     | The ARN of the user who created the flow.                                                                                                                                                                                                                                     |
| description                       | core | string     | A description of the flow.                                                                                                                                                                                                                                                    |
| destination_flow_config_list      | core | json       | The configuration that controls how Amazon AppFlow transfers data to the destination connector.                                                                                                                                                                               |
| flow_arn                          | core | string     | The flow's Amazon Resource Name (ARN).                                                                                                                                                                                                                                        |
| flow_name                         | core | string     | The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only.                                                                                                                                                                              |
| flow_status                       | core | string     | Indicates the current status of the flow.                                                                                                                                                                                                                                     |
| flow_status_message               | core | string     | Contains an error message if the flow status is in a suspended or error state. This applies only to scheduled or event-triggered flows.                                                                                                                                       |
| kms_arn                           | core | string     | The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key. |
| last_run_execution_details        | core | json       | Describes the details of the most recent flow run.                                                                                                                                                                                                                            |
| last_run_metadata_catalog_details | core | json       | Describes the metadata catalog, metadata table, and data partitions that Amazon AppFlow used for the associated flow run.                                                                                                                                                     |
| last_updated_at                   | core | timestamp  | Specifies when the flow was last updated.                                                                                                                                                                                                                                     |
| last_updated_by                   | core | string     | Specifies the user name of the account that performed the most recent update.                                                                                                                                                                                                 |
| metadata_catalog_config           | core | json       | Specifies the configuration that Amazon AppFlow uses when it catalogs the data that's transferred by the associated flow. When Amazon AppFlow catalogs the data from a flow, it stores metadata in a data catalog.                                                            |
| schema_version                    | core | int64      | The version number of your data schema. Amazon AppFlow assigns this version number. The version number increases by one when you change any of the following settings in your flow configuration: Source-to-destination field mappings Field data types Partition keys        |
| source_flow_config                | core | json       | The configuration that controls how Amazon AppFlow retrieves data from the source connector.                                                                                                                                                                                  |
| tags                              | core | hstore_csv |
| tasks                             | core | json       | A list of tasks that Amazon AppFlow performs while transferring the data in the flow run.                                                                                                                                                                                     |
| trigger_config                    | core | json       | The trigger settings that determine how and when the flow runs.                                                                                                                                                                                                               |
