# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appsync_channel_namespace.dataset.md

---
title: AppSync Channel Namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppSync Channel Namespace
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.appsync_channel_namespace.dataset/index.html
---

# AppSync Channel Namespace

This table represents the AppSync Channel Namespace resource from Amazon Web Services.

```
aws.appsync_channel_namespace
```

## Fields

| Title                 | ID   | Type      | Data Type                                                                                                                                                    | Description |
| --------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string    |
| account_id            | core | string    |
| api_id                | core | string    | The Api ID.                                                                                                                                                  |
| channel_namespace_arn | core | string    | The Amazon Resource Name (ARN) for the ChannelNamespace.                                                                                                     |
| code_handlers         | core | string    | The event handler functions that run custom business logic to process published events and subscribe requests.                                               |
| created               | core | timestamp | The date and time that the ChannelNamespace was created.                                                                                                     |
| last_modified         | core | timestamp | The date and time that the ChannelNamespace was last changed.                                                                                                |
| name                  | core | string    | The name of the channel namespace. This name must be unique within the Api.                                                                                  |
| publish_auth_modes    | core | json      | The authorization mode to use for publishing messages on the channel namespace. This configuration overrides the default Apiauthorization configuration.     |
| subscribe_auth_modes  | core | json      | The authorization mode to use for subscribing to messages on the channel namespace. This configuration overrides the default Apiauthorization configuration. |
| tags                  | core | hstore    |
