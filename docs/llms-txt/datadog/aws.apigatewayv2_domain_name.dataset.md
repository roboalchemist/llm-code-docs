# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigatewayv2_domain_name.dataset.md

---
title: API Gateway Domain Name
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Domain Name
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigatewayv2_domain_name.dataset/index.html
---

# API Gateway Domain Name

API Gateway Domain Name in AWS allows you to set up a custom domain for your API Gateway APIs. Instead of using the default execute-api endpoint, you can map your own domain name to the API, making it easier for clients to access. It supports both REST and WebSocket APIs and can be integrated with Route 53 for DNS management and AWS Certificate Manager for SSL/TLS certificates.

```
aws.apigatewayv2_domain_name
```

## Fields

| Title                            | ID   | Type   | Data Type                                                             | Description |
| -------------------------------- | ---- | ------ | --------------------------------------------------------------------- | ----------- |
| _key                             | core | string |
| account_id                       | core | string |
| api_mapping_selection_expression | core | string | The API mapping selection expression.                                 |
| domain_name                      | core | string | The name of the DomainName resource.                                  |
| domain_name_arn                  | core | string | Represents an Amazon Resource Name (ARN).                             |
| domain_name_configurations       | core | json   | The domain name configurations.                                       |
| mutual_tls_authentication        | core | json   | The mutual TLS authentication configuration for a custom domain name. |
| tags                             | core | hstore |
