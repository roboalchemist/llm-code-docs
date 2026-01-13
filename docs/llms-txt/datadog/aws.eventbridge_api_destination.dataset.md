# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eventbridge_api_destination.dataset.md

---
title: EventBridge API Destination
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge API Destination
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.eventbridge_api_destination.dataset/index.html
---

# EventBridge API Destination

EventBridge API Destination in AWS allows you to send events from EventBridge to any HTTP-based API endpoint. It provides a managed way to integrate with external services or custom applications without building additional infrastructure. You can configure connection details, authentication, and rate limits, enabling secure and controlled event delivery to third-party APIs or internal endpoints.

```
aws.eventbridge_api_destination
```

## Fields

| Title                            | ID   | Type      | Data Type                                                                  | Description |
| -------------------------------- | ---- | --------- | -------------------------------------------------------------------------- | ----------- |
| _key                             | core | string    |
| account_id                       | core | string    |
| api_destination_arn              | core | string    | The ARN of the API destination.                                            |
| api_destination_state            | core | string    | The state of the API destination.                                          |
| connection_arn                   | core | string    | The ARN of the connection specified for the API destination.               |
| creation_time                    | core | timestamp | A time stamp for the time that the API destination was created.            |
| http_method                      | core | string    | The method to use to connect to the HTTP endpoint.                         |
| invocation_endpoint              | core | string    | The URL to the endpoint for the API destination.                           |
| invocation_rate_limit_per_second | core | int64     | The maximum number of invocations per second to send to the HTTP endpoint. |
| last_modified_time               | core | timestamp | A time stamp for the time that the API destination was last modified.      |
| name                             | core | string    | The name of the API destination.                                           |
| tags                             | core | hstore    |
