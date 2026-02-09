# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qbusiness_plugin.dataset.md

---
title: Q Business Plugin
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Q Business Plugin
---

# Q Business Plugin

Q Business Plugin in AWS is part of the Amazon Q Business service, which enables integration of external applications and data sources into the Q Business environment. The GetPluginResponse shape provides details about a specific plugin, such as its configuration, status, and metadata, allowing users to manage and monitor how the plugin connects external systems with Q Business. This resource helps extend Q Business functionality by enabling seamless access to third-party tools and data.

```
aws.qbusiness_plugin
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                   | Description |
| --------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| application_id              | core | string     | The identifier of the application which contains the plugin.                                                |
| auth_configuration          | core | json       | Authentication configuration information for an Amazon Q Business plugin.                                   |
| build_status                | core | string     | The current status of a plugin. A plugin is modified asynchronously.                                        |
| created_at                  | core | timestamp  | The timestamp for when the plugin was created.                                                              |
| custom_plugin_configuration | core | json       | Configuration information required to create a custom plugin.                                               |
| plugin_arn                  | core | string     | The Amazon Resource Name (ARN) of the role with permission to access resources needed to create the plugin. |
| plugin_id                   | core | string     | The identifier of the plugin.                                                                               |
| server_url                  | core | string     | The source URL used for plugin configuration.                                                               |
| state                       | core | string     | The current state of the plugin.                                                                            |
| tags                        | core | hstore_csv |
| type                        | core | string     | The type of the plugin.                                                                                     |
| updated_at                  | core | timestamp  | The timestamp for when the plugin was last updated.                                                         |
