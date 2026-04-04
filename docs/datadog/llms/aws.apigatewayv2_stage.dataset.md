# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigatewayv2_stage.dataset.md

---
title: API Gateway Stage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Stage
---

# API Gateway Stage

An API Gateway Stage in AWS represents a specific deployment of an API Gateway API, serving as an environment where the API is accessible to clients. Stages allow you to manage different versions of your API, such as development, testing, and production, each with its own settings, logging, throttling, and caching configurations.

```
aws.apigatewayv2_stage
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                                                                                         | Description |
| ------------------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| access_log_settings            | core | json       | Settings for logging access in this stage.                                                                                                                                        |
| account_id                     | core | string     |
| api_gateway_managed            | core | bool       | Specifies whether a stage is managed by API Gateway. If you created an API using quick create, the $default stage is managed by API Gateway. You can't modify the $default stage. |
| auto_deploy                    | core | bool       | Specifies whether updates to an API automatically trigger a new deployment. The default value is false.                                                                           |
| client_certificate_id          | core | string     | The identifier of a client certificate for a Stage. Supported only for WebSocket APIs.                                                                                            |
| created_date                   | core | timestamp  | The timestamp when the stage was created.                                                                                                                                         |
| default_route_settings         | core | json       | Default route settings for the stage.                                                                                                                                             |
| deployment_id                  | core | string     | The identifier of the Deployment that the Stage is associated with. Can't be updated if autoDeploy is enabled.                                                                    |
| description                    | core | string     | The description of the stage.                                                                                                                                                     |
| last_deployment_status_message | core | string     | Describes the status of the last deployment of a stage. Supported only for stages with autoDeploy enabled.                                                                        |
| last_updated_date              | core | timestamp  | The timestamp when the stage was last updated.                                                                                                                                    |
| route_settings                 | core | string     | Route settings for the stage, by routeKey.                                                                                                                                        |
| stage_arn                      | core | string     |
| stage_name                     | core | string     | The name of the stage.                                                                                                                                                            |
| stage_variables                | core | hstore     | A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.   |
| tags                           | core | hstore_csv |
