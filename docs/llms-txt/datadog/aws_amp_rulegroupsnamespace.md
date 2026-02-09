# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_amp_rulegroupsnamespace.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_amp_rulegroupsnamespace{% #aws_amp_rulegroupsnamespace %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `arn`{% #arn %}

**Type**: `STRING`**Provider name**: `arn`**Description**: The ARN of the rule groups namespace. For example, `arn:aws:aps:<region>:123456789012:rulegroupsnamespace/ws-example1-1234-abcd-5678-ef90abcd1234/rulesfile1`.

## `created_at`{% #created_at %}

**Type**: `TIMESTAMP`**Provider name**: `createdAt`**Description**: The date and time that the rule groups namespace was created.

## `modified_at`{% #modified_at %}

**Type**: `TIMESTAMP`**Provider name**: `modifiedAt`**Description**: The date and time that the rule groups namespace was most recently changed.

## `name`{% #name %}

**Type**: `STRING`**Provider name**: `name`**Description**: The name of the rule groups namespace.

## `status`{% #status %}

**Type**: `STRUCT`**Provider name**: `status`**Description**: The current status of the rule groups namespace.

- `status_code`**Type**: `STRING`**Provider name**: `statusCode`**Description**: The current status of the namespace.
- `status_reason`**Type**: `STRING`**Provider name**: `statusReason`**Description**: The reason for the failure, if any.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`
