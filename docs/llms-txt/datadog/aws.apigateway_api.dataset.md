# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_api.dataset.md

---
title: API Gateway API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway API
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigateway_api.dataset/index.html
---

# API Gateway API

This table represents the API Gateway API resource from Amazon Web Services.

```
aws.apigateway_api
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ---------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| account_id                   | core | string        |
| api_arn                      | core | string        |
| api_key_source               | core | string        | The source of the API key for metering requests according to a usage plan. Valid values are: &gt;<code>HEADER</code> to read the API key from the <code>X-API-Key</code> header of a request. <code>AUTHORIZER</code> to read the API key from the <code>UsageIdentifierKey</code> from a custom authorizer.                                                                      |
| binary_media_types           | core | array<string> | The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.                                                                                                                                                                                                                                                       |
| created_date                 | core | timestamp     | The timestamp when the API was created.                                                                                                                                                                                                                                                                                                                                           |
| description                  | core | string        | The API's description.                                                                                                                                                                                                                                                                                                                                                            |
| disable_execute_api_endpoint | core | bool          | Specifies whether clients can invoke your API by using the default <code>execute-api</code> endpoint. By default, clients can invoke your API with the default <code>https://{api_id}.execute-api.{region}.amazonaws.com</code> endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.                                      |
| endpoint_configuration       | core | json          | The endpoint configuration of this RestApi showing the endpoint types of the API.                                                                                                                                                                                                                                                                                                 |
| id                           | core | string        | The API's identifier. This identifier is unique across all of your APIs in API Gateway.                                                                                                                                                                                                                                                                                           |
| minimum_compression_size     | core | int64         | A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size. |
| name                         | core | string        | The API's name.                                                                                                                                                                                                                                                                                                                                                                   |
| policy                       | core | string        | A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.                                                                                                                                                                                                                                                                |
| root_resource_id             | core | string        | The API's root resource ID.                                                                                                                                                                                                                                                                                                                                                       |
| tags                         | core | hstore        |
| version                      | core | string        | A version identifier for the API.                                                                                                                                                                                                                                                                                                                                                 |
| warnings                     | core | array<string> | The warning messages reported when <code>failonwarnings</code> is turned on during API import.                                                                                                                                                                                                                                                                                    |
