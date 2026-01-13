# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_hours_of_operation.dataset.md

---
title: Connect Hours of Operation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Hours of Operation
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.connect_hours_of_operation.dataset/index.html
---

# Connect Hours of Operation

Connect Hours of Operation in AWS defines the time ranges when a contact center is open to handle customer interactions. It allows you to configure specific days and hours during which agents are available, helping route contacts only within those defined periods. This ensures efficient scheduling and proper handling of customer requests.

```
aws.connect_hours_of_operation
```

## Fields

| Title                  | ID   | Type      | Data Type                                                             | Description |
| ---------------------- | ---- | --------- | --------------------------------------------------------------------- | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| config                 | core | json      | Configuration information for the hours of operation.                 |
| description            | core | string    | The description for the hours of operation.                           |
| hours_of_operation_arn | core | string    | The Amazon Resource Name (ARN) for the hours of operation.            |
| hours_of_operation_id  | core | string    | The identifier for the hours of operation.                            |
| last_modified_region   | core | string    | The Amazon Web Services Region where this resource was last modified. |
| last_modified_time     | core | timestamp | The timestamp when this resource was last modified.                   |
| name                   | core | string    | The name for the hours of operation.                                  |
| tags                   | core | hstore    |
| time_zone              | core | string    | The time zone for the hours of operation.                             |
