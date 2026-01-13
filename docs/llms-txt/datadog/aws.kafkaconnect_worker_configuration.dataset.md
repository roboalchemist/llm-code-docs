# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kafkaconnect_worker_configuration.dataset.md

---
title: MSK Connect Worker Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MSK Connect Worker Configuration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.kafkaconnect_worker_configuration.dataset/index.html
---

# MSK Connect Worker Configuration

MSK Connect Worker Configuration in AWS defines reusable settings for Kafka Connect workers that run connectors in Amazon MSK Connect. It allows you to specify parameters such as worker properties, logging, and scaling options, ensuring consistent and controlled deployments of connectors across environments.

```
aws.kafkaconnect_worker_configuration
```

## Fields

| Title                      | ID   | Type      | Data Type                                                   | Description |
| -------------------------- | ---- | --------- | ----------------------------------------------------------- | ----------- |
| _key                       | core | string    |
| account_id                 | core | string    |
| creation_time              | core | timestamp | The time that a worker configuration was created.           |
| description                | core | string    | The description of a worker configuration.                  |
| latest_revision            | core | json      | The latest revision of a worker configuration.              |
| name                       | core | string    | The name of the worker configuration.                       |
| tags                       | core | hstore    |
| worker_configuration_arn   | core | string    | The Amazon Resource Name (ARN) of the worker configuration. |
| worker_configuration_state | core | string    | The state of the worker configuration.                      |
