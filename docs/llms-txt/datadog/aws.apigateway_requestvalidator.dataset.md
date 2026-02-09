# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_requestvalidator.dataset.md

---
title: API Gateway Request Validator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Request Validator
---

# API Gateway Request Validator

This table represents the API Gateway Request Validator resource from Amazon Web Services.

```
aws.apigateway_requestvalidator
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                          | Description |
| --------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| id                          | core | string     | The identifier of this RequestValidator.                                                                           |
| name                        | core | string     | The name of this RequestValidator                                                                                  |
| tags                        | core | hstore_csv |
| validate_request_body       | core | bool       | A Boolean flag to indicate whether to validate a request body according to the configured Model schema.            |
| validate_request_parameters | core | bool       | A Boolean flag to indicate whether to validate request parameters (<code>true</code>) or not (<code>false</code>). |
