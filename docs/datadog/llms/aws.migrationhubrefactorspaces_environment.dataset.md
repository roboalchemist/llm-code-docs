# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.migrationhubrefactorspaces_environment.dataset.md

---
title: Migration Hub Refactor Spaces Environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Migration Hub Refactor Spaces
  Environment
---

# Migration Hub Refactor Spaces Environment

Migration Hub Refactor Spaces Environment is an AWS resource that provides a managed environment for refactoring applications into microservices. It acts as a foundational container where services, routes, and applications are created and managed, enabling teams to incrementally modernize monolithic applications while maintaining existing functionality.

```
aws.migrationhubrefactorspaces_environment
```

## Fields

| Title               | ID   | Type       | Data Type                                                         | Description |
| ------------------- | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| arn                 | core | string     | The Amazon Resource Name (ARN) of the environment.                |
| created_time        | core | timestamp  | A timestamp that indicates when the environment is created.       |
| description         | core | string     | A description of the environment.                                 |
| environment_id      | core | string     | The unique identifier of the environment.                         |
| error               | core | json       | Any error associated with the environment resource.               |
| last_updated_time   | core | timestamp  | A timestamp that indicates when the environment was last updated. |
| name                | core | string     | The name of the environment.                                      |
| network_fabric_type | core | string     | The network fabric type of the environment.                       |
| owner_account_id    | core | string     | The Amazon Web Services account ID of the environment owner.      |
| state               | core | string     | The current state of the environment.                             |
| tags                | core | hstore_csv |
| transit_gateway_id  | core | string     | The ID of the Transit Gateway set up by the environment.          |
