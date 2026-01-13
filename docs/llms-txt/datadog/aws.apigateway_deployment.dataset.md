# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_deployment.dataset.md

---
title: API Gateway Deployment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Deployment
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigateway_deployment.dataset/index.html
---

# API Gateway Deployment

An API Gateway Deployment in AWS represents a snapshot of an API's configuration that can be deployed to a specific stage. It captures the current state of resources and methods, making it possible to publish and manage different versions of an API. Deployments are essential for promoting changes from development to production environments.

```
aws.apigateway_deployment
```

## Fields

| Title        | ID   | Type      | Data Type                                                                               | Description |
| ------------ | ---- | --------- | --------------------------------------------------------------------------------------- | ----------- |
| _key         | core | string    |
| account_id   | core | string    |
| api_summary  | core | hstore    | A summary of the RestApi at the date and time that the deployment resource was created. |
| created_date | core | timestamp | The date and time that the deployment resource was created.                             |
| description  | core | string    | The description for the deployment resource.                                            |
| id           | core | string    | The identifier for the deployment resource.                                             |
| tags         | core | hstore    |
