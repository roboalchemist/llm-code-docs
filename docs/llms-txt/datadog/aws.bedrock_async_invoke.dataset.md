# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_async_invoke.dataset.md

---
title: Bedrock Async Invoke
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Async Invoke
---

# Bedrock Async Invoke

This table represents the Bedrock Async Invoke resource from Amazon Web Services.

```
aws.bedrock_async_invoke
```

## Fields

| Title                | ID   | Type       | Data Type                                  | Description |
| -------------------- | ---- | ---------- | ------------------------------------------ | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| client_request_token | core | string     | The invocation's idempotency token.        |
| end_time             | core | timestamp  | When the invocation ended.                 |
| failure_message      | core | string     | An error message.                          |
| invocation_arn       | core | string     | The invocation's ARN.                      |
| last_modified_time   | core | timestamp  | The invocation's last modified time.       |
| model_arn            | core | string     | The invocation's model ARN.                |
| output_data_config   | core | json       | Output data settings.                      |
| status               | core | string     | The invocation's status.                   |
| submit_time          | core | timestamp  | When the invocation request was submitted. |
| tags                 | core | hstore_csv |
