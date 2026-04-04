# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lambda_layer.dataset.md

---
title: Lambda Layer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lambda Layer
---

# Lambda Layer

This table represents the Lambda Layer resource from Amazon Web Services.

```
aws.lambda_layer
```

## Fields

| Title                   | ID   | Type       | Data Type                                                   | Description |
| ----------------------- | ---- | ---------- | ----------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| latest_matching_version | core | json       | The newest version of the layer.                            |
| layer_arn               | core | string     | The Amazon Resource Name (ARN) of the function layer.       |
| layer_name              | core | string     | The name of the layer.                                      |
| policy                  | core | string     | The policy document.                                        |
| revision_id             | core | string     | A unique identifier for the current revision of the policy. |
| tags                    | core | hstore_csv |
