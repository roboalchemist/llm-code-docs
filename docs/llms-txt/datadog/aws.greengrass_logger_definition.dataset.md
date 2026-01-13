# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_logger_definition.dataset.md

---
title: Greengrass Logger Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Greengrass Logger Definition
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.greengrass_logger_definition.dataset/index.html
---

# Greengrass Logger Definition

Greengrass Logger Definition in AWS defines logging configurations for AWS Greengrass groups. It specifies how logs are collected from Greengrass components, including the level of detail, the type of logs, and the destination such as CloudWatch Logs or the local file system. This helps monitor and troubleshoot Greengrass applications running on edge devices.

```
aws.greengrass_logger_definition
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
