# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_stage.dataset.md

---
title: API Gateway Stage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Stage
---

# API Gateway Stage

An API Gateway Stage in AWS represents a specific deployment of an API, serving as an environment (such as dev, test, or prod) where the API is accessible. It defines settings like logging, caching, throttling, and stage variables that control runtime behavior. Stages allow versioning and controlled rollout of API changes.

```
aws.apigateway_stage
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                                                                                                    | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string     |
| access_log_settings   | core | json       | Settings for logging access in this stage.                                                                                                                                                                                                                   |
| account_id            | core | string     |
| cache_cluster_enabled | core | bool       | Specifies whether a cache cluster is enabled for the stage. To activate a method-level cache, set CachingEnabled to true for a method.                                                                                                                       |
| cache_cluster_size    | core | string     | The stage's cache capacity in GB. For more information about choosing a cache size, see Enabling API caching to enhance responsiveness.                                                                                                                      |
| cache_cluster_status  | core | string     | The status of the cache cluster for the stage, if enabled.                                                                                                                                                                                                   |
| canary_settings       | core | json       | Settings for the canary deployment in this stage.                                                                                                                                                                                                            |
| client_certificate_id | core | string     | The identifier of a client certificate for an API stage.                                                                                                                                                                                                     |
| created_date          | core | timestamp  | The timestamp when the stage was created.                                                                                                                                                                                                                    |
| deployment_id         | core | string     | The identifier of the Deployment that the stage points to.                                                                                                                                                                                                   |
| description           | core | string     | The stage's description.                                                                                                                                                                                                                                     |
| documentation_version | core | string     | The version of the associated API documentation.                                                                                                                                                                                                             |
| last_updated_date     | core | timestamp  | The timestamp when the stage last updated.                                                                                                                                                                                                                   |
| method_settings       | core | string     | A map that defines the method settings for a Stage resource. Keys (designated as /{method_setting_key below) are method paths defined as {resource_path}/{http_method} for an individual method override, or /\*/\* for overriding all methods in the stage. |
| stage_arn             | core | string     |
| stage_name            | core | string     | The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.                         |
| tags                  | core | hstore_csv |
| tracing_enabled       | core | bool       | Specifies whether active tracing with X-ray is enabled for the Stage.                                                                                                                                                                                        |
| variables             | core | hstore     | A map that defines the stage variables for a Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.                                                                              |
| web_acl_arn           | core | string     | The ARN of the WebAcl associated with the Stage.                                                                                                                                                                                                             |
