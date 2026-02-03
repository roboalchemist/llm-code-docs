# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mq_configuration_revision.dataset.md

---
title: MQ Configuration Revision
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MQ Configuration Revision
---

# MQ Configuration Revision

An MQ Configuration Revision in AWS represents a specific version of a configuration for Amazon MQ brokers. Each revision captures the settings and parameters applied to a broker at a given point in time, allowing you to track changes, review details, and manage broker configurations consistently.

```
aws.mq_configuration_revision
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                        | Description |
| ----------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| configuration_id              | core | string     | Required. The unique ID that Amazon MQ generates for the configuration.                                          |
| created                       | core | timestamp  | Required. The date and time of the configuration.                                                                |
| data                          | core | string     | Amazon MQ for ActiveMQ: the base64-encoded XML configuration. Amazon MQ for RabbitMQ: base64-encoded Cuttlefish. |
| description                   | core | string     | The description of the configuration.                                                                            |
| mq_configuration_revision_arn | core | string     |
| tags                          | core | hstore_csv |
