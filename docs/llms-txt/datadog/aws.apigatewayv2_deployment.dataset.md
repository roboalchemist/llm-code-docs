# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigatewayv2_deployment.dataset.md

---
title: API Gateway Deployment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Deployment
---

# API Gateway Deployment

An API Gateway Deployment in AWS represents a snapshot of an API configuration that can be deployed to a specific stage. It captures the current state of routes, integrations, and settings, allowing you to promote consistent versions of your API to different environments such as development, staging, or production.

```
aws.apigatewayv2_deployment
```

## Fields

| Title                     | ID   | Type       | Data Type                                                           | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| auto_deployed             | core | bool       | Specifies whether a deployment was automatically released.          |
| created_date              | core | timestamp  | The date and time when the Deployment resource was created.         |
| deployment_id             | core | string     | The identifier for the deployment.                                  |
| deployment_status         | core | string     | The status of the deployment: PENDING, FAILED, or SUCCEEDED.        |
| deployment_status_message | core | string     | May contain additional feedback on the status of an API deployment. |
| description               | core | string     | The description for the deployment.                                 |
| tags                      | core | hstore_csv |
