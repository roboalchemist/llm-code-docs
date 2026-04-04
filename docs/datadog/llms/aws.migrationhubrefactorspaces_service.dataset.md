# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.migrationhubrefactorspaces_service.dataset.md

---
title: Migration Hub Refactor Spaces Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Migration Hub Refactor Spaces
  Service
---

# Migration Hub Refactor Spaces Service

Migration Hub Refactor Spaces Service in AWS provides a managed environment to help organizations transition from monolithic applications to microservices. It offers a unified space where teams can create, manage, and operate refactored services with built-in networking, routing, and security. This service simplifies the process of incrementally modernizing applications by enabling hybrid architectures that combine existing systems with new microservices.

```
aws.migrationhubrefactorspaces_service
```

## Fields

| Title                 | ID   | Type       | Data Type                                                     | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| application_id        | core | string     | The unique identifier of the application.                     |
| arn                   | core | string     | The Amazon Resource Name (ARN) of the service.                |
| created_by_account_id | core | string     | The Amazon Web Services account ID of the service creator.    |
| created_time          | core | timestamp  | A timestamp that indicates when the service is created.       |
| description           | core | string     | A description of the service.                                 |
| endpoint_type         | core | string     | The endpoint type of the service.                             |
| environment_id        | core | string     | The unique identifier of the environment.                     |
| error                 | core | json       | Any error associated with the service resource.               |
| lambda_endpoint       | core | json       | A summary of the configuration for the Lambda endpoint type.  |
| last_updated_time     | core | timestamp  | A timestamp that indicates when the service was last updated. |
| name                  | core | string     | The name of the service.                                      |
| owner_account_id      | core | string     | The Amazon Web Services account ID of the service owner.      |
| service_id            | core | string     | The unique identifier of the service.                         |
| state                 | core | string     | The current state of the service.                             |
| tags                  | core | hstore_csv |
| url_endpoint          | core | json       | The summary of the configuration for the URL endpoint type.   |
| vpc_id                | core | string     | The ID of the virtual private cloud (VPC).                    |
