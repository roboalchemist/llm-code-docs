# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigatewayv2_routeresponse.dataset.md

---
title: API Gateway Route Response
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Route Response
---

# API Gateway Route Response

An API Gateway Route Response in AWS defines how API Gateway responds to a client when a particular route is matched. It specifies the response settings, including status codes, headers, and models, that are returned to the caller. This allows you to customize responses for different outcomes of a route, such as success or error cases, and ensures consistent communication between your API and its consumers.

```
aws.apigatewayv2_routeresponse
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                         | Description |
| -------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| model_selection_expression | core | string     | Represents the model selection expression of a route response. Supported only for WebSocket APIs. |
| response_models            | core | hstore     | Represents the response models of a route response.                                               |
| response_parameters        | core | string     | Represents the response parameters of a route response.                                           |
| route_response_id          | core | string     | Represents the identifier of a route response.                                                    |
| tags                       | core | hstore_csv |
