# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kafkaconnect_connector.dataset.md

---
title: MSK Connect Connector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MSK Connect Connector
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.kafkaconnect_connector.dataset/index.html
---

# MSK Connect Connector

MSK Connect Connector in AWS is a managed resource that represents a Kafka Connect connector running on Amazon MSK Connect. It allows you to integrate Apache Kafka topics with external systems such as databases, object stores, or other services without managing the underlying infrastructure. This resource provides details about the connector's configuration, status, capacity, and runtime settings, making it easier to monitor and manage data streaming pipelines at scale.

```
aws.kafkaconnect_connector
```

## Fields

| Title                               | ID   | Type      | Data Type                                                                                                                               | Description |
| ----------------------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string    |
| account_id                          | core | string    |
| capacity                            | core | json      | Information about the capacity of the connector, whether it is auto scaled or provisioned.                                              |
| connector_arn                       | core | string    | The Amazon Resource Name (ARN) of the connector.                                                                                        |
| connector_configuration             | core | hstore    | A map of keys to values that represent the configuration for the connector.                                                             |
| connector_description               | core | string    | A summary description of the connector.                                                                                                 |
| connector_name                      | core | string    | The name of the connector.                                                                                                              |
| connector_state                     | core | string    | The state of the connector.                                                                                                             |
| creation_time                       | core | timestamp | The time the connector was created.                                                                                                     |
| current_version                     | core | string    | The current version of the connector.                                                                                                   |
| kafka_cluster                       | core | json      | The Apache Kafka cluster that the connector is connected to.                                                                            |
| kafka_cluster_client_authentication | core | json      | The type of client authentication used to connect to the Apache Kafka cluster. The value is NONE when no client authentication is used. |
| kafka_cluster_encryption_in_transit | core | json      | Details of encryption in transit to the Apache Kafka cluster.                                                                           |
| kafka_connect_version               | core | string    | The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.                     |
| log_delivery                        | core | json      | Details about delivering logs to Amazon CloudWatch Logs.                                                                                |
| plugins                             | core | json      | Specifies which plugins were used for this connector.                                                                                   |
| service_execution_role_arn          | core | string    | The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.                           |
| state_description                   | core | json      | Details about the state of a connector.                                                                                                 |
| tags                                | core | hstore    |
| worker_configuration                | core | json      | Specifies which worker configuration was used for the connector.                                                                        |
