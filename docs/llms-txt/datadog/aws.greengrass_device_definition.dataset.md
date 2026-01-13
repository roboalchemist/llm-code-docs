# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_device_definition.dataset.md

---
title: Greengrass Device Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Greengrass Device Definition
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.greengrass_device_definition.dataset/index.html
---

# Greengrass Device Definition

Greengrass Device Definition in AWS represents a group of devices, such as IoT things, that can interact with an AWS Greengrass group. It defines the set of devices that can communicate securely with the Greengrass core, enabling local messaging, data processing, and integration with cloud services. This resource helps manage and organize devices for edge computing scenarios.

```
aws.greengrass_device_definition
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
