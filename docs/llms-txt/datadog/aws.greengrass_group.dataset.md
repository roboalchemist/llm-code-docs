# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_group.dataset.md

---
title: IoT Greengrass Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Greengrass Group
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.greengrass_group.dataset/index.html
---

# IoT Greengrass Group

An IoT Greengrass Group in AWS represents a collection of Greengrass Core devices and their associated settings, resources, and configurations. It allows you to manage and deploy local compute, messaging, data caching, and machine learning inference on edge devices. Groups define how devices interact with each other and with the cloud, enabling secure and efficient local processing while maintaining cloud connectivity for updates and management.

```
aws.greengrass_group
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
