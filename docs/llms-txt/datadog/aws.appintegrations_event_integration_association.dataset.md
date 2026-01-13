# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appintegrations_event_integration_association.dataset.md

---
title: AppIntegrations Event Integration Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > AppIntegrations Event Integration
  Association
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.appintegrations_event_integration_association.dataset/index.html
---

# AppIntegrations Event Integration Association

AppIntegrations Event Integration Association in AWS links an event integration with specific resources such as event buses or applications. It defines how events from a source are associated with a target, enabling seamless event-driven communication between services. This resource helps manage and organize event flows by connecting integrations to the right destinations.

```
aws.appintegrations_event_integration_association
```

## Fields

| Title                             | ID   | Type   | Data Type                                                                    | Description |
| --------------------------------- | ---- | ------ | ---------------------------------------------------------------------------- | ----------- |
| _key                              | core | string |
| account_id                        | core | string |
| client_association_metadata       | core | hstore | The metadata associated with the client.                                     |
| client_id                         | core | string | The identifier for the client that is associated with the event integration. |
| event_bridge_rule_name            | core | string | The name of the EventBridge rule.                                            |
| event_integration_association_arn | core | string | The Amazon Resource Name (ARN) for the event integration association.        |
| event_integration_association_id  | core | string | The identifier for the event integration association.                        |
| event_integration_name            | core | string | The name of the event integration.                                           |
| tags                              | core | hstore |
