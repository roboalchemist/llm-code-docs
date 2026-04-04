# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.migrationhubrefactorspaces_route.dataset.md

---
title: Migration Hub Refactor Spaces Route
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Migration Hub Refactor Spaces Route
---

# Migration Hub Refactor Spaces Route

Migration Hub Refactor Spaces Route represents a network path configuration within an application environment created in Refactor Spaces. It defines how incoming requests are routed to specific services or endpoints, enabling traffic management between legacy and modernized applications. This resource helps control routing rules, target destinations, and supports incremental migration by directing traffic to different service versions during refactoring.

```
aws.migrationhubrefactorspaces_route
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                         | Description |
| --------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| account_id            | core | string        |
| append_source_path    | core | bool          | If set to true, this option appends the source path to the service URL endpoint.                                                                                                                                                                                                                  |
| application_id        | core | string        | The unique identifier of the application.                                                                                                                                                                                                                                                         |
| arn                   | core | string        | The Amazon Resource Name (ARN) of the route.                                                                                                                                                                                                                                                      |
| created_by_account_id | core | string        | The Amazon Web Services account ID of the route creator.                                                                                                                                                                                                                                          |
| created_time          | core | timestamp     | A timestamp that indicates when the route is created.                                                                                                                                                                                                                                             |
| environment_id        | core | string        | The unique identifier of the environment.                                                                                                                                                                                                                                                         |
| error                 | core | json          | Any error associated with the route resource.                                                                                                                                                                                                                                                     |
| include_child_paths   | core | bool          | Indicates whether to match all subpaths of the given source path. If this value is false, requests must match the source path exactly before they are forwarded to this route's service.                                                                                                          |
| last_updated_time     | core | timestamp     | A timestamp that indicates when the route was last updated.                                                                                                                                                                                                                                       |
| methods               | core | array<string> | A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route's service.                                                                                                                            |
| owner_account_id      | core | string        | The Amazon Web Services account ID of the route owner.                                                                                                                                                                                                                                            |
| path_resource_to_id   | core | hstore        | A mapping of Amazon API Gateway path resources to resource IDs.                                                                                                                                                                                                                                   |
| route_id              | core | string        | The unique identifier of the route.                                                                                                                                                                                                                                                               |
| route_type            | core | string        | The route type of the route.                                                                                                                                                                                                                                                                      |
| service_id            | core | string        | The unique identifier of the service.                                                                                                                                                                                                                                                             |
| source_path           | core | string        | This is the path that Refactor Spaces uses to match traffic. Paths must start with / and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'. |
| state                 | core | string        | The current state of the route.                                                                                                                                                                                                                                                                   |
| tags                  | core | hstore_csv    |
