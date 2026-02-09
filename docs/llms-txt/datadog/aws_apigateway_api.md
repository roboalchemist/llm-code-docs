# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_apigateway_api.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_apigateway_api{% #aws_apigateway_api %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `api_arn`{% #api_arn %}

**Type**: `STRING`

## `api_key_source`{% #api_key_source %}

**Type**: `STRING`**Provider name**: `apiKeySource`**Description**: The source of the API key for metering requests according to a usage plan. Valid values are: >`HEADER` to read the API key from the `X-API-Key` header of a request. `AUTHORIZER` to read the API key from the `UsageIdentifierKey` from a custom authorizer.

## `binary_media_types`{% #binary_media_types %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `binaryMediaTypes`**Description**: The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

## `created_date`{% #created_date %}

**Type**: `TIMESTAMP`**Provider name**: `createdDate`**Description**: The timestamp when the API was created.

## `description`{% #description %}

**Type**: `STRING`**Provider name**: `description`**Description**: The API's description.

## `disable_execute_api_endpoint`{% #disable_execute_api_endpoint %}

**Type**: `BOOLEAN`**Provider name**: `disableExecuteApiEndpoint`**Description**: Specifies whether clients can invoke your API by using the default `execute-api` endpoint. By default, clients can invoke your API with the default `https://{api_id}.execute-api.{region}.amazonaws.com` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.

## `endpoint_configuration`{% #endpoint_configuration %}

**Type**: `STRUCT`**Provider name**: `endpointConfiguration`**Description**: The endpoint configuration of this RestApi showing the endpoint types of the API.

- `types`**Type**: `UNORDERED_LIST_STRING`**Provider name**: `types`**Description**: A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is `"EDGE"`. For a regional API and its custom domain name, the endpoint type is `REGIONAL`. For a private API, the endpoint type is `PRIVATE`.
- `vpc_endpoint_ids`**Type**: `UNORDERED_LIST_STRING`**Provider name**: `vpcEndpointIds`**Description**: A list of VpcEndpointIds of an API (RestApi) against which to create Route53 ALIASes. It is only supported for `PRIVATE` endpoint type.

## `id`{% #id %}

**Type**: `STRING`**Provider name**: `id`**Description**: The API's identifier. This identifier is unique across all of your APIs in API Gateway.

## `minimum_compression_size`{% #minimum_compression_size %}

**Type**: `INT32`**Provider name**: `minimumCompressionSize`**Description**: A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.

## `name`{% #name %}

**Type**: `STRING`**Provider name**: `name`**Description**: The API's name.

## `policy`{% #policy %}

**Type**: `STRING`**Provider name**: `policy`**Description**: A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.

## `root_resource_id`{% #root_resource_id %}

**Type**: `STRING`**Provider name**: `rootResourceId`**Description**: The API's root resource ID.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `version`{% #version %}

**Type**: `STRING`**Provider name**: `version`**Description**: A version identifier for the API.

## `warnings`{% #warnings %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `warnings`**Description**: The warning messages reported when `failonwarnings` is turned on during API import.
