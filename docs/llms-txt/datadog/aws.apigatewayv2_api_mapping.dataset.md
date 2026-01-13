# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigatewayv2_api_mapping.dataset.md

---
title: API Gateway API Mapping
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway API Mapping
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigatewayv2_api_mapping.dataset/index.html
---

# API Gateway API Mapping

API Gateway API Mapping in AWS connects a custom domain name to a specific API stage in API Gateway v2. It allows you to route requests from a custom domain to the correct API and version, enabling cleaner URLs and better organization of multiple APIs under a single domain. This resource is essential for managing custom domains and directing traffic to the right backend services.

```
aws.apigatewayv2_api_mapping
```

## Fields

| Title           | ID   | Type   | Data Type                   | Description |
| --------------- | ---- | ------ | --------------------------- | ----------- |
| _key            | core | string |
| account_id      | core | string |
| api_id          | core | string | The API identifier.         |
| api_mapping_arn | core | string |
| api_mapping_id  | core | string | The API mapping identifier. |
| stage           | core | string | The API stage.              |
| tags            | core | hstore |
