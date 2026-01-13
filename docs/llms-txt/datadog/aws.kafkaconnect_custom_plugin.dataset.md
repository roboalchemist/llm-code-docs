# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kafkaconnect_custom_plugin.dataset.md

---
title: MSK Connect Custom Plugin
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MSK Connect Custom Plugin
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.kafkaconnect_custom_plugin.dataset/index.html
---

# MSK Connect Custom Plugin

MSK Connect Custom Plugin in AWS represents a user-defined plugin that extends the functionality of Kafka Connect connectors. It allows you to package and deploy custom logic, such as transformations or connector implementations, to integrate with Amazon MSK Connect. This resource provides details about the plugin, including its version, status, and associated metadata, enabling you to manage and monitor custom plugins used in your streaming data pipelines.

```
aws.kafkaconnect_custom_plugin
```

## Fields

| Title               | ID   | Type      | Data Type                                                                                                                                 | Description |
| ------------------- | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string    |
| account_id          | core | string    |
| creation_time       | core | timestamp | The time that the custom plugin was created.                                                                                              |
| custom_plugin_arn   | core | string    | The Amazon Resource Name (ARN) of the custom plugin.                                                                                      |
| custom_plugin_state | core | string    | The state of the custom plugin.                                                                                                           |
| description         | core | string    | The description of the custom plugin.                                                                                                     |
| latest_revision     | core | json      | The latest successfully created revision of the custom plugin. If there are no successfully created revisions, this field will be absent. |
| name                | core | string    | The name of the custom plugin.                                                                                                            |
| state_description   | core | json      | Details about the state of a custom plugin.                                                                                               |
| tags                | core | hstore    |
