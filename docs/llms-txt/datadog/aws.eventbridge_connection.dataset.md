# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eventbridge_connection.dataset.md

---
title: EventBridge Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Connection
---

# EventBridge Connection

An EventBridge Connection in AWS is a resource that stores authentication and authorization details for securely integrating EventBridge with external API destinations. It allows you to define credentials, such as API keys or OAuth tokens, so EventBridge can reliably send events to third-party services or custom applications without embedding sensitive information directly in event rules.

```
aws.eventbridge_connection
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                               | Description |
| -------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| authorization_type   | core | string     | The authorization type specified for the connection. OAUTH tokens are refreshed when a 401 or 407 response is returned. |
| connection_arn       | core | string     | The ARN of the connection.                                                                                              |
| connection_state     | core | string     | The state of the connection.                                                                                            |
| creation_time        | core | timestamp  | A time stamp for the time that the connection was created.                                                              |
| last_authorized_time | core | timestamp  | A time stamp for the time that the connection was last authorized.                                                      |
| last_modified_time   | core | timestamp  | A time stamp for the time that the connection was last modified.                                                        |
| name                 | core | string     | The name of the connection.                                                                                             |
| state_reason         | core | string     | The reason that the connection is in the connection state.                                                              |
| tags                 | core | hstore_csv |
