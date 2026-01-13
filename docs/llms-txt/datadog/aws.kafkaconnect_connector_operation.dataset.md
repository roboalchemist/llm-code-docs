# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kafkaconnect_connector_operation.dataset.md

---
title: MSK Connect Connector Operation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MSK Connect Connector Operation
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.kafkaconnect_connector_operation.dataset/index.html
---

# MSK Connect Connector Operation

MSK Connect Connector Operation in AWS represents the details of an operation performed on an MSK Connect connector, such as describing its current state, configuration, and status. It helps users monitor and manage Kafka Connect connectors running on Amazon MSK, providing insights into operational health, lifecycle state, and any issues that may affect data streaming workloads.

```
aws.kafkaconnect_connector_operation
```

## Fields

| Title                          | ID   | Type      | Data Type                                                  | Description |
| ------------------------------ | ---- | --------- | ---------------------------------------------------------- | ----------- |
| _key                           | core | string    |
| account_id                     | core | string    |
| connector_arn                  | core | string    | The Amazon Resource Name (ARN) of the connector.           |
| connector_operation_arn        | core | string    | The Amazon Resource Name (ARN) of the connector operation. |
| connector_operation_state      | core | string    | The state of the connector operation.                      |
| connector_operation_type       | core | string    | The type of connector operation performed.                 |
| creation_time                  | core | timestamp | The time when the operation was created.                   |
| end_time                       | core | timestamp | The time when the operation ended.                         |
| error_info                     | core | json      | Details about the state of a resource.                     |
| operation_steps                | core | json      | The array of operation steps taken.                        |
| origin_connector_configuration | core | hstore    | The origin connector configuration.                        |
| origin_worker_setting          | core | json      | The origin worker setting.                                 |
| tags                           | core | hstore    |
| target_connector_configuration | core | hstore    | The target connector configuration.                        |
| target_worker_setting          | core | json      | The target worker setting.                                 |
