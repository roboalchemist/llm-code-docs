# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_prompt_router.dataset.md

---
title: Bedrock Prompt Router
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Prompt Router
---

# Bedrock Prompt Router

Bedrock Prompt Router in AWS is a resource that helps manage and route prompts to different foundation models available in Amazon Bedrock. It provides a way to organize, summarize, and direct requests to the most suitable model based on defined configurations, making it easier to integrate multiple models into applications without manually handling routing logic.

```
aws.bedrock_prompt_router
```

## Fields

| Title              | ID   | Type       | Data Type                      | Description |
| ------------------ | ---- | ---------- | ------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| created_at         | core | timestamp  | When the router was created.   |
| description        | core | string     | The router's description.      |
| fallback_model     | core | json       | The router's fallback model.   |
| models             | core | json       | The router's models.           |
| prompt_router_arn  | core | string     | The router's ARN.              |
| prompt_router_name | core | string     | The router's name.             |
| routing_criteria   | core | json       | The router's routing criteria. |
| status             | core | string     | The router's status.           |
| tags               | core | hstore_csv |
| type               | core | string     | The summary's type.            |
| updated_at         | core | timestamp  | When the router was updated.   |
