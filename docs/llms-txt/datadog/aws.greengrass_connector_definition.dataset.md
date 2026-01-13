# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_connector_definition.dataset.md

---
title: Greengrass Connector Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Greengrass Connector Definition
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.greengrass_connector_definition.dataset/index.html
---

# Greengrass Connector Definition

Greengrass Connector Definition in AWS represents the configuration of connectors used in AWS IoT Greengrass. Connectors are prebuilt integrations that allow Greengrass groups to interact with external services or devices without custom code. A Connector Definition stores information about these connectors, including their settings and versions, enabling easier deployment and management of IoT solutions at the edge.

```
aws.greengrass_connector_definition
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
