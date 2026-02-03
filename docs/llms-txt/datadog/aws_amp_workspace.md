# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_amp_workspace.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_amp_workspace{% #aws_amp_workspace %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `alias`{% #alias %}

**Type**: `STRING`**Provider name**: `alias`**Description**: The alias that is assigned to this workspace to help identify it. It does not need to be unique.

## `arn`{% #arn %}

**Type**: `STRING`**Provider name**: `arn`**Description**: The ARN of the workspace. For example, `arn:aws:aps:<region>:123456789012:workspace/ws-example1-1234-abcd-5678-ef90abcd1234`.

## `created_at`{% #created_at %}

**Type**: `TIMESTAMP`**Provider name**: `createdAt`**Description**: The date and time that the workspace was created.

## `kms_key_arn`{% #kms_key_arn %}

**Type**: `STRING`**Provider name**: `kmsKeyArn`**Description**: (optional) If the workspace was created with a customer managed KMS key, the ARN for the key used.

## `prometheus_endpoint`{% #prometheus_endpoint %}

**Type**: `STRING`**Provider name**: `prometheusEndpoint`**Description**: The Prometheus endpoint available for this workspace. For example, `https://aps-workspaces.<region>.amazonaws.com/workspaces/ws-example1-1234-abcd-5678-ef90abcd1234/api/v1/`.

## `status`{% #status %}

**Type**: `STRUCT`**Provider name**: `status`**Description**: The current status of the workspace.

- `status_code`**Type**: `STRING`**Provider name**: `statusCode`**Description**: The current status of the workspace.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `workspace_id`{% #workspace_id %}

**Type**: `STRING`**Provider name**: `workspaceId`**Description**: The unique ID for the workspace. For example, `ws-example1-1234-abcd-5678-ef90abcd1234`.
