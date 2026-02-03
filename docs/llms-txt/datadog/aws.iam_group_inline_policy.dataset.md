# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_group_inline_policy.dataset.md

---
title: IAM Group Inline Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM Group Inline Policy
---

# IAM Group Inline Policy

This table represents the IAM Group Inline Policy resource from Amazon Web Services.

```
aws.iam_group_inline_policy
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                                                                       | Description |
| ----------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| group_inline_policy_arn | core | string     |
| group_name              | core | string     | The group the policy is associated with.                                                                                                                                                                                                        |
| policy_document         | core | string     | The policy document. IAM stores policies in JSON format. However, resources that were created using CloudFormation templates can be formatted in YAML. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. |
| policy_name             | core | string     | The name of the policy.                                                                                                                                                                                                                         |
| tags                    | core | hstore_csv |
