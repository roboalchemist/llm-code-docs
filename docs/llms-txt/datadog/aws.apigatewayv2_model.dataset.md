# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigatewayv2_model.dataset.md

---
title: API Gateway Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Model
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigatewayv2_model.dataset/index.html
---

# API Gateway Model

An API Gateway Model in AWS defines the data structure for request and response payloads in API Gateway. It uses JSON schema to validate and transform data exchanged between clients and backend services. Models help ensure that incoming requests meet expected formats and that responses are consistent, improving reliability and reducing errors in API communication.

```
aws.apigatewayv2_model
```

## Fields

| Title        | ID   | Type   | Data Type                                                                                        | Description |
| ------------ | ---- | ------ | ------------------------------------------------------------------------------------------------ | ----------- |
| _key         | core | string |
| account_id   | core | string |
| content_type | core | string | The content-type for the model, for example, "application/json".                                 |
| description  | core | string | The description of the model.                                                                    |
| model_id     | core | string | The model identifier.                                                                            |
| name         | core | string | The name of the model. Must be alphanumeric.                                                     |
| schema       | core | string | The schema for the model. For application/json models, this should be JSON schema draft 4 model. |
| tags         | core | hstore |
