# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appintegrations_event_integration.dataset.md

---
title: AppIntegrations Event Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppIntegrations Event Integration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.appintegrations_event_integration.dataset/index.html
---

# AppIntegrations Event Integration

AppIntegrations Event Integration in AWS allows you to capture events from supported SaaS applications and route them to AWS services for processing. It helps connect external event sources with AWS event-driven architectures, enabling automation and data flow between third-party applications and AWS resources.

```
aws.appintegrations_event_integration
```

## Fields

| Title                 | ID   | Type   | Data Type                                                | Description |
| --------------------- | ---- | ------ | -------------------------------------------------------- | ----------- |
| _key                  | core | string |
| account_id            | core | string |
| description           | core | string | The event integration description.                       |
| event_bridge_bus      | core | string | The Amazon EventBridge bus for the event integration.    |
| event_filter          | core | json   | The event integration filter.                            |
| event_integration_arn | core | string | The Amazon Resource Name (ARN) of the event integration. |
| name                  | core | string | The name of the event integration.                       |
| tags                  | core | hstore |
