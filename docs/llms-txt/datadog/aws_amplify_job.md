# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_amplify_job.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_amplify_job{% #aws_amplify_job %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `commit_id`{% #commit_id %}

**Type**: `STRING`**Provider name**: `commitId`**Description**: The commit ID from a third-party repository provider for the job.

## `commit_message`{% #commit_message %}

**Type**: `STRING`**Provider name**: `commitMessage`**Description**: The commit message from a third-party repository provider for the job.

## `commit_time`{% #commit_time %}

**Type**: `TIMESTAMP`**Provider name**: `commitTime`**Description**: The commit date and time for the job.

## `end_time`{% #end_time %}

**Type**: `TIMESTAMP`**Provider name**: `endTime`**Description**: The end date and time for the job.

## `job_arn`{% #job_arn %}

**Type**: `STRING`**Provider name**: `jobArn`**Description**: The Amazon Resource Name (ARN) for the job.

## `job_id`{% #job_id %}

**Type**: `STRING`**Provider name**: `jobId`**Description**: The unique ID for the job.

## `job_type`{% #job_type %}

**Type**: `STRING`**Provider name**: `jobType`**Description**: The type for the job. If the value is `RELEASE`, the job was manually released from its source by using the `StartJob` API. This value is available only for apps that are connected to a repository. If the value is `RETRY`, the job was manually retried using the `StartJob` API. If the value is `WEB_HOOK`, the job was automatically triggered by webhooks. If the value is `MANUAL`, the job is for a manually deployed app. Manually deployed apps are not connected to a Git repository.

## `source_url`{% #source_url %}

**Type**: `STRING`**Provider name**: `sourceUrl`**Description**: The source URL for the files to deploy. The source URL can be either an HTTP GET URL that is publicly accessible and downloads a single .zip file, or an Amazon S3 bucket and prefix.

## `source_url_type`{% #source_url_type %}

**Type**: `STRING`**Provider name**: `sourceUrlType`**Description**: The type of source specified by the `sourceURL`. If the value is `ZIP`, the source is a .zip file. If the value is `BUCKET_PREFIX`, the source is an Amazon S3 bucket and prefix. If no value is specified, the default is `ZIP`.

## `start_time`{% #start_time %}

**Type**: `TIMESTAMP`**Provider name**: `startTime`**Description**: The start date and time for the job.

## `status`{% #status %}

**Type**: `STRING`**Provider name**: `status`**Description**: The current status for the job.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`
