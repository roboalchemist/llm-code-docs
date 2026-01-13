# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_subscription_definition.dataset.md

---
title: Greengrass Subscription Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Greengrass Subscription Definition
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.greengrass_subscription_definition.dataset/index.html
---

# Greengrass Subscription Definition

Greengrass Subscription Definition in AWS represents a configuration that defines how messages are transmitted between Greengrass components, such as Lambda functions, connectors, devices, and the cloud. It specifies the source, target, and topic of the communication, enabling secure and managed message routing within a Greengrass group.

```
aws.greengrass_subscription_definition
```

## Fields

| Title                  | ID   | Type   | Data Type                                                                        | Description |
| ---------------------- | ---- | ------ | -------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string |
| account_id             | core | string |
| arn                    | core | string | The ARN of the definition.                                                       |
| creation_timestamp     | core | string | The time, in milliseconds since the epoch, when the definition was created.      |
| id                     | core | string | The ID of the definition.                                                        |
| last_updated_timestamp | core | string | The time, in milliseconds since the epoch, when the definition was last updated. |
| latest_version         | core | string | The ID of the latest version associated with the definition.                     |
| latest_version_arn     | core | string | The ARN of the latest version associated with the definition.                    |
| name                   | core | string | The name of the definition.                                                      |
| tags                   | core | hstore |
