# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kafka_configuration.dataset.md

---
title: MSK Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MSK Configuration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.kafka_configuration.dataset/index.html
---

# MSK Configuration

MSK Configuration in AWS defines customizable settings for Amazon Managed Streaming for Apache Kafka (MSK) clusters. It allows you to create and manage configuration objects that specify Kafka broker properties, such as log retention, replication factors, and performance tuning parameters. These configurations can be applied to one or more MSK clusters, enabling consistent and centralized management of Kafka settings.

```
aws.kafka_configuration
```

## Fields

| Title           | ID   | Type          | Data Type                                                                                                                                                                                                                   | Description |
| --------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string        |
| account_id      | core | string        |
| arn             | core | string        | The Amazon Resource Name (ARN) of the configuration.                                                                                                                                                                        |
| creation_time   | core | timestamp     | The time when the configuration was created.                                                                                                                                                                                |
| description     | core | string        | The description of the configuration.                                                                                                                                                                                       |
| kafka_versions  | core | array<string> | An array of the versions of Apache Kafka with which you can use this MSK configuration. You can use this configuration for an MSK cluster only if the Apache Kafka version specified for the cluster appears in this array. |
| latest_revision | core | json          | Latest revision of the configuration.                                                                                                                                                                                       |
| name            | core | string        | The name of the configuration.                                                                                                                                                                                              |
| state           | core | string        | The state of the configuration. The possible states are ACTIVE, DELETING, and DELETE_FAILED.                                                                                                                                |
| tags            | core | hstore        |
