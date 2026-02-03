# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.migrationhubrefactorspaces_application.dataset.md

---
title: Migration Hub Refactor Spaces Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Migration Hub Refactor Spaces
  Application
---

# Migration Hub Refactor Spaces Application

Migration Hub Refactor Spaces Application is an AWS resource that represents an application created within Refactor Spaces, a service that helps manage the process of refactoring monolithic applications into microservices. It provides a logical grouping of services, environments, and routes, enabling teams to incrementally modernize applications while maintaining control and visibility through a central management hub.

```
aws.migrationhubrefactorspaces_application
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                   | Description |
| --------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| api_gateway_proxy     | core | json       | The endpoint URL of the Amazon API Gateway proxy.                                                                           |
| application_id        | core | string     | The unique identifier of the application.                                                                                   |
| arn                   | core | string     | The Amazon Resource Name (ARN) of the application.                                                                          |
| created_by_account_id | core | string     | The Amazon Web Services account ID of the application creator.                                                              |
| created_time          | core | timestamp  | A timestamp that indicates when the application is created.                                                                 |
| environment_id        | core | string     | The unique identifier of the environment.                                                                                   |
| error                 | core | json       | Any error associated with the application resource.                                                                         |
| last_updated_time     | core | timestamp  | A timestamp that indicates when the application was last updated.                                                           |
| name                  | core | string     | The name of the application.                                                                                                |
| owner_account_id      | core | string     | The Amazon Web Services account ID of the application owner (which is always the same as the environment owner account ID). |
| proxy_type            | core | string     | The proxy type of the proxy created within the application.                                                                 |
| state                 | core | string     | The current state of the application.                                                                                       |
| tags                  | core | hstore_csv |
| vpc_id                | core | string     | The ID of the virtual private cloud (VPC).                                                                                  |
