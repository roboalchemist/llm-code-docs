# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appintegrations_application.dataset.md

---
title: AppIntegrations Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppIntegrations Application
---

# AppIntegrations Application

AppIntegrations Application in AWS represents a resource that allows you to integrate external applications and data sources with AWS services. It provides a way to connect, manage, and route data between SaaS applications and AWS, enabling event-driven workflows and data synchronization. This resource helps simplify building integrations without custom code, supporting use cases like customer data unification, analytics, and operational automation.

```
aws.appintegrations_application
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                   | Description |
| ------------------------- | ---- | ------------- | --------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| account_id                | core | string        |
| application_source_config | core | json          | The configuration for where the application should be loaded from.          |
| arn                       | core | string        | The Amazon Resource Name (ARN) of the Application.                          |
| created_time              | core | timestamp     | The created time of the Application.                                        |
| description               | core | string        | The description of the application.                                         |
| id                        | core | string        | A unique identifier for the Application.                                    |
| last_modified_time        | core | timestamp     | The last modified time of the Application.                                  |
| name                      | core | string        | The name of the application.                                                |
| namespace                 | core | string        | The namespace of the application.                                           |
| permissions               | core | array<string> | The configuration of events or requests that the application has access to. |
| publications              | core | json          | The events that the application publishes.                                  |
| subscriptions             | core | json          | The events that the application subscribes.                                 |
| tags                      | core | hstore_csv    |
