# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.amplify_webhook.dataset.md

---
title: Amplify Webhook
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amplify Webhook
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.amplify_webhook.dataset/index.html
---

# Amplify Webhook

An Amplify Webhook in AWS is a resource that allows external systems or services to trigger actions in an Amplify app, such as starting a new build or deployment. It provides a secure endpoint that can be invoked to automate workflows and integrate Amplify with other tools or CI/CD pipelines.

```
aws.amplify_webhook
```

## Fields

| Title       | ID   | Type      | Data Type                                                               | Description |
| ----------- | ---- | --------- | ----------------------------------------------------------------------- | ----------- |
| _key        | core | string    |
| account_id  | core | string    |
| branch_name | core | string    | The name for a branch that is part of an Amplify app.                   |
| create_time | core | timestamp | A timestamp of when Amplify created the webhook in your Git repository. |
| description | core | string    | The description for a webhook.                                          |
| tags        | core | hstore    |
| update_time | core | timestamp | A timestamp of when Amplify updated the webhook in your Git repository. |
| webhook_arn | core | string    | The Amazon Resource Name (ARN) for the webhook.                         |
| webhook_id  | core | string    | The ID of the webhook.                                                  |
| webhook_url | core | string    | The URL of the webhook.                                                 |
