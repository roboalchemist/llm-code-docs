# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_apigateway_account.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_apigateway_account{% #aws_apigateway_account %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `api_key_version`{% #api_key_version %}

**Type**: `STRING`**Provider name**: `apiKeyVersion`**Description**: The version of the API keys used for the account.

## `cloudwatch_role_arn`{% #cloudwatch_role_arn %}

**Type**: `STRING`**Provider name**: `cloudwatchRoleArn`**Description**: The ARN of an Amazon CloudWatch role for the current Account.

## `features`{% #features %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `features`**Description**: A list of features supported for the account. When usage plans are enabled, the features list will include an entry of `"UsagePlans"`.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `throttle_settings`{% #throttle_settings %}

**Type**: `STRUCT`**Provider name**: `throttleSettings`**Description**: Specifies the API request limits configured for the current Account.

- `burst_limit`**Type**: `INT32`**Provider name**: `burstLimit`**Description**: The API target request burst rate limit. This allows more requests through for a period of time than the target rate limit.
- `rate_limit`**Type**: `DOUBLE`**Provider name**: `rateLimit`**Description**: The API target request rate limit.
