# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_usageplankey.dataset.md

---
title: API Gateway Usage Plan Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Usage Plan Key
---

# API Gateway Usage Plan Key

This table represents the API Gateway Usage Plan Key resource from Amazon Web Services.

```
aws.apigateway_usageplankey
```

## Fields

| Title      | ID   | Type       | Data Type                                                                            | Description |
| ---------- | ---- | ---------- | ------------------------------------------------------------------------------------ | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| id         | core | string     | The Id of a usage plan key.                                                          |
| name       | core | string     | The name of a usage plan key.                                                        |
| tags       | core | hstore_csv |
| type       | core | string     | The type of a usage plan key. Currently, the valid key type is <code>API_KEY</code>. |
| value      | core | string     | The value of a usage plan key.                                                       |
