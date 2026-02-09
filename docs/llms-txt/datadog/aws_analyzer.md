# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_analyzer.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_analyzer{% #aws_analyzer %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `arn`{% #arn %}

**Type**: `STRING`**Provider name**: `arn`**Description**: The ARN of the analyzer.

## `configuration`{% #configuration %}

**Type**: `STRUCT`**Provider name**: `configuration`**Description**: Specifies whether the analyzer is an external access or unused access analyzer.

- `unused_access`**Type**: `STRUCT`**Provider name**: `unusedAccess`**Description**: Specifies the configuration of an unused access analyzer for an Amazon Web Services organization or account. External access analyzers do not support any configuration.
  - `unused_access_age`**Type**: `INT32`**Provider name**: `unusedAccessAge`**Description**: The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 180 days.

## `created_at`{% #created_at %}

**Type**: `TIMESTAMP`**Provider name**: `createdAt`**Description**: A timestamp for the time at which the analyzer was created.

## `last_resource_analyzed`{% #last_resource_analyzed %}

**Type**: `STRING`**Provider name**: `lastResourceAnalyzed`**Description**: The resource that was most recently analyzed by the analyzer.

## `last_resource_analyzed_at`{% #last_resource_analyzed_at %}

**Type**: `TIMESTAMP`**Provider name**: `lastResourceAnalyzedAt`**Description**: The time at which the most recently analyzed resource was analyzed.

## `name`{% #name %}

**Type**: `STRING`**Provider name**: `name`**Description**: The name of the analyzer.

## `status`{% #status %}

**Type**: `STRING`**Provider name**: `status`**Description**: The status of the analyzer. An `Active` analyzer successfully monitors supported resources and generates new findings. The analyzer is `Disabled` when a user action, such as removing trusted access for Identity and Access Management Access Analyzer from Organizations, causes the analyzer to stop generating new findings. The status is `Creating` when the analyzer creation is in progress and `Failed` when the analyzer creation has failed.

## `status_reason`{% #status_reason %}

**Type**: `STRUCT`**Provider name**: `statusReason`**Description**: The `statusReason` provides more details about the current status of the analyzer. For example, if the creation for the analyzer fails, a `Failed` status is returned. For an analyzer with organization as the type, this failure can be due to an issue with creating the service-linked roles required in the member accounts of the Amazon Web Services organization.

- `code`**Type**: `STRING`**Provider name**: `code`**Description**: The reason code for the current status of the analyzer.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `type`{% #type %}

**Type**: `STRING`**Provider name**: `type`**Description**: The type of analyzer, which corresponds to the zone of trust chosen for the analyzer.
