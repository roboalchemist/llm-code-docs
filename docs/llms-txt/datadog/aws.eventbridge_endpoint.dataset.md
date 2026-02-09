# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eventbridge_endpoint.dataset.md

---
title: EventBridge Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Endpoint
---

# EventBridge Endpoint

An EventBridge Endpoint in AWS is a regional resource that allows you to route events between EventBridge event buses across different AWS Regions or accounts. It provides a secure and controlled way to send and receive events, supporting private connectivity through VPC endpoints and enabling cross-region event-driven architectures. This helps improve reliability, reduce latency, and maintain compliance by keeping event traffic within specific network boundaries.

```
aws.eventbridge_endpoint
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                    | Description |
| ------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The ARN of the endpoint.                                                                                                                                                                                                                     |
| creation_time      | core | timestamp  | The time the endpoint was created.                                                                                                                                                                                                           |
| description        | core | string     | A description for the endpoint.                                                                                                                                                                                                              |
| endpoint_id        | core | string     | The URL subdomain of the endpoint. For example, if the URL for Endpoint is https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is abcde.veo.                                                                                |
| endpoint_url       | core | string     | The URL of the endpoint.                                                                                                                                                                                                                     |
| event_buses        | core | json       | The event buses being used by the endpoint.                                                                                                                                                                                                  |
| last_modified_time | core | timestamp  | The last time the endpoint was modified.                                                                                                                                                                                                     |
| name               | core | string     | The name of the endpoint.                                                                                                                                                                                                                    |
| replication_config | core | json       | Whether event replication was enabled or disabled for this endpoint. The default state is ENABLED which means you must supply a RoleArn. If you don't have a RoleArn or you don't want event replication enabled, set the state to DISABLED. |
| role_arn           | core | string     | The ARN of the role used by event replication for the endpoint.                                                                                                                                                                              |
| routing_config     | core | json       | The routing configuration of the endpoint.                                                                                                                                                                                                   |
| state              | core | string     | The current state of the endpoint.                                                                                                                                                                                                           |
| state_reason       | core | string     | The reason the endpoint is in its current state.                                                                                                                                                                                             |
| tags               | core | hstore_csv |
