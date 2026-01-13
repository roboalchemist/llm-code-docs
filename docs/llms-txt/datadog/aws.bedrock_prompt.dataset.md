# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_prompt.dataset.md

---
title: Bedrock Prompt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Prompt
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_prompt.dataset/index.html
---

# Bedrock Prompt

This table represents the Bedrock Prompt resource from Amazon Web Services.

```
aws.bedrock_prompt
```

## Fields

| Title                       | ID   | Type      | Data Type                                                                                                                                                                                                                                  | Description |
| --------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                        | core | string    |
| account_id                  | core | string    |
| arn                         | core | string    | The Amazon Resource Name (ARN) of the prompt or the prompt version (if you specified a version in the request).                                                                                                                            |
| created_at                  | core | timestamp | The time at which the prompt was created.                                                                                                                                                                                                  |
| customer_encryption_key_arn | core | string    | The Amazon Resource Name (ARN) of the KMS key that the prompt is encrypted with.                                                                                                                                                           |
| default_variant             | core | string    | The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html">PromptVariant</a> object. |
| description                 | core | string    | The descriptino of the prompt.                                                                                                                                                                                                             |
| id                          | core | string    | The unique identifier of the prompt.                                                                                                                                                                                                       |
| name                        | core | string    | The name of the prompt.                                                                                                                                                                                                                    |
| tags                        | core | hstore    |
| updated_at                  | core | timestamp | The time at which the prompt was last updated.                                                                                                                                                                                             |
| variants                    | core | json      | A list of objects, each containing details about a variant of the prompt.                                                                                                                                                                  |
| version                     | core | string    | The version of the prompt.                                                                                                                                                                                                                 |
