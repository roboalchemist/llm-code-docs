# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_base_path_mapping.dataset.md

---
title: API Gateway Base Path Mapping
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Base Path Mapping
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigateway_base_path_mapping.dataset/index.html
---

# API Gateway Base Path Mapping

API Gateway Base Path Mapping in AWS links a custom domain name to a specific API stage within API Gateway. It allows you to define a base path that routes incoming requests on the custom domain to the correct API and stage. This makes it easier to provide user-friendly URLs and manage multiple APIs under a single domain.

```
aws.apigateway_base_path_mapping
```

## Fields

| Title                 | ID   | Type   | Data Type                                                                                         | Description |
| --------------------- | ---- | ------ | ------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string |
| account_id            | core | string |
| base_path             | core | string | The base path name that callers of the API must provide as part of the URL after the domain name. |
| base_path_mapping_arn | core | string |
| rest_api_id           | core | string | The string identifier of the associated RestApi.                                                  |
| stage                 | core | string | The name of the associated stage.                                                                 |
| tags                  | core | hstore |
