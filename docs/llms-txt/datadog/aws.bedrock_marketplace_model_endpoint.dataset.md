# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_marketplace_model_endpoint.dataset.md

---
title: Bedrock Marketplace Model Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Marketplace Model Endpoint
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_marketplace_model_endpoint.dataset/index.html
---

# Bedrock Marketplace Model Endpoint

An AWS Bedrock Marketplace Model Endpoint is a managed endpoint that provides access to foundation models purchased or subscribed to through the Bedrock Marketplace. It allows you to invoke and integrate third-party models into your applications without managing infrastructure, scaling, or deployment.

```
aws.bedrock_marketplace_model_endpoint
```

## Fields

| Title                   | ID   | Type      | Data Type                                                                                  | Description |
| ----------------------- | ---- | --------- | ------------------------------------------------------------------------------------------ | ----------- |
| _key                    | core | string    |
| account_id              | core | string    |
| created_at              | core | timestamp | The timestamp when the endpoint was registered.                                            |
| endpoint_arn            | core | string    | The Amazon Resource Name (ARN) of the endpoint.                                            |
| endpoint_config         | core | json      | The configuration of the endpoint, including the number and type of instances used.        |
| endpoint_status         | core | string    | The current status of the endpoint (e.g., Creating, InService, Updating, Failed).          |
| endpoint_status_message | core | string    | Additional information about the endpoint status, if available.                            |
| model_source_identifier | core | string    | The ARN of the model from Amazon Bedrock Marketplace that is deployed on this endpoint.    |
| status                  | core | string    | The overall status of the endpoint in Amazon Bedrock Marketplace (e.g., ACTIVE, INACTIVE). |
| status_message          | core | string    | Additional information about the overall status, if available.                             |
| tags                    | core | hstore    |
| updated_at              | core | timestamp | The timestamp when the endpoint was last updated.                                          |
