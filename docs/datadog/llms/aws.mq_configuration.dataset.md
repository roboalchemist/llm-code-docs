# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mq_configuration.dataset.md

---
title: MQ Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MQ Configuration
---

# MQ Configuration

An AWS MQ Configuration is a resource that defines the settings for an Amazon MQ broker, such as broker engine type, version, and custom configuration details. It allows you to manage and apply reusable configuration templates across multiple brokers, ensuring consistency and simplifying updates.

```
aws.mq_configuration
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                                                                                             | Description |
| ----------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| arn                     | core | string     | Required. The ARN of the configuration.                                                                                                                                                                                                                               |
| authentication_strategy | core | string     | Optional. The authentication strategy associated with the configuration. The default is SIMPLE.                                                                                                                                                                       |
| created                 | core | timestamp  | Required. The date and time of the configuration revision.                                                                                                                                                                                                            |
| description             | core | string     | Required. The description of the configuration.                                                                                                                                                                                                                       |
| engine_type             | core | string     | Required. The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.                                                                                                                                                                             |
| engine_version          | core | string     | The broker engine version. Defaults to the latest available version for the specified broker engine type. For a list of supported engine versions, see the ActiveMQ version management and the RabbitMQ version management sections in the Amazon MQ Developer Guide. |
| id                      | core | string     | Required. The unique ID that Amazon MQ generates for the configuration.                                                                                                                                                                                               |
| latest_revision         | core | json       | Required. The latest revision of the configuration.                                                                                                                                                                                                                   |
| name                    | core | string     | Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.                                                                           |
| tags                    | core | hstore_csv |
