# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_amp_scraper.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_amp_scraper{% #aws_amp_scraper %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `alias`{% #alias %}

**Type**: `STRING`**Provider name**: `alias`**Description**: (Optional) A name associated with the scraper.

## `arn`{% #arn %}

**Type**: `STRING`**Provider name**: `arn`**Description**: The Amazon Resource Name (ARN) of the scraper. For example, `arn:aws:aps:<region>:123456798012:scraper/s-example1-1234-abcd-5678-ef9012abcd34`.

## `created_at`{% #created_at %}

**Type**: `TIMESTAMP`**Provider name**: `createdAt`**Description**: The date and time that the scraper was created.

## `destination`{% #destination %}

**Type**: `STRUCT`**Provider name**: `destination`**Description**: The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.

- `amp_configuration`**Type**: `STRUCT`**Provider name**: `ampConfiguration`**Description**: The Amazon Managed Service for Prometheus workspace to send metrics to.
  - `workspace_arn`**Type**: `STRING`**Provider name**: `workspaceArn`**Description**: ARN of the Amazon Managed Service for Prometheus workspace.

## `last_modified_at`{% #last_modified_at %}

**Type**: `TIMESTAMP`**Provider name**: `lastModifiedAt`**Description**: The date and time that the scraper was last modified.

## `role_arn`{% #role_arn %}

**Type**: `STRING`**Provider name**: `roleArn`**Description**: The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf. For example, `arn:aws:iam::123456789012:role/service-role/AmazonGrafanaServiceRole-12example`.

## `role_configuration`{% #role_configuration %}

**Type**: `STRUCT`**Provider name**: `roleConfiguration`

- `source_role_arn`**Type**: `STRING`**Provider name**: `sourceRoleArn`**Description**: A ARN identifying the source role configuration.
- `target_role_arn`**Type**: `STRING`**Provider name**: `targetRoleArn`**Description**: A ARN identifying the target role configuration.

## `scrape_configuration`{% #scrape_configuration %}

**Type**: `STRUCT`**Provider name**: `scrapeConfiguration`**Description**: The configuration in use by the scraper.

## `scraper_id`{% #scraper_id %}

**Type**: `STRING`**Provider name**: `scraperId`**Description**: The ID of the scraper. For example, `s-example1-1234-abcd-5678-ef9012abcd34`.

## `status`{% #status %}

**Type**: `STRUCT`**Provider name**: `status`**Description**: A structure that contains the current status of the scraper.

- `status_code`**Type**: `STRING`**Provider name**: `statusCode`**Description**: The current status of the scraper.

## `status_reason`{% #status_reason %}

**Type**: `STRING`**Provider name**: `statusReason`**Description**: If there is a failure, the reason for the failure.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`
