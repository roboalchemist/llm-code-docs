# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigatewayv2_api.dataset.md

---
title: API Gateway API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway API
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigatewayv2_api.dataset/index.html
---

# API Gateway API

API Gateway API in AWS is a managed service that allows you to create, publish, maintain, monitor, and secure APIs at scale. It supports both RESTful and WebSocket APIs, enabling communication between clients and backend services. This resource defines the configuration of an API, including its protocols, routes, integrations, and deployment settings, making it easier to build serverless applications and expose services securely.

```
aws.apigatewayv2_api
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                          | Description |
| ---------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                         | core | string        |
| account_id                   | core | string        |
| api_arn                      | core | string        |
| api_endpoint                 | core | string        | The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.                                                                                                                                     |
| api_gateway_managed          | core | bool          | Specifies whether an API is managed by API Gateway. You can't update or delete a managed API by using API Gateway. A managed API can be deleted only through the tooling or service that created it.                                                                                                               |
| api_id                       | core | string        | The API ID.                                                                                                                                                                                                                                                                                                        |
| api_key_selection_expression | core | string        | An API key selection expression. Supported only for WebSocket APIs. See API Key Selection Expressions.                                                                                                                                                                                                             |
| cors_configuration           | core | json          | A CORS configuration. Supported only for HTTP APIs.                                                                                                                                                                                                                                                                |
| created_date                 | core | timestamp     | The timestamp when the API was created.                                                                                                                                                                                                                                                                            |
| description                  | core | string        | The description of the API.                                                                                                                                                                                                                                                                                        |
| disable_execute_api_endpoint | core | bool          | Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint. |
| disable_schema_validation    | core | bool          | Avoid validating models when creating a deployment. Supported only for WebSocket APIs.                                                                                                                                                                                                                             |
| import_info                  | core | array<string> | The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.                                                                                                                                     |
| name                         | core | string        | The name of the API.                                                                                                                                                                                                                                                                                               |
| protocol_type                | core | string        | The API protocol.                                                                                                                                                                                                                                                                                                  |
| route_selection_expression   | core | string        | The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.                                                                          |
| tags                         | core | hstore        |
| version                      | core | string        | A version identifier for the API.                                                                                                                                                                                                                                                                                  |
| warnings                     | core | array<string> | The warning messages reported when failonwarnings is turned on during API import.                                                                                                                                                                                                                                  |
