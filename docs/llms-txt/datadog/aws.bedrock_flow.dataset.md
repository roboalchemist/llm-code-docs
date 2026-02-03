# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_flow.dataset.md

---
title: Bedrock Flow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Flow
---

# Bedrock Flow

This table represents the Bedrock Flow resource from Amazon Web Services.

```
aws.bedrock_flow
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                     | Description |
| --------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| arn                         | core | string     | The Amazon Resource Name (ARN) of the flow.                                                                                                                                                                                                                                                   |
| created_at                  | core | timestamp  | The time at which the flow was created.                                                                                                                                                                                                                                                       |
| customer_encryption_key_arn | core | string     | The Amazon Resource Name (ARN) of the KMS key that the version of the flow is encrypted with.                                                                                                                                                                                                 |
| definition                  | core | json       | The definition of the nodes and connections between nodes in the flow.                                                                                                                                                                                                                        |
| description                 | core | string     | The description of the flow.                                                                                                                                                                                                                                                                  |
| execution_role_arn          | core | string     | The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide. |
| id                          | core | string     | The unique identifier of the flow.                                                                                                                                                                                                                                                            |
| name                        | core | string     | The name of the version.                                                                                                                                                                                                                                                                      |
| status                      | core | string     | The status of the flow.                                                                                                                                                                                                                                                                       |
| tags                        | core | hstore_csv |
| updated_at                  | core | timestamp  | The time at which the flow was last updated.                                                                                                                                                                                                                                                  |
| validations                 | core | json       | A list of validation error messages related to the last failed operation on the flow.                                                                                                                                                                                                         |
| version                     | core | string     | The version of the flow for which information was retrieved.                                                                                                                                                                                                                                  |
