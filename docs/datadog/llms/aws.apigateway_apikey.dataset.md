# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_apikey.dataset.md

---
title: API Gateway API Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway API Key
---

# API Gateway API Key

This table represents the API Gateway API Key resource from Amazon Web Services.

```
aws.apigateway_apikey
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                                               | Description |
| ----------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| account_id        | core | string        |
| created_date      | core | timestamp     | The timestamp when the API Key was created.                                                                             |
| customer_id       | core | string        | An Amazon Web Services Marketplace customer identifier, when integrating with the Amazon Web Services SaaS Marketplace. |
| description       | core | string        | The description of the API Key.                                                                                         |
| enabled           | core | bool          | Specifies whether the API Key can be used by callers.                                                                   |
| id                | core | string        | The identifier of the API Key.                                                                                          |
| last_updated_date | core | timestamp     | The timestamp when the API Key was last updated.                                                                        |
| name              | core | string        | The name of the API Key.                                                                                                |
| stage_keys        | core | array<string> | A list of Stage resources that are associated with the ApiKey resource.                                                 |
| tags              | core | hstore_csv    |
| value             | core | string        | The value of the API Key.                                                                                               |
