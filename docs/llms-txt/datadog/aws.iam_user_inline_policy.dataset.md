# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_user_inline_policy.dataset.md

---
title: IAM User Inline Policies
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM User Inline Policies
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iam_user_inline_policy.dataset/index.html
---

# IAM User Inline Policies

This table represents the IAM User Inline Policies resource from Amazon Web Services.

```
aws.iam_user_inline_policy
```

## Fields

| Title                  | ID   | Type   | Data Type                                                                                                                                                                                                                                       | Description |
| ---------------------- | ---- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string |
| account_id             | core | string |
| policy_document        | core | string | The policy document. IAM stores policies in JSON format. However, resources that were created using CloudFormation templates can be formatted in YAML. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. |
| policy_name            | core | string | The name of the policy.                                                                                                                                                                                                                         |
| tags                   | core | hstore |
| user_inline_policy_arn | core | string |
| user_name              | core | string | The user the policy is associated with.                                                                                                                                                                                                         |
