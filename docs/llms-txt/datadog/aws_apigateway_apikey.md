# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_apigateway_apikey.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_apigateway_apikey{% #aws_apigateway_apikey %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `created_date`{% #created_date %}

**Type**: `TIMESTAMP`**Provider name**: `createdDate`**Description**: The timestamp when the API Key was created.

## `customer_id`{% #customer_id %}

**Type**: `STRING`**Provider name**: `customerId`**Description**: An Amazon Web Services Marketplace customer identifier, when integrating with the Amazon Web Services SaaS Marketplace.

## `description`{% #description %}

**Type**: `STRING`**Provider name**: `description`**Description**: The description of the API Key.

## `enabled`{% #enabled %}

**Type**: `BOOLEAN`**Provider name**: `enabled`**Description**: Specifies whether the API Key can be used by callers.

## `id`{% #id %}

**Type**: `STRING`**Provider name**: `id`**Description**: The identifier of the API Key.

## `last_updated_date`{% #last_updated_date %}

**Type**: `TIMESTAMP`**Provider name**: `lastUpdatedDate`**Description**: The timestamp when the API Key was last updated.

## `name`{% #name %}

**Type**: `STRING`**Provider name**: `name`**Description**: The name of the API Key.

## `stage_keys`{% #stage_keys %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `stageKeys`**Description**: A list of Stage resources that are associated with the ApiKey resource.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `value`{% #value %}

**Type**: `STRING`**Provider name**: `value`**Description**: The value of the API Key.
