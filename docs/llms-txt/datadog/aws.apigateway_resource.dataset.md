# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_resource.dataset.md

---
title: API Gateway Resource
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Resource
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigateway_resource.dataset/index.html
---

# API Gateway Resource

An API Gateway Resource in AWS represents a specific path segment within an API. It acts as a container for methods (such as GET, POST, PUT) that define how the API responds to requests on that path. Resources can be organized hierarchically to model RESTful APIs, allowing developers to structure endpoints and integrate them with backend services like Lambda, DynamoDB, or HTTP endpoints.

```
aws.apigateway_resource
```

## Fields

| Title            | ID   | Type   | Data Type                                           | Description |
| ---------------- | ---- | ------ | --------------------------------------------------- | ----------- |
| _key             | core | string |
| account_id       | core | string |
| id               | core | string | The resource's identifier.                          |
| parent_id        | core | string | The parent resource's identifier.                   |
| path             | core | string | The full path for this resource.                    |
| path_part        | core | string | The last path segment for this resource.            |
| resource_arn     | core | string |
| resource_methods | core | string | Gets an API resource's method of a given HTTP verb. |
| tags             | core | hstore |
